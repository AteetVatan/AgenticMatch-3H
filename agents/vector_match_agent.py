import faiss
import numpy as np
import os

class VectorMatchAgent:
    def __init__(self, index_path: str = "partner_index.faiss"):
        if not os.path.exists(index_path):
            raise FileNotFoundError(f"FAISS index file not found: {index_path}")
        self.index = faiss.read_index(index_path)

    def find_matches(self, vector: np.ndarray, top_k: int = 3):
        if vector.ndim == 1:
            vector = np.expand_dims(vector, axis=0)
        _, indices = self.index.search(vector.astype("float32"), top_k)
        return indices[0].tolist()