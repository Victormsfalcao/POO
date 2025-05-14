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

