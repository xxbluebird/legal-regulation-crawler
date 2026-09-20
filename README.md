# Indonesian Legal Regulation Crawler

A Python-based web crawler built with Scrapy to collect and structure publicly available Indonesian regulation metadata from peraturan.go.id.

## Features

- Crawls paginated regulation listing pages
- Extracts metadata from regulation detail pages
- Normalizes Indonesian dates to ISO format
- Extracts official regulation PDF URLs
- Prevents duplicate records
- Validates required fields
- Exports structured data as JSONL
- Includes automated unit tests with pytest
- Uses polite crawling settings with AutoThrottle and request delays

## Tech Stack

- Python
- Scrapy
- BeautifulSoup
- Requests
- pytest

## Data Schema

- regulation_type
- initiator
- number
- year
- title
- enactment_place
- enactment_date
- enacting_official
- status
- promulgation_year
- promulgation_number
- additional_number
- promulgation_date
- promulgating_official
- document_url
- source_url

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