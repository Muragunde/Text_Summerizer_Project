import setuptools

with open("REaDME.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Text_Summerizer_Project"
AUTHOR_USER_NAME = "Muragunde"
SRC_REPO = "textSummerizer"
AUTHOR_EMAIL = "sheetalmuragunde2001@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Muragunde/Text_Summerizer_Project",
    project_urls={
        "Bug Tracker": f"https://github.com/Muragunde/Text_Summerizer_Project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)