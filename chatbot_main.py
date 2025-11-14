import os
from utils import gemini_api, doc_generator, code_parser

OUTPUT_DIR = "generated_docs/project_001"
PROMPT_DIR = "prompts"

def get_input(prompt, options=None):
    while True:
        value = input(prompt)
        if not options or value.lower() in options:
            return value.strip()
        print(f"❌ Please enter one of: {', '.join(options)}")

def get_documents_to_generate():
    print("\n📄 Available documents: brd, hld, fsd, lld, ppt, excel")
    selected = input("🧾 Which documents would you like to generate? (comma-separated): ")
    return [doc.strip().lower() for doc in selected.split(',')]

def get_zip_file():
    raw_path = input("\n📦 Enter full path to your code ZIP file: ").strip()
    zip_path = os.path.abspath(raw_path.strip('"').strip("'"))
    if not os.path.isfile(zip_path) or not zip_path.lower().endswith(".zip"):
        print(f"❌ Invalid ZIP file or path: {zip_path}")
        return None
    return zip_path

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("\n🤖 Welcome to the LLM Terminal Document Generator")

    selected_docs = get_documents_to_generate()

    # Get multiline user requirements
    print("\n📝 Enter user requirements (press Enter for new line, type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    requirements = "\n".join(lines)

    needs_code = any(doc in selected_docs for doc in ["fsd", "lld", "ppt", "excel"])

    # BRD
    if "brd" in selected_docs:
        prompt_path = os.path.join(PROMPT_DIR, "brd_prompt.txt")
        content = doc_generator.generate_brd(requirements, prompt_path)
        with open(os.path.join(OUTPUT_DIR, "brd.docx"), "wb") as f:
            f.write(content)
        print("✅ BRD saved to generated_docs/project_001/brd.docx")

    # HLD
    if "hld" in selected_docs:
        prompt_path = os.path.join(PROMPT_DIR, "hld_prompt.txt")
        content = doc_generator.generate_hld(requirements, prompt_path)
        with open(os.path.join(OUTPUT_DIR, "hld.docx"), "wb") as f:
            f.write(content)
        print("✅ HLD saved to generated_docs/project_001/hld.docx")

    # If code-based docs requested
    if needs_code:
        zip_path = get_zip_file()
        if not zip_path:
            return
        parsed_code = code_parser.parse_code(zip_path)

        if "fsd" in selected_docs:
            prompt_path = os.path.join(PROMPT_DIR, "fsd_prompt.txt")
            content = doc_generator.generate_fsd(parsed_code, requirements, prompt_path)
            with open(os.path.join(OUTPUT_DIR, "fsd.docx"), "wb") as f:
                f.write(content)
            print("✅ FSD saved to generated_docs/project_001/fsd.docx")

        if "lld" in selected_docs:
            prompt_path = os.path.join(PROMPT_DIR, "lld_prompt.txt")
            content = doc_generator.generate_lld(parsed_code, requirements, prompt_path)
            with open(os.path.join(OUTPUT_DIR, "lld.docx"), "wb") as f:
                f.write(content)
            print("✅ LLD saved to generated_docs/project_001/lld.docx")

        if "ppt" in selected_docs:
            prompt_path = os.path.join(PROMPT_DIR, "ppt_prompt.txt")
            content = doc_generator.generate_ppt(parsed_code, requirements, prompt_path)
            with open(os.path.join(OUTPUT_DIR, "slides.pptx"), "wb") as f:
                f.write(content)
            print("✅ PPT saved to generated_docs/project_001/slides.pptx")

        if "excel" in selected_docs:
            prompt_path = os.path.join(PROMPT_DIR, "mapping_prompt.txt")
            content = doc_generator.generate_excel(requirements, parsed_code, prompt_path)
            with open(os.path.join(OUTPUT_DIR, "requirement_mapping.xlsx"), "wb") as f:
                f.write(content)
            print("✅ Excel Mapping saved to generated_docs/project_001/requirement_mapping.xlsx")

    print("\n🎉 All requested documents have been generated!")

if __name__ == "__main__":
    main()
