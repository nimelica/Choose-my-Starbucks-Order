import sqlite3, requests

# Get data from the Mock API using GET HTTP method
# response data type will be byte
response = requests.get("https://mock-starbucs-api.herokuapp.com/drinks")

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# Convert bytes into a JSON list data
drinks = response.json()

# Create an empty database 
connection = sqlite3.connect('drinks_list.db')

# communication with database via cursor with SQL commands
cursor = connection.cursor()

# Create table/s for our database
cursor.execute("create table drinks (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

# Fill that table
for i in range(len(drinks)):
  cursor.execute("insert into drinks (name) values (?)",[drinks[i]])
  print("added ", drinks[i])
  # all_drinks = cursor.fetchall()


# Do not forget to save (commit) and close the database connection
connection.commit()
connection.close()