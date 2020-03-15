
#Pilha e operações padrão - Push, Pop, Top, isEmpty, Size 
#A implementação considera que o primeiro item do array é a base da pilha

#Retorna o numero de elementos da Pilha
def pilha_size(lista):
    return len(lista)

#Insere o elemento no topo da pilha
def pilha_push(lista, elemento):
    lista.append(elemento)
    return lista

#Retorna o primeiro elemento da pilha passada retornando a pilha sem remover o elemento
def pilha_top(lista):
    if lista[cont] == 0:
        return null
    else:
        return lista[cont]

def pilha_is_empty(lista):
    if cont == 0:
        return True
    else:
        return False

#Remove o primeiro elemento da pilha passada retornando a pilha sem o elemento
def pilha_pop(lista):
    lista.pop()
    return lista

#Entrada de teste
input_teste = [1,3,5,7,9]
cont = pilha_size(input_teste) #Recebe a informação do tamanho da fila

#Testes das funções
print ("A Pilha original: ", input_teste)
print ("O tamanho da Pilha: ", pilha_size(input_teste))
print ("Se adicionarmos um elemento por Push: ", pilha_push(input_teste,12))
print ("O elemento do topo da Pilha: ", pilha_top(input_teste))
print ("A Pilha esta vazia? ", pilha_is_empty(input_teste))
print ("Removendo o elemento do topo da Pilha: ", pilha_pop(input_teste))