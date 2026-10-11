import subprocess
import sys
from importlib.metadata import version

import pytest

import llm_zipper
from llm_zipper.cli import main


def test_version_matches_installed_metadata():
    assert version("llm-zipper") == llm_zipper.__version__


def test_cli_version(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert capsys.readouterr().out.strip() == f"llm-zipper {llm_zipper.__version__}"


def test_cli_shows_status_and_roadmap(capsys):
    assert main([]) == 0
    out = capsys.readouterr().out
    assert "pre-alpha" in out
    assert "KV-cache" in out


def test_python_dash_m():
    result = subprocess.run(
        [sys.executable, "-m", "llm_zipper", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert llm_zipper.__version__ in result.stdout
