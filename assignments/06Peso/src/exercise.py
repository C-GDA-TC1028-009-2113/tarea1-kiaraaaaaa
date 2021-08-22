def main():
    #escribe tu código abajo de esta línea
    pass
    peso=float(input('Dame el peso inicial: '))
    pesof=float(input('Dame el peso final: '))
    meses= int(input('Dame la cantidad de meses: '))
    perdida=(peso-pesof)/meses
    print ('Lo que debes bajar por mes es: '+ str(perdida))



if __name__ == '__main__':
    main()
