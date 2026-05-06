import os
import time
import random

B = '\033[1m' # bold
END = '\033[0m' # end bold

class InvalidInput(Exception):
    pass

class InsufficientFunds(Exception):
    pass

class user:
    def __init__(self, tester = False):
        self.money = random.randint(30, 40)
        self.inventory = {"bread": 0, "potion": 0, "sword": 0,
                          "aetherium": 0, "dragonegg": 0,
                          }
        self.daycount = 0
        self.daycounttax = 4
        self.level = 0
        self.exp = 0
        self.exp_multi = 1
        self.exp_cap = int((1.15)**(self.level + 5) + (10 + self.level))

        if tester != False:
            self.money = 1000
            self.inventory = {"bread": 10, "potion": 10, "sword": 10,
                            "aetherium": 10, "dragonegg": 10,
                            }
            self.daycount = 0
            self.daycounttax = 4
            self.level = 100
            self.exp_multi = 999999
            self.exp_cap = int((1.15)**(self.level + 5) + (10 + self.level))

    def day_pass(self):
        self.daycount += 1
        self.daycounttax -= 1
        if self.daycounttax == 0:
            self.money = self.money * 0.88
            self.daycounttax = 4

    def leveling_check(self):
        leveling = 1
        while leveling == 1:
            if self.exp >= self.exp_cap:
                leveling = 1
            else:
                leveling = 0
                break

            self.level += 1
            self.exp -= self.exp_cap
            self.exp_cap = int((1.15)**(self.level + 5) + (10 + self.level))

    def inventory_print(self):
        os.system("cls")
        print(r"""
   _____________
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
        print(f"{B}----+----INVENTORY----+----{END}")
        print("")
        print(f"{B}     --Common Items--{END}")
        print(f"Bread: {self.inventory["bread"]} (common)")
        print(f"Potion: {self.inventory["potion"]} (uncommon)")
        print(f"Sword: {self.inventory["sword"]} (rare)")
        print("")
        print(f"{B}     --Rarer Items--{END}")
        print(f"Aetherium: {self.inventory['aetherium']} (epic)")
        print(f"Dragon Egg: {self.inventory['dragonegg']} (legendary)")
        print("")
        input("'ENTER' to continue")

    def tutorial_print(self):
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
        print("(also i made it so the order of (ACTION) (ITEM) (AMOUNT) can be inter-changeable)")
        input("'ENTER' to continue, tutorial may be acessed again via inputting * in the main inpu Good luck!")
    
class store():
    def __init__(self):
        self.state = "market"

    def market(self):
        if self.state == "market":
            return(fr"""
      _______________________________________
     /                                       \

    |   ___________________________________   |
    |  |                                   |  |
    |  |           GENERAL STORE           |  |
    |  |___________________________________|  |
    |                                         |
    |    [ITEM]        [PRICE]      [STOCK]   |
    |   1. Bread        ${bread.price}            {bread.stock}      |
    |   2. Potion       ${potion.price}           {potion.stock}      |
    |   3. Sword        ${sword.price}           {sword.stock}      |
    |_________________________________________|
    |___|___|___|___|___|___|___|___|___|___|_|
      |                                     |
      |      [B]uy    [S]ell    [W]ait      |
      |_____________________________________| 
    """)
        
        elif self.state == "black_market":
            coming_soon = "N/A"
            return(fr"""
      _______________________________________
     /                                       \

    |   ___________________________________   |
    |  |                                   |  |
    |  |            BLACK MARKET           |  |
    |  |___________________________________|  |
    |                                         |
    |    [ITEM]        [PRICE]      [STOCK]   |
    |   1. Aetherium    ${aetherium.price}          {aetherium.stock}      |
    |   2. Dragon Egg   ${dragonegg.price}          {dragonegg.stock}      |
    |   3. Coming soon  ${coming_soon}          {coming_soon}     |
    |_________________________________________|
    |___|___|___|___|___|___|___|___|___|___|_|
      |                                     |
      |      [B]uy    [S]ell    [W]ait      |
      |_____________________________________| 
    """)
        
class item:
    def __init__(self, name, classification, price_range, stock_range, market):
        self.name = name
        self.stock = 0
        self.price = 0
        self.classification = classification
        self.price_range = price_range
        self.stock_range = stock_range
        self.market = market

        self.market_reset()

    def market_reset(self):
        if self.classification != "relic": 
            self.price = random.randint(self.price_range[0], self.price_range[1])
            self.stock = random.randint(self.stock_range[0], self.stock_range[1])
        else:
            pass
    
    def buy(self, action_multiplier, contestant):
        contestant.inventory[self.name] += action_multiplier
        contestant.money -= self.price * action_multiplier
        self.stock -= action_multiplier
        contestant.exp += 2 * action_multiplier * rarity[self.classification] * contestant.exp_multi

    def sell(self, action_multiplier, contestant):
        contestant.inventory[self.name] -= action_multiplier
        contestant.money += self.price * action_multiplier
        contestant.exp += contestant.level

def pass_day():
    for obj in name_to_object:
        name_to_object[obj].market_reset()

    player.day_pass()

def secondary_input_logic(user_input, contestant):
    if "e" in user_input:
        contestant.inventory_print()

    elif "w" in user_input:
        pass_day()
    elif "*" in user_input:
        contestant.tutorial_print()

    else:
        raise InvalidInput
def main_input_logic(user_input, shop, contestant):
    user_input = user_input.split()
    action = 0
    action_multiplier = 0
    item = 0

    if len(user_input) != 3:
        raise InvalidInput
    
    if "b" in user_input:
        action = "buy"
    elif "s" in user_input:
        action = "sell"
    else:
        raise InvalidInput
    
    if all(obj not in user_input for obj in name_to_object):
        raise InvalidInput

    while item == 0:
        for obj in name_to_object:
            if obj in user_input and name_to_object[obj].market == shop.state:
                item = obj
                break
        else:
            raise InvalidInput
    

    for part in user_input:
        try:
            action_multiplier = int(part)

            if action_multiplier < 1:
                raise InvalidInput
            else:
                break

        except:
            continue
    else:
        raise InvalidInput
    
    if action == "buy":
        action_multiplier = min(name_to_object[item].stock,
                                contestant.money//name_to_object[item].price,
                                action_multiplier)
        if action_multiplier == 0:
            raise InsufficientFunds
        
    elif action == "sell":
        action_multiplier = min(action_multiplier, contestant.inventory[item])
        if action_multiplier < 1:
            raise InsufficientFunds
        
    if action == "buy":
        # its the action multiplier then contestant (as in the player that was already passed into here as an arg aswell)
        name_to_object[item].buy(action_multiplier, contestant)
        print(f"Transaction sucessful, brought {action_multiplier} {item}")
        input("'ENTER' to continue")

    elif action == "sell":
        name_to_object[item].sell(action_multiplier, contestant)
        print(f"Transaction sucessful, sold {action_multiplier} {item}")
        input("'ENTER' to continue")

    contestant.leveling_check()

# FLAG
# Tester/Player mode (Enter true, for Tester, leave empty/False for player)
player = user()
market = store()
# its name, classification, price_range, stock_range, market. IN THAT ORDER, also both of the range MUST be list or tuple
bread = item("bread", "common", (10, 25), (2, 6), "market")
potion = item("potion", "uncommon", (110, 150), (1, 3), "market")
sword = item("sword", "rare", (550, 830), (0, 2), "market")
aetherium = item("aetherium", "epic", (950, 2000), (1, 3), "black_market")
dragonegg = item("dragonegg", "legendary", (1750, 3500), (0, 1), "black_market")

name_to_object = {"bread": bread, "potion": potion, "sword": sword,
                  "aetherium": aetherium, "dragonegg": dragonegg,
                  }
rarity = {"common": 2, "uncommon": 4, "rare": 7, "epic": 10, "legendary": 25,
          }

def game():
        user_input = 0
        os.system("cls")
        print(f"{player.daycounttax} days until tax (18%)")
        print(f"day: {player.daycount}")
        print(f"${int(player.money)}")
        print(f"level {player.level} ({player.exp}/{player.exp_cap})xp")
        print(market.market())
        user_input = input(">>>:").lower()
        for char in['!', '"', '#', '$', '%', '&', "'", '(', ')', '+', ',', '-', 
                    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', 
                    '^', '_', '`', '{', '|', '}', '~']:
            user_input = user_input.replace(char, "")
        if len(user_input.split()) == 1:
        # its input, then player
            secondary_input_logic(user_input, player)
        # its input, then market, then player
        else:
            main_input_logic(user_input, market, player)
while True:
    game()