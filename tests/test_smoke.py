from jss_compiler.frontend import analyze_source


def test_frontend_smoke() -> None:
    analyze_source("function void main() {}")
