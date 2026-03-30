# UPDATE LOG
# Version 1.1, finished on the date: 26/03/2026
# -basic system and fuctions
# -more coming soon
# 
# Version 1.2, finished on the date: 28/03/2026
# -black market
# -first scroll
#
#Version 1.3, finsihed on the date:
# -black market actually working
# -new items
# -relics

import random as r
import time
import os

# used this for bolding text, ai-generated
B = '\033[1m'
E = '\033[0m'

os.system("color")
# also the system color thingy cuz i didnt know how to do that

# so like i like to leave my variable stuff at the start and ye
player = {"money" : r.randint(30, 37) ,
          "inventory" : {"bread" : 0,
                         "potion" : 0,
                         "sword" : 0,
                         "aetherium": 0,
                         "dragonegg": 0
                         },
          "relics" : {"a pair of dice": False,
                      "shiny coin": False}
                         
}
#------------------------------------------------------------------------------------------------
thingy = [0, 0, 0, 0, 0, 1, 1, 2]
thingy2 = ["apairofdice", "shinycoin"]

blmk_stocknprice = {"relics":{"apairofdice" : {"stock":1, "price":5750},
                              "shinycoin":{"stock": 1, "price":6000},
                              "n/a":{"stock":"n/a", "price":"n/a"}},
                    "items":{"dragonegg":{"stock":int(r.choice(thingy)), "price":r.randint(1750,3500)},
                             "aetherium":{"stock":r.randint(1,4), "price":r.randint(950,2000)}},
                    "onstockrelic": r.choice(thingy2)}
#------------------------------------------------------------------------------------------------
mk_stocknprice = {"bread" : {"stock":r.randint(2,6), "price":r.randint(10,25)},
                  "potion" : {"stock":r.randint(1,3), "price":r.randint(110,150)},
                  "sword" : {"stock":r.randint(0,2), "price":r.randint(550,830)}}

# ignore mk_opt will be used for something in da future
game_sys = {"blmk_unlock" : False,
            "day" : 1,
            "day2tax" : 3,
            "mk_opt" : ["w","b","s","*","e"],
            "scrolls" : {"darkscroll":False},
            "blmkactivate" : False
            }
 
user_input = 0

def scroll_darkscroll():
    lines = [
        f"Three steps {B}forward{E}, none to the rear,",
        "I shift the truth to hide what's here.",
        "A trio of turns makes A into D,",
        "Slide the alphabet to talk to me.",
        "Where the alleys dim and the laws blind,",
        "The shadowed stalls won't speak a word,",
        "Unless this secret shift is heard:",
        "",
        f"{B}EODFNPDUNHW{E}"
    ]

    WIDTH = 60 

    os.system("cls")
    print(r"      _______________________________________________________________")
    print(r"     ()______________________________________________________________) ")
    print(r"      |                                                              |")

    for line in lines:
        visible_len = len(line.replace(B, "").replace(E, ""))
        total_padding = WIDTH - visible_len
        left_pad = total_padding // 2
        right_pad = total_padding - left_pad
        
        print(f"      | {' ' * left_pad}{line}{' ' * (right_pad)} |")

    print(r"      |                                                              |")
    print(r"      |______________________________________________________________|")
    print(r"     ()______________________________________________________________) ")
    print("")
    blmk_arg = input("'ENTER' to continue, or answer it:").lower().replace(" ","")
    if blmk_arg != "blackmarket":
        time.sleep(0.5)
    else:
        game_sys['blmk_unlock'] = True
        time.sleep(0.5)
        return
    
scroll = {"darkscroll" : scroll_darkscroll} 

def reset_market():
    """Finish balck market restock system"""
    for stuff in mk_stocknprice:
        if "bread" in stuff:
            mk_stocknprice[stuff]["stock"] = r.randint(2,6)
            mk_stocknprice[stuff]["price"] = r.randint(10,25)
        elif "potion" in stuff:
            mk_stocknprice[stuff]["stock"] = r.randint(1,3)
            mk_stocknprice[stuff]["price"] = r.randint(110,150)
        elif "sword" in stuff:
            mk_stocknprice[stuff]["stock"] = r.randint(0,2)
            mk_stocknprice[stuff]["price"] = r.randint(550,830)
    
    for stuff2 in blmk_stocknprice["items"]:
        if "aetherium" in stuff2:
            blmk_stocknprice["items"][stuff2]["stock"] = r.randint(1,4)
            blmk_stocknprice["items"][stuff2]["price"] = r.randint(950,2000)
        elif "dragonegg" in stuff2:
            blmk_stocknprice["items"][stuff2]["stock"] = int(r.choice(thingy))
            blmk_stocknprice["items"][stuff2]["price"] = r.randint(1750,3500)

