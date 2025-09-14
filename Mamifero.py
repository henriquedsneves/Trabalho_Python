from abc import ABC, abstractmethod


class Mamifero(ABC):

#o Self serve para que cada objeto guarde os seu metodos e atributos

    # Construtor
    def __init__(self, nome, idade): # atributos comuns
        self.nome = nome
        # com o underscore, indica que é protegido
        # caso tenha dois underscores, indica que é privado
        self.__idade = idade
    
    @abstractmethod
    def emitir_som(self):
        pass   # Cada mamífero vai implementar do seu jeito

    # Método comum a todos os mamíferos
    def dormir(self):
        print(f"{self.nome} está dormindo... ZzZz")
    #encapsulamento para pegar algum dado
    def get_idade(self):
        return self.__idade
    # definir uma regra para modificar um dado
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida!")  