MONTHS_ID = {
    "Januari": 1,
    "Februari": 2,
    "Maret": 3,
    "April": 4,
    "Mei": 5,
    "Juni": 6,
    "Juli": 7,
    "Agustus": 8,
    "September": 9,
    "Oktober": 10,
    "November": 11,
    "Desember": 12,
}


def clean_value(value):

    if value is None:
        return None

    value = value.strip()

    if value == "":
        return None

    return value


def to_int(value):

    value = clean_value(value)

    if value is None:
        return None

    try:
        return int(value)

    except ValueError:
        return None


def parse_indonesian_date(value):

    value = clean_value(value)

    if value is None:
        return None

    parts = value.split()

    if len(parts) != 3:
        return value

    try:
        day = int(parts[0])
        year = int(parts[2])

    except ValueError:
        return value

    month_name = parts[1]

    month = MONTHS_ID.get(
        month_name
    )

    if month is None:
        return value

    return (
        f"{year:04d}-"
        f"{month:02d}-"
        f"{day:02d}"
    )