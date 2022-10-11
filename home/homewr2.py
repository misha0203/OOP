from homewr1 import Hero
class ground_hero(Hero):
    fly = False
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname
    def brand_phrase(self):
        fly = True
        print(f'Hooray, I can fly! {fly}')
    def __Gen_X(self):
        pass
class air_hero(Hero):
    fly = False
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname
    def brand_phrase(self):
        fly = True
        print(f'Fly in the {fly}')
    def __Gen_X(self):
        pass
class space_hero(Hero):
    fly = False
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname
    def brand_phrase(self):
        fly = True
        print(f'Fly in the {fly}')
    def __Gen_X(self):
        pass
g_hero = ground_hero('Barry', 'Flash')
g_hero.brand_phrase()
a_hero = air_hero('Bruce', 'Batman')
a_hero.brand_phrase()
s_hero = space_hero('Clark', 'Superman')
s_hero.brand_phrase()


