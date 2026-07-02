from modules.rag import build_vector_store
from modules.rag import search_vector_store

text = """
John Doe

Email : john@gmail.com

Phone : 9876543210

Skills

Python
Machine Learning
Flask
React
"""

build_vector_store(text)

results = search_vector_store(
    "What skills are mentioned?"
)

print(results)