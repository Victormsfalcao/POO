class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.esta_comendo = False
        self.esta_dormindo = False
        self.esta_falando = False

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")
        print(f"Tenho {self.idade} anos.")
        print(f"Meu peso é {self.peso} kg")

    def comer(self):
        if self.esta_dormindo:
            print(f"{self.nome} está dormindo e não pode comer.")
            return
        if self.esta_comendo:
            print(f"{self.nome} já está comendo.")
        else:
            self.esta_comendo = True
            self.esta_falando = False
            print(f"{self.nome} começou a comer.")

    def dormir(self):
        if self.esta_comendo:
            print(f"{self.nome} está comendo e não pode dormir.")
            return
        if self.esta_dormindo:
            print(f"{self.nome} já está dormindo.")
        else:
            self.esta_dormindo = True
            self.esta_falando = False
            print(f"{self.nome} foi dormir.")

    def falar(self):
        if self.esta_dormindo:
            print(f"{self.nome} está dormindo e não pode falar.")
            return
        if self.esta_comendo:
            print(f"{self.nome} está comendo e não pode falar.")
            return
        if self.esta_falando:
            print(f"{self.nome} já está falando.")
        else:
            self.esta_falando = True
            print(f"{self.nome} começou a falar.")

# ---------------------------------------------------------------------
class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f" {self.nome} foi comer...")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"{self.nome} foi miando...")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f" {self.nome} foi latindo...")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f" {self.nome} foi mugindo...")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def grunhir(self):
        print(f" {self.nome} foi grunindo...")


#-------------------------------------------------------------------------

class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor}")


class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor * 1.5)

    def imprimeValor(self):
        print(f"Valor do ingresso VIP: R${self.valor}")


#-------------------------------------------------------------------------

class Forma():
    def __init__(self, area=0, perimetro=0):
        self.area = area
        self.perimetro = perimetro


class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, base, altura):
        area = base * altura
        print(f"A área do retângulo é de {area}")

    def calculaPerimetro(self, base, altura):
        perimetro = 2 * (base + altura)
        print(f"O perímetro do retângulo é de {perimetro}")


class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, base, altura):
        area = (base * altura) / 2
        print(f"A área do triângulo é de {area}")

    def calculaPerimetro(self, lado):
        perimetro = 3 * lado
        print(f"O perímetro do triângulo é de {perimetro}")

#-----------------------------------------------------------------------------

class Atleta():
    def __init__(self,peso):
        self.aposentado = False
        self.peso = peso

    def aposentar(self):
        self.aposentado = True
        print("O atleta está aposentado")

    def aquecer(self):
        if not self.aposentado:
            print("O atleta está aquecendo")

        else:
            print("O atleta está aposentado e não pode se aquecer")

class Corredor(Atleta):
    def correr(self):
        if not self.aposentado:
            print("O atleta está correndo.")
        else:
            print("O atleta está aposentado e não pode correr.")


class Nadador(Atleta):
    def nadar(self):
        if not self.aposentado:
            print("O atleta está nadando.")
        else:
            print("O atleta está aposentado e não pode nadar.")


class Ciclista(Atleta):
    def pedalar(self):
        if not self.aposentado:
            print("O atleta está pedalando.")
        else:
            print("O atleta está aposentado e não pode pedalar.")


class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, peso):
        super().__init__(peso)
