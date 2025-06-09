class Game:
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
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
        
class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = []
        
    def add_game(self, game):
        self.games.append(game)
        
    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games) 
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estudio {self.name} ainda não lançou jogo")
        else:
            averege_note = total_notes / num_games
            print(f"Avaliação média dos jogos do estudio {self.name}: {averege_note:.2f}")    

game1 = Game("Batman: Arkham City", 2012, False, 9.5)
game2 = Game("Batman™: Arkham Origins ", 2013, False, 10)    
game3 = Game("Hitman: Absolution", 2012, False, 10)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()