from pathlib import Path

# ROOT = Path(__file__).parent.resolve().parent

ROOT = Path().resolve().parent

print(f"ROOT {ROOT}")

PROJECT_DIR = ROOT / "project_folder"
DATA_DIR = PROJECT_DIR / "datasets"
EMBEDDING_DIR = PROJECT_DIR / "embeddings"
CHECKPOINT_DIR = PROJECT_DIR / "checkpoints"
FIGURE_DIR = PROJECT_DIR / "figures"
