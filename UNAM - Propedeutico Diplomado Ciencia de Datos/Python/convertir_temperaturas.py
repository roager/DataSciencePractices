def convert_value(value, base='F'):
    match base.lower():
        case 'c':
            return round(value + 273.15, 2), round((9 * value / 5) + 32, 2)
        case 'f':
            return round(5 * ((value - 32) / 9), 2), round((5 * ((value - 32) / 9)) + 273.15, 2)
        case 'k':
            return round(value - 273.15, 2), round((9 * (value - 273.15) / 5) + 32, 2)
        case _:
            print("Valor invalido")
            return None



def main():
    print("Tabla de equivalencias de temperatura\n")
    base = input("Elegir la base de conversión (C/K/F): ")
    min=int(input("Introducir valor mínimo: "))
    max=int(input("Introducir valor máximo: "))
    print("C\t\tK\t\tF")
    for i in range(min, max + 1):
        current = convert_value(i, base)
        if not current:
            print("NA\t\tNA\t\tNA")    
            
        print("{}\t\t{}\t\t{}".format(i, current[0], current[1]))

    

if __name__ == '__main__':
    main()