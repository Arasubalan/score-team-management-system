class Team:
    def __init__(self, name):
        self.name = name
        self.batsmens = {}
        self.bowlers = {}

    def add_batsman(self, name, runs, age, place):
        self.batsmens[name] = {"runs":runs,"age": age, "place": place}

    def get_total_runs(self):
        return sum(player["runs"]for player in self.batsmens.values())

    def add_bowler(self, name, wickets, age, place):
        self.bowlers[name] = {"wickets":wickets,"age": age, "place": place}

    def get_total_wickets(self):
        return sum(player["wickets"] for player in self.bowlers.values())

    def update_batsman(self, name, runs, age, place):
        if name in self.batsmens:
            self.batsmens[name] = {"runs": runs, "age": age, "place": place}
        else:
            print("Batsman not found.")

    def update_bowler(self, name, wickets, age, place):
        if name in self.bowlers:
            self.bowlers[name] = {"wickets": wickets, "age": age, "place": place}
        else:
            print("Bowler not found.")

    def display(self):
        print(f"\nTeam: {self.name}")
        print("Batsmen and their stats:")
        for name, info in self.batsmens.items():
            print(f"{name}: {info['age']} years old, from {info['place']}")
        print(f"Total Runs: {self.get_total_runs()}")

        print("\nBowlers and their stats:")
        for name, info in self.bowlers.items():
            print(f"{name}: {info['age']} years old, from {info['place']}")
        print(f"Total Wickets: {self.get_total_wickets()}")

    def view_batsmens(self):
        print("\nList of Batsmen:")
        if not self.batsmens:
            print("No batsmen added yet.")
        else:
            for name, info in self.batsmens.items():
                print(f"{name}: {info['runs']} runs")

    def view_bowlers(self):
        print("\nList of Bowlers:")
        if not self.bowlers:
            print("No bowlers added yet.")
        else:
            for name, info in self.bowlers.items():
                print(f"{name}: {info['wickets']} wickets")

    def show_score(self):
        print(f"\nTeam Score Summary for {self.name}")
        print(f"Total Runs: {self.get_total_runs()}")
        print(f"Total Wickets: {self.get_total_wickets()}")


# ---- MAIN PROGRAM ----
team_name = input("Enter team name: ")
match = Team(team_name)

while True:
    print("\n_______MENU________")
    print("1: Add Batsman")
    print("2: View Batsman")
    print("3: Add Bowler")
    print("4: View Bowler")
    print("5: Update Batsman")
    print("6: Update Bowler")
    print("7: Show Team Details")
    print("8: Show Team Score")
    print("9: Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        player = input("Enter the batsman name: ").upper()
        age = int(input("Enter the age: "))
        place = input("Enter the place: ").upper()
        runs = int(input("Enter the runs (1-100): "))
        match.add_batsman(player, runs, age, place)

    elif choice == "2":
        match.view_batsmens()

    elif choice == "3":
        player = input("Enter the bowler name: ").upper()
        age = int(input("Enter the age: "))
        place = input("Enter the place: ").upper()
        wickets = int(input("Enter the wickets (1-9): "))
        match.add_bowler(player, wickets, age, place)

    elif choice == "4":
        match.view_bowlers()

    elif choice == "5":
        player = input("Enter the batsman name to update: ").upper()
        age = int(input("Enter the age: "))
        place = input("Enter the place: ").upper()
        runs = int(input("Enter the new runs: "))
        match.update_batsman(player, runs, age, place)

    elif choice == "6":
        player = input("Enter the bowler name to update: ").upper()
        age = int(input("Enter the age: "))
        place = input("Enter the place: ").upper()
        wickets = int(input("Enter the new wickets: "))
        match.update_bowler(player, wickets, age, place)

    elif choice == "7":
        match.display()

    elif choice == "8":
        match.show_score()

    elif choice == "9":
        print("Exiting program.")
        break

    else:
        print("Invalid option, please choose between 1 to 9.")
