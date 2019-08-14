import click

from {{cookiecutter.package_dir}} import main

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(
    invoke_without_command=True,
    context_settings=CONTEXT_SETTINGS
)
@click.version_option(
    version='{{cookiecutter.package_version}}'
)
def cli():
    main()
    return 0
