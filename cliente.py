class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property # Anotação para o getter.
    def nome(self):
        print('Chamando a @property nome()...')
        return self.__nome.title() # title() coloca a inicial em maiúscula.

    @nome.setter # Anotação para o setter.
    def nome(self, nome):
        print('Chamando o setter nome()...')
        self.__nome = nome
