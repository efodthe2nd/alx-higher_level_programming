import mysql.connector

# connect to the MySQL server
mydb = mysql.connector.connect(
    host = "localhost",
    user = "vagrant",
    password = "davidebajiefod"
)

# get a cursor to execute commands
mycursor = mydb.cursor()

# execute the command to show all databases
mycursor.execute("SHOW DATABASES")

# open the output file
with open("files", "W") as file:

    # iterate over the results and write each databases name
    for db in mycursor:
        file.write(db[0] + "\n")
