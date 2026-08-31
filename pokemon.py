class Pokémon:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque

        if inimigo.vida < 0:
            inimigo.vida = 0

        print("Vida de", inimigo.nome, ":", inimigo.vida)


Pikachu = Pokémon("Pikachu", 100, 30)
Charmander = Pokémon("Charmander", 110, 25)


# Batalha
while Pikachu.vida > 0 and Charmander.vida > 0:

    Pikachu.atacar(Charmander)

    if Charmander.vida <= 0:
        print("Charmander foi derrotado")
        print("Pikachu venceu")
        break

    Charmander.atacar(Pikachu)

    if Pikachu.vida <= 0:
        print("Pikachu foi derrotado")
        print("Charmander venceu")
        break

    print()
