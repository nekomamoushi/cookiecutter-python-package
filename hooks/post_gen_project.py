import os

def del_license_file():
    os.unlink("LICENSE")

def del_cli_file():
    os.unlink("src/{{cookiecutter.package_dir}}/cli.py")
    os.unlink("tests/test_cli.py")

if __name__ == "__main__":
# Be careful with whitespace control from jinja
{% if cookiecutter.package_license == "No License" %}
    del_license_file()
{% endif %}

{% if cookiecutter.package_use_cli == "No command line" %}
    del_cli_file()
{% endif %}

    print("Cookiecutter succeeded to create <{{cookiecutter.package_name}}>")
