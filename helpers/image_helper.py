from PIL import Image
import io
from fastapi import UploadFile


class ImageHelper:

    @staticmethod
    async def read_image(image_file: UploadFile) -> Image.Image:
        contents = await image_file.read()
        return Image.open(io.BytesIO(contents)).convert("RGB")
