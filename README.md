# AgenticMatch-3H

A 3-hour Agentic AI prototype that lets users upload an image and matches it to partner brands based on 
**visual style and mood** 
using CLIP embeddings and FAISS similarity search.

---

## Features

- Upload images via web UI or API
- Extract CLIP-based image embeddings (512-d vectors)
- Store and search embeddings using FAISS
- Match uploaded images to predefined partner aesthetics
- Return mood/style metadata from `partner_metadata.json`
- Modular, agent-based architecture (EmbeddingAgent, MatcherAgent, etc.)
- Fast and efficient similarity search with FAISS
- Support for both CPU and GPU inference

---

## Folder Structure

```
AgenticMatch-3H/
├── ai_models/           # AI model implementations
│   ├── CLIPModelLoader.py
│   └── __init__.py
├── agents/             # Agent implementations
├── configs/            # Configuration files
├── data/              # Data storage
│   └── partners/      # Partner images and metadata
├── helpers/           # Utility functions
├── templates/         # Web UI templates
├── app.py            # FastAPI application
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## ⚙️ Setup Instructions

### 1. Clone and Install

```bash
git clone https://github.com/yourname/AgenticMatch-3H.git
cd AgenticMatch-3H
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Prepare Partner Data

1. Place partner brand images in `data/partners/images/`
2. Run the index builder:
```bash
python data/partners/build_partner_index.py
```

### 3. Start the Server

```bash
python app.py
```

The server will start at `http://localhost:8000`

## 🛠️ API Usage

### Upload and Match Image

```python
import requests

url = "http://localhost:8000/match"
files = {"file": open("your_image.jpg", "rb")}
response = requests.post(url, files=files)
matches = response.json()
```



### Components

1. **CLIPModelLoader**
   - Handles CLIP model initialization
   - Provides image embedding functionality
   - Supports both CPU and GPU inference

2. **EmbeddingAgent**
   - Processes uploaded images
   - Generates CLIP embeddings
   - Manages image preprocessing

3. **MatcherAgent**
   - Performs similarity search using FAISS
   - Ranks and returns best matches
   - Handles metadata enrichment

### Data Flow

1. Image upload → EmbeddingAgent
2. Embedding generation → FAISS index
3. Similarity search → MatcherAgent
4. Results → API response

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- OpenAI CLIP model
- Facebook AI Research (FAISS)
- FastAPI framework
