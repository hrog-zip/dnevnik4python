from setuptools import setup, find_packages

with open("README.md", mode = "r", encoding = "utf-8") as r:
    long_description = r.read()

setup(
    name = "dnevnik4python",
    version = "0.0.3",
    url = "https://github.com/hrog-zip/dnevnik4python",
    packages = find_packages(),
    description = "Wrapper for python that simplifies work with dnevnik.ru",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = ["beautifulsoup4==4.9.3",
                        "bs4==0.0.1",
                        "certifi==2021.5.30",
                        "chardet==4.0.0",
                        "fake-useragent==0.1.11",
                        "idna==2.10",
                        "lxml==4.6.3",
                        "pytz==2021.1",
                        "requests==2.25.1",
                        "soupsieve==2.2.1",
                        "urllib3==1.26.6"],
    keywords = ["python", "dnevnik", "dnevnikru", "api", "dnevnikru api", "dnevnik api", "wrapper"]
)
