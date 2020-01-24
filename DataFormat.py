
# coding: utf-8

# In[1]:


import json
import csv


# In[2]:


# Only import one of the following leagues at a time


# In[3]:


# Euro 2016
# Read event JSON file
with open('/Users/JordanKruguer/Desktop/events/events_European_Championship.json', 'r') as myfile1:
    dataEvents=myfile1.read()

# Read match JSON file
with open('/Users/JordanKruguer/Desktop/matches/matches_European_Championship.json', 'r') as myfile2:
    dataMatches=myfile2.read()


# In[2]:


# Premier League - England
# Read event JSON file
with open('/Users/JordanKruguer/Desktop/events/events_England.json', 'r') as myfile1:
    dataEvents=myfile1.read()

# Read match JSON file
with open('/Users/JordanKruguer/Desktop/matches/matches_England.json', 'r') as myfile2:
    dataMatches=myfile2.read()


# In[2]:


# Ligue 1 - France 
# Read event JSON file
with open('/Users/JordanKruguer/Desktop/events/events_France.json', 'r') as myfile1:
    dataEvents=myfile1.read()

# Read match JSON file
with open('/Users/JordanKruguer/Desktop/matches/matches_France.json', 'r') as myfile2:
    dataMatches=myfile2.read()


# In[2]:


# Germany 
# Read event JSON file
with open('/Users/JordanKruguer/Desktop/events/events_Germany.json', 'r') as myfile1:
    dataEvents=myfile1.read()

# Read match JSON file
with open('/Users/JordanKruguer/Desktop/matches/matches_Germany.json', 'r') as myfile2:
    dataMatches=myfile2.read()


# In[2]:


# Italy 
# Read event JSON file
with open('/Users/JordanKruguer/Desktop/events/events_Italy.json', 'r') as myfile1:
    dataEvents=myfile1.read()

# Read match JSON file
with open('/Users/JordanKruguer/Desktop/matches/matches_Italy.json', 'r') as myfile2:
    dataMatches=myfile2.read()


# In[2]:


# Spain 
# Read event JSON file
with open('/Users/JordanKruguer/Desktop/events/events_Spain.json', 'r') as myfile1:
    dataEvents=myfile1.read()

# Read match JSON file
with open('/Users/JordanKruguer/Desktop/matches/matches_Spain.json', 'r') as myfile2:
    dataMatches=myfile2.read()


# In[3]:


# Parse event JSON file --> Convert to list of dictionaries 
leagueData = json.loads(dataEvents)

# Parse matches JSON file --> Convert to list of dictionaries 
matchData = json.loads(dataMatches)


# In[4]:


# Compile dict of team dicts
teamStats = {}
for event in leagueData: # New dictionary for relevent data
    if event['teamId'] not in teamStats.keys():
        teamStats[event['teamId']] = {}
        


# In[5]:


# All Event Types 
eventTypes = {}
for event in leagueData:
    if event['eventName'] not in eventTypes.keys():
        eventTypes[event['eventName']] = 0
print(eventTypes)


# In[6]:


# All subEvent Types 
subEventTypes = {}
for event in leagueData:
    if event['subEventName'] not in subEventTypes.keys():
        subEventTypes[event['subEventName']] = 0
print(subEventTypes)


# In[7]:


# Add relevant keys to each team
for team in teamStats:
    # Passes
    teamStats[team]['numShortPassesPerGame'] = 0
    teamStats[team]['numLongPassesPerGame'] = 0
    teamStats[team]['totPassesPerGame'] = 0
    
    # Duels + Fouls + Offsides
    teamStats[team]['numOffDuelsPerGame'] = 0
    teamStats[team]['numDefDuelsPerGame'] = 0
    teamStats[team]['numFoulsPerGame'] = 0
    teamStats[team]['numOffsidesPerGame'] = 0
    
    # Shots
    teamStats[team]['numShotsPerGame'] = 0
    teamStats[team]['numFreeKicksPerGame'] = 0
    
    # Touches 
    teamStats[team]['numTouchesPerGame'] = 0
    
    # Wins
    teamStats[team]['numWins'] = 0
    


# In[8]:


