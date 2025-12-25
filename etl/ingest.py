import pandas as pd
import logging

logging.basicConfig(
    filename="logs/errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(message)s"
)

def load_csv(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        logging.error(f"Failed to load CSV: {e}")
        raise
