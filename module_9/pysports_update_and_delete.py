## pysports_update_and_delete.py
## Name:Steven Spencer
## Date: February 13 2022
## Class: CYBR 410 T302


##import

import mysql.connector


##config for pysports
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
##method/function for join
def player_method(cursor, title):
#inner join 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #fetch
    players = cursor.fetchall()
    #print and format output
    print("\n  -- {} --".format(title))
    
    #for loop
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    #connect
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    #insert
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES('Smeagol', 'Shire Folk', 1)")

    #execute add
    cursor.execute(add_player)

    #insert commit
    db.commit()

    #show all - step 4
    player_method(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #update record - step 5
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    #execute
    cursor.execute(update_player)

    #display players after updating - step 5
    player_method(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #delete a player - step 6 The instructions are wrong here, Smeagol would have been updated and will not work, must use the new updated Gollum
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    #execute
    cursor.execute(delete_player)

    #display all players after delete
    player_method(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")


finally:
    db.close()
