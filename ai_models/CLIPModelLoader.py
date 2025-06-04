from transformers import CLIPModel, CLIPProcessor
from typing import Optional
import torch

class CLIPModelLoader:
    """
    Loads the HuggingFace CLIP model and processor.
    """
    def __init__(self, model_name: str = "openai/clip-vit-base-patch32", device: Optional[str] = None):
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = None
        self.processor = None
        self.__load()

    def __load(self):
        print(f"🔍 Loading model: {self.model_name} on [{self.device}]")
        self.model = CLIPModel.from_pretrained(self.model_name).to(self.device)
        self.processor = CLIPProcessor.from_pretrained(self.model_name)

    def get_model(self):
        if self.model is None or self.processor is None:
            raise RuntimeError("Model not loaded. Call `load()` first.")
        return self.model, self.processor

    # def to(self, device: str):
    #     self.device = device
    #     if self.model:
    #         self.model.to(self.device)
    #         print(f"⚡ Moved model to {self.device}")
