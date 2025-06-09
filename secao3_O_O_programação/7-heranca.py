# Classe Pai (Super classe) - Generalista
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
    
# Classe derivada (Subclasse) - Especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0, storyline=""):
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.storyline = storyline
        
    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")
        
mult_game = Game("Call of Duty: Modern Warfare II", 2022, True, 9.5)
mult_game.technical_sheet()

sing_game = SinglePlayerGame("The Witcher 3: Wild Hunt", 2015, False, 10, "Geralt of Rivia's journey to find his adopted daughter.")
sing_game.technical_sheet()