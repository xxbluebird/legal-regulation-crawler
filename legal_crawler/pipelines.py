from scrapy.exceptions import DropItem


class RegulationValidationPipeline:

    REQUIRED_FIELDS = [
        "regulation_type",
        "number",
        "year",
        "title",
        "status",
        "source_url",
    ]


    def process_item(
        self,
        item,
        spider
    ):

        missing_fields = []

        for field in self.REQUIRED_FIELDS:

            value = item.get(field)

            if value is None:

                missing_fields.append(
                    field
                )


        if missing_fields:

            raise DropItem(
                f"Missing required fields "
                f"{missing_fields} "
                f"in {item.get('source_url')}"
            )


        return item


class DuplicateRegulationPipeline:

    def __init__(self):

        self.seen_urls = set()


    def process_item(
        self,
        item,
        spider
    ):

        source_url = item.get(
            "source_url"
        )


        if source_url in self.seen_urls:

            raise DropItem(
                f"Duplicate regulation: "
                f"{source_url}"
            )


        self.seen_urls.add(
            source_url
        )


        return item