class Game:
    total_games = 0
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
        
    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer?: {self.multiplayer}")
        print(f"Avaliação do jogo: {self.note}\n")
        
    def evaluete(self, note):
        self.totalEvaluation += note
        self.evaluators += 1 
        
    def average(self):
        print(f"Média do Jogo {self.name}: {self.totalEvaluation / self.evaluators}")    
    
game1 = Game("Batman: Arkham City", 2012, False, 9.5)
game2 = Game("Batman™: Arkham Origins ", 2013, False, 10)
game3 = Game("Hitman: Absolution", 2012, False, 10)

game1.technical_sheet()
game2.technical_sheet()
game3.technical_sheet()
game1.evaluete(9.5)
game1.evaluete(8.5)
game1.average()
game2.evaluete(10)
game2.evaluete(9.0)
game2.average()

# Exibindo o numero total de jogos Criados
print(f"Total de jogos criados: {Game.total_games}")