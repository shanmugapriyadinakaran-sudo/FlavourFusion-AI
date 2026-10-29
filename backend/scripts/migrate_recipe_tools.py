import sqlite3
import os

db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "flavorfusion.db")
print(f"Connecting to {db_path}...")

con = sqlite3.connect(db_path)
cur = con.cursor()

cur.execute("PRAGMA table_info(recipes)")
cols = [r[1] for r in cur.fetchall()]

if "required_tools" not in cols:
    cur.execute("ALTER TABLE recipes ADD COLUMN required_tools JSON DEFAULT '[]'")
    print("Added required_tools column to recipes")

if "needed_ingredients" not in cols:
    cur.execute("ALTER TABLE recipes ADD COLUMN needed_ingredients JSON DEFAULT '[]'")
    print("Added needed_ingredients column to recipes")

con.commit()

cur.execute("PRAGMA table_info(recipes)")
print("Updated recipes columns:", [r[1] for r in cur.fetchall()])
con.close()
