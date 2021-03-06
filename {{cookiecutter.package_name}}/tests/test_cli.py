import pytest

from click.testing import CliRunner

from {{cookiecutter.package_dir}}.cli import cli

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert 0 == result.exit_code
    assert "Using {{cookiecutter.package_name}}" in result.output
