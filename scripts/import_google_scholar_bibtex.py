#!/usr/bin/env python3
"""Import a Google Scholar BibTeX export into Jekyll publication pages."""

from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path


MONTH_LOOKUP = {
    "jan": "01",
    "feb": "02",
    "mar": "03",
    "apr": "04",
    "may": "05",
    "jun": "06",
    "jul": "07",
    "aug": "08",
    "sep": "09",
    "oct": "10",
    "nov": "11",
    "dec": "12",
}


ENTRY_TYPE_TO_CATEGORY = {
    "article": "manuscripts",
    "inproceedings": "conference",
    "conference": "conference",
    "proceedings": "conference",
    "phdthesis": "thesis",
    "mastersthesis": "thesis",
    "thesis": "thesis",
}


@dataclass
class BibEntry:
    entry_type: str
    citekey: str
    fields: dict[str, str]


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def cleanup_tex(text: str) -> str:
    value = text.replace("\\&", "&").replace("\\_", "_").replace("\\%", "%")
    value = value.replace("\\'", "").replace('\\"', "").replace("\\`", "")
    value = value.replace("\\~", "").replace("\\^", "")
    value = value.replace("{", "").replace("}", "")
    return normalize_whitespace(value)


def normalize_for_match(text: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "", ascii_text.lower())


