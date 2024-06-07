from dataclasses import dataclass

@dataclass
class Aluno:
    nome:str
    matricula:int
    nota: dict


    def adicionar_notas(self, disciplina, notas):
        lista_not = []
        self.nota['disciplica'] = disciplina
        self.nota['nota'] = notas
        lista_not.append(self.nota)
        print(lista_not)

            
