# Classes
## Classes
Declaração de classes no Python tem a seguinte estrutura:

```python
class Classe:
    atributo1 = 'atributo'
    numero = 2
    ativo = False
```
Nesse exemplo, mostramos apenas os atributos da classe antes de instanciá-la. Para criar a instância, usamos o nome da classe seguida de parênteses - e eventualmente dentro dos parênteses colocamos os argumentos para a construção do objeto. Exemplo:

```python
objeto = Classe()
```

Ao imprimir o objeto, vemos o nome do módulo da execução seguido de ponto seguido do nome da classe. Após o nome da classe temos o endereço de memória onde o objeto está localizado. Veja o exemplo: 

```python
print(objeto)
# Saída: <__main__.Classe object at 0x000001E105ADC7D0>
```

Segue o código do arquivo `modelos/restaurante.py`:
```python
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
print(restaurantes)
```
## Atributos de instância
Para acessar os atributos da classe, use o operador ponto:
```python
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
print(restaurante_praca.ativo) # Imprime False
```
Para ver todos os métodos e atributos de um objeto, use a função `dir`:
```python
print(dir(restaurante_praca))
# Saída: 
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', '__weakref__', 'ativo', 'categoria', 'nome']
```

Para ver um dicionário com os atributos de classe do objeto, use a função `vars`:
```python
print(vars(restaurante_praca))
# Saída: {'nome': 'Praça', 'categoria': 'Gourmet'}
```
> Curiosidade: somente os atributos modificados após a construção aparecem no resultado. Note que o atributo `ativo` não apareceu no dicionário porque ele não foi alterado depois da construção.

# Construtor e instanciando objetos
## Construtor
Em Python, o construtor é definido pela sobrescrita do método `__init__` da classe, que precisa de ter pelo menos um primeiro parâmetro - geralmente batizado de `self`, pois se refere ao próprio objeto. O método `__init__` pode ter outros parâmetros além do `self`, conforme exemplo:

```python
class Restaurante:
    def __init__(me, nome, categoria):
        # Substitui o nome self por me para teste. Ainda assim o 
        # código funciona: não é obrigatório usar a palavra self.
        me.nome = nome
        me.categoria = categoria
        me.ativo = False
```

Mensagem que aparece ao tentar instanciar o objeto restaurante sem fornecer os parâmetros para construção conforme método `__init__`:
```python
print(
    Restaurante())
```
Saída:
```
Traceback (most recent call last):
  File "D:\git\python-oo\modelos\restaurante.py", line 8, in <module>
    restaurante_praca = Restaurante()
                        ^^^^^^^^^^^^^
TypeError: Restaurante.__init__() missing 2 required positional arguments: 'nome' and 'categoria'     
```

Código alterado em `models/restaurante.py`:
```Python
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

print(vars(restaurante_praca))
print(vars(restaurante_pizza))
```
## Métodos especiais
O dunder method `__str__` muda a string que representa o objeto quando ele é impresso. Por padrão, ele retorna `<__nome_modulo__.Classe object at 0x_endereco_de_memoria`.

Reimplementando o método `__str__` na classe restaurante:
```python
class Restaurante:
    # Resto do código
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
```
## Criando meus métodos
Vamos criar agora um método de classe (não de objeto).

```Python
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        # Resto do código
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
```
> Note que o acesso aos atributos da classe depende de referenciar a própria e em seguida invocar o método/atributo desejado. Exemplos:
> 1. `Restaurante.restaurantes.append(self)` (para acrescentar o objeto `self` no atributo de tipo lista `restaurantes` da classe `Restaurante`)
> 2. `Restaurante.listar_restaurantes()` (para invocar o método `listar_restaurantes()` da classe `Restaurante`).

# Property e métodos de classe
## Property
Vamos aprender a criar um getter de um atributo da classe. Para isso, usamos a anotação `@property`:
```python
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False # Prefixe com underline este atributo.
        Restaurante.restaurantes.append(self)

    # Resto do código

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
```
> Perceba o underline no atributo `self._ativo`: é uma convenção que os atributos prefixados com underline não sejam acessados diretamente. Eles não são necessariamente privados - pois podem ser acessados - mas convencionou-se de nunca acessar variáveis com esse prefixo.

## Aprofundando em propriedades
O VSCode possui um atalho para renomear um atributo/método de uma classe: a tecla `F2`. Note que os atributos `nome`, `categoria` e `ativo` agora são prefixados com underline, ou seja, são "privados". O código da aplicação foi mudado conforme a seguir:

```python
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # Privado.
        self._categoria = categoria.upper() # Privado.
        self._ativo = False # Privado.
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        # Privado.
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'}") 
        for restaurante in Restaurante.restaurantes:
            # Privado.
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐' # Privado.
    
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca._nome = 'Praça 2.0' # Privado.
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
```

## Métodos de classes
Métodos de classe (ou estáticos) são declarados com a anotação `@classmethod`, e ela deve ter pelo menos um parâmetro que represente a classe - algo semelhante aos métodos de objeto. 

Enquanto o primeiro parâmetro dos métodos de objetos geralmente seja chamado de `self`, o primeiro parâmetro dos métodos de classe/estático geralmente é chamado de `cls`.

```python
class Restaurante:
    # Resto do código
    
    @classmethod
    def listar_restaurantes(minha_classe): # cls
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'}")
        for restaurante in minha_classe.restaurantes: # cls
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    # Resto do código
```
> Note que o método `listar_restaurantes` está anotado com `@classmethod` e tem como primeiro parâmetro uma variável que batizamos de `minha_classe`. A variável `minha_classe` geralmente é escrita como `cls`, mas usamos outro nome de variável para mostrar que isso não é obrigatório no Python.

Também implementamos um método para ligar/desligar o estado de ativo do restaurante: 

```python
class Restaurante:
    # Resto do código
        
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    # Resto do código
```
# Importando classe e composição
## From e import
Vamos criar um arquivo `main.py` e nele vamos importar a classe `Restaurante` do módulo `modelo.resturante.py`:

```python
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
```
## Criando a classe de avaliação
A classe `Avaliacao` será muito pequena. Lembre-se de prefixar com underline os atributos privados da classe: 

```python
# modelos/avaliacao.py
class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
```

Vamos embutir as avaliações noa classe `Restaurante`:
```python
# modelos/restaurante.py
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._avaliacao = []
        # Resto do código
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

# Resto do código
```
E finalmente vamos usar a classe no arquivo `main.py`:
```python
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Laís', 8)
restaurante_praca.receber_avaliacao('Emy', 5)
```
## Composição
Implementação da propriedade `media_avaliacoes` na classe `Restaurante`:
```python
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    # Resto do código

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        return round(soma_das_notas / quantidade_de_notas, 1)
```

## Listando avaliações
Adaptando o método `listar_restaurantes` da classe `Restaurante`:
```python
# modelos/restaurante.py
from modelos.avaliacao import Avaliacao

class Restaurante:
    # Resto do código
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
                str(restaurante.media_avaliacoes).ljust(25), # Float para string.
                restaurante.ativo
            ]))
```
> Note que a propriedade `media_avaliacoes` é do tipo `float`, portanto o método `ljust` não se aplica a esse tipo. Por isso foi necessário converter o float para string.
> O método `join` da classe string serve para intercalar a string em uma lista.
