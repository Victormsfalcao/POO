class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.estaComendo = False
        self.estaDormindo = False
        self.estaFalando = False

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")
        print(f"Tenho {self.idade} anos.")
        print(f"Meu peso é {self.peso} kg")

    def comer(self):
        if self.estaDormindo:
            print(f"{self.nome} está dormindo e não pode comer.")
        else:
            self.estaComendo = True
            self.estaDormindo = False
            print(f"{self.nome} está comendo.")

    def dormir(self):
        if self.estaComendo:
            print(f"{self.nome} está comendo e não pode dormir.")
        else:
            self.estaDormindo = True
            self.estaComendo = False
            print(f"{self.nome} está dormindo.")

    def falar(self):
        if self.estaDormindo:
            print(f"{self.nome} está dormindo e não pode falar.")
        else:
            self.estaFalando = True
            print(f"{self.nome} está falando.")
