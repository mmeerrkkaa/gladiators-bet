import random 



class Gladiators:
    def __init__(self, streng, agility, luck, points):
        self.streng = streng
        self.agility = agility
        self.luck = luck      
        self.points = points
        self.hp = 100
        self.damage = 1
        self.chance_critical = 0

        self.random_points()

    # ========= Перерасчёт жизней, урона, шанс крит удара =========
    def calculation_hp(self):
        """Функция перерасчёта кол-ва жизней"""
        self.hp += self.streng * 20
        
    def calculation_damage(self):
        """Функция перерасчёта кол-ва урона"""
        self.damage += self.streng * 0.3 + self.agility * 0.3

    def calculation_chance_critical(self):
        """Функция перерасчёта шанса крит удара"""
        self.chance_critical += self.agility * 0.001 + self.luck * 0.01

    # =======================================

    def random_points(self):
        """Тратим все очки навыков гладиатора на рандом характеристики"""
        for _ in range(self.points):
            name = {1: "streng",
                   2: "agility",
                   3: 'luck'}

            skill = name[random.randint(1,3)]
            self.__dict__[skill] += 1
            self.__dict__['points'] -= 1
            self.calculation_hp()
            self.calculation_damage()
            self.calculation_chance_critical()


class Battle:
    def __init__(self, points):
        self.gladiators_one = Gladiators(1, 1, 1, points)
        self.gladiators_two = Gladiators(1, 1, 1, points)

        

    def who_one(self):
        # Если рандомное число 1, то они меняются местами, если 0 то не меняются
      if random.randint(0,1) == 1:
        self.gladiators_one, self.gladiators_two = self.gladiators_two, self.gladiators_one
        


    def calculation_hit(self, gladiators) -> float:
        return gladiators.damage * 2 if random.randint(0, 100) <= gladiators.chance_critical else gladiators.damage

    
        
    def show_gladiators(self):
        print(self.gladiators_one.__dict__)
            

a = Battle(80)

class Game:
    def __init__(self):
        self.money = 100
        self.stats = {"win": 0, "lose": 0, "total_win_money": 0, "total_lose_money": 0, "total_win": 0}

        self.current_gladiators = None
