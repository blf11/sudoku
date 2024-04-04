#BRUNO LIMA FONSECA
#12321EAU011
#Trabalho09_sudoku

def criar_matriz(sudoku): #cria uma matriz a partir de números digitados com espaço
    sudoku = []
    for i in range(9):
        linha =[int(x) for x in input().split()]
        sudoku.append(linha)
    return sudoku

def verificar(o): #verifica os casos em que o sudoku está errado
    for linha in range(9): #verifica as linhas 
        teste = []
        for coluna in range(9):
            if teste.count(o[linha][coluna]) == 0:
                teste.append(o[linha][coluna])
                continue
            else:
                return False
            
    for coluna in range(9): #verifica as colunas
        teste=[]
        for linha in range(9):
            if teste.count(o[linha][coluna]) == 0:
                teste.append(o[linha][coluna])
                continue
            else:
                return False

    for a in range(0,9,3): #verifica cada quadrado 3x3
        for q in range(0,9,3):
            teste=[]
            for linha in range(a,a+3,1):
                for coluna in range(q,q+3,1):
                    if teste.count(o[linha][coluna]) == 0:
                        teste.append(o[linha][coluna])
                        continue
                    else:
                        return False
    return True

n = int(input()) #número de matrizes para conferir
sudoku = []

for m in range(n):
    o = criar_matriz(sudoku)
    verificar(o)
    print('Instancia {}'.format(m+1))
    if verificar(o):
        print('SIM')
    else:
        print('NAO')
    print()
