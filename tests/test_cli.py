import subprocess
import sys

from shared_scripts import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "shared_scripts", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
