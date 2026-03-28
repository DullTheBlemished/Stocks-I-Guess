import time
import random
import os

print("Hello World!")

bm_stock_choice = ["(Eragon's sword) Brisingr", "Knockback 255 stick", "Frieren's staff", "Dreamvisitor",]

bm_stock = 0
player_bm_input = 0

inventory_bread = 0
inventory_potion = 0
inventory_sword = 0
bread_price = 0
potion_price = 0
sword_price = 0

player_money = 40
day = 0
player_input = 0
player_input_2 = 0
player_input_3 = 0
buy_amount = 1
sell_amount = 1
player_input_changespeed = 0
changebuyamount = 1
changesellamount = 1
daysbeforetax = 3
shop = 0

black_market = 0
black_market_r = 0
black_market_r2 = 0

def market_change():
	global bread_price, potion_price, sword_price, bread_stock, potion_stock, sword_stock, day, player_money

	bread_price = random.randint(10, 25)
	potion_price = random.randint(120, 140)
	sword_price = random.randint(400, 800)
	bread_stock =random.randint(2,6)
	potion_stock =random.randint(1,2)
	sword_stock =random.randint(0,2)
	day +=1

def start_game():
	os.system("cls")
	
	global bread_price, potion_price, sword_price, bread_stock, potion_stock, sword_stock, day, player_money, daysbeforetax, changesellamount, changebuyamount, player_input_changespeed, player_input, player_input_2, player_input_3, inventory_bread, inventory_potion, inventory_sword, buy_amount, sell_amount
	
	print(f"day:{day}")
	print(f"{daysbeforetax} days before tax (12%)")
	print(f"""inventory:
Bread: {inventory_bread}
Potion: {inventory_potion}
Sword: {inventory_sword}""")
	print(f"Money: ${player_money}")
	print(f"""
    _______________________________________
   /                                       \\

  |   ___________________________________   |
  |  |                                   |  |
  |  |           GENERAL STORE           |  |
  |  |___________________________________|  |
  |                                         |
  |    [ITEM]        [PRICE]      [STOCK]   |
  |   1. Bread        ${bread_price}            {bread_stock}      |
  |   2. Potion       ${potion_price}           {potion_stock}      |
  |   3. Sword        ${sword_price}           {sword_stock}      |
  |_________________________________________|
  |___|___|___|___|___|___|___|___|___|___|_|
    |                                     |
    |      [B]uy    [S]ell    [W]ait      |
    |_____________________________________|
""")
	print(f"Buy Amount: {buy_amount}")
	print(f"Sell Amount: {sell_amount}")

	player_input = input("Action (B/S/W), P to change Buy/Sell Amount:")
	
	if player_input == "W":
		market_change()
		daysbeforetax -=1
		player_input = 0
		if day % 3 == 0:
			player_money=int(player_money * 0.88)
			daysbeforetax = 3
			print("TAX COLLECTED!")
			time.sleep(0.6)
	elif player_input == "B":
		player_input_2=input("Bread/Potion/Sword?:")
		player_input = 0
	elif player_input == "S":
		player_input_3=input("Bread/Potion/Sword?:")
		player_input = 0
	elif player_input == "P":
		player_input_changespeed = input("Buy amount or Sell amount? (Buy/Sell):")
		player_input = 0
	elif player_input == "BLACKMARKET" and day >= 55 and black_market_r2 == 0:
		os.system("cls")
		player_input_2 = input("""In which direction does Hellios rise to claim his throne? In which does he bows his head where the shadows grow long and the day goes to drown? He who searches must CENTER his path; march FOWARD, and never look BACK:""")
	elif player_input == "BLACKMARKET" and day >= 55:
		os.system("cls")
		player_input_2 == "north"
	else:
		player_input = 0 
		player_input_2 = 0
		player_input_3 = 0
		print("Invalid input!")
		time.sleep(0.6)

	if player_input_changespeed == "Buy":
		changebuyamount = input("Set to? (PLEASE ONLY USER NUMBERS, OR ELSE GAME WILL CRASH):")
		buy_amount = int(changebuyamount)
		player_input_changespeed = 0
		changebuyamount = 0
	if player_input_changespeed == "Sell":
		changesellamount = input("Set to? (PLEASE ONLY USER NUMBERS, OR ELSE GAME WILL CRASH):")
		sell_amount = int(changesellamount)
		player_input_changespeed = 0
		changesellamount = 0

	

	if player_input_2 != 0:
		if player_input_2 == "Bread" and bread_stock >= 1 * buy_amount and player_money >= bread_price * buy_amount:
				inventory_bread +=1 * buy_amount
				player_money -= bread_price * buy_amount
				bread_stock -=1 * buy_amount
				player_input_2 = 0
		elif player_input_2 == "Potion" and potion_stock >= 1 * buy_amount and player_money >= potion_price * buy_amount:
				inventory_potion +=1 * buy_amount
				player_money -= potion_price * buy_amount
				potion_stock -=1 * buy_amount
				player_input_2 = 0
		elif player_input_2 == "Sword" and sword_stock >= 1 * buy_amount and player_money >= sword_price * buy_amount:
				inventory_sword +=1 * buy_amount
				player_money -= sword_price * buy_amount
				sword_stock -=1 * buy_amount
				player_input_2 = 0
		elif player_input_2.lower() == "north":
			black_market = 1
		else:
			print("Insufficient funds/stock/Invalid input!")
			time.sleep(0.5)
			player_input_2 = 0
	

	if player_input_3 !=0:
		if player_input_3 == "Bread" and inventory_bread >= 1 * sell_amount:
			inventory_bread -=1 * sell_amount
			player_money += bread_price * sell_amount
			player_input_3 = 0

		elif player_input_3 == "Potion" and inventory_potion >= 1 * sell_amount:
			inventory_potion -=1 * sell_amount
			player_money += potion_price * sell_amount
			player_input_3 = 0

		elif player_input_3 == "Sword" and inventory_sword >= 1 * sell_amount:
			inventory_sword -=1 * sell_amount
			player_money += sword_price * sell_amount
			player_input_3 = 0
		else:
			print("You can't sell what you dont have you bum")
			time.sleep(0.5)
			player_input_3=0

def black_market_riddle():
	global day, black_market_r

	if day == 55 and black_market_r == 0:
		os.system("cls")
		print("""Three steps forward, none to the rear,
I shift the truth to hide what's here.
A trio of turns makes A into D,
Slide the alphabet to talk to me.
Where the alleys dim and the laws go blind,
Exchange your coins for the forbidden kind.
The shadowed stalls won't speak a word,
Unless this secret shift is heard""")
		time.sleep(4)
		print("YIXZHJXOHBQ")
		input("Enter To Continue (remember this code very carefully)")
		black_market_r = 1

def black_market():
	global player_bm_input, bm_stock
	print("Buying will pass a day")
	print(f"""
    _______________________________________
   /                                       \\

  |   ___________________________________   |
  |  |                                   |  |
  |  |           BLACK MARKET            |  |
  |  |___________________________________|  |
  |                                         |
  |    [CONTRABAND]     [PRICE]     [STOCK] |
  |   1. {black_market_item}  ${item_price:<9}  {item_stock:<7} |
  |_________________________________________|
  |___|___|___|___|___|___|___|___|___|___|_|
    |                                     |
    |      [B]uy    [S]ell    [L]eave     |
    |_____________________________________|
""")
	
	player_bm_input = input(f"Buy {bm_stock}? Y/N")

market_change()

while True:
	start_game()
	
	black_market_riddle()
	#i give up here, will finsihed this on a new file one day