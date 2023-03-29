import requests
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("Zeri: Riot Api Caller")
windowIconPlacee = PhotoImage(file= "/Users/edo/Desktop/codePy/Zeri/Zeri_0.gif")
backgroundPhotoPlace = PhotoImage(file= "/Users/edo/Desktop/codePy/Zeri/Zeri_1.gif")

root.iconphoto(False, windowIconPlacee)

def hide_button(widget):
    
    widget.pack_forget()
  
  
def show_button(widget):
    widget.pack()

# Adjust size
root.geometry( "1200x750" )#1215 × 717
mystring = StringVar()

labebel_background = Label(root, image=backgroundPhotoPlace)
labebel_background.place(x=0, y=0, relwidth=1, relheight=1)

labelHead = Label(root, text="Enter Summoner name", font=("Helvetica", 35))
labelHead.pack(pady=50)

entry1=Entry(root, textvariable = mystring, width=32)
entry1.pack()




def get_sum_name():  
        summName = entry1.get()
        region = clicked.get()
        l.config( text = region + " " + summName )
        ##summName = input("Type summoner name:\n")
        ##region = input("Type selected region(na1/euw1):\n")
        ##region = "euw1"


        if(region == "euw1"): massregion = "europe"
        if(region == "eun1"): massregion = "europe" 

        if(region == "na1"): massregion = "americas"


        ##Return summoner name and level + get puuid
        print("LOG: Riot Api initialised")
        api_key = "YOUR_API_KEY"#note thats personal dev key lasts 24 h

        ##call summoner 4
        api_url_Summonerv5 = "https://" + region +".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ summName
        api_url_Final_SummonerV5 = api_url_Summonerv5 + '?api_key=' + api_key


        #Summonerv4 
        requests.get(api_url_Final_SummonerV5)
        print("apiLog.summonerv5")
        print(requests.get(api_url_Final_SummonerV5))
                #should be 200
        resprRiotApi = requests.get(api_url_Final_SummonerV5)
        playInfo = resprRiotApi.json()
                ##print(playInfo)
        playlvl = playInfo['summonerLevel']
        EncrId = playInfo['id']
        playName = playInfo['name']
        #print("LOG: Summoner Name : ", playName)
        lname.config(text="Nome dell'evocatore : "+ playName)
        show_button(lname)
        #print("LOG: Summoner Level : ", playlvl)
        llevel.config(text="Livello: "+ str(playlvl))
        show_button(llevel)
        puuid = playInfo['puuid']
                #print(puuid)
        #got puuid



        #call matchv5
        api_url_Final_SummonerV5 = api_url_Summonerv5 + '?api_key=' + api_key
        api_url_Matchv4 = "https://" +massregion + ".api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=20" + '&api_key=' + api_key


        #matchv5light
        requests.get(api_url_Matchv4)
        print("apiLog.matchv4")
        print(requests.get(api_url_Matchv4))   
        respRiotMatchv4 = requests.get(api_url_Matchv4)
        LastGamesId = respRiotMatchv4.json()
        Gameid0 = LastGamesId[0]#<-- last game = 0, second last 1 ...
                #print(Gameid0)


        #call league v4
        api_url_leaguev4 = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + EncrId + '?api_key= ' + api_key
        
        print("apiLog.leaguev4")
        print(requests.get(api_url_Matchv4))
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
        #print("LOG : Rank : ", playerRank, " ", playerDivision, " ", playerPoints, "lp")
        lrank.config(text="\tRank : "+ playerRank + " " + playerDivision + " "+ str(playerPoints)+ "lp\n" + "Totale partite: "+ str(playerWins + playerLoss) + " . Winrate: "+ str((playerWins/(playerLoss+playerWins))*100) + "%")
        #print("LOG: Total games: ", playerWins + playerLoss, " . Winrate: ", (playerWins/(playerLoss+playerWins))*100 , "%")
        show_button(lrank)



        api_url_gameid0 = "https://" + massregion + ".api.riotgames.com/lol/match/v5/matches/" + Gameid0 + '?api_key=' + api_key
        print("apiLog.matchv5.matches")
        print(requests.get(api_url_gameid0))
        respGameid0 = requests.get(api_url_gameid0)
        GameId0info = respGameid0.json()
        GameId0Time = GameId0info['info']['gameDuration']
        #print("LOG: Last game Duration : ", GameId0Time/60, " min")
        lgamedur.config(text="Ultima partita\nGame 1\n"+ str(GameId0Time/60)+ " min")
                #initialise summoner 0 data from last game
        show_button(lgamedur)
        len(GameId0info['info']['participants'])
        player0data = GameId0info['info']['participants'][0]
        player0champion = player0data['championName']
        #print("LOG: Last Champion Played : ", player0champion, "  liv.", player0data['champLevel'], "  ", player0data['totalMinionsKilled']," cs")
        lchamp.config(text="Ultimo campione giocato: "+ player0champion+ "  liv."+ str(player0data['champLevel'])+ "  "+ str(player0data['totalMinionsKilled'])+" cs")
        show_button(lchamp)
        #print(GameId0info['info']['participants'][0]['championName'],"  ", (GameId0info['info']['participants'][0]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][0]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][0]['assists'],"\t",
          #    GameId0info['info']['participants'][5]['championName'],"  ", (GameId0info['info']['participants'][5]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][5]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][5]['assists'],"\n", 
           #   GameId0info['info']['participants'][1]['championName'],"  ", (GameId0info['info']['participants'][1]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][1]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][1]['assists'],"\t", 
            #  GameId0info['info']['participants'][6]['championName'],"  ", (GameId0info['info']['participants'][6]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][6]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][6]['assists'],"\n", 
             # GameId0info['info']['participants'][2]['championName'],"  ", (GameId0info['info']['participants'][2]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][2]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][2]['assists'],"\t", 
              #GameId0info['info']['participants'][7]['championName'],"  ", (GameId0info['info']['participants'][7]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][7]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][7]['assists'],"\n", 
              #GameId0info['info']['participants'][3]['championName'],"  ", (GameId0info['info']['participants'][3]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][3]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][3]['assists'],"\t", 
              #GameId0info['info']['participants'][8]['championName'],"  ", (GameId0info['info']['participants'][8]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][8]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][8]['assists'],"\n", 
              #GameId0info['info']['participants'][4]['championName'],"  ", (GameId0info['info']['participants'][4]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][5]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][4]['assists'],"\t", 
              #GameId0info['info']['participants'][9]['championName'],"  ", (GameId0info['info']['participants'][9]['totalMinionsKilled']/(GameId0Time/60)), " cs/min\t" , GameId0info['info']['participants'][9]['kills'],"/",GameId0info['info']['participants'][0]['deaths'],"/",GameId0info['info']['participants'][9]['assists'],"\n", 

              
              
