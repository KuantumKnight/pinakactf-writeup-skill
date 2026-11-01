#!/usr/bin/env python3
"""Assemble a plain DOCX from participant-authored text and genuine screenshots.

No title, metadata, headings, numbering, tables, captions, or decorative layout
are added. The ordered content is kept in the order supplied by the manifest.
"""

import argparse
import json
from pathlib import Path

from docx import Document
from docx.shared import Inches


def build(manifest_path: Path, output_path: Path) -> int:
    manifest_path = manifest_path.resolve()
    base_dir = manifest_path.parent
    with manifest_path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)

    doc = Document()
    screenshot_count = 0

    for item in manifest.get("content", []):
        item_type = item.get("type")

        if item_type == "text":
            if item.get("source") != "user":
                raise ValueError(
                    "Text blocks must have source='user'. "
                    "Do not place assistant-written prose in the reference document."
                )
            value = (item.get("text") or "").strip()
            if value:
                doc.add_paragraph(value)

        elif item_type == "screenshot":
            screenshot_count += 1
            raw_path = (item.get("path") or "").strip()
            target = (item.get("target") or "").strip()

            if raw_path:
                image_path = Path(raw_path)
                if not image_path.is_absolute():
                    image_path = base_dir / image_path
                if not image_path.exists():
                    raise FileNotFoundError(f"Screenshot not found: {image_path}")
                paragraph = doc.add_paragraph()
                paragraph.add_run().add_picture(str(image_path), width=Inches(6.0))
            elif target:
                # A plain reminder at the exact insertion point; replace it
                # with the genuine screenshot before the participant submits.
                doc.add_paragraph(f"(screenshot needed: {target})")
            else:
                raise ValueError(
                    "Each screenshot block needs either a real image path or a target reminder."
                )

        else:
            raise ValueError(f"Unsupported content block type: {item_type!r}")

    flag = (manifest.get("flag") or "").strip()
    if flag:
        doc.add_paragraph(flag)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_path)

    if not (3 <= screenshot_count <= 6):
        print(
            f"WARNING: found {screenshot_count} screenshot item(s); "
            "PinakaCTF requires 3–6 per challenge."
        )
    print(f"Wrote plain reference document: {output_path}")
    return screenshot_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", help="Ordered content manifest")
    parser.add_argument("output", help="Output .docx path")
    args = parser.parse_args()
    build(Path(args.manifest), Path(args.output))


if __name__ == "__main__":
    main()
