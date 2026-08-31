import json

# Opening the Json with the character information
def open_file():
    with open("./Info/data/Character info.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


#Opening exactly the whole Killer and perk list, the individual Killer names or the respective Killer perks

def killers():
    data = open_file()
    killers = data["Killers"]
    return killers

def killer_list():
    list = []
    for key in killers():
        list.append(key)
    return list

def killer_perks():
    list = []
    ckillers = killers()
    for key in ckillers:
        for perk in ckillers[key]:
            list.append(perk)
    return sorted(list)

#Opening exactly the whole Survivor and perk list, the individual survivor names or the respective Survivor perks

def survivors():
    data = open_file()
    survivors = data["Survivors"]
    return survivors

def survivor_list():
    list = []
    for key in survivors():
        list.append(key)
    return list

def survivor_perks():
    list = []
    csurvivors = survivors()
    for key in csurvivors:
        for perk in csurvivors[key]:
            list.append(perk)
    return sorted(list)
