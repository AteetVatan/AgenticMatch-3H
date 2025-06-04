"""Backend Server Fast API."""
"""
Calls the core agents:
Embedding Agent → turns image into vector using CLIP.
Vector Match Agent → searches FAISS for similar images.
Metadata Agent → fetches mood/style data from JSON.
Returns → matching partners and reasons as JSON response.
"""
