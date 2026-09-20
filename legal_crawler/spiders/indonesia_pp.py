import scrapy
from legal_crawler.items import RegulationItem

from legal_crawler.utils import (
    clean_value,
    to_int,
    parse_indonesian_date,
)

class IndonesiaPPSpider(scrapy.Spider):

    name = "indonesia_pp"

    allowed_domains = [
        "peraturan.go.id"
    ]

    start_urls = [
        "https://peraturan.go.id/pp?page=1"
    ]

    MAX_LIST_PAGES = 3


    # MONTHS_ID = {
    #     "Januari": 1,
    #     "Februari": 2,
    #     "Maret": 3,
    #     "April": 4,
    #     "Mei": 5,
    #     "Juni": 6,
    #     "Juli": 7,
    #     "Agustus": 8,
    #     "September": 9,
    #     "Oktober": 10,
    #     "November": 11,
    #     "Desember": 12,
    # }


    def __init__(self, *args, **kwargs):

        super().__init__(
            *args,
            **kwargs
        )

        self.seen_detail_urls = set()


    # def clean_value(
    #     self,
    #     value
    # ):

    #     if value is None:
    #         return None

    #     value = value.strip()

    #     if value == "":
    #         return None

    #     return value


    # def to_int(
    #     self,
    #     value
    # ):

    #     value = self.clean_value(
    #         value
    #     )

    #     if value is None:
    #         return None

    #     try:
    #         return int(value)

    #     except ValueError:
    #         return None


    # def parse_indonesian_date(
    #     self,
    #     value
    # ):

    #     value = self.clean_value(
    #         value
    #     )

    #     if value is None:
    #         return None


    #     parts = value.split()

    #     if len(parts) != 3:
    #         return value


    #     try:
    #         day = int(parts[0])
    #         year = int(parts[2])

    #     except ValueError:
    #         return value


    #     month_name = parts[1]

    #     month = self.MONTHS_ID.get(
    #         month_name
    #     )


    #     if month is None:
    #         return value


    #     return (
    #         f"{year:04d}-"
    #         f"{month:02d}-"
    #         f"{day:02d}"
    #     )


    def parse(
        self,
        response
    ):

        page_number = response.meta.get(
            "page_number",
            1
        )


        self.logger.info(
            "Parsing list page %s: %s",
            page_number,
            response.url
        )


        detail_links = response.css(
            "a[href*='/id/pp-']::attr(href)"
        ).getall()


        detail_links = list(
            dict.fromkeys(
                detail_links
            )
        )


        self.logger.info(
            "PP detail links found: %s",
            len(detail_links)
        )


        for href in detail_links:

            detail_url = response.urljoin(
                href
            )


            if detail_url in self.seen_detail_urls:

                self.logger.info(
                    "Skipping duplicate: %s",
                    detail_url
                )

                continue


            self.seen_detail_urls.add(
                detail_url
            )


            yield scrapy.Request(
                url=detail_url,
                callback=self.parse_detail
            )


        # Follow pagination only until MAX_LIST_PAGES
        if page_number < self.MAX_LIST_PAGES:

            next_page = response.xpath(
                "//a[normalize-space(text())='»']/@href"
            ).get()


            if next_page:

                next_url = response.urljoin(
                    next_page
                )


                self.logger.info(
                    "Following next page: %s",
                    next_url
                )


                yield scrapy.Request(
                    url=next_url,
                    callback=self.parse,
                    meta={
                        "page_number":
                            page_number + 1
                    }
                )

            else:

                self.logger.warning(
                    "Next page link not found "
                    "on list page %s",
                    page_number
                )


    def parse_detail(
        self,
        response
    ):

        metadata = {}

        document_url = None


        rows = response.css("tr")


        for row in rows:

            key = row.css(
                "th"
            ).xpath(
                "string(.)"
            ).get()


            value = row.css(
                "td"
            ).xpath(
                "string(.)"
            ).get()


            key = self.clean_value(
                key
            )

            value = clean_value(
                value
            )


            if not key:
                continue


            metadata[key] = value


            if key == "Dokumen Peraturan":

                document_href = row.css(
                    "td a::attr(href)"
                ).get()


                if document_href:

                    document_url = (
                        response.urljoin(
                            document_href
                        )
                    )


        item = RegulationItem()


        item["regulation_type"] = metadata.get(
            "Jenis/Bentuk Peraturan"
        )

        item["initiator"] = metadata.get(
            "Pemrakarsa"
        )

        item["number"] = metadata.get(
            "Nomor"
        )

        to_int(
            metadata.get("Tahun")
        )

        item["title"] = metadata.get(
            "Tentang"
        )

        item["enactment_place"] = metadata.get(
            "Tempat Penetapan"
        )

        item["enactment_date"] = (
            parse_indonesian_date(
                metadata.get(
                    "Ditetapkan Tanggal"
                )
            )
        )

        item["enacting_official"] = metadata.get(
            "Pejabat yang Menetapkan"
        )

        item["status"] = metadata.get(
            "Status"
        )

        item["promulgation_year"] = (
            self.to_int(
                metadata.get(
                    "Tahun Pengundangan"
                )
            )
        )

        item["promulgation_number"] = (
            metadata.get(
                "Nomor Pengundangan"
            )
        )

        item["additional_number"] = metadata.get(
            "Nomor Tambahan"
        )

        item["promulgation_date"] = (
            parse_indonesian_date(
                metadata.get(
                    "Tanggal Pengundangan"
                )
            )
        )

        item["promulgating_official"] = (
            metadata.get(
                "Pejabat Pengundangan"
            )
        )

        item["document_url"] = document_url

        item["source_url"] = response.url


        yield item