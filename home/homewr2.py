from homewr1 import Hero
class ground_hero(Hero):
    def __init__(self, name, nickname, fly):
        self.name = name
        self.nickname = nickname
        self.fly = fly
    def brand_phrase(self):
        fly = True
        print(f'Hooray, I can fly! {fly}')
    def __Gen_X(self):
        pass
class air_hero(Hero):
    def __init__(self, name, nickname, fly):
        self.name = name
        self.nickname = nickname
        self.fly = fly
    def brand_phrase(self):
        fly = True
        print (f'Fly in the {fly}')
    def __Gen_X(self):
        pass
class space_hero(Hero):
    def __init__(self, name, nickname, fly):
        self.name = name
        self.nickname = nickname
        self.fly = fly
    def brand_phrase(self):
            fly = True
            print(f'Fly in the {fly}')
    def __Gen_X(self):
        pass
g_hero = ground_hero('Barry', 'Flash', False)
g_hero.brand_phrase()
a_hero = air_hero('Bruce', 'Batman', False)
a_hero.brand_phrase()
s_hero = space_hero('Clark', 'Superman', False)
s_hero.brand_phrase()


