class Family:
    def __init__(self, address) -> None:
        self.address = address

class school:
    def __init__(self,id ,level) -> None:
        self.id=id
        self.level=level

class Sports:
    def __init__(self,game)-> None:
        self.game=game

class Student(Family,school,Sports) :
    def __init__(self, address,id ,level,game):
        super().__init__(address)

class throphy(Sports):
    def __init__(self, game):
        super().__init__(game)