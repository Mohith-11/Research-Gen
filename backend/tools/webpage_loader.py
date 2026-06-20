#
from langchain_community.document_loaders import WebBaseLoader


def load_webpage(url: str):
    """
    Load and extract text from a webpage.
    Returns the page content as a string.
    """

    try:
        loader = WebBaseLoader(url)
        docs = loader.load()

        if docs:
            return docs[0].page_content

        return ""

    except Exception as e:
        print(f"Error loading {url}: {e}")
        return ""