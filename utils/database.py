import sqlite3

def login(user, password):
  conn = sqlite3.connect('database.db')
  database = conn.cursor()
  database.execute(f"SELECT * FROM users WHERE name='{user}' AND password='{password}';")
  info = database.fetchone()
  if info:
    conn.close()
    return info
  else:
    conn.close()
    return False

def getClients(idClient=None):
  if idClient != None:
    conn = sqlite3.connect('database.db')
    database = conn.cursor()
    database.execute(f"SELECT * FROM clients WHERE id = {idClient}")
    data = database.fetchone()
    conn.close()
    return data
  else: 
    conn = sqlite3.connect('database.db')
    database = conn.cursor()
    database.execute("SELECT * FROM clients")
    data = database.fetchall()
    conn.close()
    return data

def createClient(name, email, phone):
  conn = sqlite3.connect('database.db')
  database = conn.cursor()

  database.execute(f"INSERT INTO clients (name, email, phone) VALUES ('{name}', '{email}', '{phone}')")

  conn.commit()
  database.execute('SELECT name, email, phone FROM clients')
  data = database.fetchall()
  
  conn.close()
  return data

def updateClient(idClient, name, email, phone):
  conn = sqlite3.connect('database.db')
  database = conn.cursor()

  database.execute(f"""
      UPDATE 
        clients 
      SET 
        name = "{name}",
        email = "{email}",
        phone = "{phone}"
      WHERE 
        id = "{idClient}"
    """)

  conn.commit()
  database.execute('SELECT name, email, phone FROM clients')
  data = database.fetchall()
  
  conn.close()
  return data

def deleteClient(idClient):
  conn = sqlite3.connect('database.db')
  database = conn.cursor()
  
  database.execute(f"DELETE FROM clients WHERE id = {idClient}")
  
  conn.commit()
  database.execute("SELECT name, email, phone FROM clients")
  data = database.fetchall()
  
  conn.close()
  return data
