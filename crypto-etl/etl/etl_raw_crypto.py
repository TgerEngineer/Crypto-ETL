import requests
import psycopg2
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

def etl_raw_crypto():
    logger.info("🚀 Bắt đầu ETL dữ liệu từ CoinGecko API")

    try:
        conn = psycopg2.connect(
            dbname="crypto_db",
            user="user",
            password="pass",
            host="crypto_postgres",
            port="5432"
        )
        cursor = conn.cursor()
        logger.info("✅ Kết nối đến PostgreSQL thành công")
    except Exception as e:
        logger.error(f"❌ Lỗi kết nối PostgreSQL: {e}")
        return

    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 100,
            "page": 1,
            "sparkline": "false"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        logger.info(f"📦 Đã lấy được {len(data)} coins từ API")
    except Exception as e:
        logger.error(f"❌ Lỗi khi gọi API: {e}")
        conn.close()
        return

    inserted_rows = 0
    try:
        for coin in data:
            cursor.execute("""
                INSERT INTO raw_crypto_prices (
                    symbol, name, price_usd, market_cap, volume_24h, percent_change_24h, timestamp
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                coin["symbol"],
                coin["name"],
                coin["current_price"],
                coin["market_cap"],
                coin["total_volume"],
                coin["price_change_percentage_24h"],
                datetime.utcnow()
            ))
            inserted_rows += 1

        conn.commit()
        logger.info(f"✅ Đã insert {inserted_rows} dòng vào bảng raw_crypto_prices")
    except Exception as e:
        logger.error(f"❌ Lỗi khi ghi dữ liệu vào bảng: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        logger.info("🔒 Đã đóng kết nối database")
