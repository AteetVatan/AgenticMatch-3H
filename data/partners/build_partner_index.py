from PIL import Image
import numpy as np
import faiss
import os
import json
import torch
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from ai_models import CLIPModelLoader

image_dir = os.path.join(os.getcwd(), "data/partners/images")
index_out_path = os.path.join(os.getcwd(), "data/partners/partner_index.faiss")
id_map_out_path = os.path.join(os.getcwd(), "data/partners/id_to_partner.json")


# Load CLIP Model
clip_model = CLIPModelLoader()
model, processor = clip_model.get_model()

# Embeddings
embeddings = []
id_to_partner = {}

for idx, filename in enumerate(sorted(os.listdir(image_dir))):
    if filename.endswith(".jpg"):
        partner_id = filename.split(".")[0]
        id_to_partner[idx] = partner_id

        # Load and process--------
        image = Image.open(os.path.join(image_dir, filename)).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        with torch.no_grad():
            embedding = model.get_image_features(**inputs)[0]
        embeddings.append(embedding.numpy())

# === Build FAISS Index ===
embedding_matrix = np.stack(embeddings).astype("float32")
index = faiss.IndexFlatL2(embedding_matrix.shape[1])
index.add(embedding_matrix)

# === Save Index and ID Map ===
faiss.write_index(index, index_out_path)

with open(id_map_out_path, "w") as f:
    json.dump(id_to_partner, f, indent=4)
