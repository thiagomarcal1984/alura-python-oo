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
