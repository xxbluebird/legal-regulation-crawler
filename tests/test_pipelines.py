import pytest

from scrapy.exceptions import DropItem

from legal_crawler.pipelines import (
    RegulationValidationPipeline,
    DuplicateRegulationPipeline,
)


def test_valid_item_passes_validation():

    pipeline = RegulationValidationPipeline()

    item = {
        "regulation_type": "PERATURAN PEMERINTAH",
        "number": "30",
        "year": 2026,
        "title": "Contoh Peraturan",
        "status": "Berlaku",
        "source_url": "https://example.com/regulation/30",
    }

    result = pipeline.process_item(
        item,
        spider=None
    )

    assert result == item


def test_missing_required_field_is_dropped():

    pipeline = RegulationValidationPipeline()

    item = {
        "regulation_type": "PERATURAN PEMERINTAH",
        "number": "31",
        "year": 2026,
        "title": None,
        "status": "Berlaku",
        "source_url": "https://example.com/regulation/31",
    }

    with pytest.raises(DropItem):

        pipeline.process_item(
            item,
            spider=None
        )


def test_duplicate_url_is_dropped():

    pipeline = DuplicateRegulationPipeline()

    first_item = {
        "source_url": "https://example.com/regulation/100"
    }

    duplicate_item = {
        "source_url": "https://example.com/regulation/100"
    }

    pipeline.process_item(
        first_item,
        spider=None
    )

    with pytest.raises(DropItem):

        pipeline.process_item(
            duplicate_item,
            spider=None
        )