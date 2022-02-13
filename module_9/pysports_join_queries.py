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
    
    #select query from team
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    #results
    teams = cursor.fetchall()
    
    #output
    print("\n -DISPLAYING TEAM RECORDS- ")
    
    #iteration for teams
    for team in teams:
        print(" Team ID: {}\n Team Name: {}\n Mascot: {}\n".format(team[0], team[1], team[2]))

    #query player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    #results
    players = cursor.fetchall()

    #output
    print("\n -DISPLAYING PLAYER RECORDS'")

    #iteration for player
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n Press any key to continue...")


finally:
    db.close()
