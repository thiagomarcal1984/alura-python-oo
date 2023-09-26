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
