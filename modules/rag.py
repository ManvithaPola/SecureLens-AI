import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Global variables
index = None
document_chunks = []


def split_text(text, chunk_size=800, overlap=100):
    """
    Split text into overlapping chunks.
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


def build_vector_store(text):
    """
    Create FAISS vector database from document text.
    """

    global index
    global document_chunks

    document_chunks = split_text(text)

    embeddings = embedding_model.encode(
        document_chunks,
        convert_to_numpy=True
    )

    embeddings = embeddings.astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    print(f"Created FAISS Index with {len(document_chunks)} chunks")


def search_vector_store(question, k=3):
    """
    Retrieve the most relevant document chunks.
    """

    global index
    global document_chunks

    if index is None:
        return []

    query_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:

        if idx != -1 and idx < len(document_chunks):

            results.append(document_chunks[idx])

    return results