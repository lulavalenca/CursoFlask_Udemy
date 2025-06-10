from modelos.avaliacao import Avaliacao

class Biblioteca:
    bibliotecas = []
    
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacoes = []
        Biblioteca.bibliotecas.append(self)
    
    def __str__(self):
        return self.nome

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Nota média'.ljust(25)} | {'Status'}")
        for biblioteca in cls.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {str(biblioteca.media_avaliacoes).ljust(25)} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media = round(soma / len(self._avaliacoes), 1)
        return media
