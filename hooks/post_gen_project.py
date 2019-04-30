import os

def del_license_file():
    print("Deleting LICENSE file")
    os.unlink("LICENSE")

if __name__ == "__main__":
# Be careful with whitespace control from jinja
{% if cookiecutter.package_license == "No License" %}
    del_license_file()
{% endif %}
    print("Cookiecutter succeeded to create <{{cookiecutter.package_name}}>")
