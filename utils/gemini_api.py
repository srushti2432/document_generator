import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def call_llm(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text

def generate_brd(requirements: str) -> str:
    prompt = open("prompts/brd_prompt.txt").read().format(requirements=requirements)
    return call_llm(prompt)

def generate_hld(requirements: str, structure: str) -> str:
    prompt = open("prompts/hld_prompt.txt").read().format(requirements=requirements, structure=structure)
    return call_llm(prompt)

def generate_fsd(code_summary: str) -> str:
    prompt = open("prompts/fsd_prompt.txt").read().format(summary=code_summary)
    return call_llm(prompt)

def generate_lld(code_summary: str, code_index: list) -> str:
    index_str = json.dumps(code_index, indent=2)
    prompt = open("prompts/lld_prompt.txt").read().format(summary=code_summary, index=index_str)
    return call_llm(prompt)

def generate_ppt_outline(code_summary: str) -> str:
    prompt = open("prompts/ppt_prompt.txt").read().format(summary=code_summary)
    return call_llm(prompt)

def generate_excel_mapping(code_index: list, code_summary: str) -> str:
    index_str = json.dumps(code_index, indent=2)
    prompt = open("prompts/mapping_prompt.txt").read().format(index=index_str, summary=code_summary)
    return call_llm(prompt)

# ✅ Add this alias so other modules can call generate_content()
generate_content = call_llm
