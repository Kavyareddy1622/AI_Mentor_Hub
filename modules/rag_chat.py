import streamlit as st

from utils.pdf_reader import extract_text
from rag.chunker import split_text
from rag.embeddings import get_embeddings
from rag.vector_store import add_documents
from rag.retriever import retrieve

from services.gemini_service import GeminiService


def show():

    st.title("📚 AI Document Chat")

    pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf:

        text = extract_text(pdf)

        chunks = split_text(text)

        embeddings = get_embeddings(chunks)

        add_documents(chunks, embeddings)

        st.success("Document Indexed Successfully!")

    question = st.text_input(
        "Ask a Question"
    )

    if st.button("Ask"):

        docs = retrieve(question)

        context = "\n\n".join(docs)

        prompt = f"""
Answer ONLY using the following context.

Context:
{context}

Question:
{question}
"""

        ai = GeminiService()

        answer = ai.generate_response(prompt)

        st.markdown(answer)