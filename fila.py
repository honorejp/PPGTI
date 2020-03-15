# Fila e operações padrão

# size – retorna o número de elementos na fila
# isEmpty – verifica se a fila está vazia ou não
# Queue– insere um elemento na fila
# Peek – retorna o elemento na frente da fila, sem removê-lo
# Dequeue – remove um elemento da fila

# Retorna o numero de elementos da Fila
def fila_size(lista):
    return len(lista)

# isEmpty – verifica se a fila está vazia ou não
def fila_is_empty(lista):
    if cont == 0:
        return True
    else:
        return False

# Queue– insere um elemento na fila
# Insere o passada retornando no topo da pilha
def fila_queue(lista, elemento):
    lista.append(elemento)
    return lista

# Retorna o primeiro elemento da pilha passada retornando a pilha sem remover o elemento
def fila_peek(lista):
    # if(not FilaisEmpty):
    return lista[0]

# Dequeue – remove um elemento da fila
# Remove o primeiro elemento a entrar na fila passada retornando a pilha sem o elemento
def fila_dequeue(lista):
    lista.pop(0)
    return lista

# Entrada de teste
input_teste = [1, 2, 3, 4, 5, 6]
cont = fila_size(input_teste) #Recebe a informação do tamanho da fila

# Testes das funções
print("A Fila original: ", input_teste)
print("O tamanho da Fila: ", fila_size(input_teste))
print("Se adicionarmos um elemento na fila: ", fila_queue(input_teste, 12))
print("O elemento do topo da Fila: ", fila_peek(input_teste))
print("A Pilha esta vazia? ", fila_is_empty(input_teste))
print("O elemento da frente da fila: ", fila_peek(input_teste))
print("Removendo o primeiro elemento do Fila: ", fila_dequeue(input_teste))
