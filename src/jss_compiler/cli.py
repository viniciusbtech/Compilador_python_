"""Interface de linha de comando do compilador JSS."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from .errors import JSSCompilerError
from .frontend import analyze_source
from .llvm_generator import generate_llvm


def _build_executable(ir_path: Path, exe_path: Path) -> bool:
    clang = shutil.which("clang")
    if clang is None:
        print("Erro: clang nao encontrado no PATH. Nao foi possivel gerar o executavel.")
        return False

    try:
        cmd = [clang, str(ir_path), "-o", str(exe_path)]
        if sys.platform == "win32":
            cmd.append("-llegacy_stdio_definitions")

        result = subprocess.run(
            cmd,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as e:
        print(f"Erro ao executar clang: {e}")
        return False

    if result.returncode != 0:
        print("Erro ao gerar executavel com clang:")
        if result.stderr.strip():
            print(result.stderr.strip())
        elif result.stdout.strip():
            print(result.stdout.strip())
        return False

    return True


def _default_exe_path(source_path: Path, run_mode: bool) -> Path:
    if not run_mode:
        return source_path.with_suffix(".exe")

    temp_dir = Path(tempfile.gettempdir())
    return temp_dir / f"{source_path.stem}.jss.exe"


def _run_executable(exe_path: Path) -> int:
    try:
        result = subprocess.run([str(exe_path)], check=False)
    except OSError as e:
        print(f"Erro ao executar '{exe_path}': {e}")
        return 1
    return result.returncode


def main() -> int:
    """Gera LLVM IR, compila para executavel e opcionalmente executa."""
    parser = argparse.ArgumentParser(description="Compilador JSS")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--build",
        action="store_true",
        help="Gera LLVM IR e executavel, sem executar o programa",
    )
    mode.add_argument(
        "--run",
        action="store_true",
        help="Gera LLVM IR, executavel e executa o programa final",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Arquivo executavel de saida .exe",
        default=None,
    )
    parser.add_argument("arquivo", help="Arquivo fonte .jss a ser compilado")
    args = parser.parse_args()

    source_path = Path(args.arquivo)

    try:
        with open(source_path, encoding="utf-8") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Erro: arquivo '{args.arquivo}' não encontrado.")
        return 1

    if not source.strip():
        print(f"Erro: arquivo '{args.arquivo}' está vazio.")
        return 1

    try:
        ast, analyzer = analyze_source(source)
    except JSSCompilerError as error:
        print(error)
        return 1

    ir = generate_llvm(ast, analyzer)
    ir_path = source_path.with_suffix(".ll")

    try:
        with open(ir_path, "w", encoding="utf-8") as f:
            f.write(ir)
    except OSError as e:
        print(f"Erro ao escrever '{ir_path}': {e}")
        return 1

    exe_path = Path(args.output) if args.output else _default_exe_path(source_path, args.run)

    if not args.run:
        print(f"LLVM IR gerado: {ir_path}", flush=True)
    if not _build_executable(ir_path, exe_path):
        return 1
    if not args.run:
        print(f"Executavel gerado: {exe_path}", flush=True)

    if args.run:
        return _run_executable(exe_path)

    return 0
