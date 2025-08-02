import sqlite3

# Connect to the database
conn = sqlite3.connect('colonial.db')
cursor = conn.cursor()

# Example query
cursor.execute("SELECT * FROM GUIDE")
guides = cursor.fetchall()

print("Guides:")
for guide in guides:
    print(guide)

# Close the connection
conn.close()    