class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'}")
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca._nome = 'Praça 2.0'
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
