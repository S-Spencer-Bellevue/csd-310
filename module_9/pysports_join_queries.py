## pysports_queries.py
## Name:Steven Spencer
## Date: February 13 2022
## Class: CYBR 410 T302


##import

import mysql.connector
##from mysql.connector import errorcode

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
    
    cursor = db.cursor()
    
    #inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    #results
    players = cursor.fetchall()

    #print
    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    #forloop for iteration
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n  Press any key to continue.. ")



finally:
    db.close()
