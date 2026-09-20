# Indonesian Legal Regulation Crawler

A Python web crawler built with Scrapy to collect, normalize, validate, and export publicly available Indonesian government regulation metadata from [peraturan.go.id](https://peraturan.go.id/).

The current implementation targets **Peraturan Pemerintah (PP)** and is structured so that additional regulation categories can be added through new spiders.

## Features

- Crawls paginated regulation listing pages
- Visits individual regulation detail pages
- Extracts structured regulation metadata
- Normalizes Indonesian dates into ISO `YYYY-MM-DD` format
- Converts numeric fields into appropriate data types
- Extracts official regulation document URLs
- Validates required fields using a Scrapy item pipeline
- Detects and removes duplicate regulation records
- Exports structured records as JSONL
- Respects `robots.txt`
- Uses request delays and Scrapy AutoThrottle for polite crawling
- Includes automated unit tests with pytest

## Tech Stack

- Python
- Scrapy
- pytest

## Data Schema

Each regulation record may contain:

- `regulation_type`
- `initiator`
- `number`
- `year`
- `title`
- `enactment_place`
- `enactment_date`
- `enacting_official`
- `status`
- `promulgation_year`
- `promulgation_number`
- `additional_number`
- `promulgation_date`
- `promulgating_official`
- `document_url`
- `source_url`

## Example Output

```json
{
  "regulation_type": "PERATURAN PEMERINTAH",
  "initiator": "PEMERINTAH PUSAT",
  "number": "8",
  "year": 2026,
  "title": "Perubahan Atas Peraturan Pemerintah Nomor 23 Tahun 2021 Tentang Penyelenggaraan Kehutanan",
  "status": "Berlaku",
  "document_url": "https://peraturan.go.id/files/pp-no-8-tahun-2026.pdf",
  "source_url": "https://peraturan.go.id/id/pp-no-8-tahun-2026"
}
```

A small sample dataset is available in:

```text
samples/sample_regulations.jsonl
```

## Project Structure

```text
legal-regulation-crawler/
├── legal_crawler/
│   ├── spiders/
│   │   └── indonesia_pp.py
│   ├── items.py
│   ├── pipelines.py
│   ├── settings.py
│   └── utils.py
├── samples/
│   └── sample_regulations.jsonl
├── tests/
│   ├── test_pipelines.py
│   └── test_utils.py
├── requirements.txt
├── scrapy.cfg
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/xxbluebird/legal-regulation-crawler.git
cd legal-regulation-crawler
```

Create a virtual environment:

```bash
python -m venv .venv
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the crawler:

```bash
scrapy crawl indonesia_pp -O regulations.jsonl
```

The crawler will collect regulation metadata and export the results as JSONL.

## Testing

Run the automated test suite:

```bash
python -m pytest -v
```

The test suite currently covers:

- required-field validation
- duplicate detection
- whitespace and empty-value normalization
- integer conversion
- Indonesian date normalization

## Responsible Crawling

The crawler is configured to respect `robots.txt`, limit concurrent requests, apply request delays, and use Scrapy AutoThrottle to reduce unnecessary load on the source website.

## Data Source

Public regulation metadata is obtained from:

**peraturan.go.id**

This project is an independent educational and portfolio project and is not affiliated with or endorsed by the website operator.