def slugify(text: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return re.sub(r"-{2,}", "-", slug) or "publication"


def parse_bibtex_value(text: str, start: int) -> tuple[str, int]:
    if text[start] == "{":
        depth = 1
        index = start + 1
        chunks: list[str] = []
        while index < len(text) and depth > 0:
            char = text[index]
            if char == "{":
                depth += 1
                if depth > 1:
                    chunks.append(char)
            elif char == "}":
                depth -= 1
                if depth > 0:
                    chunks.append(char)
            else:
                chunks.append(char)
            index += 1
        return "".join(chunks), index

    if text[start] == '"':
        index = start + 1
        chunks: list[str] = []
        escaped = False
        while index < len(text):
            char = text[index]
            if char == '"' and not escaped:
                index += 1
                break
            if char == "\\" and not escaped:
                escaped = True
                chunks.append(char)
            else:
                escaped = False
                chunks.append(char)
            index += 1
        return "".join(chunks), index

    index = start
    while index < len(text) and text[index] not in ",\n\r}":
        index += 1
    return text[start:index].strip(), index


def parse_bibtex_entries(text: str) -> list[BibEntry]:
    entries: list[BibEntry] = []
    index = 0
    while index < len(text):
        at_sign = text.find("@", index)
        if at_sign == -1:
            break

        match = re.match(r"@([A-Za-z]+)\s*([({])", text[at_sign:])
        if not match:
            index = at_sign + 1
            continue

        entry_type = match.group(1).lower()
        opener = match.group(2)
        closer = ")" if opener == "(" else "}"
        cursor = at_sign + match.end()

        key_start = cursor
        while cursor < len(text) and text[cursor] != ",":
            cursor += 1
        citekey = text[key_start:cursor].strip()
        cursor += 1

        fields: dict[str, str] = {}
        while cursor < len(text):
            while cursor < len(text) and text[cursor] in " \t\r\n,":
                cursor += 1

            if cursor >= len(text):
                break
            if text[cursor] == closer:
                cursor += 1
                break

            name_start = cursor
            while cursor < len(text) and re.match(r"[A-Za-z0-9_:-]", text[cursor]):
                cursor += 1
            field_name = text[name_start:cursor].strip().lower()

            while cursor < len(text) and text[cursor] in " \t\r\n":
                cursor += 1
            if cursor >= len(text) or text[cursor] != "=":
                break
            cursor += 1
            while cursor < len(text) and text[cursor] in " \t\r\n":
                cursor += 1

            if cursor >= len(text):
                break

            value, cursor = parse_bibtex_value(text, cursor)
            fields[field_name] = value.strip()

        entries.append(BibEntry(entry_type=entry_type, citekey=citekey, fields=fields))
        index = cursor

    return entries


def split_authors(raw_authors: str) -> list[str]:
    parts = re.split(r"\s+and\s+", raw_authors)
    names: list[str] = []
    for part in parts:
        name = cleanup_tex(part)
        if "," in name:
            last, first = [segment.strip() for segment in name.split(",", 1)]
            full_name = f"{first} {last}".strip()
        else:
            full_name = name
        names.append(normalize_whitespace(full_name))
    return [name for name in names if name]


def format_authors(names: list[str], highlight_authors: list[str]) -> str:
    highlight_keys = {normalize_for_match(name) for name in highlight_authors}
    rendered: list[str] = []
    for name in names:
        if normalize_for_match(name) in highlight_keys:
            rendered.append(f"<b>{html.escape(name)}</b>")
        else:
            rendered.append(html.escape(name))

    if not rendered:
        return "Unknown author"
    if len(rendered) == 1:
        return rendered[0]
    if len(rendered) == 2:
        return f"{rendered[0]} and {rendered[1]}"
    return ", ".join(rendered[:-1]) + f", and {rendered[-1]}"


def month_to_number(raw_month: str | None) -> str:
    if not raw_month:
        return "01"
    cleaned = cleanup_tex(raw_month).strip().lower()
    if cleaned.isdigit():
        return f"{int(cleaned):02d}"
    return MONTH_LOOKUP.get(cleaned[:3], "01")


def infer_category(entry_type: str) -> str:
    return ENTRY_TYPE_TO_CATEGORY.get(entry_type, "manuscripts")


def build_venue(fields: dict[str, str], entry_type: str) -> str:
    cleaned = {key: cleanup_tex(value) for key, value in fields.items()}
    category = infer_category(entry_type)

    if category == "manuscripts":
        if cleaned.get("archiveprefix") == "arXiv" and cleaned.get("eprint"):
            return f"arXiv preprint arXiv:{cleaned['eprint']}"

        journal = cleaned.get("journal") or cleaned.get("booktitle") or cleaned.get("publisher", "")
        parts = [journal] if journal else []
        if cleaned.get("volume"):
            parts.append(f"vol. {cleaned['volume']}")
        if cleaned.get("number"):
            parts.append(f"no. {cleaned['number']}")
        if cleaned.get("pages"):
            page_label = "pp." if "-" in cleaned["pages"] else "p."
            parts.append(f"{page_label} {cleaned['pages'].replace('--', '-')}")
        return ", ".join(part for part in parts if part)

    if category == "conference":
        booktitle = cleaned.get("booktitle") or cleaned.get("journal") or cleaned.get("publisher", "")
        parts = [booktitle] if booktitle else []
        if cleaned.get("pages"):
            parts.append(f"pp. {cleaned['pages'].replace('--', '-')}")
        return ", ".join(part for part in parts if part)

    school = cleaned.get("school") or cleaned.get("institution") or cleaned.get("publisher", "")
    thesis_label = {
        "phdthesis": "PhD Thesis",
        "mastersthesis": "MSc Thesis",
    }.get(entry_type, "Thesis")
    if school:
        return f"{thesis_label}, {school}"
    return thesis_label


def build_paper_url(fields: dict[str, str]) -> tuple[str | None, str | None]:
    url = cleanup_tex(fields.get("url", "")) or None
    doi = cleanup_tex(fields.get("doi", "")) or None

    if not url and doi:
        url = f"https://doi.org/{doi}"

    preprint_url = None
    if url and "arxiv.org" in url:
        preprint_url = url

    return url, preprint_url


def parse_front_matter_fields(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}

    fields: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        value = raw_value.strip().strip("'").strip('"')
        fields[key.strip()] = value
    return fields


def index_existing_publications(outdir: Path) -> tuple[dict[str, Path], dict[str, Path]]:
    doi_index: dict[str, Path] = {}
    title_index: dict[str, Path] = {}
    if not outdir.exists():
        return doi_index, title_index

    for path in outdir.glob("*.md"):
        fields = parse_front_matter_fields(path)
        if fields.get("doi"):
            doi_index[normalize_for_match(fields["doi"])] = path
        if fields.get("title"):
            title_index[normalize_for_match(fields["title"])] = path
    return doi_index, title_index


def build_excerpt(fields: dict[str, str]) -> str | None:
    for key in ("abstract", "note"):
        if fields.get(key):
            return cleanup_tex(fields[key])
    return None


def build_citation(authors: list[str], title: str, year: str, venue: str, highlight_authors: list[str]) -> str:
    citation = f"{format_authors(authors, highlight_authors)}. ({year}). \"{html.escape(title)}.\""
    if venue:
        citation += f" <i>{html.escape(venue)}</i>."
    return citation


def front_matter(entry: BibEntry, highlight_authors: list[str]) -> tuple[str, str]:
    fields = entry.fields
    year = cleanup_tex(fields.get("year", "")) or "1900"
    month = month_to_number(fields.get("month"))
    day = f"{int(cleanup_tex(fields.get('day', '1')) or '1'):02d}"
    date_value = f"{year}-{month}-{day}"

    title = cleanup_tex(fields.get("title", entry.citekey or "Untitled publication"))
    slug = slugify(title)
    category = infer_category(entry.entry_type)
    permalink = f"/publication/{date_value}-{slug}"
    venue = build_venue(fields, entry.entry_type)
    url, preprint_url = build_paper_url(fields)
    excerpt = build_excerpt(fields)
    authors = split_authors(fields.get("author", ""))
    citation = build_citation(authors, title, year, venue, highlight_authors)
    doi = cleanup_tex(fields.get("doi", "")) or None

    lines = [
        "---",
        f'title: "{html.escape(title)}"',
        "collection: publications",
        f"category: {category}",
        f"permalink: {permalink}",
    ]

    if excerpt:
        lines.append(f'excerpt: "{html.escape(excerpt)}"')

    lines.extend(
        [
            f"date: {date_value}",
            f"venue: '{html.escape(venue)}'",
        ]
    )

    if url:
        lines.append(f"paperurl: '{url}'")
    if preprint_url:
        lines.append(f"preprinturl: '{preprint_url}'")
    if doi:
        lines.append(f"doi: '{doi}'")

    lines.append(f"citation: '{citation}'")
    lines.append("---")

    body = ""
    if excerpt:
        body = f"\n{excerpt}\n"
    else:
        body = "\n<!-- Imported from Google Scholar BibTeX export. Add an abstract, media, or additional links as needed. -->\n"

    file_name = f"{date_value}-{slug}.md"
    return file_name, "\n".join(lines) + body


def import_bibtex(args: argparse.Namespace) -> int:
    source = Path(args.bibtex_file)
    outdir = Path(args.outdir)

    if not source.exists():
        print(f"Input file not found: {source}", file=sys.stderr)
        return 1

    text = source.read_text(encoding="utf-8")
    entries = parse_bibtex_entries(text)
    if not entries:
        print("No BibTeX entries found.", file=sys.stderr)
        return 1

    outdir.mkdir(parents=True, exist_ok=True)

    existing_doi_index, existing_title_index = index_existing_publications(outdir)

    written = 0
    skipped = 0
    for entry in entries:
        file_name, content = front_matter(entry, args.highlight_author)
        fields = entry.fields
        title = cleanup_tex(fields.get("title", entry.citekey or ""))
        doi = cleanup_tex(fields.get("doi", ""))

        destination = outdir / file_name
        if doi and normalize_for_match(doi) in existing_doi_index:
            destination = existing_doi_index[normalize_for_match(doi)]
        elif title and normalize_for_match(title) in existing_title_index:
            destination = existing_title_index[normalize_for_match(title)]

        if destination.exists() and not args.overwrite:
            skipped += 1
            print(f"skip   {destination} (already exists)")
            continue

        if args.write:
            destination.write_text(content, encoding="utf-8")
            action = "write"
        else:
            action = "plan"

        written += 1
        print(f"{action:5} {destination}")

    mode = "Wrote" if args.write else "Planned"
    print(f"{mode} {written} file(s); skipped {skipped} existing file(s).")
    if not args.write:
        print("Dry run only. Re-run with --write to create files.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a Google Scholar BibTeX export into Jekyll publication markdown files."
    )
    parser.add_argument("bibtex_file", help="Path to the BibTeX file exported from Google Scholar.")
    parser.add_argument(
        "--outdir",
        default="_publications",
        help="Output directory for generated markdown files. Default: _publications",
    )
    parser.add_argument(
        "--highlight-author",
        action="append",
        default=[],
        help="Author name to bold in citations. Repeat for multiple names.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing markdown files. Existing publications are matched by DOI first, then title.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write files. Without this flag, the script performs a dry run.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return import_bibtex(args)


if __name__ == "__main__":
    raise SystemExit(main())
