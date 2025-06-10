class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        Biblioteca.bibliotecas.append(self)
    
    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} | {biblioteca.ativo}")
            
    def alterna_estado(self):
        self._ativo = not self._ativo
        
    @property
    def ativo(self):
       return "ativada" if self._ativo else "desativada"         
    


#print(biblioteca_cidade)
#print(biblioteca_shopping)

