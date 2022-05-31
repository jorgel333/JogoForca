import getpass as gt
def reiniciar_game():
    global gaming
    reply = input('Gostaria de jogar de novo? Digite qualquer tecla para sim "n" para parar.\n').lower()
    if reply == 'n':
        print('Obrigado por jogar forca!')
        gaming = False
        return gaming
    else:
        print('Vamos a mais uma rodada então!')
        
def vitoria():
    if password == word:
        print('Você acertou a última letra!')
        return True

def arriscar():
    if tent == 'tentar':
        return True
    else:
        return False

def palpite():
    global error
    palpite = input('Digite seu palpite:\n').lower()
    if palpite == word:
        print('Você acertou!')    
        return True
    else:
        print('Você errou!')
        error += 1
        return False

def display():
    print()
    print("|----- ")
    print("|    | ")
    print(f'|{line_3}')
    print(f'|{line_4}')
    print(f'|{line_5}')
    print("|")
    print(f'| {password}')
    print()

def verificar_erros():
    global line_3, line_4, line_5
    if error == 1:
        line_3 = '    O '
        return False
    elif error == 2:
        line_4 = '    | '
        return False   
    elif error == 3:
        line_4 = '   /| '
        return False   
    elif error == 4:
        line_4 = '   /|\ '
        return False  
    elif error == 5:
        line_5 = '   /  '
        return False   
    elif error == 6:
        line_5 = '   / \ '
        display()
        print(f'Letras digitadas: {typed}')
        print(f'Você foi enforcado, a palavra era {word}')
        print('--------------------------------------------------------------------')
        return True

def formar_senha():
    global password
    password = ''
    for letters in word:
        if letters in hits: password += letters  
        else: password += '_ '

def introduction():
    print('Bem vindo ao jogo da forca.\nEsse jogo consiste em adicionar uma palavra e desafiar seu oponente a acerta-la.')
    print('Não se assuste quando digitar a palavra e ela não aparecer, ela só está sendo ocultada para que a pessoa que vai tentar adivinhar não a veja antes da hora.')
    print('Então fique atento ao digita-la para não errar alguma letra.')
    print('Você começa-rá com 0 erros, cada erro no palpite ou letra será atribuído +1 erro.')
    print('A cada erro será adicionado uma parte do corpo a forca e ao errar 6 vezes o corpo estará completo e você será enforcado.')
    print('Você poderá tentar um palpite a qualquer momento e vencerá caso acerte o palpite ou todas as letras.')
    print('Bom jogo!!!\n')

def tentativas():
    global error, tent, typed, hits
    while True:
        tent = input('Digite apenas uma letra ou digite "tentar" para arriscar a palavra:\n').lower()
        print('--------------------------------------------------------------------')
        if tent == 'tentar':
            break
        if len(tent) == 1:
            if tent in typed: #se ele escolher uma letra apenas aqui vai verificar se já foi usada
                print(f'Você já usou essa!!\nLetras usadas: {typed}')
                continue
            if tent not in typed: #se a letra não foi usada, aqui irá adicionala as digitadas
                typed += tent
                if tent in word: #se a letra digitada exixtir na palavra ele vai adicionar aos acertos
                    hits += tent
                    break
                else: #se não tiver ele vai adicionar mais um erro e consequentemente uma parte do corpo a forca
                    error += 1 
                    break             
        elif len(tent) > 1: 
            print(f'{tent} são {len(tent)} caracteres.')

def gaming_forca():
    global password
    while True: 
        formar_senha()
        if verificar_erros(): break
        display()
        if vitoria(): break
        print('--------------------------------------------------------------------')
        print (f'Sua palavra contém {len(word)} letras.\nDica: {dica}.')
        print(f'Letras digitadas: {typed}')
        print('--------------------------------------------------------------------')
        tentativas()
        if arriscar():
            if palpite(): 
                password = word
                display()
                break

def entradas():
    global word, dica
    word = gt.getpass('Digite uma palavra:\n').lower().replace(' ', '')
    dica = input('Escreva uma dica sobre a palavra digitada:\n')

#Depois de definir as funções do jogo aqui vamos iniciar ele
introduction()
gaming = True
while gaming:
    #aqui vai dar resetão na forca
    hits = []
    error = 0
    typed = []
    line_3 = ''
    line_4 = ''
    line_5 = ''
    entradas()
    gaming_forca()
    reiniciar_game()
                    