#--------------------------------------------------------------------------------
    for stuff3 in blmk_stocknprice["relics"]:
        try:
            if blmk_stocknprice["relics"][stuff3]["stock"] == 0:
                thingy2.remove(stuff3)
        except:
            pass
#--------------------------------------------------------------------------------

    if len(thingy2) == 0:
        thingy2.append("n/a")

    blmk_stocknprice["onstockrelic"] = r.choice(thingy2)

    game_sys["day2tax"] -= 1
    if game_sys["day2tax"] <= 0:
        game_sys["day2tax"] = 4


# this art is also ai generated but only the art (cant draw chat)
def inventory():
    global scroll
    os.system("cls")
    print(r"""       _____________
      /             \
     /   _________   \
    |   /         \   |
    |  |           |  |
    |   \____0____/   |
    |   [||]   [||]   |
    |   |__|   |__|   |
    \_________________/
     (_______________)
""")
    print(f"{B}----+----INVENTORY----+----{E}")
    print("")
    print(f"{B}     --Common Items--{E}")
    print(f"Bread: {player['inventory']['bread']} ")
    print(f"Potion: {player['inventory']['potion']} ")
    print(f"Sword: {player['inventory']['sword']} ")
    print(f"Aetherium: {player['inventory']['aetherium']} ")
    print(f"Dragon Egg: {player['inventory']['dragonegg']} ")
    print("")
    print(f"{B}       --Scrolls--{E}")

    try:
        for s,s2 in game_sys["scrolls"].items():
            if s2 == True:
                print(f"📜 {s.title()}")
    except:
        pass
# ---------------------------------------------------
    print("")
    user_input_inv = input("'ENTER' to exit back to the main screen, or enter the name of a scroll to read it:").replace(" ", "").lower()
# ---------------------------------------------------
    if user_input_inv in game_sys["scrolls"] and game_sys["scrolls"][user_input_inv] == True:
        scroll[user_input_inv]()
        

def tutorial_screen():
    os.system("cls")
    print("Welcome to Hung's 'Stock I Guess' game!")
    print("""* for tutorial screen
    e for inventory
    b for buy(more about that in the commands thingy)
    w for wait (passes a day)
    s for sell""")
    
    print("")
    print(f"{B}--+--HOW TO PLAY--+--")
    print(f"My new system runs on a 'command system' like that of a (blue app) bot's:")
    print("input as so: (ACTION) (ITEM) (AMOUNT), e.g. b bread 2 or s bread 5")
    print("special inputs such as * and w does not need to be follow by anything, just themselves")
    input("'ENTER' to continue, tutorial may be acessed again via inputting * in the main input. Good luck!")

def game():
    if game_sys["blmkactivate"] == False:
        print(f"{game_sys['day2tax']} days until tax (18%)")
        print(f"day: {game_sys['day']}")
        print(f"${player["money"]}")
        print(fr"""
      _______________________________________
     /                                       \

    |   ___________________________________   |
    |  |                                   |  |
    |  |           GENERAL STORE           |  |
    |  |___________________________________|  |
    |                                         |
    |    [ITEM]        [PRICE]      [STOCK]   |
    |   1. Bread        ${mk_stocknprice['bread']['price']}            {mk_stocknprice['bread']['stock']}      |
    |   2. Potion       ${mk_stocknprice['potion']['price']}           {mk_stocknprice['potion']['stock']}      |
    |   3. Sword        ${mk_stocknprice['sword']['price']}           {mk_stocknprice['sword']['stock']}      |
    |_________________________________________|
    |___|___|___|___|___|___|___|___|___|___|_|
      |                                     |
      |      [B]uy    [S]ell    [W]ait      |
      |_____________________________________| 
    """)
    print("* for tutorial, e for inventory")
    if game_sys["blmk_unlock"] == True:
        print("'blmk' to enter the black market")
    
    if game_sys["day"] >= 50:
            game_sys["scrolls"]["darkscroll"] = True

    main_input_logic()

    if game_sys["blmkactivate"] == True:
        black_market()
        
