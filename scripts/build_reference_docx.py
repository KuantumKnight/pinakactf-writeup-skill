#!/usr/bin/env python3
"""Build a compact PinakaCTF handwritten-reference DOCX from a JSON manifest.

Narrative text is expected to be participant-authored. This script only formats it.
"""

import argparse
import json
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def set_cell_shading(cell, fill="F2F2F2"):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_margins(section):
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)


def add_meta_table(doc, data):
    rows = [
        ("CTF", data.get("ctf", "PinakaCTF 2026")),
        ("Challenge", data.get("challenge", "")),
        ("Category", data.get("category", "")),
        ("Points", str(data.get("points", ""))),
    ]
    table = doc.add_table(rows=len(rows), cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.style = "Table Grid"
    for i, (key, value) in enumerate(rows):
        left, right = table.rows[i].cells
        left.text = key
        right.text = value
        left.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        right.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_shading(left)
        for run in left.paragraphs[0].runs:
            run.bold = True
            run.font.size = Pt(9.5)
        for run in right.paragraphs[0].runs:
            run.font.size = Pt(9.5)
    doc.add_paragraph()


def add_placeholder(doc, idx, target):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    cell = table.cell(0, 0)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"SS{idx} — {target or 'Insert genuine screenshot here'}")
    r.bold = True
    r.font.size = Pt(9)
    p.add_run("\n\n")
    doc.add_paragraph()


def add_step(doc, idx, step, screenshot_index):
    text = (step.get("text") or "").strip()
    command = (step.get("command") or "").strip()

    if text:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(f"{idx}. {text}")
        r.font.size = Pt(10.5)

    if command:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.2)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(command)
        r.font.name = "Consolas"
        r.font.size = Pt(8.5)

    screenshot = (step.get("screenshot") or "").strip()
    target = (step.get("screenshot_target") or "").strip()
    if screenshot or target:
        screenshot_index += 1
        if screenshot and Path(screenshot).exists():
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(screenshot, width=Inches(5.9))
            cap = doc.add_paragraph(f"SS{screenshot_index} — {target or Path(screenshot).name}")
            cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in cap.runs:
                r.italic = True
                r.font.size = Pt(8)
        else:
            add_placeholder(doc, screenshot_index, target)
    return screenshot_index


def build(manifest, output_path):
    doc = Document()
    for section in doc.sections:
        set_margins(section)

    styles = doc.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10.5)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("PinakaCTF 2026 — Handwritten Write-up Reference")
    run.bold = True
    run.font.size = Pt(14)

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sr = subtitle.add_run("Participant-authored notes + genuine screenshot plan")
    sr.italic = True
    sr.font.size = Pt(8.5)

    add_meta_table(doc, manifest)

    h = doc.add_paragraph()
    rr = h.add_run("Solve path")
    rr.bold = True
    rr.font.size = Pt(11.5)

    ss_idx = 0
    steps = manifest.get("steps") or []
    for i, step in enumerate(steps, 1):
        ss_idx = add_step(doc, i, step, ss_idx)

    flag = (manifest.get("flag") or "").strip()
    doc.add_paragraph()
    fp = doc.add_paragraph()
    fr = fp.add_run("Flag: ")
    fr.bold = True
    fr.font.size = Pt(11)
    fv = fp.add_run(flag)
    fv.font.name = "Consolas"
    fv.font.size = Pt(10.5)

    note = doc.add_paragraph()
    note.paragraph_format.space_before = Pt(8)
    nr = note.add_run("Check before handwriting: use only your own wording and your own screenshots; keep 3–6 screenshots.")
    nr.italic = True
    nr.font.size = Pt(7.5)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)
    return ss_idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", help="Path to JSON manifest")
    ap.add_argument("output", help="Output .docx path")
    args = ap.parse_args()

    with open(args.manifest, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    count = build(manifest, args.output)
    if not (3 <= count <= 6):
        print(f"WARNING: manifest produces {count} screenshot slot(s); PinakaCTF requires 3–6.")
    print(f"Wrote {args.output} with {count} screenshot slot(s).")


if __name__ == "__main__":
    main()
