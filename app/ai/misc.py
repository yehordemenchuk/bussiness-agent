import os

import tiktoken

from app.config import Config

tokenizer = tiktoken.get_encoding("cl100k_base")

def read_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)

def truncate_text(text, max_tokens=2000):
    tokens = tokenizer.encode(text)

    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]

    return tokenizer.decode(tokens)

def get_trimmed_history(input_data: dict, memory):
    raw_context = ''.join(memory.load_memory_variables({"input": input_data['input']})['history'])

    return truncate_text(raw_context)

def get_trimmed_context(input_data: dict, retriever):
    raw_context_docs = retriever.invoke(input_data['input'])

    raw_context_text = format_docs(raw_context_docs)

    return truncate_text(raw_context_text)

def count_tokens_from_messages(messages):
    total_tokens = 0
    for msg in messages:
        content = getattr(msg, "content", "")
        tokens = tokenizer.encode(content)
        total_tokens += len(tokens)
    return total_tokens

def setup_tracer():
    os.environ['LANGCHAIN_API_KEY'] = Config.LANGCHAIN_API_KEY
    os.environ['LANGCHAIN_ENDPOINT'] = Config.LANGCHAIN_ENDPOINT
    os.environ['LANGCHAIN_PROJECT'] = Config.LANGCHAIN_PROJECT
    os.environ['LANGCHAIN_TRACING_V2'] = Config.LANGCHAIN_TRACING_V2