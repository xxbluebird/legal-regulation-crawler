import scrapy


class RegulationItem(scrapy.Item):

    regulation_type = scrapy.Field()
    initiator = scrapy.Field()

    number = scrapy.Field()
    year = scrapy.Field()

    title = scrapy.Field()

    enactment_place = scrapy.Field()
    enactment_date = scrapy.Field()
    enacting_official = scrapy.Field()

    status = scrapy.Field()

    promulgation_year = scrapy.Field()
    promulgation_number = scrapy.Field()
    additional_number = scrapy.Field()
    promulgation_date = scrapy.Field()
    promulgating_official = scrapy.Field()

    document_url = scrapy.Field()
    source_url = scrapy.Field()