import zipfile
import os
import ast

def extract_function_info(node):
    args = [arg.arg for arg in node.args.args]
    returns = ast.unparse(node.returns) if node.returns else "None"
    return {
        "function": node.name,
        "inputs": args,
        "returns": returns,
        "docstring": ast.get_docstring(node) or "No docstring",
        "code": ast.unparse(node)[:1000]
    }

def parse_code(zip_path, return_index=False):
    extract_path = zip_path.replace(".zip", "_extracted")
    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    summary = ""
    code_index = {}

    for root, _, files in os.walk(extract_path):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        code = f.read()

                    summary += f"\n\nFile: {file}\n{code[:2000]}..."

                    tree = ast.parse(code)
                    functions = [
                        extract_function_info(node)
                        for node in ast.walk(tree)
                        if isinstance(node, ast.FunctionDef)
                    ]
                    if functions:
                        code_index[file] = functions

                except Exception as e:
                    summary += f"\n\n[ERROR reading {file}: {e}]"

    return (summary, code_index) if return_index else summary
