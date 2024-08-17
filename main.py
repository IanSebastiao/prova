from models.pizza import Pizza
from models.pizza_especial import PizzaEspecial

adicionais = []
nome = input('Digite o sabor da pizza'
             '\nCalabresa = 1'
             '\nFrango com catupiry =2 '
             '\nModa da casa = 3'
             '\nAtum = 4\n'
             )
adicional = input('Escolha os adicionais ou enter para continuar'
                  '\nCheddar $5 = 1'
                  '\nBacon $5 = 2\n'
                  )
adicionais.append(adicional)
tamanho = input('Informe o tamanho da pizza (P, M, G): ')
pizza = PizzaEspecial(nome, tamanho, adicional)
pizza.detalhes()
