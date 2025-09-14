from Mamifero import Mamifero



class Gato(Mamifero):
    def emitir_som(self):
        print(f"{self.nome} está miando: Miau!")
    def arranhar(self):
        print(f"{self.nome} está arranhando o sofá!")