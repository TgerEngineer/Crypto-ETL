import psycopg2
import logging

logger = logging.getLogger(__name__)

def transform_load_fact():
    logger.info("[START] Transforming and loading data into fact_crypto_price table")

    try:
        conn = psycopg2.connect(
            dbname="crypto_db",
            user="user",
            password="pass",
            host="crypto_postgres",
            port="5432"
        )
        cursor = conn.cursor()

        cursor.execute("""
            SELECT symbol, price_usd, market_cap, volume_24h, percent_change_24h, timestamp
            FROM raw_crypto_prices
            WHERE price_usd IS NOT NULL
        """)
        rows = cursor.fetchall()

        for row in rows:
            symbol, price_usd, market_cap, volume_24h, percent_change_24h, timestamp = row

            cursor.execute("""
                INSERT INTO fact_crypto_price (
                    symbol, price_usd, market_cap, volume_24h, percent_change_24h, timestamp
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (symbol, price_usd, market_cap, volume_24h, percent_change_24h, timestamp))

        conn.commit()
        logger.info(f"[SUCCESS] Inserted {len(rows)} rows into fact_crypto_price.")

    except Exception as e:
        logger.error(f"[ERROR] Failed to load fact_crypto_price: {e}")
        raise

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        logger.info("[DONE] Closed DB connection for fact_crypto_price.")
