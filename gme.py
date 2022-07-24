def main():
    health_monster = 100
    health_hero = 100
    finish = False
    while not finish:
        print('Монстр: мое здоровье', health_monster,  'ударь меня!')
        damage = int(input())
        back_hit = 0.5 * damage
        health_hero -= back_hit
        health_monster -= damage
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
