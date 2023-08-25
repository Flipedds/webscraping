class Fila:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.__valores = [None] * self.capacidade
    
    def __fila_vazia(self):
        return self.numero_elementos == 0
    
    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            raise Exception("A fila está cheia")

        self.final = (self.final + 1) % self.capacidade
        self.__valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            raise Exception("A fila está vazia")
        
        temp = self.__valores[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.__valores[self.inicio]