
name_hero = input("Твое имя герой:")
print("Привет,", name_hero)
damage_hero = input("Ударь меня: ")
damage_hero = int(damage_hero)
health_monster = 100
health_hero = 100

#class hero():

    #def __init__(self, health_hero = 100):
       # self.health_hero = health_hero


#class monster:


    #def __init__(self, health_monster = 100, damage_monster= 10):
        #self.health_monster = health_monster
       # self.damage_monster = damage_monster




def main():

    global health_monster, health_hero, hit_monster , hit_hero
    finish = False
    while not finish:
        print('Монстр: мое здоровье', health_monster, 'ударь меня!')
        health_hero -= monster(hit_monster)
        health_monster -= hero(hit_hero)
        print('Здоровье героя:', health_hero)
    if health_monster <= 0 < health_hero:
        finish = True
        print('Ты победил!', 'сверх урон', -health_monster)
    elif health_hero <= 0 < health_monster:
        finish = True
        print('Ты проиграл Ха Ха Ха!', 'сверх урон', (-health_hero), (-health_monster))
    elif health_hero <= 0 and health_monster <= 0:
        finish = True
        print('Ничья вы оба сдохли Ха Ха Ха!', 'сверх урон', (-health_monster))


main()
