class Aluno: 
    nome =""
    nota = 0

    def mostrarSituacao(self):
        if self.nota >= 5:
            print(self.nome, "Foi aprovado") 
        else:
            print(self.nome, "Foi reprovado") 

a1 = Aluno() 
a1.nome = "Diego"
a1.nota = 3

a2 = Aluno() 
a2.nome = "Leandro"
a2.nota = 2

a3 = Aluno() 
a3.nome = "Aliaga"
a3.nota = 4

a4 = Aluno() 
a4.nome = "Phelipe"
a4.nota = 10

a5 = Aluno() 
a5.nome = "Jonathan"
a5.nota = 6

a6 = Aluno() 
a6.nome = "Matheus"
a6.nota = 9

a7 = Aluno() 
a7.nome = "Luan"
a7.nota = 3


a1.mostrarSituacao() 
a2.mostrarSituacao()
a3.mostrarSituacao()
a4.mostrarSituacao()
a5.mostrarSituacao()
a6.mostrarSituacao()
a7.mostrarSituacao()
