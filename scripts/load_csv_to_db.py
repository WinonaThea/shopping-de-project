
import os
import pandas as pd
from sqlalchemy import create_engine, text, inspect

file_path = os.getenv(
    "CSV_PATH",
    "/home/thea2701/project-data/raw/shopping_trends_updated.csv"
)

df = pd.read_csv(file_path)

df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

db_user = os.getenv("DB_USER", "admin")
db_password = os.getenv("DB_PASSWORD", "admin123")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "mydb")

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

table_name = "customer_shopping_trends"
schema_name = "raw2"

with engine.begin() as conn:
    conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))

inspector = inspect(engine)

if inspector.has_table(table_name, schema=schema_name):
    with engine.begin() as conn:
        conn.execute(text(f"DELETE FROM {schema_name}.{table_name}"))

    df.to_sql(
        name=table_name,
        con=engine,
        schema=schema_name,
        if_exists="append",
        index=False
    )
else:
    df.to_sql(
        name=table_name,
        con=engine,
        schema=schema_name,
        if_exists="replace",
        index=False
    )

print(f"CSV berhasil dimasukkan ke PostgreSQL schema {schema_name}.")
