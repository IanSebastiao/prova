def detalhes(self):
        if self.nome == '1':
                print('Pizza de Calabresa')
        elif self.nome == '2':
                print('Pizza de Frango com catupiry')
        elif self.nome == '3':
                print('Pizza Moda da casa')
        elif self.nome == '4':
                print('Pizza de Atum')
        else:
                print('Sabor não encontrado')

        if self.adicional == '1':
                print('Adicional de Cheddar $5')
        elif self.adicional == '2':
                print('Adicional de bacon $5')
        else:
                print('Nenhum adicional')
                
        print(f'Tamanho: {self.tamanho}')
        print(f'Valor: {self.valor()}')