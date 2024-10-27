import os
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Personagem:
    def __init__(self, name, classe, life, attack, defense):
        self.name = name
        self.classe = classe
        self.life = life
        self.attack = attack
        self.defense = defense
    def atacar(self, life, attack, defense):
        self.life -= attack - defense
    def curar(self, life):
        self.life += 70


alfred = Personagem("Alfred", "Mago", 250, 73, 23)
frank = Personagem("Frank", "Guerreiro", 300, 65, 45)

while True:
    personagem = input("Escolha seu personagem: Alfred, o mago ou Frank o guerreiro\n> ")
    limpar_console()
    if personagem.lower() == "alfred":
        enemy = frank
        my = alfred
        print(f"Você escolheu: {alfred.name}, suas stats são:")
        print(f"Classe: {alfred.classe}")
        print(f"Vida: {alfred.life}")
        print(f"Ataque: {alfred.attack}")
        print(f"Defesa: {alfred.defense}\n")
        break

    elif personagem.lower() == "frank":
        enemy = alfred
        my = frank
        print(f"Você escolheu: {frank.name}, suas stats são:")
        print(f"Classe: {frank.classe}")
        print(f"Vida: {frank.life}")
        print(f"Ataque: {frank.attack}")
        print(f"Defesa: {frank.defense}\n")
        break
    else:
        print("Personagem não encontrado. Tente novamente")

if personagem.lower() == "alfred":
    print("Você lutará contra Frank, o guerreiro\n")
else:
    print("Você lutará contra Alfred, o mago\n")
input("Assim que estiver pronto, presione enter...\n> ")
limpar_console()

print(f"Você está andando por um vale sombrio e encontra uma pessoa encostada em uma árvore, percebe que é na verdade {enemy.name}, um {enemy.classe} muito forte.\nVocê percebe que ele está possuído por algo.\nEle apenas diz friamente: \"eu irei te matar\" e vai pra cima de você.\n")
while True:
    option = input("Você tem duas opções, contra-atacar (1) ou esquivar (2), o que escolhe?\n> ")
    limpar_console()
    if option == "1":
        esquivou = 0
        print(f"Você acerta o golpe e a vida do {enemy.name} foi de: {enemy.life} para:", end=" ")
        enemy.atacar(enemy.life, my.attack, enemy.defense)
        print(f"{enemy.life}")
        input("> ")
        limpar_console()
        break
    elif option == "2":
        esquivou = 1
        print("Você se esquiva e consegue não ser atingido")
        input("> ")
        break
if esquivou == 0:
    print(f"Agora o negócio ficou sério. {enemy.name} está furioso e começa a te atacar sem parar.")
else: 
    print(f"{enemy.name} fica furioso em não acertar o golpe e começa a te atacar sem parar.")
print(f"Sua vida caiu de {my.life} para:", end=" ")
my.atacar(my.life, enemy.attack, my.defense)
my.atacar(my.life, enemy.attack, my.defense)
my.atacar(my.life, enemy.attack, my.defense)
print(f"{my.life}")
input("> ")
limpar_console()
if my.classe == "Mago":
    print("Como seu personagem é um mago, você pode se curar durante a batalha.")
    option = input("Pressione (3) para se curar ou (1) para atacar\n> ")
    if option == "3":
        limpar_console()
        my.curar(my.life)
        print(f"Sua vida agora é: {my.life}")
        input("A batalha se intensifica e vocês vão lutar até a morte\n> ")
        limpar_console()
    elif option == "1":
        limpar_console()
        enemy.atacar(enemy.life, my.attack, enemy.defense)
        input(f"Você o ataca. A vida de {enemy.name} é: {enemy.life}\n> ")
        limpar_console()
else:
    input("Você não pode se curar, te resta apenas atacar... até a morte\n> ")
limpar_console()
while enemy.life > 0 and my.life > 0:
    if my.classe == "Mago":
        curou = input("Pressione (1) para atacar ou (3) para se curar\n> ")
        limpar_console()
        if curou == "3":
            my.curar(my.life)
            print(f"Você cura e sua vida agora é: {my.life}")
        elif curou == "1":
            enemy.atacar(enemy.life, my.attack, enemy.defense)
            print(f"Você ataca {enemy.name}, a vida dele agora é: {enemy.life}")
        else:
            print("Você nem atacou , nem curou")
    else:
        bateu = input("Pressione (1) para atacar\n> ")
        limpar_console()
        if bateu == "1":
            enemy.atacar(enemy.life, my.attack, enemy.defense)
            print(f"Você ataca {enemy.name}, a vida dele agora é de: {enemy.life}")
        else:
            print(f"Você não faz nada, a vida dele é: {enemy.life}")
    my.atacar(my.life, enemy.attack, my.defense)
    print(f"O {enemy.name} te ataca e sua vida cai para: {my.life}")
if enemy.life < 0 and my.life < 0:
    input(f"Você e {enemy.name} lutaram até a morte e nenhum dos dois sobreviveu...\n> ")
elif enemy.life < 0:
    if my.classe == "Mago":
        input(f"Você conseguiu matar {enemy.name}, seu cajado emana uma energia ruim...\nEle parece ter absorvido a alma deste guerreiro corrompido...\n> ")
    else:
        input(f"Você conseguiu matar {enemy.name}, sua espada está cheia de sangue...\nUma energia ruim parece te consumir aos poucos...\n> ")
elif my.life < 0:
    input(f"Você não aguentou a fúria de {enemy.name}, um homem corrompido pelo vazio, e acabou morrendo durante a batalha...\n> ")
limpar_console()
print("E através desse simples projeto, eu consegui aplicar na prática um novo conceito que eu achei\nmuito interessante: Orientação a objetos :)")
print("Obrigado por jogar (ou por ler isso no meu github)")