class Hero:
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        print(f'{self.nickname} heals {self.hp + 100} hit points')

    def double_damage(self):
        print(f'{self.nickname} is dealing double damage {self.damage * 2}')

    def greetings(self):
        print(f'My name is {self.name}, people knows me like {self.nickname}')

    def brand_phrase(self):
        print(f'{self.nickname} says: "Good always triumphs over evil!!!')

hero1 = Hero('Peter', 'Spider-Man', 100, 100)
hero2 = Hero('Logan', 'Wolverine', 200, 100)
hero3 = Hero('Bruce', 'Hulk', 500 , 200)
hero4 = Hero('Tony', 'Iron-Man', 300, 250)

hero1.heal()
hero2.double_damage()
hero3.greetings()
hero4.brand_phrase()