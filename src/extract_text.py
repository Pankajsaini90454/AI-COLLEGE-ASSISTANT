import json
from pathlib import Path
import pypdf


def extract_text_from_pdf(pdf_path: str | Path, output_json_path: str | Path) -> None:
    pdf_path = Path(pdf_path)
    reader = pypdf.PdfReader(pdf_path)
    extracted_data = []

    for idx, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            extracted_data.append(
                {
                    "page_number": idx,
                    "content": text.strip(),
                    "source": pdf_path.name,
                }
            )

    output_file = Path(output_json_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)

    print(f"Text extraction complete! Total pages saved: {len(extracted_data)}")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    pdf_path = project_root / "data" / "utu slaybus.pdf"
    output_path = project_root / "data" / "output" / "parsed_text.json"
    extract_text_from_pdf(pdf_path, output_path)