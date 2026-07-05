from app.ai.text_loading import load_docs
from app.logger import logger

from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

from app.config import Config

K_VALUE = 3

docs = load_docs()

def get_retriever(docs: list):
    logger.info('Loading docs to FAISS')

    embeddings = HuggingFaceEmbeddings(model_name=Config.EMBEDDINGS_MODEL_NAME)

    db = FAISS.from_documents(docs, embeddings)

    return db.as_retriever()