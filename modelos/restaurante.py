from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(" | ".join([
            'Nome'.ljust(25), 
            'Categoria'.ljust(25), 
            'Avaliação'.ljust(25), 
            'Ativo'
        ]))
        for restaurante in cls.restaurantes:
            print(' | '.join([
                restaurante._nome.ljust(25),
                restaurante._categoria.ljust(25),
                str(restaurante.media_avaliacoes).ljust(25),
                restaurante.ativo
            ]))
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        # else:
        #     raise ValueError('A nota deve estar entre 1 e 5')

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        return round(soma_das_notas / quantidade_de_notas, 1)
