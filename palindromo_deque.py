class Deque:
    def __init__(self):
        self.items = []

    def vazio(self):
        return self.items == []

    def pushFront(self, item):
        self.items.append(item)

    def pushBack(self, item):
        self.items.insert(0, item)

    def popFront(self):
        return self.items.pop()

    def popBack(self):
        return self.items.pop(0)

    def dequeSize(self):
        return len(self.items)

#########################################################################
def palindromo(frase):
    char_deque = Deque()

    for ch in frase:  # Adiciona os caracteres no final do deque um a um
        char_deque.pushBack(ch)

    igual = True  # Inicial objeto 'igual' como True

    while char_deque.dequeSize() > 1 and igual:
        primeiro = char_deque.popFront()
        ultimo = char_deque.popBack()
        if primeiro != ultimo:  # Se o último item for diferente do primeiro
            igual = False  # Não é um palíndromo

    return igual

#Teste das funções

print('A entrada: 1234321 é palíndromo?', (palindromo("1234321")))
print('A entrada: 12345678 é palíndromo?',palindromo("12345678"))
print('A entrada: osso é palíndromo?',palindromo("osso"))
print('A entrada: afafafafaa é palíndromo?',palindromo("afafafafaa"))
print('A entrada: teste é palíndromo?',palindromo("teste"))