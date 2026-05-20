import ast
from pathlib import Path


def extract_code_chunks(file_path):
    """
    Extract functions, classes, and imports
    from a Python file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    chunks = []

    imports = []

    # Extract imports first
    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            module = node.module if node.module else ""
            imports.append(module)

    # Extract functions/classes
    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            chunks.append({
                "file": Path(file_path).name,
                "type": "function",
                "name": node.name,
                "start_line": node.lineno,
                "end_line": getattr(node, "end_lineno", node.lineno),
                "imports": imports,
                "code": ast.get_source_segment(source_code, node)
            })

        elif isinstance(node, ast.ClassDef):
            chunks.append({
                "file": Path(file_path).name,
                "type": "class",
                "name": node.name,
                "start_line": node.lineno,
                "end_line": getattr(node, "end_lineno", node.lineno),
                "imports": imports,
                "code": ast.get_source_segment(source_code, node)
            })

    return chunks