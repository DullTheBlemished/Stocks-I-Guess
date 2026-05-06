# Stocks-I-Guess

!!!IMPORTANT: ALL ARTWORKS, INCLUDING LITURATURE ART WORK AND CODE FOR THE ART WORK IS AI-GENERATED, all remaining code is mine and mine alone!!!

Stock-I-Guess V2:
so like i started this whole thing after tic tac toe, makeing it technically my third project but its actually not. so what happened was that in my first version, i had only knew how to use variables, no lists, no dictionaries, no NOTHING, and somehow i actually got it working... untill i realsied how much of a pain in the ass it was gonna be to update and write glbobal for every single damn variable and so i abandoned it, about 2 weeks-ish later, maybe mror maybe less (im officially 3 weeks into python now YIPPE!) i came back to remake it, on this repos you will see two files at all time (as of before 6/05/2026): one for my new version, which has an update log in it if you are wondering:

THE CODE:
so, notice that in my old version i had the market and the logic of the players input in one thingy? i seperated it since that input logic is gonna be used for other stuff as well but thats not important, the important part is that i practised this thing idk waht its called but i call it not-so-coincidentally-simmilarly-named-variables and what it is is like in scratch you can kind of like join <variable> with string or another varible and then that is the name of anojhter variable and yeyeyeyyey but holy that saved me 75% of my if blocks or something, but now my player input logic def block is so thick it looks like an english paragraph but its fine, and i also used a LOT of dictionaries for this instead of variables cuz then no global and better data controll and stuff, also learnt the as in import something as s so i used that to import random as r because im lazy.

what i consider is the best improvement of this version from my abandoned one is the player input system; this one utalizes a system of commands such as b bread 3 becuase i learnt about .split() and stuff and figured out i can just make a system of commands instead of like THREEEEE diffrent input options like back then, you had to (input 1) B, (input 2) bread and you had to do the same to change the buy amount and sell amount and that also led to the glitch of inf money where you staretd buying negative items and yeaaa, i also made a dedicated inventory because im gonna add a lot more stuff and i also imporved how the black market riddle worked in case some idiots decides to like read the poem once, ignore it, turn it off without remembering it and never unlocking the black market - 28/03/2026, version 1.2

hello again, i need to learn a lesson in humility or smth because goddam i thought i could finish this without classes, well i did get up to version 1.3, where the black market should work but the relics dont, and as again, i will come back and make a final, truly final version once i've mastered classes - 31/03/2026

Stock-I-Guess V3:
at 8 weeks into Python, ive sucessfully learnt  more about classes, of course, no inheritance or polymorphisim yet but im getting there.

THE CODE:
once i switched everything to mainly classes and arguement passing, the later logic was actually relatively easy to code, unlike V2, i had:
a class for the items, with has its own self.stock and self.price variable (that is not listed in the __init__ brackets because i had both a self.stock_range and price range listed in the brakets, more on that later), its own resseting stock/price method (my earlier drafts for this was using the self.name and if/elif to manaually list out every price and stock range for each item inside the method, i remade it so that it will just reset itself via the self.stock(and also price)_range) that i simply ran inside the __init__ to set the initial self.price and stock at the same time, another big change here (from my first draft of this, and also from V2) is the fact that the market moved from being in a def block to a class with the only self. variable being its state (market or black market), this allows for easier state controll (just returns the whole market art thing AND makes it easier for the main_input_logic to reject attempts to buy an item from a market which you are not on (for example, running b bread 3 whiel you are in the black market), not only that but the player is now also a class instead of a dictionary, but then it also has an inventory dictionary, and this made it 10x easier to add the leveling system I'd planed in my first draft, and after finishing the code, the math goes like so: 

(note that its contestant and not player as the math is located in the main_input_logic where player is passed as an arguement named as contestant)
exp_cap = int((1.15)**(self.level + 5) + (10 + self.level))
xp gaim (buying) 2 * action_multiplier * rarity[self.classification] * contestant.exp_multi
xp gain (selling) contestant.level
rarity = {
    "common": 2, 
    "uncommon": 4, 
    "rare": 7, 
    "epic": 10, 
    "legendary": 25
}

meaning that the exp required to level up uses the formula (in y = mx + c format): y = 1.15(current level + 5) + (10 + current level), the actual xp gaining is a base of 2 xp for buying anything, multiplied by the action multiplier becuase ye buying 1 bread is different from buying 5, and then multiplied by the rarity multiplier (a self. variable in the item class, refer to that dictionary up there) because its only logical to do as such, the xp gained from selling, however is a small amount that matches your level (e.g. lv 5 selling xp earnings = 5 xp per item sold). And finally, some quality-of-life changes, first of all, my V2 REQUIRED a static (action) (item) (amount) format, this is unsatisfying, but i switched to a buch of varying if (thingy here) in (thingy there) to make it so you can change those around if you wanted to, plus i also made an  auto-scaling thingy, for example: if the player can afford 6 bread and theres 9 bread in stock and the player inputs b bread 999, it will immeadiately set the action to 6 via a min() thingy, also note that I didnt get around to dealing with the custom errors i set to raise in the main_input_logic, but yeah thats a playable "beta" version, more stuff will be coming.
