from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    idade : int
    email: str
    pin: str

    def Ta_certo(self):
        senha = self.pin
        if len(senha) == 4:
            print(f'Seu pin {self.pin} está certo!')

cliente1 = Cliente('Jean', 21, 'jeancarlos03092003@gmail.com', '2003')
print(cliente1.nome)
print(cliente1.idade)
cliente1.Ta_certo()