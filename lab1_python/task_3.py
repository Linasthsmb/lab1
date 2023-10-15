list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
num = len(list_players)

first_team = list_players[:int(num//2)]
sec_team = list_players[int(num//2)::]
print(first_team)
print(sec_team)
