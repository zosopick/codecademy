'''
In this project, you will be using Python Classes to create a game system similar to the popular game series Pokémon.
If you’re unfamiliar with Pokémon, it is a game where creatures (Pokémon) battle against each other.
Every Pokémon has statistics associated with it like health, level, type, and a name. In this project we’ll make
several classes that interact with each other so you can create your own Pokémon battles!
'''
import random
import time


class Pokemon:
    def __init__(self, name, lvl, type, xp=0, is_ko=False):
        self.name = name
        self.lvl = lvl
        self.type = type
        self.max_health = lvl * 10
        self.current_health = lvl * 10
        self.xp = xp
        self.is_ko = is_ko

    def attack(self, other):
        dmg = 1.0
        for typ1 in self.type:
            for typ2 in other.type:
                if (typ1 == 'Fire' and typ2 == 'Grass') or (typ1 == 'Grass' and typ2 == 'Water') or (
                        typ1 == 'Water' and typ2 == 'Fire'):
                    dmg += 0.5

                elif (typ1 == 'Grass' and typ2 == 'Fire') or (typ1 == 'Fire' and typ2 == 'Water') or (
                        typ2 == 'Water' and typ2 == 'Grass'):
                    dmg -= 0.5

        damage = self.lvl * dmg + (random.randint(-5, 5) * 0.1)
        other.current_health = max(other.current_health - damage, 0)
        print('{0} has attacked {1}, dealing {2} damage.'.format(self.name, other.name, damage, 1))

        if other.current_health == 0:
            other.is_ko = True

    def level_up(self):
        self.lvl += 1
        self.max_health = self.lvl * 10


class Trainer:

    def __init__(self, name, belt, pack, wallet):
        self.name = name
        self.belt = belt
        self.pack = pack
        self.wallet = wallet

    def average_lvl(self):
        return sum(slot.lvl for slot in self.belt) / len(self.belt)

    def own_pokemon(self):
        for pokemon in self.belt:
            if (not pokemon.is_ko):
                return True
        return False

    def view_pokemon(self):
        print("{0}'s Pokemon: ".format(self.name))
        for id, pokemon in enumerate(self.belt):
            ko_status = ''
            if (pokemon.is_ko == True):
                ko_status = '- fainted!'
            print('{0} - {1} Level {2} {3}/{4} HP'.format(id + 1, pokemon.name, pokemon.lvl,
                                                          round(pokemon.current_health, 2),
                                                          pokemon.max_health, ko_status))

    def catch_pokemon(self, items_a, selection):

        balls = {'Pokeball': 30, 'Ultraball': 75}
        self.pack[items_a[selection]] -= 1
        print('You threw a Pokeball')
        time.sleep(1)
        phrases = ['The ball bounces buoyantly.',
                   'The ball teeters tediously',
                   'The ball convulses in confusion.']
        for i in range(3):
            chance = random.randint(0, 100)
            if chance < balls[items_a[selection]]:
                return True
            else:
                print(phrases[random.randint(1, 3)])
                time.sleep(1)
        print('The ball breaks')
        return False

    def view_pack(self, wild=False):
        items_a = {}
        i = 1
        for k, j in self.pack.items():
            items_a[str(i)] = k
            i += 1
        print('Wallet: {0}'.format(self.wallet))
        for num, name in items_a.items():
            print('{0}) {1} - {2}'.format(num, name, self.pack[name]))
        selection = input('[Number] to select or [Enter] to close: ')
        if (selection in [str(i + 1) for i in range(len(self.belt))] and self.pack[items_a[selection]] > 0):
            if (items_a[selection] in ['Pokeball', 'Ultraball']):
                if wild == True:
                    return self.catch_pokemon(items_a, selection)
                else:
                    print('There are no Pokemon around to catch')
                    return False
            self.view_pokemon()
            slot = input('[Number] to select or [Enter] to close: ')
            if slot in [str(i + 1) for i in range(len(self.belt))]:
                if items_a[selection] == 'Potion':
                    self.belt[int(slot) - 1].current_health = min(self.belt[int(slot) - 1].current_health + 30,
                                                                  self.belt[int(slot) - 1].max_health)
                    self.pack[items_a[selection]] -= 1
                elif items_a[selection] == 'Revive':
                    self.belt[int(slot) - 1].current_health = min(self.belt[int(slot) - 1].current_health + 30,
                                                                  self.belt[int(slot) - 1].max_health)
                    self.belt[int(slot) - 1].is_ko = False
                    self.pack[items_a[selection]] -= 1
                return False
            return False
        return False

    def set_active_pokemon(self, selection):
        self.belt.insert(0, self.belt.pop(self.belt.index(self.belt[selection])))

    def swap_pokemon(self):
        self.view_pokemon()
        selection = input('[Number] to change Pokemon or [Enter] to close: ')
        if selection in [str(i + 1) for i in range(len(self.belt))]:
            if (not self.belt[int(selection) - 1].is_ko):
                self.set_active_pokemon(int(selection) - 1)
            else:
                self.swap_pokemon()
        elif self.belt[0].is_ko:
            self.swap_pokemon()


