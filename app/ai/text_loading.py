import os

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging

SIZE = 1000

OVERLAP = 200

def load_docs():
    all_docs = []

    splitter = RecursiveCharacterTextSplitter(chunk_size=SIZE, chunk_overlap=OVERLAP)

    for file in os.listdir("docs"):
        logging.info('Loading files...')

        file_path = os.path.join("docs", file)

        loader = (PyPDFLoader(file_path) if file.endswith(".pdf") else (TextLoader(file_path)
            if file.endswith(".txt") else None))

        if not loader:
            return

        docs = loader.load()

        split_docs = splitter.split_documents(docs)

        all_docs.extend(split_docs)

        logging.info("Loading finished.")

        return all_docs