#              )
        k = player0data['kills']
        d = player0data['deaths']
        a = player0data['assists']
        #print("")
        #print("Kills:", k)
        lkills.config(text="Kills:"+ str(k))
        #print("Deaths:", d)
        show_button(lkills)
        ldeaths.config(text="Morti: " + str(d))
        #print("Assists:", a)
        show_button(ldeaths)
        lassist.config(text="Assists: "+ str(a))
        show_button(lassist)
        #print("KDA:", (k + a) / d)
        lkda.config(text= "KDA:"+ str((k + a) / d))
        show_button(lkda)
        #print("role : "+ player0data['teamPosition'])
        lrole.config(text="Ruolo : "+ player0data['teamPosition'])
        show_button(lrole)



        url_ladder_leaguev4 = "https://" + region + ".api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1" + '&api_key=' +api_key 
        respLadder = requests.get(url_ladder_leaguev4)
        print("apiLog.ladder")
        print(respLadder)
        ladderDta = respLadder.json()
        #print(ladderDta[0]['summonerName'], " ",ladderDta[0]['leaguePoints'], "lp")
        lLadder.config(text="Classifica :\n\n"+ " " +ladderDta[0]['summonerName']+ "                             "+str(ladderDta[0]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[1]['summonerName']+ "                             "+str(ladderDta[1]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[2]['summonerName']+ " \t\t"+str(ladderDta[2]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[3]['summonerName']+ " \t"+str(ladderDta[3]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[4]['summonerName']+ " \t"+str(ladderDta[4]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[5]['summonerName']+ " \t"+str(ladderDta[5]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[6]['summonerName']+ " \t"+str(ladderDta[6]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[7]['summonerName']+ " \t"+str(ladderDta[7]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[8]['summonerName']+ " \t"+str(ladderDta[8]['leaguePoints'])+ "lp\n" +
                       " " +ladderDta[9]['summonerName']+ " \t"+str(ladderDta[9]['leaguePoints'])+ "lp" )
        show_button(lLadder)
        lLadder.pack(side= LEFT, padx=100)
        llasstgame.config(text=GameId0info['info']['participants'][0]['summonerName']+" ("+GameId0info['info']['participants'][0]['championName'] + ")"+  str(GameId0info['info']['participants'][0]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][0]['kills'])+"/"+str(GameId0info['info']['participants'][0]['deaths'])+"/"+str(GameId0info['info']['participants'][0]['assists'])+"\t"+
              GameId0info['info']['participants'][5]['summonerName']+" ("+ GameId0info['info']['participants'][5]['championName'] + ")"+  str(GameId0info['info']['participants'][5]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][5]['kills'])+"/"+str(GameId0info['info']['participants'][5]['deaths'])+"/"+str(GameId0info['info']['participants'][5]['assists'])+"\n"+
              GameId0info['info']['participants'][1]['summonerName']+" ("+GameId0info['info']['participants'][1]['championName'] + ")"+  str(GameId0info['info']['participants'][1]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][1]['kills'])+"/"+str(GameId0info['info']['participants'][1]['deaths'])+"/"+str(GameId0info['info']['participants'][1]['assists'])+"\t"+ 
              GameId0info['info']['participants'][6]['summonerName']+" ("+GameId0info['info']['participants'][6]['championName'] + ")"+str(GameId0info['info']['participants'][6]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][6]['kills'])+"/"+str(GameId0info['info']['participants'][6]['deaths'])+"/"+str(GameId0info['info']['participants'][6]['assists'])+"\n"+ 
              GameId0info['info']['participants'][2]['summonerName']+" ("+GameId0info['info']['participants'][2]['championName'] + ")"+ str(GameId0info['info']['participants'][2]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t\t" + str(GameId0info['info']['participants'][2]['kills'])+"/"+str(GameId0info['info']['participants'][2]['deaths'])+"/"+str(GameId0info['info']['participants'][2]['assists'])+"\t"+ 
              GameId0info['info']['participants'][7]['summonerName']+" ("+GameId0info['info']['participants'][7]['championName'] + ")"+  str(GameId0info['info']['participants'][7]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][7]['kills'])+"/"+str(GameId0info['info']['participants'][7]['deaths'])+"/"+str(GameId0info['info']['participants'][7]['assists'])+"\n"+ 
              GameId0info['info']['participants'][3]['summonerName']+" ("+GameId0info['info']['participants'][3]['championName'] + ")"+   str(GameId0info['info']['participants'][3]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][3]['kills'])+"/"+str(GameId0info['info']['participants'][3]['deaths'])+"/"+str(GameId0info['info']['participants'][3]['assists'])+"\t"+ 
              GameId0info['info']['participants'][8]['summonerName']+" ("+GameId0info['info']['participants'][8]['championName'] + ")"+ str(GameId0info['info']['participants'][8]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][8]['kills'])+"/"+str(GameId0info['info']['participants'][8]['deaths'])+"/"+str(GameId0info['info']['participants'][8]['assists'])+"\n"+ 
              GameId0info['info']['participants'][4]['summonerName']+" ("+GameId0info['info']['participants'][4]['championName'] + ")"+ str(GameId0info['info']['participants'][4]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][4]['kills'])+"/"+str(GameId0info['info']['participants'][4]['deaths'])+"/"+str(GameId0info['info']['participants'][9]['assists'])+"\t"+
              GameId0info['info']['participants'][9]['summonerName']+" ("+GameId0info['info']['participants'][9]['championName'] + ")"+ str(GameId0info['info']['participants'][9]['totalMinionsKilled']/(GameId0Time/60))+ " cs/min\t" + str(GameId0info['info']['participants'][9]['kills'])+"/"+str(GameId0info['info']['participants'][9]['deaths'])+"/"+str(GameId0info['info']['participants'][9]['assists']))
        
        #gg =GameId0info['info']['participants'][1].keys() 
        #print(gg) 
                
  
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
button = Button( root , text = "Continue " , command=get_sum_name, width=12)
button.pack()
# Create Label
l = Label( root )
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
lrole = Label(root,)
lrole.pack()
lLadder = Label(root)
lLadder.pack(side= LEFT, padx=100)
llasstgame =Label(root)
llasstgame.pack(side=BOTTOM)


hide_button(lname)
hide_button(llevel)
hide_button(lrank)
hide_button(ltotgames)
hide_button(lgamedur)
hide_button(lchamp)
hide_button(lkills)
hide_button(ldeaths)
hide_button(lassist)
hide_button(lkda)
hide_button(lrole)
hide_button(lLadder)

root.mainloop()
