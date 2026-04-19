import random
import pandas as pd
import time

cards = ["Red","Blue","Green","Yellow","Pink","Purple","Orange"]
Card_deck = []
NUM_OF_CARDS = 105
NUM_OF_COLORS = len(cards)
CARDINDEX = 0
Cards_remaining = 105 
for i in range(NUM_OF_CARDS):
    index = random.randint(0,NUM_OF_COLORS-1)
    Card_deck.append(cards[index])


class Player:
    def __init__(self,name,cards,state):
        self.name = name
        self.mycards= []
        self.points = 0
        self.numcards= cards
        self.state = state
    
    def Set_Cards(self):
        global CARDINDEX
        global Cards_remaining
        print(f"Initial cards for {self.name}: [", end=" ")
        for i in range(self.numcards):
            self.mycards.append(Card_deck[CARDINDEX])
            print(f"{self.mycards[i]} ", end = " ")
            if CARDINDEX >= NUM_OF_CARDS-1:
                print("All cards have been allocated")
                return False
            CARDINDEX +=1
            Cards_remaining -=1
        print("]")
        print()
        return True
    
    def Draw_Card(self,index):
        check = False
        for i in range(len(self.mycards)-1,-1,-1):
            if self.mycards[i] == Card_deck[index]:
                self.points +=1
                self.mycards.pop(i)
                self.numcards -=1
                check = True
                break 
        if check:
            self.points +=1
        else:
            self.mycards.append(Card_deck[index])
        print(F"Successfully drawn the card {Card_deck[index]}")

    def Steal_Card(self,Player2):
        flag = False
        for j in range(len(Player2.mycards)-1,-1,-1):
            if(Card_deck[CARDINDEX] == Player2.mycards[j]):
                self.mycards.append(Player2.mycards[j])
                Player2.mycards.pop(j)
                Player2.numcards -=1
                self.numcards +=1
                flag = True
        if flag:
            self.mycards.append(Card_deck[CARDINDEX])
            print(f" {self.name} has Successfully stolen {Card_deck[CARDINDEX]} from {Player2.name}")

        else:
            Player2.mycards.append(Card_deck[CARDINDEX])
            Player2.numcards +=1
            print(f"UNSUCCESSFUL: Player {Player2.name} will have the card {Card_deck[CARDINDEX]}")
class AIPlayer(Player):
    def __init__(self,name,cards,state):
        super().__init__(name,cards,state)

    def Convert_to_dictionary(self,playerarray,index,size):

        colors_dict = {playerarray[i].name: {cards[j%7]:0 for j in range(7)} for i in range(size) if i!= index} 

        return colors_dict

    def AIplay(self,index,numofplayers,playerarray):
        print("AI is thinking...")
        time.sleep(2)
        player_dict = self.Convert_to_dictionary(playerarray,index,numofplayers)
        df = pd.DataFrame(player_dict)
        some_list = Shuffle_list()
        for i in range(len(playerarray)):
            if i == index:
                continue
            for item in playerarray[i].mycards:
                df.loc[item,playerarray[i].name] +=1
        print(df)

        Twoplayerflag = False
        if numofplayers <=2:
            Twoplayerflag = True


        AIdict = {self.name: {cards[j%7]:0 for j in range(7)}}
        dfAI = pd.DataFrame(AIdict)
        for items in self.mycards:
            dfAI.loc[items,self.name] +=1
        if (any(dfAI[self.name][color] >=2 for color in some_list)):
            self.Draw_Card(CARDINDEX)
            return True



        colormax = [df.loc[some_list[0]].idxmax(),
                    df.loc[some_list[1]].idxmax(),
                    df.loc[some_list[2]].idxmax()
                 ]
        colorindexes = [0,0,0]
        for i in range(len(playerarray)):
            if i==index:
                continue
            if (any(df[playerarray[i].name][color] >=4 for color in some_list)):
                self.Steal_Card(playerarray[i])
                return True
            if (any(df[playerarray[i].name][color] >=2 for color in some_list))and (playerarray[i].points >7):
                self.Steal_Card(playerarray[i])
                return True
            
            if playerarray[i].name == colormax[0]:
                colorindexes[0] = i
            if playerarray[i].name == colormax[1]:
                colorindexes[1] = i
            if playerarray[i].name == colormax[2]:
                colorindexes[2] = i
        if(not Twoplayerflag and (colormax[0] == colormax[1] == colormax[2])):
            self.Steal_Card(playerarray[colorindexes[0]])
            return True

        elif(not Twoplayerflag and (df[playerarray[colorindexes[0]].name][some_list[0]] >=3) or (any(df[playerarray[colorindexes[0]].name][color] >=2 for color in some_list) and (playerarray[colorindexes[0]].points >=6))):
            self.Steal_Card(playerarray[colorindexes[0]])
            return True

        elif(not Twoplayerflag and (df[playerarray[colorindexes[1]].name][some_list[1]] >=3) or (any(df[playerarray[colorindexes[1]].name][color] >=2 for color in some_list) and (playerarray[colorindexes[1]].points >=6))):
            self.Steal_Card(playerarray[colorindexes[1]])
            return True

        elif(not Twoplayerflag and (df[playerarray[colorindexes[2]].name][some_list[2]] >=3) or (any(df[playerarray[colorindexes[2]].name][color] >=2 for color in some_list) and (playerarray[colorindexes[2]].points >=6))):
            self.Steal_Card(playerarray[colorindexes[2]])
            return True
        
        self.Draw_Card(CARDINDEX)
        return True


        

        












    