player = Trainer('Nick', [], {'Potion': 10, 'Revive': 3}, 1000)
opponents = ['Brock', 'Misty', 'Red', 'Professor Oaks Evil Twin', 'Brendan', 'Dawn']
pokedex = [{"Name": "Bulbasaur", "Type": ["Grass"]},
           {"Name": "Charmander", "Type": ["Fire"]},
           {"Name": "Squirtle", "Type": ["Water"]},
           {"Name": "Bellsprout", "Type": ["Grass"]},
           {"Name": "Chikorita", "Type": ["Grass"]},
           {"Name": "Sindaquil", "Type": ["Fire"]},
           {"Name": "Torchic", "Type": ["Fire"]},
           {"Name": "Ponita", "Type": ["Fire"]},
           {"Name": "Houndoom", "Type": ["Fire"]},
           {"Name": "Mudkip", "Type": ["Water"]},
           {"Name": "Psyduck", "Type": ["Water"]},
           {"Name": "Tototdile", "Type": ["Water"]},
           {"Name": "Goldeen", "Type": ["Water"]}]


def show_belt(player, pokemon):
    print(player.name, end=' - ')
    for slot in player.belt:
        if slot.is_ko == True:
            print('[/]', end=' ')
        else:
            print('[_]', end=' ')

    print('\n{0}    Level {1}   {2}/{3} HP'.format(pokemon.name, pokemon.lvl, round(pokemon.current_health, 2),
                                                   int(pokemon.max_health)))


def manifest_opponent_trainer():
    belt = []
    lvl = 0
    for slot in range(random.randint(1, 6)):
        random_pokemon = random.choice(pokedex)
        lvl = player.average_lvl() + random.randint(-3, 3)
        belt.append(Pokemon(random_pokemon['Name'], lvl, random_pokemon['Type']))
    wallet = random.randint(100, 10000)
    return Trainer(random.choice(opponents), belt, {}, wallet)


