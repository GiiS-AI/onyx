import csv
import io
from collections.abc import Generator

from pydantic import BaseModel

# Python's csv default field size limit is 131072 bytes (128 KiB), which
# real-world data (long descriptions, pasted docs, base64 blobs) routinely
# exceeds — the parser then raises `Error: field larger than field limit
# (131072)` and fails the whole row, aborting indexing of the CSV section
# (ONYX-BACKEND-H6FM). Bump to 128 MiB, matching the order of magnitude the
# salesforce connector already opts into for bulk exports.
_CSV_FIELD_SIZE_LIMIT_BYTES = 128 * 1024 * 1024
csv.field_size_limit(_CSV_FIELD_SIZE_LIMIT_BYTES)


class ParsedRow(BaseModel):
    header: list[str]
    row: list[str]


def read_csv_header(csv_text: str) -> list[str]:
    """Return the first non-blank row (the header) of a CSV string, or
    [] if the text has no usable header.
    """
    if not csv_text.strip():
        return []
    for row in csv.reader(io.StringIO(csv_text)):
        if any(c.strip() for c in row):
            return row
    return []


def parse_csv_string(csv_text: str) -> Generator[ParsedRow, None, None]:
    """
    Takes in a string in the form of a CSV and yields back
    each row + header in the csv.
    """
    if not csv_text.strip():
        return

    reader = csv.reader(io.StringIO(csv_text))
    header: list[str] | None = None
    for row in reader:
        if not any(cell.strip() for cell in row):
            continue
        if header is None:
            header = row
            continue
        yield ParsedRow(header=header, row=row)