def Shuffle_list():
    flag = True
    while(flag):
        my_list = list(random.sample(cards,2))
        for index in range(0,2):
            if(my_list[index] == Card_deck[CARDINDEX]):
                   break
        else:
                flag = False
    my_list.append(Card_deck[CARDINDEX])
    random.shuffle(my_list)
    print("The following colors are the options [ ", end = " ")
    for i in range(3):
            print(f"{my_list[i]} ", end =" ")
    print(" ]")
    return my_list
        
    



def PrintAllPlayers(players):
    print("\n" + "="*40)
    print(f"{'PLAYER':<12} | {'POINTS':<7} | {'AQUARIUM (CARDS)'}")
    print("-" * 40)
    for p in players:
        print(f"{p.name:<12} | {p.points:<7} | {p.mycards}")
    print("-"*40 + "\n")
print("WELCOME to the Mantis game: You can either choose to play entirely with humans or along with AI!")


Player_record = []


input_validation = True
while(input_validation):
    card_check =  True
    num_players = int(input("Enter number of human players: "))
    ai_player = int(input("Enter number of AI players (if you dont want to play with an AI type 0):  "))
    card_player = int(input("Enter num of cards per player: "))
    for i in range(num_players):
        Player_name = input(f"Enter the name of player {i+1}: ")
        Player0 = Player(Player_name,card_player,"H")
        if (Player0.Set_Cards()):
            Player_record.append(Player0)
        else:
            card_check = False
            break
    if ai_player != 0:
        for i in range(ai_player):
            PlayerAI = AIPlayer(f"AI {i+1}" ,card_player,"AI")
            if (PlayerAI.Set_Cards()):
                Player_record.append(PlayerAI)
            else:
                card_check = False
                break
    if not card_check:
        print("you put too many players/cards per player ! Reduce the amount of players or the amount of cards per player")
    if card_check:
        input_validation = False



game_check = True
order_turn = 0
if card_check:
    while(game_check):
        if CARDINDEX >= NUM_OF_CARDS:
            print("No more cards in the deck!")
            break
        print(f"--- {Player_record[order_turn].name}'s Turn ---")
        my_list = Shuffle_list()
    
        

        valid_input = False
        while not valid_input:
            decision = int(input(f"Pick player to steal from (1-{num_players+ai_player}) or -1 to draw: "))
            
            if decision == (order_turn + 1):
                print("You cannot steal from yourself! Pick someone else.")
            else:
                valid_input = True
                
        if decision == -1:
            Player_record[order_turn].Draw_Card(CARDINDEX)
        else:
            Player_record[order_turn].Steal_Card(Player_record[decision-1])
        
        PrintAllPlayers(Player_record)

        if Player_record[order_turn].points >= 10:
            print(f"YEEESS THE PLAYER {Player_record[order_turn].name} WINS THE GAME !!! HUMANS WONN")
            game_check = False
            break

        CARDINDEX += 1
        order_turn += 1
        if order_turn == num_players:
            order_turn = 0
            for i in range(num_players-1,len(Player_record)):
                if Player_record[i].state == "AI":
                    Player_record[i].AIplay(i,num_players+ai_player,Player_record)

                    PrintAllPlayers(Player_record)
                    if Player_record[i].points >=10:
                        print(f"THE AI {Player_record[i].name} has won the game! Humanity has fallen :( ")
                    CARDINDEX +=1
                    




print("\nGame Over!")





