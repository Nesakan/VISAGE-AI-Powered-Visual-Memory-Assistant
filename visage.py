import os

# List of folders to create
folders = [
    "backend/app/routes",
    "backend/app/core",
    "backend/app/db",
    "backend/app/services",
    "backend/tests",

    "cv/capture",
    "cv/detection",
    "cv/processing",
    "cv/embedding",
    "cv/pipeline",
    "cv/tests",

    "llm/rag",
    "llm/prompts",
    "llm/inference",
    "llm/tests",

    "genai/sd",
    "genai/presets",
    "genai/client",
    "genai/tests",

    "frontend/src/components",
    "frontend/src/pages",
    "frontend/public",

    "data/sample_images",
    "data/sample_embeddings",
    "data/raw",
    "data/processed",

    "embeddings",
    "models",
    "notebooks",
    "scripts",
    "deployment/docker",
    "deployment/k8s",
    "architecture",
    "docs"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folders created successfully!")

# -----------------------------
# Create README.md files
# -----------------------------
readmes = {
    "README.md": "# VISAGE\nProject scaffold created with Python.",
    "backend/README.md": "# Backend Module\nFastAPI backend.",
    "cv/README.md": "# CV Module\nComputer vision pipelines.",
    "frontend/README.md": "# Frontend Module\nReact + Tailwind frontend.",
    "llm/README.md": "# LLM Module\nInference & RAG.",
    "genai/README.md": "# GenAI Module\nImage generation via SD/Replicate."
}

for path, content in readmes.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("README files created.")

# -----------------------------
# Create environment.yml
# -----------------------------
env_content = """name: visage
channels:
  - pytorch
  - conda-forge
dependencies:
  - python=3.10
  - pip
  - numpy
  - jupyter
  - opencv
  - pillow
  - scikit-image
  - faiss-cpu
  - pytorch
  - torchvision
  - torchaudio
  - cpuonly
  - sqlite

  - pip:
      - transformers
      - sentence-transformers
      - diffusers
      - accelerate
      - xformers
      - chromadb
      - fastapi
      - uvicorn
      - pydantic
      - python-dotenv
      - requests
      - httpx
"""

with open("environment.yml", "w", encoding="utf-8") as f:
    f.write(env_content)

print("environment.yml created successfully!")
print("\nVISAGE project scaffold created.")
