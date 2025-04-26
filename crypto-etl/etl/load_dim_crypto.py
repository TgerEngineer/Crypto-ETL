import psycopg2
import logging

logger = logging.getLogger(__name__)

def load_dim_crypto():
    logger.info("[START] Loading data into dim_crypto table")

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
            SELECT DISTINCT symbol, name
            FROM raw_crypto_prices
            WHERE symbol IS NOT NULL AND name IS NOT NULL
        """)
        rows = cursor.fetchall()

        for symbol, name in rows:
            cursor.execute("""
                INSERT INTO dim_crypto (symbol, name, category, launch_date)
                VALUES (%s, %s, NULL, NULL)
                ON CONFLICT (symbol) DO NOTHING
            """, (symbol, name))

        conn.commit()
        logger.info(f"[SUCCESS] Inserted {len(rows)} rows into dim_crypto table.")

    except Exception as e:
        logger.error(f"[ERROR] Failed to load dim_crypto: {e}")
        raise

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        logger.info("[DONE] Closed DB connection for dim_crypto.")
