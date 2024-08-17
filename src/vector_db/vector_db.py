import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class VectorDB:
    def __init__(self):
        self.documents = []
        self.embeddings = []

    def add_document(self, document, embedding):
        self.documents.append(document)
        self.embeddings.append(embedding)

    def search(self, query_embedding, top_k=5):
        if not self.embeddings:
            return []

        similarities = cosine_similarity([query_embedding], self.embeddings)[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [self.documents[i] for i in top_indices]


# Usage example
if __name__ == "__main__":
    db = VectorDB()
    db.add_document("Paris is the capital of France", np.random.rand(768))
    db.add_document("London is the capital of England", np.random.rand(768))

    query_embedding = np.random.rand(768)
    results = db.search(query_embedding)
    print(f"Search results: {results}")
