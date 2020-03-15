
#Deque - Double-Ended Queue e operações padrão

#dequeSize - Informa tamanho da entrada
#pushBack – Insere um novo elemento no fim do Deque
#pushFront – Insere um novo elemento no início do Deque
#popBack – Remove um elemento do fim do Deque
#popFront – Remove um elemento do início do Deque

def dequeSize(lista):
    return len(lista)

def pushBack(lista, elemento):
    lista.append(elemento)
    return lista

def pushFront(lista, elemento):
    lista.insert(0, elemento)
    return lista

def popFront(lista):
    lista.pop(0)
    return lista

def popBack(lista):
    lista.pop(cont)
    return lista

#Entrada de teste
input_teste = [1, 2, 3, 4, 5, 6]
cont = dequeSize(input_teste)

#Testes das funções
print ("O deque original: ", input_teste)
print ("PushBack - Se adicionarmos um elemento no fim do Deque: ", pushBack(input_teste,10))
print ("PushFront - Se adicionarmos um elemento no inicio do Deque: ", pushFront(input_teste,20))
print ("PopFront - Removendo o elemento do inicio do deque : ", popFront(input_teste))
print ("PopBack - Removendo o elemento no fim do Deque: ", popBack(input_teste))