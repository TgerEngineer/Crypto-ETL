import requests
import pandas as pd
from datetime import datetime
import os
import logging

logger = logging.getLogger(__name__)  # Logger chuẩn

def extract_coins():
    logger.info("[START] Extracting top 10 coins from CoinGecko API")

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except Exception as e:
        logger.error(f"[ERROR] Failed to fetch data from API: {e}")
        raise

    data = response.json()

    rows = []
    for coin in data:
        rows.append({
            "id": coin["id"],
            "symbol": coin["symbol"],
            "name": coin["name"],
            "current_price": coin["current_price"],
            "market_cap": coin["market_cap"],
            "last_updated": coin["last_updated"]
        })

    df = pd.DataFrame(rows)
    df["last_updated"] = pd.to_datetime(df["last_updated"])
    df["extracted_at"] = datetime.utcnow()

    try:
        os.makedirs("/opt/airflow/data", exist_ok=True)
        output_file1 = "/opt/airflow/data/crypto_prices_raw.csv"
        df.to_csv(output_file1, index=False)
        logger.info(f"[SUCCESS] Extracted data saved to {output_file1}")
    except Exception as e:
        logger.error(f"[ERROR] Failed to save CSV: {e}")
        raise

if __name__ == "__main__":
    extract_coins()
