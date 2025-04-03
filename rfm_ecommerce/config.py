from pathlib import Path

from dotenv import load_dotenv
from loguru import logger
import pandas as pd

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Load data
df = pd.read_excel(PROCESSED_DATA_DIR / "online_retail_II.xlsx")

# Subset data to only 2009 datetime
df = df[(df["InvoiceDate"] >= "2009-01-01") & (df["InvoiceDate"] <= "2009-12-31")]

# Save subset to processed data directory
df.to_csv(PROCESSED_DATA_DIR / "online_retail_II_2009.csv", index=False)
