# def cria funções (ou métodos dentro da classe)
class Animal: 
    nome = "" 
    especie = "" 
    idade = 0 

    def rugido1(self): 
        print("AAAAAAAAAAAAAAAAAAAAA...") 
    def dormindo(self):
        print("ZZZZZZZZZZZZZZZZZZZ...")

    def rugido2(self): 
        print("UHUHUHUHUHAHAHAHA...") 
    def dormindo(self):
        print("ZZZZZZZZZZZZZZZZZZZ...")

    def rugido3(self): 
        print("HUHUHUHUHUUHUHUHAHAHAH...") 
    def dormindo(self):
        print("ZZZZZZZZZZZZZZZZZZZ...")

    def rugido4(self): 
        print("AUAUAUAUAUAUAUAUAUAU...") 
    def dormindo(self):
        print("ZZZZZZZZZZZZZZZZZZZ...")

    def rugido5(self): 
        print("MIAUUUUU...") 
    def dormindo(self):
        print("ZZZZZZZZZZZZZZZZZZZ...")


c1 = Animal()
c1.nome = "Po" 
c1.especie = "Urso Panda" 
c1.idade = 15

c2 = Animal()
c2.nome = "Leandro" 
c2.especie = "Chinpanzé" 
c2.idade = 17

c3 = Animal()
c3.nome = "Aliaga" 
c3.especie = "Orangutango" 
c3.idade = 16

c4 = Animal()
c4.nome = "Lulu" 
c4.especie = "Cachorro" 
c4.idade = 7

c5 = Animal()
c5.nome = "Preciosa" 
c5.especie = "Gato" 
c5.idade = 5

print("Animal: ", c1.nome, "-", c1.especie, 
    " Idade: ", c1.idade, ) 
c1.rugido1()
c1.dormindo()

print("Animal: ", c2.nome, "-", c2.especie, 
    " Idade: ", c2.idade, ) 
c2.rugido2()
c2.dormindo()

print("Animal: ", c3.nome, "-", c3.especie, 
    " Idade: ", c3.idade, ) 
c3.rugido3()
c3.dormindo()

print("Animal: ", c4.nome, "-", c4.especie, 
    " Idade: ", c4.idade, ) 
c4.rugido4()
c4.dormindo()

print("Animal: ", c5.nome, "-", c5.especie, 
    " Idade: ", c5.idade, ) 
c5.rugido5()
c5.dormindo() 
