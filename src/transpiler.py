import sys
import re
import os
import subprocess

CARLINHO_H_CONTENT = """#ifndef CARLINHO_H
#define CARLINHO_H

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

#define float static_assert(false, "O tipo 'float' não existe no Carlos. Use 'double'.");

#define facilitador std

#endif
"""

def ensure_carlinho_header():
    include_dir = "./include"
    if not os.path.exists(include_dir):
        os.makedirs(include_dir)
    header_path = os.path.join(include_dir, "carlinho.h")
    if not os.path.exists(header_path):
        with open(header_path, 'w', encoding='utf-8') as f:
            f.write(CARLINHO_H_CONTENT)

def transpile_line(line):
    stripped = line.strip()
    if not stripped or stripped.startswith("//"):
        return line 
    stripped = re.sub(r'match\s*\((.*?)\)', r'switch(\1)', stripped)
    stripped = stripped.replace("case _:", "default:")
    
    if stripped.startswith("elif"):
        stripped = stripped.replace("elif", "else if", 1)

    if stripped.startswith("for"):
        match = re.search(r'\((.*?)\)', stripped)
        if match:
            inner_for = match.group(1).replace(",", ";")
            stripped = stripped[:match.start(1)] + inner_for + stripped[match.end(1):]

    if not (stripped.endswith("{") or stripped.endswith("}") or stripped.endswith(";") or stripped.startswith("#")):
        stripped += ";"

    indent = len(line) - len(line.lstrip())
    return (" " * indent) + stripped

def compile_carlos(filepath):
    if not filepath.endswith(".crl"):
        print("Erro: O arquivo deve ter a extensão .crl")
        sys.exit(1)

    ensure_carlinho_header()

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cpp_code = []
    for line in lines:
        cpp_code.append(transpile_line(line))

    out_cpp = filepath.replace(".crl", ".cpp")
    with open(out_cpp, 'w', encoding='utf-8') as f:
        f.write("\n".join(cpp_code))
    
    exe_name = filepath.replace(".crl", "")
    if os.name == 'nt': 
        exe_name += ".exe"
        
    result = subprocess.run(["g++", out_cpp, "-o", exe_name, "-I./include", "-O3"])
    
    if result.returncode == 0:
        print(f"Sucesso! Executável gerado: {exe_name}")
    else:
        print("Erro durante a compilação C++.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: carlos-compiler <arquivo.crl>")
        sys.exit(1)
    compile_carlos(sys.argv[1])
