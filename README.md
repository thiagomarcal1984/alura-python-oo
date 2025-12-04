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
