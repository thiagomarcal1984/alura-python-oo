# Dados da conta
Formas de definir dados de uma conta bancária em Python:

```python
# 1. Declarando variáveis de tipos primitivos e com 
# nomes diferentes para cada instância de conta:
numero = 123
titular = "Nico"
saldo = 55.0
limite = 1000.0

# 2. Criando um dicionário com os dados de cada conta:
conta = { 
    "numero": 123,
    "titular": "Nico",
    "saldo": 55.0,
    "limite": 1000.0
}
# Eventualmente você pode usar uma função para 
# encapsular a criação da conta:
def cria_conta(numero, titular, saldo, limite):
    conta = { 
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite,
    }
    return conta

conta2 = cria(321, "Marco", 100.0, 1000.0)
```
# Dados e comportamento
Uma das propostas da orientação a objetos é unir dados e comportamento a uma mesma estrutura de dados, que chamamos de objeto.

O conteúdo do arquivo `teste.py` a seguir mostra várias funções cujos códigos são independentes umas das outras. Com a OO, essa independência é diminuída em prol da consistência do objeto (dados + comportamento):

```python
def cria_conta(numero, titular, saldo, limite):
    conta = { 
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite,
    }
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))
```

# Classe e Objeto
Classes são modelos de como os objetos serão criados e estruturados, bem como define as funções/métodos que compõem seu comportamento.
```python
>>> from conta import Conta
# A variável conta é a referência para o objeto conta.Conta
>>> conta = Conta()
>>> type(conta)
<class 'conta.Conta'>
>>> conta
<conta.Conta object at 0x0000012CB2682CD0>
>>>
```

# Construtor
Os construtores em Python são criados usando o nome de função `__init__(self, parâmetros)`.

É necessário fornecer o `self` como o primeiro parâmetro do construtor de uma classe em Python. O parâmetro `self` é fornecido pelo Python.

Definição da classe `Conta` no arquivo `conta.py`:
```python
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
```

# Acessando atributos
Para acessar atributos de um objeto, use um ponto seguido do nome do atributo que deseja acessar: 
```python
>>> from conta import Conta
>>> conta1 = Conta(123, 'Nico', 50, 2000) 
Construindo objeto... <conta.Conta object at 0x0000020E9A2D2CD0>
>>> conta2 = Conta(456, 'Marco', 100, 1000)   
Construindo objeto... <conta.Conta object at 0x0000020E9A64B150>
>>> conta1.titular
'Nico'
>>> conta2.titular 
'Marco'
>>> conta1.saldo   
50
>>> conta2.saldo 
100
>>>
```

# Usando métodos
Sempre forneça o parâmetro `self` ao declarar métodos de uma classe.

Ao chamar os métodos/construtores, o parâmetro `self` não precisa ser incluído, pois o Python já o insere implicitamente.

Conteúdo do arquivo `conta.py`:
```python
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
```

Usando a classe Conta:
```python
>>> from conta import Conta
>>> conta = Conta(1, 'Nico', 600, 1000)
Construindo objeto... <conta.Conta object at 0x00000243C48F2F50>
>>> conta2 = Conta(2, 'Marco', 700, 3000)  
Construindo objeto... <conta.Conta object at 0x00000243C491D0D0>
>>> conta.extrato()
Saldo de 600 do titular Nico
>>> conta2.extrato() 
Saldo de 700 do titular Marco
>>> conta2.deposita(300)
>>> conta2.extrato()
Saldo de 1000 do titular Marco
>>> conta.saca(200)
>>> conta.extrato()
Saldo de 400 do titular Nico
>>>
```
