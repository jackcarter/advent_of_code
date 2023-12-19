from copy import deepcopy
from math import inf

with open("data.txt") as data:
    bossdata = data.read().splitlines()
    bhp_start = int(bossdata[0].split(' ')[-1])
    bdmg = int(bossdata[1].split(' ')[-1])

mana_start = 500
php_start = 50

game = ({}, {"php": php_start, "bhp": bhp_start, "mana": mana_start, "spent_mana": 0, "armor": 0,
        "shield_active": 0, "recharge_active": 0, "poison_active": 0, 
        "magic_missile_active": 0, "drain_active": 0, #these two are always 0, just simplifies checking availability
        "bdmg": bdmg})

games = [game]

def available_spells(game):
    spells_cast, gamestate = game
    available_spells = [{"mana": 53, "action": "magic_missile", "effect": 0, "duration": 0},
        {"mana": 73, "action": "drain", "effect": 0, "duration": 0},
        {"mana": 113, "action": "shield", "effect": 7, "duration": 6},
        {"mana": 173, "action": "poison", "effect": 3, "duration": 6},
        {"mana": 229, "action": "recharge", "effect": 101, "duration": 5}
                        ]
    available_spells = [s for s in available_spells if s["mana"]<=gamestate["mana"] and gamestate[s["action"]+"_active"] == 0]
    return available_spells

def cast_spell(game, spell):
    spells_cast, gamestate = game
    if spell["action"] in spells_cast:
        spells_cast[spell["action"]] += 1
    else:
        spells_cast[spell["action"]] = 1
    #spells_cast += (spell["action"],)
    gamestate["mana"] -= spell["mana"]
    gamestate["spent_mana"] += spell["mana"]
    if spell["action"] == "shield":
        gamestate["shield_active"] = spell["duration"]
        gamestate["armor"] = spell["effect"]
    elif spell["action"] == "poison":
        gamestate["poison_active"] = spell["duration"]
    elif spell["action"] == "recharge":
        gamestate["recharge_active"] = spell["duration"]
    elif spell["action"] == "magic_missile":
        gamestate["bhp"] -= 4
    elif spell["action"] == "drain":
        gamestate["bhp"] -= 2
        gamestate["php"] += 2
    return spells_cast, gamestate

def apply_effects(game):
    spells_cast, gamestate = game
    if gamestate["shield_active"] > 0:
        gamestate["shield_active"] -= 1
        gamestate["armor"] = 7
    elif gamestate["shield_active"] == 0:
        gamestate["armor"] = 0

    if gamestate["poison_active"] > 0:
        gamestate["poison_active"] -= 1
        gamestate["bhp"] -= 3

    if gamestate["recharge_active"] > 0:
        gamestate["recharge_active"] -= 1
        gamestate["mana"] += 101
    return spells_cast, gamestate

min_mana = inf
while len(games) > 0:
    game = min(games, key=lambda x: x[1]["bhp"])
    games.remove(game)
    spells = available_spells(game)
    
    #apply effects and decrement timers
    game = apply_effects(game)
    #fork and cast spells
    spells = available_spells(game)
    for spell in spells:
        newgame = deepcopy(game)
        newgame = cast_spell(newgame, spell)

        #boss's turn
        newgame = apply_effects(newgame)
        if newgame[1]["bhp"] <= 0:
            games.append(newgame)
            continue
        newgame[1]["php"] -= max(1, newgame[1]["bdmg"] - newgame[1]["armor"])
        if newgame[1]["php"] <= 0:
            #don't add to games
            continue
        if newgame[1]["bhp"] <= 0:
            games.append(newgame)
            continue
        games.append(newgame)


    winners = [g[1]["bhp"] <= 0 for g in games]
    if any(winners):
        new_min_mana = min([(g[0], g[1]["spent_mana"]) for g in games if g[1]["bhp"] <= 0], key=lambda x: x[1])
        if new_min_mana[1] < min_mana:
            min_mana = new_min_mana[1]
    #prune games that have spent more mana than the current minimum
    games = [g for g in games if g[1]["spent_mana"] <= min_mana]

print(min_mana)