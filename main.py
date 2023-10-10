# Get data
import requests
key = 'e538a8055c054c5c9190f2e7ba766a9e'
header = {'Ocp-Apim-Subscription-Key': key}
url = 'https://api.sportsdata.io/api/nfl/fantasy/json/PlayerSeasonStats/2023'
response = requests.get(url, headers = header)
data = response.json()

# Global Vars for printing stats
flex_stats = ['Name', "Team", "Played",'RushingAttempts',"RushingYards","RushingYardsPerAttempt","RushingTouchdowns","RushingLong","ReceivingTargets","Receptions","ReceivingYards","ReceivingYardsPerReception","ReceivingTouchdowns","ReceivingLong"]
kicker_stats = ['Name', "Team", "Played",'FieldGoalsAttempted',"FieldGoalsMade","ExtraPointsMade","FieldGoalsMade0to19","FieldGoalsMade20to29","FieldGoalsMade30to39","FieldGoalsMade40to49","FieldGoalsMade50Plus"]
qb_stats = ['Name', "Team", "Played",'PassingAttempts', 'PassingCompletions', 'PassingYards',"PassingLong", 'PassingCompletionPercentage','PassingTouchdowns','PassingInterceptions','PassingRating','RushingYards','RushingAttempts',"RushingLong",'RushingTouchdowns',"PassingSacks"]
#  Global Vars for Comparing Stats
qb_compare = ["Played",'PassingAttempts', 'PassingCompletions', 'PassingYards',"PassingLong", 'PassingCompletionPercentage','PassingTouchdowns','PassingInterceptions','PassingRating','RushingYards','RushingAttempts',"RushingLong",'RushingTouchdowns',"PassingSacks"]
flex_compare = [ "Played",'RushingAttempts',"RushingYards","RushingYardsPerAttempt","RushingTouchdowns","RushingLong","ReceivingTargets","Receptions","ReceivingYards","ReceivingYardsPerReception","ReceivingTouchdowns","ReceivingLong"]
kicker_compare = [ "Played",'FieldGoalsAttempted',"FieldGoalsMade","ExtraPointsMade","FieldGoalsMade0to19","FieldGoalsMade20to29","FieldGoalsMade30to39","FieldGoalsMade40to49","FieldGoalsMade50Plus"]
# Global Var to Hold All Players
players = []
# Main Menu
def main():
    # reset players var for a fresh compare
     global players
     players = []
     call = input("What would you like to do with Football Data? \n (P) = Print Player data \n (C) = Compare Player Data \n (Q) = Quit \n")
     if call == "P":
          player = player_input()
          print_player_info(player)
     elif(call == "C"):
          add_players()
     elif(call == "Q"):
          return True
         
 #   Asks User for Input, calls other methods, returns the player
def player_input():
    player_name = input('Which Player would you like data about?\n Please input in the following format: \n First initial Capitalized followed by ".", then last name Capitilized with NO SPACES. \n Example for Aaron Rodgers: A.Rodgers \n')
    while(valid_name(player_name) == False):
        player_name = input('Which Player would you like data about?\n Please input in the following format: \n First initial Capitalized followed by ".", then last name Capitilized with NO SPACES. \n Example for Aaron Rodgers: A.Rodgers \n')
    player = get_player(player_name)
    return player
    # Makes sure that the name can be found in the proper format
def valid_name(name):
     if(name[0].islower()):
          print("The first letter must be uppercase")
          return False
     if(len(name) < 4):
          print("That is not long enough to be a name!")
          return False
     if(name[1] != "."):
          print("second character must be a '.' ")
          return False
     if(name[2].islower()):
          print("The Third letter must be uppercase")
          return False
     if(" " in name):
          print(" No Spaces Allowed")
          return False
     return True

    #  Grabs the player from the database based on name
def get_player(player_name):
    all_players = []
    for player in data:
        if(player_name == player['Name']):
            all_players.append(player)
    if len(all_players) == 1:
        return all_players[0]
    # If multiple players have same name, call method that asks user to choose
    elif (len(all_players) > 1):
       return multiple_players(all_players)
    print("That player does not exist")
    return player_input()

# Asks user which player they want
def multiple_players(all):
    i = 0
    for player in all:
          print(f'{i}) {player["Name"]} + {player["Position"]}')
          i += 1
    num = input("Which player do you want?")
    num = int(num)
    if(num < len(all)):
       return all[num]
    else:
         return multiple_players(all)
    
# Add players to compare
def add_players():
    #   Keep Track of number of players in list
      print(f"Adding the number {len(players) + 1} player to Compare \n")
      player = player_input()
    #   First player is the default position
      if len(players) == 0:
            players.append(player)
            # Make sure that players are of same position
      elif(player['Position'] != players[0]['Position']):
            print("The players must be of the same position")
            add_players()
      elif(player['Position'] == players[0]['Position']):
        players.append(player)
    # Ask user if they want to add more players to compare
      if(len(players) > 1):
        keep_compare()
      else:
        #    If there is only 1 player or less in the list, autmattically ask the user to add another
           add_players()
    
        #    Ask user if they want to compare the players or add more?
def keep_compare():
     next_step = input("Would you like to add another player? \n (Y) = Yes \n (N) = No \n")
     if next_step == "Y":
           add_players()
     elif next_step == "N":
            compare_players()
     else:
          print("invalid input!")
          keep_compare()

# Compares players, figures out which position it is comparing
def compare_players():
     compared = []
     position_to_comp = players[0]["Position"]
     comp_list = ''
    #  Choosing the stat list to compare
     if(position_to_comp == "QB"):
        comp_list = qb_compare
     elif(position_to_comp == "RB" or position_to_comp == "WR" or position_to_comp == "TE"):
        comp_list = flex_compare
     elif(position_to_comp == "K"):
        comp_list = kicker_compare
    # loops through the chosen stat and calls the max method to find the top player in that stat
     for stat in comp_list:
          compared.append(get_max(stat))
    # Loops through the new Stat List to print the results
     for max_stat in compared:
          print(max_stat)
    # Back to main menu
     main()
     
# Compares players and returns a string with the reults
def get_max(stat):
    max_stat = 0
    max_player_name = "None"
    for player in players:
        if player[stat] > max_stat:
          max_stat = player[stat]
          max_player_name = player["Name"]
   
    return  f"The leader in {stat} is {max_player_name} with {max_stat}"

# Method to compute which stats to print

def print_player_info(player):
    if(player['Position'] == "QB"):
        print_stats(player, qb_stats)
    elif(player['Position'] == "RB" or player['Position'] == "WR" or player['Position'] == "TE"):
        print_stats(player, flex_stats)
    elif(player['Position'] == "K"):
        print_stats(player, kicker_stats)

# Loop for printing stats
def print_stats(player, stats):
     for stat in stats:
             print(f'{stat}: {player[stat]}')


# Main Call
main()
