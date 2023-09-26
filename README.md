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
