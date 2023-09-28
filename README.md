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

# None e Coletor de lixo
Veja o código abaixo:
```python
>>> conta = Conta(1, 'Nico', 600, 1000) # Criação do primeiro objeto.
Construindo objeto... <conta.Conta object at 0x0000027154CEB650>
>>> conta = Conta(1, 'Nico', 600, 1000) # Criação do segundo objeto.
Construindo objeto... <conta.Conta object at 0x0000027154CEB690>
>>> outra = conta 
>>> outra # A nova variável guarda o mesmo endereço de memória da variável conta.
<conta.Conta object at 0x0000027154CEB690>
>>> outra = None # Removendo a referência da variável outra.
>>> outra
>>> type(outra)
<class 'NoneType'>
```
Repare que a referência/variável `conta` apontava para o endereço de memória `0x0000027154CEB650`, mas depois passou a apontar para outro endereço de memória, o `0x0000027154CEB690`.

O primeiro objeto que estava no endereço `0x0000027154CEB650` será removido pelo coletor de lixo do Python.

O `NoneType` é o tipo nulo do Python. Variáveis que apontam para `None` não apontam para nenhum endereço de memória. Atribuir `None` é um jeito de limpar a variável.

# Atributos privados
Os modificadores de acesso atributos no Python são diferentes de outras linguagem baseadas em C (Java, PHP, C# etc.). Por padrão, os atributos são públicos.

Para definir um atributo como privado no Python (encapsulamento), prefixamos o atributo com um sublinhado DUPLO (`objeto.__atributo`). Por baixo dos panos, o Python acrescenta, para cada atributo da classe, um underscore seguido do nome da classe (`objeto._Classe__atributo`):

```python
>>> from conta import Conta
>>> conta = Conta(21, 'Gambit', 500.0, 1500.0)
Construindo objeto... <conta.Conta object at 0x0000021F32C12F50>
>>> conta.__limite # Atributo privado prefixado com dois underscores.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Conta' object has no attribute '__limite'
>>> conta._limite # Atributo privado prefixado com um underscore.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Conta' object has no attribute '_limite'
>>> conta.limite # Atributo privado sem prefixo.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Conta' object has no attribute 'limite'
# Atributo prefixado com underscore, nome da classe e dois underscores.
>>> conta._Conta__limite 
1500.0
>>>
```
Novo código da classe Conta:
```python
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor
```

# Encapsulamento
Acréscimo do método `transfere` na classe `Conta`:
```python
class Conta:
    # Resto do código.
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
```
Execução do código:
```python
>>> from conta import Conta
>>> conta = Conta(1, 'Thiago', 5000, 10000)
Construindo objeto... <conta.Conta object at 0x00000285840E2F50>
>>> conta2 = Conta(2, 'Teste', 300, 4000)
Construindo objeto... <conta.Conta object at 0x000002858410D0D0>
>>> conta.transfere(500, conta2)
>>> conta.extrato()
Saldo de 4500 do titular Thiago
>>> conta2.extrato()
Saldo de 800 do titular Teste
>>>
```

# Coesão
A classe Conta não precisaria de ter um método `eh_inadimplente(self, cliente)`: a responsabilidade pela adimplência é de uma outra classe. Classes com responsabilidades bem definidas são classes coesas. Coesão se refere a atribuir corretamente as responsabilidades para as devidas classes. "Uma única razão para ser modificada" é a regra de coesão do código.

# Getters e Setters
Qualquer getter e setter recebe `self` como o primeiro parâmetro.

```python
class Conta:
    # Resto do código
    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite
```

# Propriedades
A anotação `@property` indica que o método correspondente ao getter de uma das variáveis privadas.

A anotação `@{nome_da_property}.setter` indica que o método correspondente ao setter da property.

```python
>>> from cliente import Cliente
>>> cliente = Cliente("Marco")
>>> cliente.nome
Chamando a @property nome()...
'Marco'
>>> cliente.nome = 'nico'
Chamando o setter nome()...
>>> cliente.nome
Chamando a @property nome()...
'Nico'
>>>
```

Código do novo arquivo `cliente.py`:
```python
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
```

Atualização do código do arquivo `conta.py`:
```python
class Conta:
    #Resto do código

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
```

# Métodos privados
Para definir um método privado, basta prefixar o método com dois underscores. Não, não há uma anotação especial para métodos privados.

Alteração no código do arquivo `conta.py`:
```python
class Conta:
    # Resto do código.

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite. ".format(valor))

    # Resto do código.
```

Usando a classe conta:
```python
>>> from conta import Conta
>>> conta = Conta(123, 'nico', 500, 800)
Construindo objeto... <conta.Conta object at 0x0000028BB3A12F50>
>>> conta.pode_sacar(1500) # Vai falhar, método privado.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Conta' object has no attribute 'pode_sacar'
>>> conta._Conta__pode_sacar(1500) # Forçando o acesso a método privado.
False
>>> conta._Conta__pode_sacar(500) # Forçando o acesso a método privado.
True
>>>
```
# Métodos da classe
Duas coisas para criar métodos estáticos (ou de classe):
1. Métodos estáticos não recebem `self` como parâmetros: quem recebe são apenas os métodos de instância;
2. É necessário usar a anotação `@staticmethod`.

```python
class Conta:
    # Resto do código.
    
    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigo_bancos():
        return {
            'BB' : '001',
            'Caixa' : '104',
            'Bradesco' : '237',
        }
```

Uso da classe Conta alterada:
```python
>>> from conta import Conta
>>> Conta.codigo_banco()
'001'
>>> codigos = Conta.codigo_bancos() 
>>> codigos['Caixa']
'104'
>>>
```

# Para saber mais: Atributo estático
Conhecemos nessa aula os métodos estáticos que podem ser chamados a partir da classe, sem ter um objeto criado. No exemplo abaixo criamos uma classe Circulo que possui um método estático `obter_pi()`:

```python
class Circulo:
    @staticmethod
    def obter_pi():
        return 3.14
```
E agora podemos usar esse método estático a partir da classe:
```python
Circulo.obter_pi()
3.14
```

Repare que o método existe apenas para devolver o valor do PI. Nada errado com isso, mas já que usamos um valor simples não bastaria usar um atributo simples? Em outras palavras, será que é preciso criar um método? A resposta é não pois podemos usar um atributo da classe. Veja como é simples:

```python
class Circulo:
    PI = 3.14
```

Repare que não usamos self e o atributo nem foi definido dentro do `__init__`. O atributo faz parte da classe, ou seja, é um atributo estático que pode ser usado sem ter criado um objeto. Veja como fica simples:

```python
Circulo.PI
3.14
```
