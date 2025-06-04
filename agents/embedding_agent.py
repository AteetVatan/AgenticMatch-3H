# agents/embedding_agent.py


from PIL import Image
import torch

from ai_models import CLIPModelLoader


class EmbeddingAgent:
    def __init__(self):        
        clip_model = CLIPModelLoader()
        self.model, self.processor = clip_model.get_model()
        

    def get_image_embedding(self, image: Image.Image):        

        inputs = self.processor(images=image, return_tensors="pt")
        with torch.no_grad():
            embedding = self.model.get_image_features(**inputs)
        return embedding[0].detach().numpy().astype("float32")
