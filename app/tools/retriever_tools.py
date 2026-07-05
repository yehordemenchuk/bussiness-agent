from langchain_core.tools import create_retriever_tool

from app.ai.retriver import get_retriever, docs

retriever_tool = create_retriever_tool(
    retriever=get_retriever(docs),
    name="knowledge_base",
    description="Use this tool to search internal company documents, product specs, FAQs, pricing, and capabilities. Use this ONLY for company-specific information, NOT for general market research or external analysis."
)