CREATE TABLE raw_crypto_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    name VARCHAR(100),
    price_usd NUMERIC,
    market_cap NUMERIC,
    volume_24h NUMERIC,
    percent_change_24h NUMERIC,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_raw_symbol ON raw_crypto_prices(symbol);


CREATE TABLE dim_crypto (
    symbol VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    launch_date DATE
);


CREATE TABLE fact_crypto_price (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    price_usd NUMERIC,
    market_cap NUMERIC,
    volume_24h NUMERIC,
    percent_change_24h NUMERIC,
    timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (symbol) REFERENCES dim_crypto(symbol)
);