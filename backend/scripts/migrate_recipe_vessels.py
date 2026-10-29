import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "flavorfusion.db")
print("Connecting to:", os.path.abspath(db_path))

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Check existing columns in recipes
cur.execute("PRAGMA table_info(recipes);")
cols = [row[1] for row in cur.fetchall()]
print("Current columns in recipes:", cols)

if "required_vessels" not in cols:
    print("Adding required_vessels column to recipes...")
    cur.execute("ALTER TABLE recipes ADD COLUMN required_vessels JSON DEFAULT '[]';")

conn.commit()
conn.close()
print("Migration completed successfully!")
