bands = int(input("Digite o número de faixas: "))

#cor = [("color", "cor", significative number, multiplier, tolerance)]

colors = [("black", "preto", 0, 1, "NULL"), ("brown", "marrom", 1, 10, 1), ("red", "vermelho", 2, 100, 2) \
          ,("orange",  "laranja", 3, 10**3, "NULL"), ("yellow", "amarelo", 4, 10**4, "NULL"), ("green", "verde", 5, 10**5, 0.5) \
          ,("blue", "azul", 6, 10**6, 0.25), ("violet", "violeta", 7, 10**7, 0.1), ("grey", "cinza", 8, 10**8, 0.05) \
          ,("white", "branco", 9, 10**9, "NULL"), ("gold", "dourado", "NULL", 0.1, 5), ("silver", "prata", "NULL", 0.01, 10) ]

def band_finder(x):
    n = 0
    while (n < len(colors)):
        try:
            colors[n].index(x)
            break
        except ValueError:
            n += 1
    return n
    
def four_bands():
    color1 = input("Digite o nome da primeira cor: ")
    color2 = input("Digite o nome da segunda cor: ")
    color3 = input("Digite o nome da terceira cor: ")
    color4 = input("Digite o nome da quarta cor: ")

    sig1 = str(colors[band_finder(color1)][2])
    sig2 = str(colors[band_finder(color2)][2])
    multi = colors[band_finder(color3)][3]
    tol = colors[band_finder(color4)][4]
    R = int(sig1 + sig2)*multi

    return R, tol

def five_bands():
    color1 = input("Digite o nome da primeira cor: ")
    color2 = input("Digite o nome da segunda cor: ")
    color3 = input("Digite o nome da terceira cor: ")
    color4 = input("Digite o nome da quarta cor: ")
    color5 = input("Digite o nome da quinta cor: ")
    
    sig1 = str(colors[band_finder(color1)][2])
    sig2 = str(colors[band_finder(color2)][2])
    sig3 = str(colors[band_finder(color3)][2])
    multi = colors[band_finder(color4)][3]
    tol = colors[band_finder(color5)][4]
    R = int(sig1 + sig2 + sig3)*multi

    return R, tol

if(bands == 4):
    R = four_bands()
    print(f"Resistencia de: {R[0]} {R[1]}%")
elif(bands == 5):
    R = five_bands()
    print(f"Resistencia de: {R[0]} {R[1]}%")
else:
    while True:
        break
