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
