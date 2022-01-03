from pathlib import Path
import sqlite3

data_path = Path("data.db")
if not data_path.is_file():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE skills
               (title text, skill text, rank int)''')
    con.commit()
    con.close()