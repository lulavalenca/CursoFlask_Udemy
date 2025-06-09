class Game():
    name = ""
    yearLauch = 0
    multiplayer = False
    note = 0
    
    def __init__(self, name="", yearLauch=0, multiplayer=False, note=0):
        self.name = name
        self.yearLauch = yearLauch
        self.multiplayer = multiplayer
        self.note = note
    
    def __str__(self):
        return f"Game: {self.name},"
    
game1 = Game("Batman: Arkham City", 2012, False, 10)
game2 = Game("Batman™: Arkham Origins", 2013, False, 9)
game3 = Game("Hitman: Absolution", 2012, False, 8.5)
game4 = Game("Dead Space", 2008, False, 10)
game5 = Game("Resident Evil 4", 2023, False, 9)



    

print("###Dados do Jogo###")
print(f"Nome do Jogo: {game1.name}\nAno de Lançamento: {game1.yearLauch}")
print(f"\nNome do Jogo: {game2.name}\nAno de Lançamento: {game2.yearLauch}")
print(f"\nNome do Jogo: {game3.name}\nAno de Lançamento: {game3.yearLauch}")
print(f"\nNome do Jogo: {game4.name}\nAno de Lançamento: {game4.yearLauch}")
print(f"\nNome do Jogo: {game5.name}\nAno de Lançamento: {game5.yearLauch}")