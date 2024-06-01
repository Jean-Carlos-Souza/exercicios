from dataclasses import dataclass
from categoria import Categoria


@dataclass
class Transacao:
    nome: str
    valor: float
    categoria: Categoria

    def exibir(self):
        print(f'Nome: {self.nome} | Valor: {self.valor} | Categoria: {self.categoria.nome}')
