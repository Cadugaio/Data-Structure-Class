class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir_no_inicio(self, nodo):
        nodo.proximo = self.head
        self.head = nodo

class TabelaHash:
    def __init__(self):
        self.tabela = [ListaEncadeada() for _ in range(10)]

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            char1_ascii = ord(sigla[0])
            char2_ascii = ord(sigla[1])
            return (char1_ascii + char2_ascii) % 10

    def inserir(self, sigla, nome_estado):
        nodo = Nodo(sigla, nome_estado)
        posicao = self.funcao_hash(sigla)
        self.tabela[posicao].inserir_no_inicio(nodo)

    def imprimir_tabela(self):
        for i, lista in enumerate(self.tabela):
            print(f"Posição {i}: ", end="")
            current = lista.head
            while current:
                print(current.sigla, end=" -> ")
                current = current.proximo
            print("None")

# Criar a tabela hash
tabela_hash = TabelaHash()

# Exibir a tabela hash vazia (Exigência de Saída de Console 1 de 3)
print("Tabela Hash vazia:")
tabela_hash.imprimir_tabela()

# Inserir os estados e o Distrito Federal
estados = {
    "AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas", "BA": "Bahia",
    "CE": "Ceará", "ES": "Espírito Santo", "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul", "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná",
    "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", "RS": "Rio Grande do Sul",
    "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina", "SP": "São Paulo", "SE": "Sergipe",
    "TO": "Tocantins", "DF": "Distrito Federal"
}

for sigla, nome_estado in estados.items():
    tabela_hash.inserir(sigla, nome_estado)

# Exibir a tabela hash após inserir os estados e o DF (Exigência de Saída de Console 2 de 3)
print("\nTabela Hash após inserir os estados e o Distrito Federal:")
tabela_hash.imprimir_tabela()

# Inserir um estado fictício
tabela_hash.inserir("CG", "Cadu")

# Exibir a tabela hash após inserir o estado fictício (Exigência de Saída de Console 3 de 3)
print("\nTabela Hash após inserir o estado fictício:")
tabela_hash.imprimir_tabela()