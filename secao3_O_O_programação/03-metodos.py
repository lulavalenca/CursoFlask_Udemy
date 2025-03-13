class Game():
    name = ""
    yearLauch = 0
    multiplayer = False
    note = 0
    
# Primeiro Jogo
game1 = Game()
game1.name = "Batman: Arkham City"
game1.yearLauch = 2012
game1.multiplayer = False
game1.note = 10


# Segundo Jogo
game2 = Game()
game2.name = "Batman™: Arkham Origins"
game2.yearLauch = 2013
game2.multiplayer = False
game2.note = 9

# Terceiro Jogo
game3 = Game()
game3.name = "Hitman: Absolution"
game3.yearLauch = 2012
game3.multiplayer = False
game3.note = 8.5

print("###Dados do Jogo###")
print(f"Nome do Jogo: {game1.name}\nAno de Lançamento: {game1.yearLauch}")
print(f"\nNome do Jogo: {game2.name}\nAno de Lançamento: {game2.yearLauch}")
print(f"\nNome do Jogo: {game3.name}\nAno de Lançamento: {game3.yearLauch}")