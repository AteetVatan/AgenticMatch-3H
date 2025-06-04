from PIL import Image, ImageDraw
import os

# Target folder for partner images
image_folder = "data/partners/images" # use os.getcwd() , this will be run from partners folder.
os.makedirs(image_folder, exist_ok=True)

# Partner visual themes (aligned with metadata)
partners = {
    "P001": ("Tokyo Beauty Lab", (224, 255, 255)),        # Light Cyan
    "P002": ("Nordic Face Studio", (176, 196, 222)),      # Steel Blue
    "P003": ("Mediterraneo Glow", (255, 160, 122)),       # Light Coral
    "P004": ("Parisian Porcelaine", (255, 182, 193)),     # Light Pink
    "P005": ("Ayurvedic Radiance", (144, 238, 144))       # Light Green
}

# Create labeled dummy image per partner
for pid, (label, color) in partners.items():
    img = Image.new("RGB", (512, 512), color=color)
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), label, fill=(0, 0, 0))
    img.save(os.path.join(image_folder, f"{pid}.jpg"))

print("Partner dummy images.")
