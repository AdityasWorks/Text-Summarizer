import setuptools

with open("README.md", "r", encoding="utf-8") as f:
  long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "AdityasWorks"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "heyaadi2@gmail.com"

setuptools.setup(
  name=REPO_NAME,
  version=__version__,
  author=AUTHOR_USER_NAME,
  author_email=AUTHOR_EMAIL,
  description="A small python package for NLP app",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/AdityasWorks/Text-Summarizer",
  project_urls={
    "bug tracker": "https://github.com/AdityasWorks/Text-Summarizer/issues"
  }
)
