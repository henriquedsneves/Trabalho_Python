import Cachorro
from Mamifero import Mamifero

import Gato


class Main:
    # Método principal
    def executar(self):
        # Criando objetos
        rex = Cachorro.Cachorro("Rex", 3)
        luna = Gato.Gato("Luna", 2)
        to = Cachorro.Cachorro("to", 4)

        # Usando métodos
        rex.emitir_som()
        luna.emitir_som()
        to.emitir_som()
        to.abanar_rabo()
        luna.arranhar()
        
        rex.dormir()
        luna.dormir()

        print(f"{rex.nome} tem {rex.get_idade()} anos.")
        #rex.set_idade(4)

        #print(f"Agora, {rex.nome} tem {rex.get_idade()} anos.")
        #print(f"{luna.nome} ")
        
        #luna.nome = "Luna Lovegood"
        #print(f"Agora, o nome do gato é {luna.nome}.")

# Execução principal
if __name__ == "__main__":
    programa = Main()
    programa.executar()


#Classe → molde/projeto.

#Objeto → instância real criada a partir da classe.

#Atributos → características do objeto.

#Métodos → ações do objeto.

#Construtor (__init__) → inicializa atributos.

#Encapsulamento → protege os dados.

#Herança → reaproveita código de outra classe.

#Polimorfismo → mesmo método, comportamentos diferentes.

#Abstração → esconde detalhes desnecessários, mostra só o essencial.