# Compile Xs data
for event in leagueData:
    
    # Passes 
    if event['eventName'] == 'Pass':
        teamStats[event['teamId']]['totPassesPerGame'] += 1
        if event['subEventName'] == 'Simple pass' or event['subEventName'] == 'Smart pass':
            teamStats[event['teamId']]['numShortPassesPerGame'] += 1
        elif event['subEventName'] == 'High pass':
            teamStats[event['teamId']]['numLongPassesPerGame'] += 1
        
    # Duels
    if event['eventName'] == 'Duel':
        if event['subEventName'] == 'Ground attacking duel':
            teamStats[event['teamId']]['numOffDuelsPerGame'] += 1
        elif event['subEventName'] == 'Ground defending duel':
            teamStats[event['teamId']]['numDefDuelsPerGame'] += 1
        
    # Fouls
    if event['eventName'] == 'Foul':
        teamStats[event['teamId']]['numFoulsPerGame'] += 1

    # Offsides
    if event['eventName'] == 'Offside':
        teamStats[event['teamId']]['numOffsidesPerGame'] += 1
    
    # Shots
    if event['eventName'] == 'Shot':
        teamStats[event['teamId']]['numShotsPerGame'] += 1
        
    # Freekicks
    if event['eventName'] == 'Free Kick':
        teamStats[event['teamId']]['numFreeKicksPerGame'] += 1

    # Touches
    if event['eventName'] == 'Others on the ball':
        if event['subEventName'] == 'Touch':
            teamStats[event['teamId']]['numTouchesPerGame'] += 1
            
            


# In[9]:


# Wins
teamStats[team]['numWins'] = 0

# Get Y data i.e. number of wins
for match in matchData:
    if match['winner'] in teamStats.keys():
        teamStats[match['winner']]['numWins'] += 1


# In[10]:


for team in teamStats:
    numGames = 0
    for match in matchData:
        if str(team) in match['teamsData'].keys():
            numGames+=1
    if team == 9905:
        print(numGames)
    # Passes
    teamStats[team]['numShortPassesPerGame'] = teamStats[team]['numShortPassesPerGame']/numGames
    teamStats[team]['numLongPassesPerGame'] = teamStats[team]['numLongPassesPerGame']/numGames
    teamStats[team]['totPassesPerGame'] = teamStats[team]['totPassesPerGame']/numGames
    
    # Duels + Fouls + Offsides
    teamStats[team]['numOffDuelsPerGame'] = teamStats[team]['numOffDuelsPerGame']/numGames
    teamStats[team]['numDefDuelsPerGame'] = teamStats[team]['numDefDuelsPerGame']/numGames
    teamStats[team]['numFoulsPerGame'] = teamStats[team]['numFoulsPerGame']/numGames
    teamStats[team]['numOffsidesPerGame'] = teamStats[team]['numOffsidesPerGame']/numGames
    
    # Shots
    teamStats[team]['numShotsPerGame'] = teamStats[team]['numShotsPerGame']/numGames
    teamStats[team]['numFreeKicksPerGame'] = teamStats[team]['numFreeKicksPerGame']/numGames
    
    # Touches 
    teamStats[team]['numTouchesPerGame'] = teamStats[team]['numTouchesPerGame']/numGames

    


# In[11]:


# Write CSV file
teamList = []
for i in teamStats.keys():
    teamList.append(i)

with open('Spain.csv', 'w', newline='') as file: # Change name for league
    writer = csv.writer(file)
    writer.writerow(['Team', 'Short Passes Per Game','Long Passes Per Game','Total Passes Per Game','Off Duels Per Game','Def. Duels Per Game','Fouls Per Game','Offsides Per Game','Shots Per Game','Free Kicks Per Game','Touches Per Game','Wins'])
    count = 0
    for team in teamStats:
        writer.writerow([teamList[count],(teamStats[team]['numShortPassesPerGame']),(teamStats[team]['numLongPassesPerGame']),(teamStats[team]['totPassesPerGame']),(teamStats[team]['numOffDuelsPerGame']),(teamStats[team]['numDefDuelsPerGame']),(teamStats[team]['numFoulsPerGame']),(teamStats[team]['numOffsidesPerGame']),(teamStats[team]['numShotsPerGame']),(teamStats[team]['numFreeKicksPerGame']),(teamStats[team]['numTouchesPerGame']),(teamStats[team]['numWins'])])
        count += 1