def wild_battle():
    texts = ['As you enter the woods, you encounter {0}.',
             'As you step into the wilderness, in front of you a wild {0} appears.',
             'Once upon a midnight dreary, while I pondered, weak and weary, in front of me a {0} appeary.']
    random_pokemon = random.choice(pokedex)
    adj_lvl = player.average_lvl() + random.randint(-3, 3)
    opponent_pokemon = Pokemon(random_pokemon['Name'], adj_lvl, random_pokemon['Type'])
    caught = False
    print(random.choice(texts).format(random_pokemon['Name']))
    time.sleep(2)

    print('Go {0}!'.format(player.belt[0].name))
    time.sleep(2)

    player_pokemon = player.belt[0]
    while (player.own_pokemon() and not opponent_pokemon.is_ko and not caught):
        print("\n{0}    Level {1}   {2}/{3} HP".format(opponent_pokemon.name, int(opponent_pokemon.lvl),
                                                       round(opponent_pokemon.current_health, 2),
                                                       int(opponent_pokemon.max_health)))
        print()
        show_belt(player, player_pokemon)
        choice = input("1) Attack\n2) Switch\n3) Use item\n")
        if (choice == '1'):

            player_pokemon.attack(opponent_pokemon)
            if opponent_pokemon.is_ko == True:
                print("Enemy {0} has fainted!".format(opponent_pokemon.name))
                player_pokemon.xp += 1
                if player_pokemon.xp == 4:
                    player_pokemon.level_up()

            else:
                opponent_pokemon.attack(player_pokemon)
            if (player_pokemon.is_ko):
                print("\n{0} has fainted!".format(player_pokemon.name))
                if (player.own_pokemon()):
                    print("Choose next pokemon:")
                    player.swap_pokemon()
                    player_pokemon = player.belt[0]
        elif (choice == '2'):
            player.swap_pokemon()
            player_pokemon = player.belt[0]
        elif (choice == '3'):
            caught = player.view_pack(wild=True)
            time.sleep(1.5)

    if (not player.own_pokemon()):
        print("\n {0} is out of usable Pokemon! {1} blacked out!".format(player.name, player.name))
        return False
    elif opponent_pokemon.is_ko == True:
        print("\n{0} defeated {1}!".format(player.name, opponent_pokemon.name))

    elif caught:
        print('Allright, you caught the {0}!'.format(opponent_pokemon.name))
        if len(player.belt) < 6:
            player.belt.append(opponent_pokemon)
        else:
            print('Your belt is already full')
        time.sleep(1.5)
    return True


def trainer_battle():
    opponent = manifest_opponent_trainer()

    print('Go {0}!'.format(player.belt[0].name))
    player_pokemon = player.belt[0]
    opponent_pokemon = opponent.belt[0]
    while (opponent.own_pokemon() and player.own_pokemon()):
        show_belt(opponent, opponent_pokemon)
        show_belt(player, player_pokemon)
        choice = int(input('1) Attack \n2) Switch \n3) Use item \n'))
        if choice == 1:
            player_pokemon.attack(opponent_pokemon)
            if opponent_pokemon.is_ko:
                print('Enemys {0} has fainted!'.format(opponent_pokemon.name))
                player_pokemon.xp += 1
                if player_pokemon.xp == 4:
                    player_pokemon.level_up()
                if opponent.own_pokemon():
                    opponent_pokemon = random.choice([poke for poke in opponent.belt if not poke.is_ko])
                    print('{0} sends out {1}!'.format(opponent.name, opponent_pokemon.name))
                else:
                    continue
            else:
                opponent_pokemon.attack(player_pokemon)
            if player_pokemon.is_ko:
                print('{0} has fainted!'.format(player_pokemon.name))
                if player.own_pokemon():
                    print('Choose next pokemon: ')
                    player.swap_pokemon()
                    player_pokemon = player.belt[0]
        elif choice == 2:
            player.swap_pokemon()
            player_pokemon = player.belt[0]
        elif choice == 3:
            player.view_pack()

    if not player.own_pokemon():
        print('{0} is out of usable Pokemon and has blacked out!'.format(player.name))
        return False
    elif not opponent.own_pokemon:
        print(
            '{0} has defeated {1} and has gotten {2} for winning.'.format(player.name, opponent.name, opponent.wallet))
        player.wallet += opponent.wallet
    return True


