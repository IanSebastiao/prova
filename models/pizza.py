class Pizza:
    def __init__(self, nome: str, tamanho: str):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = 0

    def valor(self):
        if self.tamanho.upper() == 'P':
            self.preco = '10'
        elif self.tamanho.upper() == 'M':
            self.preco = '20'
        elif self.tamanho.upper() == 'G':
            self.preco = '30'
        return self.preco
    