from legal_crawler.utils import (
    clean_value,
    to_int,
    parse_indonesian_date,
)


def test_clean_value_removes_whitespace():

    assert clean_value(
        "  Berlaku  "
    ) == "Berlaku"


def test_clean_value_empty_string_returns_none():

    assert clean_value(
        "   "
    ) is None


def test_to_int_converts_numeric_string():

    assert to_int(
        "2026"
    ) == 2026


def test_to_int_invalid_value_returns_none():

    assert to_int(
        "abc"
    ) is None


def test_parse_indonesian_date():

    result = parse_indonesian_date(
        "02 Juli 2026"
    )

    assert result == "2026-07-02"


def test_parse_indonesian_date_none():

    assert parse_indonesian_date(
        None
    ) is None