def shop():
    stock_shop = {'1': {'Name': 'Potion', 'Cost': 10},
                  '2': {'Name': 'Revive', 'Cost': 30},
                  '3': {'Name': 'Pokeball', 'Cost': 100},
                  '4': {'Name': 'Ultraball', 'Cost': 1000}}
    print('Welcome to the Poke Shop!\nYou own {0}$'.format(player.wallet))
    for num, dict in stock_shop.items():
        print('{0}) {1} - {2}$'.format(num, dict['Name'], dict['Cost']))
    item_choice = input('What would you like to buy?\n'
                        '[Number] to select or [Enter] to close:  ')
    if item_choice in stock_shop:
        quantity_choice = input('How many would you like to buy? \n1) 1\n2) 10\n3) Max\n')
        purchase(stock_shop[item_choice], quantity_choice)
    print('Thank you.')


def purchase(item, quantity):
    if (quantity == '1' and player.wallet >= item['Cost']):
        player.pack[item['Name']] = player.pack.get(item['Name'], 0) + 1
        player.wallet -= item['Cost']
    elif (quantity == '2' and player.wallet >= item['Cost'] * 10):
        player.pack[item["Name"]] = player.pack.get(item["Name"], 0) + 10
        player.wallet -= item["Cost"] * 10
    elif (quantity == '3'):
        player.pack[item["Name"]] = player.pack.get(item["Name"], 0) + player.wallet / item["Cost"]
        player.wallet = player.wallet % item["Cost"]


if __name__ == '__main__':
    time.sleep(2)
    print('Hello,there! \nGlad to meet you!')
    time.sleep(3)
    print('Welcome to the world of POKEMON.\nMy name is Oak.')
    time.sleep(3)
    print('People affectionately refer to me as the POKEMON Professor.')
    time.sleep(4)
    print('This world...\n'
          'is inhabited far and wide by creatures called POKEMON.')
    time.sleep(4)
    print('For some people, POKEMON are pets. Others use them for battling.')
    time.sleep(4)
    print('As for myself...\nI study POKEMON as a profession.')
    time.sleep(4)
    print('But first, tell me about yourself.')
    time.sleep(4)
    print("Let's begin with your name.\nWhat is it? ")
    bleh = input()
    time.sleep(2)
    print('I\'m sorry! My hearing is not what used to be. Would you mind repeating that.')
    player.name = input()
    print('Oh {0}. That\'s such a nice name.'.format(player.name))
    time.sleep(4)
    print('Your very own POKEMON legend is about to unfold!')
    time.sleep(4)
    print('A world of dreams and adventures with POKEMON awaits! Let\'s go!')
    time.sleep(4)
    print('Oh, right. Before we start, you might need some POKEMON. I hope you brought your own.')

    time.sleep(6)
    print(
        '--You look around in dread realising that you put too much effort into your outfit \nand that you completely forgot to bring any POKEMON with you!--')
    time.sleep(6)
    print(
        '--As sweat drips from your forehead you notice several Pokeball laying on the table \nand you grab them before the professor'
        ' notices anything.--')

    player.belt.extend([Pokemon("Bulbasaur", 5, ['grass']),
                        Pokemon("Charmander", 5, ['fire']),
                        Pokemon("Squirtle", 5, ['water'])])
    time.sleep(5)
    print('I had some Pokeballs laying somewhere around here, oh nevermind.')
    time.sleep(4)
    print('Ah great! I see you have some with you. Let\'s begin then!')
    time.sleep(2)
    playing = True
    while playing:
        choice = input("\nWhat would you like to do?\n"
                       "1) Search tall grass\n"
                       "2) Trainer Battle\n"
                       "3) Pokemon\n"
                       "4) Pack\n"
                       "5) Shop\n"
                       "6) Quit\n")
        if (choice == '1'):
            playing = wild_battle()
        elif (choice == '2'):
            playing = trainer_battle()
        elif (choice == '3'):
            player.view_pokemon()
        elif (choice == '4'):
            player.view_pack()
        elif (choice == '5'):
            shop()
        elif (choice == '6'):
            playing = False
    print('You completed {0}% of your Pokedex. That\'s good enough for today.'.format(random.randint(0, 15) * 0.1))
