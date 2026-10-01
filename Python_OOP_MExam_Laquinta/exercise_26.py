class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score  

    def add_points(self, points):
        self.score += points  


ana = Player("Ana", 10)
ben = Player("Ben")
ana.add_points(5)
ben.add_points(7)
print(ana.score)
print(ben.score)