from dataclasses import dataclass

@dataclass
class Livro:
    título: str
    autor: str
    ano: int

    def descri(self):
        print(f'O livro {self.título} tem o autor {self.autor} e foi lançado no ano de {self.ano}')

hp = Livro('harry potter', 'jjk', 2000)
hp.descri()