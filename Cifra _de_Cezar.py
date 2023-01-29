posicao = ""
add_posicao = []
palavra_codificada = ""
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
palavra_descodificada = input("Digite a palavra a ser codificada: ")
numero_deslocamentos = int(input("Digite a quantidade de deslocamentos que deseja realizar para a cofificação: "))
for letra in palavra_descodificada:
    posicao = alfabeto.index(letra)
    posicao += -numero_deslocamentos
    add_posicao = alfabeto[posicao]
    palavra_codificada += add_posicao
print("o resultado da codificação é:", palavra_codificada)
palavra_codificada = ""
add_posicao = []
palavra_codificada = ""