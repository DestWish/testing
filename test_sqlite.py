import pytest
import sqlite3

@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    conn.commit()

    yield cursor

    cursor.execute("DROP TABLE users")
    conn.commit()
    conn.close()
