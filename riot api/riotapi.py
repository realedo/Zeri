import requests
from tkinter import *

    


summName = input("Type summoner name:\n")
region = input("Type selected region(na1/euw1):\n")

if(region == "euw1"): massregion = "europe"
if(region == "na1"): massregion = "americas"


##Return summoner name and level + get puuid
print("Riot Api initialised")
api_key = "RGAPI-5203d6f7-ed60-45c5-b24f-61866599f722"#note thats personal dev key

##call summoner 4
api_url_Summonerv5 = "https://" + region +".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ summName
api_url_Final_SummonerV5 = api_url_Summonerv5 + '?api_key=' + api_key


#Summonerv4 
requests.get(api_url_Final_SummonerV5)
        #print("Summonerv5 api Connection status : ")
        #print(requests.get(api_url_Final_SummonerV5))
        #should be 200
resprRiotApi = requests.get(api_url_Final_SummonerV5)
playInfo = resprRiotApi.json()
        ##print(playInfo)
playlvl = playInfo['summonerLevel']
EncrId = playInfo['id']
playName = playInfo['name']
print("Summoner Name : ", playName)
print("Summoner Level : ", playlvl)
puuid = playInfo['puuid']
        #print(puuid)
#got puuid



#call matchv5
api_url_Final_SummonerV5 = api_url_Summonerv5 + '?api_key=' + api_key
api_url_Matchv4 = "https://" +massregion + ".api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=20" + '&api_key=' + api_key


#matchv5light
requests.get(api_url_Matchv4)
        #print("Matchv4 api Connection Status : ")
        #print(requests.get(api_url_Matchv4))   
respRiotMatchv4 = requests.get(api_url_Matchv4)
LastGamesId = respRiotMatchv4.json()
Gameid0 = LastGamesId[0]#<-- last game = 0, second last 1 ...
        #print(Gameid0)


#call league v4
api_url_leaguev4 = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + EncrId + '?api_key= ' + api_key

        ##print(requests.get(api_url_Matchv4))
leaguev4Resp = requests.get(api_url_leaguev4)
leaguev4Data = leaguev4Resp.json()
testinfo = leaguev4Data[0]
##print(testinfo)
##print(leaguev4Data)
playerRank = testinfo['tier']
playerDivision = testinfo['rank']
playerPoints = testinfo['leaguePoints']
playerWins = testinfo['wins']
playerLoss = testinfo['losses']
print("Rank : ", playerRank, " ", playerDivision, " ", playerPoints, "lp")
print("Total games: ", playerWins + playerLoss, " . Winrate: ", (playerWins/(playerLoss+playerWins))*100 , "%")



api_url_gameid0 = "https://" + massregion + ".api.riotgames.com/lol/match/v5/matches/" + Gameid0 + '?api_key=' + api_key
        #print("game id 0 Connection status : ")
        #print(requests.get(api_url_gameid0))
respGameid0 = requests.get(api_url_gameid0)
GameId0info = respGameid0.json()
GameId0Time = GameId0info['info']['gameDuration']
print("Last game Duration : ", GameId0Time/60, " min")
        #initialise summoner 0 data from last game
len(GameId0info['info']['participants'])
player0data = GameId0info['info']['participants'][0]
player0champion = player0data['championName']
print("Last Champion Played : ", player0champion, "  liv.", player0data['champLevel'], "  ", player0data['totalMinionsKilled']," cs")
k = player0data['kills']
d = player0data['deaths']
a = player0data['assists']
print("")
print("Kills:", k)
print("Deaths:", d)
print("Assists:", a)
print("KDA:", (k + a) / d)
print("role : "+ player0data['teamPosition']) 



