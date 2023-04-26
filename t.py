footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_footballers_by_goals)
print(list(converted_dict.keys())[0])
print(converted_dict)