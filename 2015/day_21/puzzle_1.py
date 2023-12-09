import re

with open("data.txt") as data:
    bossdata = data.read().splitlines()

arm_txt = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3""".splitlines()

arms = []
for l in arm_txt:
    if ':' in l:
        arms.append([])
    elif len(l) == 0:
        pass
    else:
        arms[-1].append(list(map(int,re.findall(r" (\d+)", l))))

def fight(pd, pa):
    bhp = int(bossdata[0].split(' ')[-1])
    bd = int(bossdata[1].split(' ')[-1])
    ba = int(bossdata[2].split(' ')[-1])
    php = 100
    while True:
        #player attacks
        if ba >= pd:
            bhp -= 1
        else:
            bhp -= pd - ba
        if bhp <= 0:
            return 1
        if pa >= bd:
            php -= 1
        else:
            php -= bd - pa
        if php <= 0:
            return 0

min_cost = 999999

arms[1].append([0,0,0])
arms[2].append([0,0,0])
arms[2].append([0,0,0])
for wc, wd, wa in arms[0]:
    for ac, ad, aa in arms[1]:
        for rc, rd, ra in arms[2]:
            for r2c, r2d, r2a in arms[2]:
                pd = wd + rd + r2d
                pa = aa + ra + r2a
                if fight(int(pd), int(pa)):
                    cost = wc+ac+rc+r2c
                    if cost < min_cost:
                        min_cost = cost
print(min_cost)