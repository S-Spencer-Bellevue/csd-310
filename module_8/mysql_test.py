##
  ##  Title: db_init.sql
  ##  database connector for MySQL
  ##  Steven Spencer
  ##  CYBR 410 T 301
  ##  February 6th 2022

##import
import mysql.connector
from mysql.connector import errorcode

##config for pysports
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
##try connections
try:
    db = mysql.connector.connect(**config)
    print("\n Database User {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The Supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else: 
        print(err)
finally:
    db.close()