def main_input_logic():

    try:
        user_input = input(">>>:").strip().lower().split()
        action = user_input[0]
            
    except:
        print("Invalid Input!")
        time.sleep(0.5)
        return
    
    if game_sys["blmkactivate"] == False:

        if len(user_input) == 1:
        
            if action == "*":
                tutorial_screen()

            elif action == "e":
                inventory()

            elif action == "w":
                game_sys["day"] += 1
                print("1 day has passed")
                time.sleep(0.6)
                if game_sys["day"] % 4 == 0:
                    player["money"] = int(player["money"] * 0.82)
                reset_market()
            elif action not in game_sys["mk_opt"]:
                print("invalid input!")
                time.sleep(0.5)

        elif len(user_input) == 3:
            try:
                if (action == "b" and 
                int(user_input[2]) >= 0 and
                mk_stocknprice[user_input[1]]["stock"] >= int(user_input[2]) and
                player["money"] >= mk_stocknprice[user_input[1]]["price"] * int(user_input[2])):
                #-----------------------------------------------------------
                    player["inventory"][user_input[1]] += int(user_input[2])
                    player["money"] -= mk_stocknprice[user_input[1]]["price"] * int(user_input[2])
                    mk_stocknprice[user_input[1]]["stock"] -= int(user_input[2])
                    print("transaction successful!")
                    time.sleep(0.6)
                elif (action == "s" and int(user_input[2]) >= 0 and
                player["inventory"][user_input[1]] >= int(user_input[2])):
                #-----------------------------------------------------------
                    player["money"] += int(user_input[2]) * mk_stocknprice[user_input[1]]["price"]
                    player["inventory"][user_input[1]] -= int(user_input[2])
                    print("transaction successful!")
                    time.sleep(0.6)
                

                elif action == "blmk" and game_sys["blmk_unlock"] == True:
                    game_sys['blmkactivate'] = True
            except:
                print("invalid input!")
                time.sleep(0.7)
        
    elif game_sys["blmkactivate"] == True:
            
            #----------------------------V-BLACK MARKET LOGIC-V------------------------#
        if len(user_input) == 1:
            if user_input[0] == "mk":
                game_sys["blmkactivate"] = False

        elif len(user_input) == 3:
            
            if (action == "b" and 
            int(user_input[2]) >= 0 and
            blmk_stocknprice["items"][user_input[1]]["stock"] >= int(user_input[2]) and
            player["money"] >= blmk_stocknprice["items"][user_input[1]]["price"] * int(user_input[2])):
                    #-----------------------------------------------------------
                    try:
                        player["inventory"][user_input[1]] += int(user_input[2])
                        player["money"] -= blmk_stocknprice["items"][user_input[1]]["price"] * int(user_input[2])
                        blmk_stocknprice["items"][user_input[1]]["stock"] -= int(user_input[2])
                    
                        print("transaction successful")
                        time.sleep(0.6)
                    except:
                        player["relics"][user_input[1]] = True
                        player["money"] -= blmk_stocknprice["relics"][user_input[1]]["price"] * int(user_input[2])
                        blmk_stocknprice["relics"][user_input[1]]["stock"] -= int(user_input[2])
                    
                        print("transaction successful")
                        time.sleep(0.6)
                
            elif (action == "s" and int(user_input[2]) >= 0 and
            player["inventory"][user_input[1]] >= int(user_input[2]) and
            user_input[1] in blmk_stocknprice["items"]):
                
                player["money"] += int(user_input[2]) * blmk_stocknprice["items"][user_input[1]]["price"]
                player["inventory"][user_input[1]] -= int(user_input[2])
                print("transaction successful!")
                time.sleep(0.6)
                
# This whole def (def black market only, the def lbuy logic is mine) block is ai cuz i never claimed to be
# an artist, credits to google's gemini ai, oh and the poems
# are also ai cuz i like logic but not english, or art

def black_market():
        print("'mk' to return to the market")
        print("'w' and 'e' and '*' do not work here")
        Aprice = blmk_stocknprice['items']['aetherium']['price']
        Astock = blmk_stocknprice['items']['aetherium']['stock']
        Dprice = blmk_stocknprice['items']['dragonegg']['price']
        Dstock = blmk_stocknprice['items']['dragonegg']['stock']

        Rname = blmk_stocknprice["onstockrelic"]
        Rstock = blmk_stocknprice["relics"][blmk_stocknprice["onstockrelic"]]["stock"]
        Rprice = blmk_stocknprice["relics"][blmk_stocknprice["onstockrelic"]]["price"]

        game_sys["blmkactivate"] = True
        os.system("cls")
        print(fr"""
    _________________________________
   /           SHADOW STALL          \


  |___________________________________|
  |                                   |
  |  [ITEM]        [PRICE]     [QTY]  |
  |  1.Aetherium  ${Aprice:<7}  {Astock:<3}  |
  |  2.Dragon Egg  ${Dprice:<7}  {Dstock:<3}  |
  |------------{B}RELIC{E}-----------------|
  |  3.{Rname:<10}  ${Rprice:<7}  {Rstock:<3}  |
  |___________________________________|
  |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
    |                               |
    |    [B]uy    [S]ell    [L]eave  |
    |_______________________________| 
""")
        if game_sys["blmk_unlock"] == True:
            print("'mk' to exit the black market")

        main_input_logic()

#---------------------------------------------------------------------------------
tutorial_screen()

while True:
    os.system("cls")
    game()
