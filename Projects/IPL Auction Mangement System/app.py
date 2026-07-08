teams = {
    1: {'name': "Mumbai Indians", 'purse': 120, 'players': []},
    2: {'name': "Chennai Super Kings", 'purse': 120, 'players': []},
    3: {'name': "Royal Challengers Bangalore", 'purse': 120, 'players': []},
    4: {'name': "Punjab Kings", 'purse': 120, 'players': []},
}

players = {
    101: {'name': "Ms Dhoni", 'role': "Wicket-Keeper", 'base_price': 25, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    102: {'name': "Rohit Sharma", 'role': "Batsmen", 'base_price': 22, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    103: {'name': "Shreyas Iyer", 'role': "Batsmen", 'base_price': 18, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    104: {'name': "Ravindra Jadeja", 'role': "All-Rounder", 'base_price': 16, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    105: {'name': "KL Rahul", 'role': "Wicket-Keeper", 'base_price': 15, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    106: {'name': "Shubman Gill", 'role': "Batsmen", 'base_price': 17, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    107: {'name': "Mohammed Siraj", 'role': "Bowler", 'base_price': 16, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    108: {'name': "Hardik Pandya", 'role': "All-Rounder", 'base_price': 20, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    109: {'name': "Jasprit Bumrah", 'role': "Bowler", 'base_price': 18, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
    110: {'name': "Mohammed Shami", 'role': "Bowler", 'base_price': 13, 'status': "unsold", 'sold_to': None, 'sold_price': 0},
}


# services

# view all teams and their purse/players
def view_teams():
    for team_id, info in teams.items():
        print(f"{team_id}. {info['name']} | Purse Left: {info['purse']} Cr | Players Bought: {len(info['players'])}")


# view all players and their status
def view_players():
    for player_id, info in players.items():
        status_info = f"SOLD to {teams[info['sold_to']]['name']} for {info['sold_price']} Cr" if info['status'] == "sold" else "UNSOLD"
        print(f"{player_id}. {info['name']} ({info['role']}) | Base Price: {info['base_price']} Cr | {status_info}")


# bid function definition
def bid(player_id: int) -> str:
    # check player exists
    if player_id not in players:
        return "Player not found"

    player = players[player_id]

    # check player already sold
    if player['status'] == "sold":
        return "Player already sold"

    current_bid = player['base_price']
    highest_bidder = None

    print(f"\nPlayer: {player['name']} ({player['role']})")
    print(f"Base Price: {current_bid} Cr")

    # only teams who can afford the base price take part
    active_teams = [team_id for team_id, info in teams.items() if info['purse'] >= current_bid]

    if not active_teams:
        return f"{player['name']} went UNSOLD (no team has sufficient purse)"

    # keep going round after round until only one team is left standing
    while len(active_teams) > 1:

        for team_id in active_teams[:]:

            print(f"\nCurrent Bid: {current_bid} Cr")
            print(f"{teams[team_id]['name']} Turn")

            response = input("Enter Bid Amount or PASS: ").strip().upper()

            if response == "PASS":
                active_teams.remove(team_id)
                print(f"{teams[team_id]['name']} Passed")
            else:
                amount = int(response)

                if amount > current_bid and amount <= teams[team_id]['purse']:
                    current_bid = amount
                    highest_bidder = team_id
                    print(f"{teams[team_id]['name']} Highest Bid: {current_bid} Cr")
                else:
                    print("Invalid Bid")

            if len(active_teams) == 1:
                break

    # if no one actually raised the bid, the last remaining team wins at base price
    if highest_bidder is None:
        highest_bidder = active_teams[0]

    # mark player as sold
    player['status'] = "sold"
    player['sold_to'] = highest_bidder
    player['sold_price'] = current_bid

    # update team purse and player list
    teams[highest_bidder]['purse'] -= current_bid
    teams[highest_bidder]['players'].append(player_id)

    return f"{player['name']} SOLD to {teams[highest_bidder]['name']} for {current_bid} Cr"


# team summary function definition
def team_summary(team_id: int):
    if team_id not in teams:
        return "Team not found"
    info = teams[team_id]
    print(f"Team: {info['name']}")
    print(f"Purse Left: {info['purse']} Cr")
    print("Players Bought:")
    if not info['players']:
        print("  No players bought yet")
    for pid in info['players']:
        p = players[pid]
        print(f"  {p['name']} ({p['role']}) - Bought for {p['sold_price']} Cr")


# auction summary - unsold players list
def unsold_list():
    unsold = [p['name'] for p in players.values() if p['status'] == "unsold"]
    if not unsold:
        return "No unsold players remaining"
    return "Unsold Players: " + ", ".join(unsold)


# main
if __name__ == "__main__":

    print("Welcome to the IPL Auction Management System")

    while True:
        print("\nIPL Auction Menu")
        print("1. View Teams \n 2. View Players \n \
              3. Start Bid \n 4. Team Summary \n \
              5. Unsold Players List \n 6. Exit")
        choice = int(input("Enter your choice(1-6): "))

        if choice == 1:
            # view all teams
            view_teams()

        elif choice == 2:
            # view all players
            view_players()

        elif choice == 3:
            # bid on a player
            player_id = int(input("Enter Player ID to bid on: "))
            res = bid(player_id=player_id)
            print(res)

        elif choice == 4:
            # view a specific team's summary
            team_id = int(input("Enter Team ID: "))
            team_summary(team_id=team_id)

        elif choice == 5:
            # view unsold players
            print(unsold_list())

        elif choice == 6:
            print("ThankYou for using IPL Auction Management System, See You Again....")
            break

        else:
            print("Invalid Choice! Please select between 1 and 6 choices.")