import sqlite3

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query = """
    INSERT INTO playoffs(city,name)
    VALUES ("Buffalo", "Bills"),
            ("Seattle", "Seahawks"),
            ("San fransisco", "49ers"),
            ("Los Angeles", "Rams"),
            ("New England", "Patriots"),
            ("Chicago", "Bears"),
            ("Denver", "Broncos"),
            ("Houstan", "Texans");
    

"""

cursor.execute(query)
conn.commit()
conn.close