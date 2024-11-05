
# Define a class for the hero
class Hero():
    def __init__(self,name,health,strength,defence):
        self.__name = name
        self.__health = health
        self.__strength = strength
        self.__defence = defence

    def getName(self):
        return self.__name

    def getStats(self):
        return self.__health, self.__strength, self.__defence


def Game():
    
    # Function to display the hero names pre-game
    def announce_heros(hero1,hero2):
        print("\n\n")
        print("Welcome to Superhero Fighter!!!".center(50))
        print("Today's Matchup".center(50))
        print(f"{"-"*50}".center(50))

        hero1_name = hero1.getName()
        hero2_name = hero2.getName()
        print(f"{hero1_name} VS {hero2_name}".center(50))
    

    # Starts the figh between two user defined heros
    def start_fight(hero1,hero2):
        
        # Functions
        def get_move():
            print("\nWould you like to:\n|Attack\n|Defend")
            hero_move = input(">> ")
            hero_move = hero_move.lower()
            if hero_move == "attack" or hero_move == "defend":
                return hero_move
            else:
                print("Invalid move input! Defaulting to Attack!")
                return "attack"
        

        # Variables for the game loop
        current_move = 0
        not_dead = True
        
        # Variables for our heros
        h1_name = hero1.getName()
        h1_health, h1_strength, h1_defence = hero1.getStats()

        h2_name = hero2.getName()
        h2_health, h2_strength, h2_defence = hero2.getStats()

        # An array to store the previous move E.g. Attack or Defend
        previous_move = ["",""]

        while not_dead:

            # If current_move % 2 == 0 then it's Hero1's turn
            if current_move % 2 == 0:
                print("\n")
                print(f"It's {h1_name}'s turn!".center(50))

                hero_move = get_move()

                if hero_move == "attack":

                    # If Hero2 defended on their last go, we must reduce to damadge taken
                    if previous_move:
                        if previous_move[1] == "defend":
                            h2_health = h2_health - ((h1_strength//2) - (h2_defence//2))

                            # Check if the hero is dead
                            if h2_health <= 0:
                                print(f"{h1_name} defeated {h2_name} with that attack!")
                                print("\n")
                                print(f"{h1_name} wins!!".center(50))
                                exit()

                            # If the hero is not dead, display a message to the user of the new Hero heal
                            else:
                                print(f"\n{h2_name} reduced an attack from {h1_name} by defending {h2_defence//2} hp, and is now on {h2_health} hp (-{h1_strength//2 - h2_defence//2} hp)")
                                previous_move[1] = ""
                            

                        # Otherwise, the Hero can't block any damadge
                        else:
                            h2_health = h2_health - (h1_strength // 2)
                            # Check if the hero is dead
                            if h2_health <= 0:
                                print(f"{h1_name} defeated {h2_name} with that attack!")
                                print("\n")
                                print(f"{h1_name} wins!!".center(50))
                                exit()

                            else:
                                print(f"\n{h2_name} was attacked by {h1_name} and is now on {h2_health} hp (-{h1_strength//2} hp)")


                else:
                    print(f"\nYou will block {h1_defence//2} hp from your next incoming attack!")
                    previous_move[1] = "defend"
                    
                current_move += 1

            # Otherwise, it is Hero2's turn
            else:
                print("\n")
                print(f"It's {h2_name}'s turn!".center(50))

                hero_move = get_move()

                if hero_move == "attack":
                    if previous_move:
                        # If Hero1 defended on their last go, we must reduce to damadge taken
                        if previous_move[1] == "defend":
                            h1_health = h1_health - ((h2_strength//2) - (h1_defence//2))

                            # Check if the hero is dead
                            if h1_health <= 0:
                                print(f"{h2_name} defeated {h1_name} with that attack!")
                                print("\n")
                                print(f"{h2_name} wins!!".center(50))
                                exit()

                            # If the hero is not dead, display a message to the user of the new Hero health
                            else:
                                print(f"\n{h1_name} reduced an attack from {h2_name} by defending {h1_defence//2} hp, and is now on {h1_health} hp (-{h2_strength//2 - h1_defence//2} hp)")
                                previous_move[1] = ""
                        # Otherwise, the Hero can't block any damadge
                        else:
                            h1_health = h1_health - (h2_strength // 2)
                            
                            # Check if the hero is dead
                            if h1_health <= 0:
                                print(f"{h2_name} defeated {h1_name} with that attack!")
                                print("\n")
                                print(f"{h2_name} wins!!".center(50))
                                exit()

                            else:
                                print(f"\n{h1_name} was attacked by {h2_name} and is now on {h1_health} hp (-{h2_strength//2} hp)")


                else:
                    print(f"\nYou will block {h2_defence//2} hp from your next incoming attack!")
                    previous_move[1] = "defend"
                    
                current_move += 1
   
    
    # Function to allow the user to make a hero
    def add_hero():
        # Perform validation on all user inputs for a hero
        while True:

            hero_name = input("Enter the Hero name >> ")


            # For each stat make sure it is more than 0    
            try:
                hero_health = int(input(f"Enter {hero_name}'s health amount >> "))
                if hero_health <= 0:
                    print(f"Thats no fair for the hero! Health has been updated to 100")
                    hero_health = 100
            except:
                print("That's not a number!! Health has been updated to 100")
                hero_health = 100

            try:
                hero_strength = int(input(f"Enter {hero_name}'s strength amount >> "))
                if hero_strength <= 0:
                    print(f"Thats no fair for the hero! Strength has been updated to 35")
                    hero_strength = 35
            except:
                print("That's not a number!! Srength has been updated to 35")
                hero_strength = 35

            try:
                hero_defence = int(input(f"Enter {hero_name}'s defence amount >> "))
                if hero_defence <= 0:
                    print(f"Thats no fair for the hero! Defence has been updated to 45")
                    hero_defence = 45
            except:
                print("That's not a number!! Defence has been updated to 45")
                hero_defence = 45
            break
        hero_instance = Hero(hero_name,hero_health,hero_strength,hero_defence) 
        return hero_instance


    # Get the user to create two heros
    print("\n\n")
    print("Time to prepare the fight!".center(50))
    print("\nLet's add the first Hero!")
    Hero1 = add_hero()
    print("\nLet's add the second Hero!")
    Hero2 = add_hero()

    print("\n")

    # Check if the user want's to begin the fight
    print("Ready to Start?".center(50))
    start_game = input(">> ")
    start_game = start_game.lower()
    if start_game== "yes" or start_game == "y":
        # Announce the game matchup 
        announce_heros(Hero1,Hero2)
        start_fight(Hero1,Hero2)
    else:
        print("What a waste of my time!! :<")
        exit()




# Call the function to start the game
Game()
        
