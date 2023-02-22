

def main():
    tamConjuntoUniversal = int(input("Ingrese la cantidad de elementos del conjunto universal: "))
    universal = definirConjuntoUniversal(tamConjuntoUniversal)
    print(universal)

    universal = definirElementos(universal)
    print(universal)

    subConjuntos = darSubconjuntos(universal)
    print("Los subconjuntos son: " + str(subConjuntos))

    darContenidosElemento(universal, subConjuntos)
    darContenidosConjunto(universal, subConjuntos)
    darSubConjuntosElemento(universal, subConjuntos)
    darSubConjuntosConjunto(universal, subConjuntos)
    darContenidosElemento(universal)
    darPertenenciaConjunto(subConjuntos)

#Fucnión para crear la lista
def definirConjuntoUniversal(tamConjuntoUniversal):
    universal = [0] * tamConjuntoUniversal
    return universal

#Metodo para darle el valor que queramos a cada elemento
def definirElementos(universal):
    elemento = 0
    for i in range(len(universal)):
        res = esElemento()
        if res == True:
            elemento = input("Ingrese el elemento para la posición " + str(i + 1) + ": ")
            universal[i] = elemento

        elif res == False:
            subConjunto = crearSubconjunto(len(universal))
            universal[i] = subConjunto

    return universal

def esElemento():
    elemento = True
    res = input("Se desea agregar un elemento (1) o un subconjunto (2): ")
    if res == "1":
        return elemento

    elif res == "2":
        elemento = False
        return elemento

    return elemento

def crearSubconjunto(tamConjuntoUniversal):
    res = False
    while res != True:
        tam = input("Ingrese el tamaño del subconjunto: ")
        if int(tam) <= tamConjuntoUniversal:
            subConjunto = [0] * int(tam)
            elemento = 0
            res = True
        
        else:
            print("El tamaño del subconjunto debe ser menor al tamaño del conjunto universal")

    for i in range(len(subConjunto)):
        elemento = input("Ingrese el elemento para la posición " + str(i + 1) + ": ")
        subConjunto[i] = elemento

    return subConjunto;

#-----------------------------------------------------------------------------------------------------------------------
#Función que me devuelve una lista con los subconjuntos de cada lista
def darSubconjuntos(universal):
    subConjuntos = []
    for i in universal:
        if isinstance(i, list):
            subConjuntos.append(i)
    return subConjuntos

#Método que me suelta el contenido(c), teniendo en cuenta a la sublista como elemento
def darContenidosElemento(universal, subConjunto):
    subCon = []
    elemento = ""
    tam = 0
    cont = 0
    for i in subConjunto:
        subCon = i
        tam = len(subCon)
        for j in subCon:
            elemento = j
            for k in universal:
                if elemento == k:
                    cont = cont + 1
        
        if cont == tam:
            print(str(subCon) + " Como elemento está contenido en " + str(universal))
            cont = 0
        
        else:
            print(str(subCon) + " Como elemento no está contenido en " + str(universal))
            cont = 0


#Método que me suelta el contenido(c), teniendo en cuenta a la sublista como conjunto
def darContenidosConjunto(universal, subConjunto):
    subCon = []
    aux = False
    for i in subConjunto:
        subCon = i
        for j in universal:
            if subCon == j:
                print(str(subCon) + " Como conjunto está contenido en " + str(universal))
                aux = True
            
        if aux == False:
            print(str(subCon) + " Como conjunto no está contenido en " + str(universal))

#Método que me suelta el subconjunto ( c ), teniendo en cuenta a la sublista como elemento
def darSubConjuntosElemento(universal, subConjunto):
    subCon = []
    elemento = ""
    tam = 0
    cont = 0
    print("Esto es la lista de subconjuntos: " + str(subConjunto))
    for i in subConjunto:
        subCon = i
        tam = len(subCon)
        for j in subCon:
            elemento = j
            for k in universal:
                if elemento == k:
                    cont = cont + 1
                    
        if cont == tam and len(subCon) < len(universal):
            print(str(subCon) + " Como elemento es subconjunto en " + str(universal))
            cont = 0
            
        
        else:
            print(str(subCon) + " Como elemento no es subconjunto en " + str(universal))
            cont = 0


#Método que me suelta el subconjunto ( c ), teniendo en cuenta a la sublista como conjunto
def darSubConjuntosConjunto(universal, subConjunto):
    subCon = []
    aux = False
    for i in subConjunto:
        subCon = i
        for j in universal:
            if subCon == j:
                print(str(subCon) + " Como conjunto es subconjunto en " + str(universal))
                aux = True
            
        if aux == False:
            print(str(subCon) + " Como conjunto no es subconjunto en " + str(universal))

#Método que me dice si el elemento pertenece (E) a el conjunto universal
def darPertenciaElemento(univeral):
    print("Los elementos que pertencen a el conjunto universal son los siguientes: ")
    for i in univeral:
        print(str(i) + " pertence (E) al conjunto universal")

#Método que me dice si un conjunto pertenece (E) al universal
def darPertenenciaConjunto(subConjunto):
    print("Los siguientes elemento como CONJUNTOS no pertenecen al conjunto universal: ")
    for i in subConjunto:
        print(str(i) + " teniendolo en cuenta como conjunto no pertenece al conjunto universal")

main()