from Mamifero import Mamifero


class Cachorro(Mamifero):
    def emitir_som(self):
        print(f"{self.nome} está latindo: Au Au!")
    def abanar_rabo(self):
            print(f"{self.nome} está abanando o rabo!")
