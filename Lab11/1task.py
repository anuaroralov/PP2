import psycopg2, csv, sys

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = '1234'
port_id = 5432
conn, cur = None, None


conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
)
cur = conn.cursor()
create_script = '''CREATE TABLE IF NOT EXISTS phonebook(
            id  varchar(3),
            first_name   varchar(30),
            last_name varchar(30),
            phone   varchar(30),
            region  varchar(30)
)'''
cur.execute(create_script)
                           
def searchbypattern():
    pattern = input("Enter the pattern: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s", (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%")
    )
    data = cur.fetchall()
    for item in data:
        print(item)

def from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    region = input("Enter region: ")
    cur.execute(
        '''INSERT INTO phonebook (first_name, last_name, phone, region) 
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (first_name) DO UPDATE SET phone = excluded.phone''', 
        (first_name, last_name, phone, region)
    )

cur.execute(
   '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
  IN users TEXT[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
  i TEXT[];
BEGIN 
   Foreach i slice 1 in array users
   LOOP
      INSERT INTO phonebook (first_name, phone) VALUES (i[1], i[2]);
   END LOOP;
 
END
$$;
'''
)

def query_with_pagination(limit, offset):
    cur.execute(
        '''
        SELECT *
        FROM phonebook
        ORDER BY id
        LIMIT %s
        OFFSET %s
        ''', (limit, offset)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data():
    print("Do you want to delete by name or by phone number?")
    print("1 - delete by name\n2 - delete by phone number")
    choice = input()
    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif choice == "2":
        phone = input("Enter phone number: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    else:
        print("Invalid choice")

    print(cur.rowcount, "record(s) deleted")

print('''1 - returns all records based on a pattern\n 2 - insert new user by name and phone, update phone if user already exists\n 3 - insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.\n 4 - querying data from the tables with pagination (by limit and offset)\n 5 - deleting data from tables by username or phone''')
num = int(input())
if num == 1:
    searchbypattern()
elif num == 2:
        from_console()
elif num == 3:
        cur.execute('''CALL insert_list_of_users(ARRAY[
            ARRAY['Bob', '87076052769'],
            ARRAY['Alex', '87079815569'],
            ARRAY['Jhon', '87074793780']
        ]);''')  
elif num == 4:
        limit=input()
        offset=input()
        query_with_pagination(limit,offset)
elif num == 5:
        delete_data()

conn.commit()

cur.close()
conn.close()        