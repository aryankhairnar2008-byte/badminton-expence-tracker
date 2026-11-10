class BadmintonSession:
    def __init__(self, session_date):
        self.session_date = session_date
        self.players = []
        self.court_rent = 0.0
        self.shuttle_cost = 0.0

    def add_players(self, player_list):
        self.players = player_list

    def set_expenses(self, court_rent, shuttle_cost):
        self.court_rent = float(court_rent)
        self.shuttle_cost = float(shuttle_cost)

    def calculate_split(self):
        total_expense = self.court_rent + self.shuttle_cost
        num_players = len(self.players)
        
        if num_players == 0:
            return "No players added."
        
        per_person_share = total_expense / num_players
        
        print("\n" + "="*40)
        print(f" 🏸 BADMINTON SESSION SUMMARY: {self.session_date}")
        print("="*40)
        print(f"Total Court Rent   : ₹{self.court_rent:.2f}")
        print(f"Total Shuttle Cost : ₹{self.shuttle_cost:.2f}")
        print(f"Total Expense      : ₹{total_expense:.2f}")
        print(f"Total Players      : {num_players}")
        print("-" * 40)
        print(f"Per Person Share   : ₹{per_person_share:.2f}")
        print("-" * 40)
        print("Players involved:")
        for idx, player in enumerate(self.players, 1):
            print(f" {idx}. {player} -> ₹{per_person_share:.2f}")
        print("="*40)

if __name__ == "__main__":
    print("--- Badminton Expense Splitter ---")
    date_input = input("Enter date: ")
    session = BadmintonSession(date_input)
    
    players_input = input("Enter player names separated by commas: ")
    player_list = [p.strip() for p in players_input.split(",") if p.strip()]
    session.add_players(player_list)
    
    rent = float(input("Enter total court rent (₹): "))
    shuttles = float(input("Enter total shuttle cost (₹): "))
    
    session.set_expenses(rent, shuttles)
    session.calculate_split()
