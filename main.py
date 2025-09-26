from funcoes import aviso, perdeu, venceu, input_dados, gerar_campo, jogar


while(True):
    tamanho, n_minas = input_dados()

    campo, coordenadas_minas = gerar_campo(tamanho, n_minas)
    resultado = jogar(campo, coordenadas_minas)

    if resultado:
        venceu()
    else:
        perdeu()

    try:
        opcao = int(input("Deseja jogar novamente(0 -> Não | 1 -> Sim)? "))

    except:
        opcao = 0
    
    if opcao:
        continue
    else:
        break

aviso("Finalizando programa", 1)
