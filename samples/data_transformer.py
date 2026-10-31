"""
SyntaxCraft Studio - Data Transformer & ETL Pipeline
High-throughput data cleaning, schema validation, and persistence engine.
Supports native Python SQLite persistence with zero external dependencies,
with high-performance Polars/Pandas acceleration when available.

Usage:
    python data_transformer.py

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import os
import sqlite3
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("syntaxcraft.etl")

# Optional Polars acceleration
try:
    import polars as pl
    POLARS_AVAILABLE = True
except ImportError:
    POLARS_AVAILABLE = False


class DataTransformer:
    """Transforms raw analytics dictionaries into clean, typed tabular structures."""

    def __init__(self, db_path: str = "data/analytics.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(os.path.abspath(self.db_path)), exist_ok=True)

    def _persist_native_sqlite(self, records: List[Dict[str, Any]], table_name: str) -> int:
        """Zero-dependency fallback: standard Python sqlite3 driver."""
        if not records:
            return 0

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        first = records[0]
        columns = []
        for col_name, val in first.items():
            if isinstance(val, int):
                col_type = "INTEGER"
            elif isinstance(val, float):
                col_type = "REAL"
            else:
                col_type = "TEXT"
            columns.append(f'"{col_name}" {col_type}')

        create_sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({", ".join(columns)});'
        cursor.execute(create_sql)

        cols_str = ", ".join([f'"{k}"' for k in first.keys()])
        placeholders = ", ".join(["?" for _ in first.keys()])
        insert_sql = f'INSERT INTO "{table_name}" ({cols_str}) VALUES ({placeholders})'

        rows = []
        for r in records:
            rows.append(tuple(r.get(k) for k in first.keys()))

        cursor.executemany(insert_sql, rows)
        conn.commit()
        conn.close()
        return len(records)

    def process_and_persist(self, raw_records: List[Dict[str, Any]], table_name: str = "seo_metrics") -> int:
        if not raw_records:
            logger.warning("Empty records supplied to DataTransformer.")
            return 0

        # High-performance Polars mode if available
        if POLARS_AVAILABLE:
            try:
                df = pl.DataFrame(raw_records)
                if "search_trend_score" in df.columns:
                    df = df.with_columns(
                        pl.col("search_trend_score").cast(pl.Float64),
                        pl.col("estimated_volume").cast(pl.Int64)
                    )
                conn = sqlite3.connect(self.db_path)
                try:
                    df.to_pandas().to_sql(table_name, conn, if_exists="append", index=False)
                    logger.info(f"Persisted {len(df)} records via Polars engine into SQLite table '{table_name}'.")
                    return len(df)
                finally:
                    conn.close()
            except Exception as e:
                logger.warning(f"Polars acceleration failed ({e}); falling back to native SQLite engine.")

        # Native SQLite execution
        count = self._persist_native_sqlite(raw_records, table_name)
        logger.info(f"Persisted {count} records via Native Engine into SQLite table '{table_name}'.")
        return count


if __name__ == "__main__":
    test_records = [
        {"keyword": "Nuxt 3 starter", "estimated_volume": 14000, "search_trend_score": 92.0, "competition_index": 0.35},
        {"keyword": "Python automation", "estimated_volume": 45000, "search_trend_score": 88.5, "competition_index": 0.65}
    ]
    transformer = DataTransformer()
    count = transformer.process_and_persist(test_records)
    print(f"✓ Transformed and stored {count} records in local SQLite database: {transformer.db_path}")
