from dataclasses import dataclass
import datetime

@dataclass
class ContaBancaria:
    título: str
    saldo: int

    def depositar(self, valor):
        self.saldo += valor
        print(f'Seu saldo atual é de {self.saldo}')

    def sacar(self, valor):
        self.saldo -= valor
        print(f'Saldo atual do {self.título} é de {self.saldo}, após sacar {valor}')

    def consulta(self):
        atual = datetime.datetime.now()
        print(f'Saldo atual do {self.título} é de {self.saldo} no dia {atual}')


pessoa1 = ContaBancaria('Jean', 2000)
pessoa1.consulta()
pessoa2 = ContaBancaria('Gustavo', 1500)
pessoa2.consulta()