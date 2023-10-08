# Get data
import requests
key = 'e538a8055c054c5c9190f2e7ba766a9e'
header = {'Ocp-Apim-Subscription-Key': key}
url = 'https://api.sportsdata.io/api/nfl/fantasy/json/PlayerSeasonStats/2023'
response = requests.get(url, headers = header)
data = response.json()
all_players = []

flex_stats = ['Name', "Team", "Played",'RushingAttempts',"RushingYards","RushingYardsPerAttempt","RushingTouchdowns","RushingLong","ReceivingTargets","Receptions","ReceivingYards","ReceivingYardsPerReception","ReceivingTouchdowns","ReceivingLong"]
kicker_stats = ['Name', "Team", "Played",'FieldGoalsAttempted',"FieldGoalsMade","ExtraPointsMade","FieldGoalsMade0to19","FieldGoalsMade20to29","FieldGoalsMade30to39","FieldGoalsMade40to49","FieldGoalsMade50Plus"]
qb_stats = ['Name', "Team", "Played",'PassingAttempts', 'PassingCompletions', 'PassingYards',"PassingLong", 'PassingCompletionPercentage','PassingTouchdowns','PassingInterceptions','PassingRating','RushingYards','RushingAttempts',"RushingLong",'RushingTouchdowns',"PassingSacks"]

qb_compare = ['Name',"Played",'PassingAttempts', 'PassingCompletions', 'PassingYards',"PassingLong", 'PassingCompletionPercentage','PassingTouchdowns','PassingInterceptions','PassingRating','RushingYards','RushingAttempts',"RushingLong",'RushingTouchdowns',"PassingSacks"]

def main():
     call = input("What would you like to do with Football Data? \n (P) = Get Player data \n (C) = Compare Player Data")
     if call == "P":
          player = player_input()
          print_player_info(player)
        
          
def player_input():
    player_name = input('Which Player would you like data about?\n Please input in the following format: \n First initial Capitalized followed by ".", then last name Capitilized with NO SPACES. \n Example for Aaron Rodgers: A.Rodgers \n')
    if valid_name(player_name):
         return get_player(player_name)
    else:
         player_input()
   
  
def compare_player():
     player1_name = input('Which is the first player you would like data about?\n')
     player2_name = input('Which is the second player you would like data about?\n')
     player1 = get_player(player1_name)
     player2 = get_player(player2_name)
     if (player1['Position'] != player2['Position']):
          print("The players must be of the same position")
     else:
          print("else")
          

def get_player(player_name):
    for player in data:
        if(player_name == player['Name']):
            return player
        else:
             print("That player does not exist")
        
def print_player_info(player):
    if(player['Position'] == "QB"):
        print_stats(player, qb_stats)
    elif(player['Position'] == "RB" or player['Position'] == "WR" or player['Position'] == "TE"):
        print_stats(player, flex_stats)
    elif(player['Position'] == "K"):
        print_stats(player, kicker_stats)

def print_stats(player, stats):
     for stat in stats:
             print(f'{stat}: {player[stat]}')

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
          


main()
