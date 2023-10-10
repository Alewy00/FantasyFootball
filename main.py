# Get data
import requests
key = 'e538a8055c054c5c9190f2e7ba766a9e'
header = {'Ocp-Apim-Subscription-Key': key}
url = 'https://api.sportsdata.io/api/nfl/fantasy/json/PlayerSeasonStats/2023'
response = requests.get(url, headers = header)
data = response.json()


flex_stats = ['Name', "Team", "Played",'RushingAttempts',"RushingYards","RushingYardsPerAttempt","RushingTouchdowns","RushingLong","ReceivingTargets","Receptions","ReceivingYards","ReceivingYardsPerReception","ReceivingTouchdowns","ReceivingLong"]
kicker_stats = ['Name', "Team", "Played",'FieldGoalsAttempted',"FieldGoalsMade","ExtraPointsMade","FieldGoalsMade0to19","FieldGoalsMade20to29","FieldGoalsMade30to39","FieldGoalsMade40to49","FieldGoalsMade50Plus"]
qb_stats = ['Name', "Team", "Played",'PassingAttempts', 'PassingCompletions', 'PassingYards',"PassingLong", 'PassingCompletionPercentage','PassingTouchdowns','PassingInterceptions','PassingRating','RushingYards','RushingAttempts',"RushingLong",'RushingTouchdowns',"PassingSacks"]

qb_compare = ["Played",'PassingAttempts', 'PassingCompletions', 'PassingYards',"PassingLong", 'PassingCompletionPercentage','PassingTouchdowns','PassingInterceptions','PassingRating','RushingYards','RushingAttempts',"RushingLong",'RushingTouchdowns',"PassingSacks"]
flex_compare = [ "Played",'RushingAttempts',"RushingYards","RushingYardsPerAttempt","RushingTouchdowns","RushingLong","ReceivingTargets","Receptions","ReceivingYards","ReceivingYardsPerReception","ReceivingTouchdowns","ReceivingLong"]
kicker_compare = [ "Played",'FieldGoalsAttempted',"FieldGoalsMade","ExtraPointsMade","FieldGoalsMade0to19","FieldGoalsMade20to29","FieldGoalsMade30to39","FieldGoalsMade40to49","FieldGoalsMade50Plus"]

players = []

def main():
     global players
     players = []
     call = input("What would you like to do with Football Data? \n (P) = Get Player data \n (C) = Compare Player Data \n (Q) = Quit \n")
     if call == "P":
          player = player_input()
          print_player_info(player)
     elif(call == "C"):
          add_players()
     elif(call == "Q"):
          return True
         
          
def player_input():
    player_name = input('Which Player would you like data about?\n Please input in the following format: \n First initial Capitalized followed by ".", then last name Capitilized with NO SPACES. \n Example for Aaron Rodgers: A.Rodgers \n')
    while(valid_name(player_name) == False):
        player_name = input('Which Player would you like data about?\n Please input in the following format: \n First initial Capitalized followed by ".", then last name Capitilized with NO SPACES. \n Example for Aaron Rodgers: A.Rodgers \n')
    player = get_player(player_name)
    return player
    
   
 
def compare_players():
     compared = []
     position_to_comp = players[0]["Position"]
     comp_list = ''
     if(position_to_comp == "QB"):
        comp_list = qb_compare
     elif(position_to_comp == "RB" or position_to_comp == "WR" or position_to_comp == "TE"):
        comp_list = flex_compare
     elif(position_to_comp == "K"):
        comp_list = kicker_compare

     for stat in comp_list:
          compared.append(get_max(stat))
     for max_stat in compared:
          print(max_stat)
     main()
     

def get_max(stat):
    max_stat = 0
    max_player_name = "None"
    for player in players:
        if player[stat] > max_stat:
          max_stat = player[stat]
          max_player_name = player["Name"]
   
    return  f"The leader in {stat} is {max_player_name} with {max_stat}"


     
     

def add_players():
      print(f"Adding the number {len(players) + 1} player to Compare \n")
      player = player_input()
      if len(players) == 0:
            players.append(player)
      elif(player['Position'] != players[0]['Position']):
            print("The players must be of the same position")
            add_players()
      elif(player['Position'] == players[0]['Position']):
        players.append(player)
      if(len(players) > 1):
        keep_compare()
      else:
           add_players()
    


     
           
def keep_compare():
     next_step = input("Would you like to add another player? \n (Y) = Yes \n (N) = No \n")
     if next_step == "Y":
           add_players()
     elif next_step == "N":
            compare_players()
     else:
          print("invalid input!")
          keep_compare()
     
def get_player(player_name):
    all_players = []
    for player in data:
        if(player_name == player['Name']):
            all_players.append(player)
    if len(all_players) == 1:
        return all_players[0]
    elif (len(all_players) > 1):
       return multiple_players(all_players)
    print("That player does not exist")
    return player_input()

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
