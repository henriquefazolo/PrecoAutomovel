class CalculadoraAutomovel:
    def __init__(self):
        self._qtd_trio_eletrico = 0
        self._qtd_ar_condicionado = 0
        self._qtd_direcao_hidraulica = 0

    def menu_inicial(self):
        try:
            opcao = int(input('1 - Deseja calcular o preço de um automóvel ?\n'
                              '0 - Sair\n'))
            if opcao == 1:
                return self.calcular_preco()
            elif opcao == 0:
                self.resumo()
                exit()
            else:
                self.menu_inicial()
        except Exception as e:
            print(e)
            self.menu_inicial()

    def calcular_preco(self):
        try:
            valor_inicial = float(input('Digite o valor de entrada do automóvel:\n'))
            if valor_inicial == 0:
                self.menu_inicial()
            opcao = int(input('Deseja algum destes opcionais?\n'
                              '1 - Trio eletrico\n'
                              '2 - Ar condicionado\n'
                              '3 - Direção hidraulica\n'
                              '4 - Completo\n'
                              '5 - Sem opcionais\n'
                              '0 - Voltar\n'))
            if opcao == 5:
                print(f'\nValor final de R$ {valor_inicial*1.08:,.2f}.\n')
                self.menu_inicial()
            if opcao == 1:
                print(f'\nValor final de R$ {(valor_inicial * 1.08)*1.02 :,.2f}.\n')
                self._qtd_trio_eletrico += 1
                self.calcular_preco()
            if opcao == 2:
                print(f'\nValor final de R$ {(valor_inicial * 1.02)*1.08 :,.2f}.\n')
                self._qtd_ar_condicionado += 1
                self.calcular_preco()
            if opcao == 3:
                print(f'\nValor final de R$ {(valor_inicial * 1.02)*1.08 :,.2f}.\n')
                self._qtd_direcao_hidraulica += 1
                self.calcular_preco()
            if opcao == 4:
                ar_condicionado = valor_inicial * 0.02
                direcao_hidraulica = valor_inicial * 0.02
                base_sem_ipi = valor_inicial + ar_condicionado + direcao_hidraulica
                base_com_ipi = base_sem_ipi * 1.08
                valor_final = base_com_ipi * 1.02

                print(f'\nValor final de R$ {valor_final:,.2f}.\n')
                self._qtd_trio_eletrico += 1
                self._qtd_ar_condicionado += 1
                self._qtd_direcao_hidraulica += 1
                self.calcular_preco()
            if opcao == 0:
                self.menu_inicial()

        except Exception as e:
            print(e)

    def resumo(self):
        print(f'Trio Eletrico : {self._qtd_trio_eletrico}\n'
              f'Ar Condicionado : {self._qtd_ar_condicionado}\n'
              f'Direção Hidraulica : {self._qtd_direcao_hidraulica}\n')


loja = CalculadoraAutomovel()
loja.menu_inicial()
