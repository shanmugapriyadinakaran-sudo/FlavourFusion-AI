import sqlite3
import os

db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "flavorfusion.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

cur.execute("PRAGMA table_info(predictions)")
cols = [r[1] for r in cur.fetchall()]

if "shared_molecules" not in cols:
    cur.execute("ALTER TABLE predictions ADD COLUMN shared_molecules JSON DEFAULT '[]'")
    print("Added shared_molecules")

if "shared_molecule_count" not in cols:
    cur.execute("ALTER TABLE predictions ADD COLUMN shared_molecule_count INTEGER DEFAULT 0")
    print("Added shared_molecule_count")

if "molecular_taste_synthesis" not in cols:
    cur.execute("ALTER TABLE predictions ADD COLUMN molecular_taste_synthesis TEXT DEFAULT ''")
    print("Added molecular_taste_synthesis")

con.commit()
con.close()
print("Migration completed.")
