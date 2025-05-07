class Pessoa():
    def __init__(self, nome , peso , idade, comer,dormir,falar):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comer = False
        self.dormir = False
        self.falar = False

    def apresentar(self):
        print(f"Olá meu nome é {self.nome}")
        print(f"Tenho {self.idade}anos.")
        print(f"Meu peso é {self.peso}kg")

    def comer(self):
        if self.comer == True:
           self.dormir = False
           print(f"{self.nome} está comendo")

        else:
            print(f"{self.nome} está dormindo, não pode comer")
    def dormir(self):
        print(f"{self.nome} está dormindo")

    def falar(self):
        print(f"{self.nome} está comendo")

    def dormir(self):
        print(f"{self.nome} está dormir")
