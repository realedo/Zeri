import requests
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("Zeri: Riot Api Caller")
windowIconPlacee = PhotoImage(file= "Zeri_0.gif")
backgroundPhotoPlace = PhotoImage(file= "Zeri_1.gif")

root.iconphoto(False, windowIconPlacee)



# Adjust size
root.geometry( "1200x700" )#1215 × 717
mystring = StringVar()

labebel_background = Label(root, image=backgroundPhotoPlace)
labebel_background.place(x=0, y=0, relwidth=1, relheight=1)

labelHead = Label(root, text="Enter Summoner name", font=("Helvetica", 35))
labelHead.pack(pady=50)

entry1=Entry(root, textvariable = mystring, width=35)
entry1.pack()


def get_sum_name():  
        summName = entry1.get()
        region = clicked.get()
        l.config( text = region + " " + summName )
        ##summName = input("Type summoner name:\n")
        ##region = input("Type selected region(na1/euw1):\n")
        ##region = "euw1"


        if(region == "euw1"): massregion = "europe"
        #if(region == "eun1"): massregion = "europe" 
        if(region == "na1"): massregion = "americas"


        ##Return summoner name and level + get puuid
        print("Riot Api initialised")
        api_key = "RGAPI-85832f67-094d-4efc-a8a7-25796ba7fed4"#note thats personal dev key

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
        lname.config(text="Summoner Name : "+ playName)
        print("Summoner Level : ", playlvl)
        llevel.config(text="Summoner Level : "+ str(playlvl))
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
        lrank.config(text="Rank : "+ playerRank + " " + playerDivision + " "+ str(playerPoints)+ "lp\n" + "Total games: "+ str(playerWins + playerLoss) + " . Winrate: "+ str((playerWins/(playerLoss+playerWins))*100) + "%")
        print("Total games: ", playerWins + playerLoss, " . Winrate: ", (playerWins/(playerLoss+playerWins))*100 , "%")
        



        api_url_gameid0 = "https://" + massregion + ".api.riotgames.com/lol/match/v5/matches/" + Gameid0 + '?api_key=' + api_key
                #print("game id 0 Connection status : ")
                #print(requests.get(api_url_gameid0))
        respGameid0 = requests.get(api_url_gameid0)
        GameId0info = respGameid0.json()
        GameId0Time = GameId0info['info']['gameDuration']
        print("Last game Duration : ", GameId0Time/60, " min")
        lgamedur.config(text="Last game Duration : "+ str(GameId0Time/60)+ " min")
                #initialise summoner 0 data from last game
        len(GameId0info['info']['participants'])
        player0data = GameId0info['info']['participants'][0]
        player0champion = player0data['championName']
        print("Last Champion Played : ", player0champion, "  liv.", player0data['champLevel'], "  ", player0data['totalMinionsKilled']," cs")
        lchamp.config(text="Last Champion Played : "+ player0champion+ "  liv."+ str(player0data['champLevel'])+ "  "+ str(player0data['totalMinionsKilled'])+" cs")
        k = player0data['kills']
        d = player0data['deaths']
        a = player0data['assists']
        print("")
        print("Kills:", k)
        lkills.config(text="Kills:"+ str(k))
        print("Deaths:", d)
        ldeaths.config(text="Deaths: " + str(d))
        print("Assists:", a)
        lassist.config(text="Assists: "+ str(a))
        print("KDA:", (k + a) / d)
        lkda.config(text= "KDA:"+ str((k + a) / d))
        print("role : "+ player0data['teamPosition'])
        lrole.config(text="Role : "+ player0data['teamPosition'])
        
        url_ladder_leaguev4 = "https://" + region + ".api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1" + '&api_key=' +api_key 
        respLadder = requests.get(url_ladder_leaguev4)
        print(respLadder)
        ladderDta = respLadder.json()
        print(ladderDta[0]['summonerName'], " ",ladderDta[0]['leaguePoints'], "lp")
        lLadder.config(text="Top ranked players:\n\n"+ " " +ladderDta[0]['summonerName']+ "                             "+str(ladderDta[0]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[1]['summonerName']+ "                             "+str(ladderDta[1]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[2]['summonerName']+ " \t\t"+str(ladderDta[2]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[3]['summonerName']+ " \t"+str(ladderDta[3]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[4]['summonerName']+ " \t"+str(ladderDta[4]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[5]['summonerName']+ " \t"+str(ladderDta[5]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[6]['summonerName']+ " \t"+str(ladderDta[6]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[7]['summonerName']+ " \t"+str(ladderDta[7]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[8]['summonerName']+ " \t"+str(ladderDta[8]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[9]['summonerName']+ " \t"+str(ladderDta[9]['leaguePoints'])+ "lp" )


         
        
    
  
# Dropdown menu optiona
options = [
    "euw1",
    "na1",
    "eun1"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set("dunno why it does not work")
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack(pady=10)
  
# Create button, it will change label text
button = Button( root , text = "Continue " , command=get_sum_name )
button.pack()
# Create Label
l = Label( root , text = "" )
l.pack()
lname = Label(root, text= "")
lname.pack()
llevel = Label(root, text= "")
llevel.pack()    
lrank = Label(root)
lrank.pack()
ltotgames = Label(root)
ltotgames.pack()
lgamedur = Label(root)
lgamedur.pack()
lchamp = Label(root)
lchamp.pack()
lkills = Label(root)
lkills.pack()
ldeaths = Label(root)
ldeaths.pack()
lassist = Label(root)
lassist.pack()
lkda = Label(root)
lkda.pack()
lrole = Label(root)
lrole.pack()
lLadder = Label(root)
lLadder.pack(side= LEFT, padx=100)




root.mainloop()