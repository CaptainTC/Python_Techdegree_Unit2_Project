import constants
import copy

if __name__ == "__main__":
    team_list = copy.deepcopy(constants.TEAMS)
    player_list = copy.deepcopy(constants.PLAYERS)
    exp_players = 0
    clean_unassigned_player_list = []

    for each_dic in player_list:
        each_dic["height"] = int(each_dic["height"][0:2])

        if each_dic["experience"] == "YES":
            each_dic["experience"] = True
            exp_players += 1
        else:
            each_dic["experience"] = False
        if each_dic["guardians"]:
            guardians_list = []
            if " and " in each_dic["guardians"]:
                end = len(each_dic["guardians"])
                num = (each_dic["guardians"].index(" and "))
                num2 = num + 5
                first_guardian = (each_dic["guardians"])[0:(num)]
                second_guardian = (each_dic["guardians"])[num2:]
                guardians_list.append(first_guardian)
                guardians_list.append(second_guardian)
                each_dic["guardians"] = guardians_list
            else:
                guardians_list.append(each_dic["guardians"])
                each_dic["guardians"] = guardians_list

        clean_player_dic = {
            'name': each_dic["name"],
            'guardians': each_dic["guardians"],
            'experience': each_dic["experience"],
            'height': each_dic["height"]}

        if True in clean_player_dic.values():
            clean_unassigned_player_list.insert(0, clean_player_dic)
        else:
            clean_unassigned_player_list.append(clean_player_dic)

    team_size = int(len(player_list)/len(team_list))
    exp_players_per_team = int(exp_players / len(team_list))
    team_dic = {}

    for team in team_list:
        assigned_teams = []

        for player in clean_unassigned_player_list[0:exp_players_per_team]:
            assigned_teams.append(clean_unassigned_player_list.pop(0))
        clean_unassigned_player_list.reverse()

        for player in clean_unassigned_player_list[0:exp_players_per_team]:
            assigned_teams.append(clean_unassigned_player_list.pop(0))
        clean_unassigned_player_list.reverse()
        team_dic[team] = assigned_teams

    while True:
        options = 1
        which_team = {}
        height_sum = 0
        name_list = []
        guardian_list = []

        print("\nBasketball Team Stats Tool\n\n    ----Menu----")
        print("Please choose an option\n1) Display Team Stats\n2) Quit")

        while True:

            choosen_option = input("\nEnter an option: ")
            try:
                choosen_option = int(choosen_option)
                if choosen_option == 2 or choosen_option == 1:
                    break
                else:
                    print("Error: Please choose from the provided options")
                    continue
            except ValueError:
                print("Error: Please enter numeric values only")
                continue

        if choosen_option == 1:
            print("\nTeams")

            for teams in team_dic.keys():
                print("{}) {}".format(options, teams))
                which_team[options] = teams
                options += 1

            while True:
                team_choice = input("\nEnter an option: ")
                try:
                    team_choice = int(team_choice)
                    if team_choice in which_team:
                        break
                    else:
                        print("Error: Please choose from the provided options")
                        continue
                except ValueError:
                    print("Error: Please enter numeric values only")
                    continue

            for players in team_dic[which_team[team_choice]]:
                for topic, info in players.items():
                    total_players = len(team_dic[which_team[team_choice]])
                    if topic == "height":
                        height_sum = height_sum + info
                    if topic == "name":
                        name_list.append(info)
                    if topic == "guardians":
                        guardian_list.extend(info)
            name_str = ", ".join(name_list)
            guardian_str = ", ".join(guardian_list)

            print("\nTeam: {} Stats\n---------------".format(which_team[team_choice]))
            print("Total players: {}".format(len(team_dic[which_team[team_choice]])))
            print("Total experienced: {}".format(exp_players_per_team))
            print("Total inexperienced: {}".format(exp_players_per_team))
            print("Average height: {}".format(height_sum / len(team_dic[which_team[team_choice]])))
            print("\nPlayers on Team:\n " + name_str)
            print("\nGuardians:\n " + guardian_str)


        if choosen_option == 2:
            print("\nThank you for using my application.")
            break

        while True:
            next_move = input("\n\nPress ENTER to continue...")
            if next_move == "":
                break
