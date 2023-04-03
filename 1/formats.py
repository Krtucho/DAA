# funcion para escribir un texto en cierto color en consola
def printc(text, color):
    print(f"\033[{color}m{text}\033[0m")

# funcion para escribir un texto en negrita en consola
def printb(text):
    print(f"\033[1m{text}\033[0m")

# funcion para escribir un texto en cursiva en consola
def printi(text):
    print(f"\033[3m{text}\033[0m")

# funcion para escribir un texto en color rojo en consola
def printr(text):
    printc(text, 31)

# funcion para escribir un texto en color verde en consola
def printg(text):
    printc(text, 32)

# funcion para escribir un texto en colores verdes y rojo en la consola, (todo en 1 linea) pasandoles los parametros para escribir en rojo y en verde respectivamente en 2 listas
def printgr(text, red, green):
    for index, char in enumerate(text):
        if index in red:
            printr(char)
        elif index in green:
            printg(char)
        else:
            print(char, end="")

# printgr("Hola", [0, 1, 2], [3, 4, 5])
