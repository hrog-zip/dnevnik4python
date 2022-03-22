from setuptools import setup, find_packages

with open("README.md", mode = "r", encoding = "utf-8") as r:
    long_description = r.read()

setup(
    name = "dnevnik4python",
    version = "0.0.5",
    url = "https://github.com/hrog-zip/dnevnik4python",
    packages = find_packages(),
    description = "Wrapper for python that simplifies work with dnevnik.ru",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = ["beautifulsoup4==4.10.0",
                        "bs4==0.0.1",
                        "certifi==2021.10.8",
                        "charset-normalizer==2.0.12",
                        "fake-useragent==0.1.11",
                        "idna==3.3",
                        "lxml==4.8.0",
                        "pytz==2022.1",
                        "requests==2.27.1",
                        "soupsieve==2.3.1",]
                        
    keywords = ["python", "dnevnik", "dnevnikru", "api", "dnevnikru api", "dnevnik api", "wrapper"]
)
