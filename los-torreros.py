#!/usr/bin/env python3

license = ''' 
    Copyright 2013, 2014 Jason MacDuffie.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    '''

author = ''' 
    Contact information:

    email:      taknamay@gmail.com
    '''

objective = ''' 
    You must walk around the castle fighting monsters to find Bellamor.
    Once you meet Bellamor, you must kill him to win the game.

    Hint: If you leave the room after battling Bellamor without
    defeating him, he will still be damaged!
    '''

intro = ''' 
*** Welcome to Los Torreros ***
Copyright 2013, 2014 Jason MacDuffie.
'''

import random

def read(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\n")
        print("Good bye! Please play another time.")
        exit()

# Define a method for fleeing combat.
def flees_combat():
    global hp
    if (combat_state == 0):
        return True
    elif (combat_state == 1):
        escape_roll = random.randint(1, 6) + evasion_mod
        if (escape_roll <= 3):
            damage_in = random.randint(1, 4) + 1
            hp -= damage_in
            print("\nYou failed to escape! Your enemy strikes, dealing " + str(damage_in) + " damage to you.")
            return False
        else:
            print("\nYou successfully fled the enemy!")
            return True
    else:
        escape_roll = random.randint(1, 6) + evasion_mod
        if (escape_roll <= 4):
            damage_in = random.randint(1, 6) + 2
            hp -= damage_in
            print("\nYou failed to escape! Your enemy strikes, dealing " + str(damage_in) + " damage to you.")
            return False
        else:
            print("\nYou successfully fled the enemy!")
            return True

# Create an array with a description for every room.
room_descriptions = [
        "\nYou are currently in the northwest watchtower. You see the knight\nUnpensador lying in the corner. He is gravely wounded. Around here\nyou see boxes of alchemical ingredients, as that is the knight's\nspecialty. This room appears safe enough to rest in. To the east is the\nnorth wing of the castle. To the south is the west wing of the castle.",
        "\nYou are currently in the north wing of the castle, in the west side.\nThe corridor is long and barren. A window is broken, letting the\ncold air in. It is frigid enough that you can see your own breath. To\nthe west is the northwest watchtower. To the east is the other side\nof the north wing. To the south is the chapel.",
        "\nYou are currently in the north wing of the castle, in the east side.\nThe moon shines brightly through a large window. You quickly pray\nthat you will live to see tomorrow's sun. To the west is the other\nside of the north wing. To the south is south is the throne room.\nTo the east is the northwest watchtower.",
        "\nYou are currently in the northeast watchtower. You see the knight\nTormenta wounded and lying on the ground, struggling to survive. A\nhuge armory lines the walls, including maces, axes, and swords. You\ndo not know how to use any of these weapons, so you are content to\nuse your spear. Tormenta knows how to use all these weapons, but\nunfortunately she cannot fight any more. This room appears safe\nenough to rest in. To the west is the north wing. To the south is\nthe royal quarters.",
        "\nYou are currently in the west wing of the castle, in the north side.\nThere are visible puddles of blood on the floor, with one large\ntrail of blood leading north. It looks like the blood came from someone\nstruggling to crawl to a safe place. To the north is the northwest\nwatchtower. To the south is the other side of the west wing. To the\neast is the chapel.",
        "\nYou are currently in the chapel. There are no worshippers here on\nthis dreaded day. The stained glass windows that promise a savior\nare almost ironic. This room appears safe enough to rest in. To the\nnorth is the north wing of the castle. To the west is the west wing\nof the castle. To the south is the garden. To the east is the throne\nroom.",
        "\nYou are currently in the throne room. The king is, unfortunately,\ndead. You take a moment of silence to mourn his loss, and appreciate\nhis efforts to unite the city-states under one banner while still\nrespecting the role of local governments. You have hope that his legacy\nwill not be in vain. To the north is the north wing of the castle.\nTo the west is the chapel. To the south is the garden. To the east is\nthe royal quarters.",
        "\nYou are currently in the royal quarters. Each bedroom is decorated\nbeautifully, but you do not have time to appreciate that now. Rather\nthan being filled with awe at its beauty, you are filled with dread\nthat the monsters will destroy the wealth that the kingdom worked so\nhard to create. To the north is the northeast watchtower. To the\nwest is the throne room. To the south is the servant quarters.",
        "\nYou are currently in the west wing of the castle, in the south side.\nYou hear scratching on the walls but you cannot tell if it is a\ntree branch or something more sinister. Of course, supposing that it may\nonly be a tree branch is just wishful thinking. To the north is the\nother side of the west wing. To the south is the southwest watchtower.\nTo the east is the garden.",
        "\nYou are currently in the garden, in the west side. The area once\nfilled with life has now become a testament of death. The ground you\nwalk on is devoid of life, and only dirt, mud and sand remains. Some of\nthe species cultivated here were extinct in the wild, which worries\nyou. To the north is the chapel. To the west is the west wing of\nthe castle. To the south is the entrance of the castle. To the east is\nthe other side of the garden.",
        "\nYou are currently in the garden, in the east side. The flowers and\nother plants here are wilted and smell of decay. Their current state\nof being is saddening to you. The damage is unlikely to ever be undone.\nTo the north is the throne room. To the west is the other side of the\ngarden. To the south is the dining hall. To the east is the\nservant quarters.",
        "You are in the servant quarters. Instead of being filled with the\nhustle and bustle of the daily work, this part of the castle is\nfrighteningly silent and still. You wonder what happened to the\nbodies of your deceased friends. To the north is the royal quarters.\nTo the west is the garden. To the south is the southeast watchtower.",
        "\nYou are currently in the southwest watchtower. You see the knight\nPacifica sitting on the stairs, breathing heavily and noticeably\ninjured. The torch on the wall has almost burned out. The flickering\nlight illuminates the piles of gold and other treasure scattered in\nthe room. Pacifica happens to be an accomplished merchant. This room\nappears safe enough to rest in. To the north is the west wing of the\ncastle. To the east is the entrance of the castle.",
        "\nYou are currently at the entrance of the castle. There is no escape,\nfor the door is sealed shut by some dark magic. Besides, there is\nno way you would abandon your friends. A gentle light source is coming\nfrom the west. Flickering shadows dance on the wall. You could tell\nyourself it is only mice, but you know better. To the north is the garden.\nTo the west is the southwest watchtower. To the east is the dining hall.",
        "\nYou are currently in the dining hall. There is no merriment here on\nthis day. Replacing the fragrant smell of delicious food is the smell\nof ashes. There are visible scorch marks on the wall. To the north is\nthe garden. To the west is the entrance to the castle. To the east is\nthe southeast watchtower.",
        "\nYou are currently in the southeast watchtower. You see the knight\nElbardo is seriously injured, and is nursing himself by the wall.\nScattered around the room are various musical instruments, but now\nis really not the time to ask Elbardo to play a tune for you. Wind\nhowls down the chamber from above you. This room appears safe enough\nto rest in. To the north is the servant quarters. To the west is the\ndining hall."
        ]
room_entrance_message = [
        "\nYou enter the northwest watchtower.",
        "\nYou enter the west side of the north wing.",
        "\nYou enter the east side of the north wing.",
        "\nYou enter the northeast watchtower.",
        "\nYou enter the north side of the west wing.",
        "\nYou enter the chapel.",
        "\nYou enter the throne room.",
        "\nYou enter the royal quarters.",
        "\nYou enter the south side of the west wing.",
        "\nYou enter the west side of the garden.",
        "\nYou enter the east side of the garden.",
        "\nYou enter the servant quarters.",
        "\nYou enter the southwest watchtower.",
        "\nYou enter the castle entrance room.",
        "\nYou enter the dining hall.",
        "\nYou enter the southeast watchtower."
        ]
print(
        "*** Welcome to Los Torreros ***\nCopyright 2013, 2014 Jason MacDuffie.\n")
print("Greetings, player. What is your name?")
pc_name = read(">>> ")
while (len(pc_name) > 16):
    print("\nYour name cannot be more than 16 letters. What is your name?")
    pc_name = read(">>> ")
# If the length is greater than 16 characters, ask for a shorter name.
print(
        "\nHello, {0} You are a guardsperson of ".format(pc_name + ".")
        + "Gran Castillo. The\ncastle is under attack by strange and evil "
        + "monsters. It is your duty\nto protect to castle from these "
        + "threats. Search for the boss to drive\nout the monsters.")
print(
        "\nPlease select your bonus stat: power, health, or intel. Power\n"
        + "increases the damage you deal to enemies. Health increases your\n"
        + "maximum hit points. Intel makes it easier to avoid and escape "
        + "combat.")
# The player chooses a bonus stat.
bonus_stat = read(">>> ").lower()
while (bonus_stat != "power" and bonus_stat != "health" and
        bonus_stat != "intel"):
    print("\nPlease choose either power, health, or intel.")
    bonus_stat = read(">>> ").lower()
print("\nYou have chosen the " + bonus_stat + " stat. Good choice!")
# Initialize all player stats and modify the bonus stat.
max_hp = 25
damage_mod = 3
evasion_mod = 1
if (bonus_stat == "power"):
    damage_mod = 6
elif (bonus_stat == "health"):
    max_hp = 40
else:
    evasion_mod = 2
hp = max_hp
# Set the room to the chapel.
current_room = 5
# Randomize the location of the boss, Bellamor. The possible rooms
# are 1, 2, 4, 6, 7, 8, 9, 10, 11, 13, and 14.
boss_location = random.randint(1,11)
if (boss_location >= 3):
    boss_location = boss_location + 1
if (boss_location >= 5):
    boss_location = boss_location + 1
if (boss_location >= 12):
    boss_location = boss_location + 1
# Set the hints being given by Unpensador, Pacifica, Tormenta and Elbardo.
if (boss_location == 1 or boss_location == 2 or boss_location == 6):
    unpensador_hint = "east"
    tormenta_hint = "west"
    pacifica_hint = "north"
    elbardo_hint = "north"
elif (boss_location == 4 or boss_location == 8 or boss_location == 9):
    unpensador_hint = "south"
    tormenta_hint = "west"
    pacifica_hint = "north"
    elbardo_hint = "west"
elif (boss_location == 7 or boss_location == 10 or boss_location == 11):
    unpensador_hint = "east"
    tormenta_hint = "south"
    pacifica_hint = "east"
    elbardo_hint = "north"
else:
    unpensador_hint = "south"
    tormenta_hint = "south"
    pacifica_hint = "east"
    elbardo_hint = "west"
# Set the boss's initial hit points.
boss_health = 50
# Game state: 0 = playing, 1 = quit, 2 = death, 3 = victory
game_state = 0
# Combat state: 0 = no enemy, 1 = basic enemy, 2 = boss
combat_state = 0
print("\nHint: For information about available commands, say 'help'.")
# Begin the game loop.
while (game_state == 0):
    moved_rooms = False
    command = read(">>> ").lower()
    # This begins the help options.
    if (command == "help"):
        print(
                "\nAvailable commands are look, move, talk, attack, status, "
                + "info, wait,\nand quit. For info about a specific "
                + "[command], type 'help [command]'.")
    elif (command == "help help"):
        print(
                "\nDisplay the available commands or information about a "
                + "specific command.")
    elif (command == "help look"):
        print("\nLook at your surroundings.")
    elif (command == "help move"):
        print(
                "\nType 'move n/s/e/w' to travel in a particular direction. "
                + "For example, to\ngo north, type 'move n'. You can also "
                + "simply type 'n' or 'north'.")
    elif (command == "help talk"):
        print("\nTalk to another character in the room.")
    elif (command == "help attack"):
        print("\nDeal damage to the enemy in the room.")
    elif (command == "help status"):
        print("\nDisplay the current status of your game.")
    elif (command == "help info"):
        print(
                "\nGet information about the game. Options are license, "
                + "objective, and\nauthor.")
    elif (command == "help wait"):
        print(
                "\nRest until you have maximum hit points. This is only "
                + "allowed in certain\nrooms.")
    elif (command == "help quit"):
        print(
                "\nImmediately end the game. The state of the game will "
                + "not be saved.")
    # This ends the help options.
    elif (command == "look"):
        print(room_descriptions[current_room]) 
    # This begins the move options.
    elif (command == "move"):
        print(
                "\nPlease say 'move [direction]' or just '[direction]' to "
                + "move. For\nexample, to go north, say 'move n' or 'n'.")
    elif (command == "move n" or command == "move north" or
            command == "n" or command == "north"):
        if (0 <= current_room < 4):
            print("\nYou cannot go north from here.")
        elif (flees_combat()):
            current_room = current_room - 4
            print(room_entrance_message[current_room])
            moved_rooms = True
            combat_state = 0
    elif (command == "move w" or command == "move west" or
            command == "w" or command == "west"):
        if (current_room % 4 == 0):
            print("\nYou cannot go west from here.")
        elif (flees_combat()):
            current_room = current_room - 1
            print(room_entrance_message[current_room])
            moved_rooms = True
            combat_state = 0
    elif (command == "move s" or command == "move south" or
            command == "s" or command == "south"):
        if (12 <= current_room < 16):
            print("\nYou cannot go south from here.")
        elif (flees_combat()):
            current_room = current_room + 4
            print(room_entrance_message[current_room])
            moved_rooms = True
            combat_state = 0
    elif (command == "move e" or command == "move east" or
            command == "e" or command == "east"):
        if (current_room % 4 == 3):
            print("\nYou cannot go east from here.")
        elif (flees_combat()):
            current_room = current_room + 1
            print(room_entrance_message[current_room])
            moved_rooms = True
            combat_state = 0
    elif (command[0:4] == "move"):
        print("\nThat is not a valid direction. Options are n, w, s, or e.")
    # This ends the move options.
    # This starts the talk dialog.
    elif (command == "talk"):
        if (current_room == 0):
            print("\nUnpensador: *Cough* Hey " + pc_name + "... I don't have much strength\nleft in me. Bellamor attacked me and fled " + unpensador_hint + " last I saw him. If only\nI had the strength to brew a healing potion... ")
        elif (current_room == 3):
            print("\nTormenta: Greetings, knight " + pc_name + ". Unfortunately I cannot\nhelp you fight ever since Bellamor wounded me. You need to track that\nmonster down and finish what I couldn't. I saw him running " + tormenta_hint + " after\nwe fought. I may not ever wield a blade again...")
        elif (current_room == 12):
            print("\nPacifica: " + pc_name + "... I'm in a lot of pain. Bellamor hurt me.\nI barely got away with my life. He was headed " + pacifica_hint + " after he struck\nme. He does not seem interested in gold, for he has not tried to enter\nthis room...")
        elif (current_room == 15):
            print("\nElbardo: Hello, " + pc_name + ". Looks like my right arm is no good\nanymore. Bellamor came out of nowhere and attacked me from behind.\nHave you checked " + elbardo_hint + " yet? That's where I saw him. Also, do you\nthink it's possible to play the mandolin with one arm? It would be\ngreat to have a song to cheer us up in these desperate times... Aha,\nI know what I can do! Now where is my harmonica...")
        elif (combat_state == 1):
            print("\nMonster: DIE DIE DIE DIE DIE DIE DIE")
        elif (combat_state == 2):
            print("\nBellamor: I don't make idle chit-chat with prey.")
        else:
            print("There is nobody to speak with.")
    # This ends the talk dialog.
    # This begins the attack command.
    elif (command == "attack"):
        if (combat_state == 0):
            print("\nThere is no enemy to attack here.")
        elif (combat_state == 1):
            damage_out = random.randint(1, 4) + damage_mod
            damage_in = random.randint(1, 4) + 1
            hp -= damage_in
            mob_health -= damage_out
            print("\nYou delivered " + str(damage_out) + " damage to the monster, and it delivered " + str(damage_in) + " damage to you!")
        else:
            damage_out = random.randint(1, 4) + damage_mod
            damage_in = random.randint(1, 6) + 2
            hp -= damage_in
            boss_health -= damage_out
            print("\nYou delivered " + str(damage_out) + " damage to Bellamor, and he delivered " + str(damage_in) + " damage to you!")
    # This ends the attack command.
    elif (command == "status"):
        print("\nHit Points: " + str(hp) + " / " + str(max_hp))
        if (current_room == 0):
            print("Location: Northwest watchtower")
        elif (current_room == 1):
            print("Location: North wing, west")
        elif (current_room == 2):
            print("Location: North wing, east")
        elif (current_room == 3):
            print("Location: Northeast watchtower")
        elif (current_room == 4):
            print("Location: West wing, north")
        elif (current_room == 5):
            print("Location: Chapel")
        elif (current_room == 6):
            print("Location: Throne room")
        elif (current_room == 7):
            print("Location: Royal quarters")
        elif (current_room == 8):
            print("Location: West wing, south")
        elif (current_room == 9):
            print("Location: Garden, west")
        elif (current_room == 10):
            print("Location: Garden, east")
        elif (current_room == 11):
            print("Location: Servant quarters")
        elif (current_room == 12):
            print("Location: Southwest watchtower")
        elif (current_room == 13):
            print("Location: Castle entrance")
        elif (current_room == 14):
            print("Location: Dining hall")
        else:
            print("Location: Southeast watchtower")
        if (combat_state == 0):
            print("Combat: None")
        elif (combat_state == 1):
            print("Combat: Enemy")
        else:
            print("Combat: Boss")
    # This begins the info options.
    elif (command == "info"):
        print(
                "\nType 'info license'   to display the copyright license "
              + "for this game.\nType 'info objective' to display the "
              + "objective of this game.\nType 'info author'    to display "
              + "information about the author of this game.")
    elif (command == "info license"):
        print(license)
    elif (command == "info objective"):
        print(objective)
    elif (command == "info author"):
        print(author)
    elif (command[0:4] == "info"):
        print("\nThat is not a valid option for info. Type 'info' for a list "
            + "of options.")
    # This ends the info options.
    elif (command == "wait"):
        if (current_room == 0 or
          current_room == 3 or
          current_room == 5 or
          current_room == 12 or
          current_room == 15):
            if (hp < max_hp):
                hp = max_hp
                print("\nYou take a break here to regain your health.")
            else:
                print("\nYou are already fully rested.")
        else:
            print("\nYou are not in a safe place to wait.")
    elif (command == "quit"):
        game_state = 1
    else:
        if (command != ""):
            print(
                    "\nThat is not a valid command. Type 'help' for "
                    + "a list of commands.")
    # Post-command instructions
    if (combat_state == 1 and mob_health <= 0 and hp > 0):
        print("\nThe enemy is defeated!")
        combat_state = 0
    elif (boss_health <= 0 and hp > 0):
        print("\nThe enemy is defeated!")
        game_state = 3
    if (moved_rooms):
        if (current_room != boss_location):
            combat_roll = random.randint(1, 6) + evasion_mod
            if (combat_roll <= 2 and
              current_room != 0 and
              current_room != 3 and
              current_room != 5 and
              current_room != 12 and
              current_room != 15):
                combat_state = 1
                mob_health = 20
                print("\nYou encountered a monster!")
        else:
            combat_state = 2
            print("\nYou encountered Bellamor!")
    
    
    if (hp <= 0):
        game_state = 2
if (game_state == 1):
    print("\nGood bye! Please play another time.")
elif (game_state == 2):
    print("\nYou died! Now the kingdom is sure to fall to the monsters.")
else:
    print("\nCongratulations! You have defeated Bellamor and saved the castle!\nEven though the king is dead, the kingdom will be restored to\npeace and normality, with the help you and the remaining knights.")

read("\nPress enter to close the program at any time...  ")
