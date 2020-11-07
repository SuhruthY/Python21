import sqlite3
import json

conn = sqlite3.connect("mycontacts.db")
cur = conn.cursor()

with open("./fake_data/dataNov-7-2020.json", "r") as fh:
    data = json.load(fh)

for contact in data:
    address = f"{contact['street']}, {contact['city']}, " \
              f"{contact['country']}, {contact['zipcode']}"

    contact["address"] = address

for contact in data[:30]:
    cur.execute(""" 
         insert into 'People' (First_Name, Last_Name, Phone_no, Email_ID, Address)
                            values (?, ?, ?, ?,?)
    """, (contact["first name"], contact["surname"], contact["Ph no"], contact["email"], contact["address"]))

    conn.commit()

print("---- Sucessfully Inserted ----")