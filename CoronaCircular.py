print("Corona Circular")
print(""
      ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
      "")
radio_ma = float(input("Ingrese radio mayor: "))
radio_me = float(input("Ingrese radio menor: "))
area = 3.14*(radio_ma**2 - radio_me**2)
perimetro = 2*3.14*(radio_ma + radio_me)
print("resultados")
print("Area: ",area.__round__(2))
print("Perimetro: ",perimetro.__round__(2))
