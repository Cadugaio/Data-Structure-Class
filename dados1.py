class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            current = self.head
            while current.proximo:
                current = current.proximo
            current.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            current = self.head
            while current.proximo and current.proximo.cor == 'A':
                current = current.proximo
            nodo.proximo = current.proximo
            current.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A/V): ").strip().upper()
        numero = int(input("Digite o número do cartão: ").strip())
        nodo = Nodo(numero, cor)

        if not self.head:
            self.head = nodo
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        elif cor == 'A':
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        if not self.head:
            print("A lista de espera está vazia.")
            return

        current = self.head
        while current:
            print(f"Cartão {current.cor}{current.numero}")
            current = current.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Não há pacientes na fila.")
            return

        paciente = self.head
        self.head = self.head.proximo
        print(f"Chamando paciente do cartão {paciente.cor}{paciente.numero} para atendimento.")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1 – Adicionar paciente à fila")
            print("2 – Mostrar pacientes na fila")
            print("3 – Chamar paciente")
            print("4 – Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.imprimirListaEspera()
            elif opcao == '3':
                self.atenderPaciente()
            elif opcao == '4':
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Criar a lista encadeada e mostrar o menu
lista = ListaEncadeada()
lista.menu()