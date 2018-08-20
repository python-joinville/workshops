# Classes em Python

## Exemplo de atributos e métodos

class Pessoa:
    def __init__(self, pnome, sobre, idade):
        self.pnome = pnome
        self.sobre = sobre
        self.idade = idade

    def nome_completo(self):
        return self.pnome + ' ' + self.sobre

## Exemplo de Herança

class ContaBase:
    def __init__(self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo

    def debitar(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            raise Exception("Sem limite para o saque")
    def creditar(self, valor):
        self.saldo += valor
    def saldo_total(self):
        return self.saldo


class ContaCorrente(ContaBase):
    def __init__(self, numero, agencia, saldo, limite):
        super().__init__(ContaCorrente, numero, agencia, saldo)
        self.limite = limite

    def debitar(self, valor):
        if self.saldo_total() >= 0:
            self.saldo -= valor
        else:
            raise Exception("Sem saldo em conta")

    def saldo_total(self):
        return self.saldo + self.limite

    def _metodo_protected(self):
        pass

    def __metodo_privad(self):
        pass


class ContaPoupanca(ContaBase):
    def __init__(self, numero, agencia, saldo):
        super().__init__(ContaPoupanca, numero, agencia, saldo)

# Implementar um sistema de gerenciamento de biblioteca, onde
# temos uma classe `Biblioteca` que representa uma bliblioteca
# e conhece todos os livros disponíveis e emprestados,
# e uma classe `Livro` que contém os atributos dos livros.

# Livro:
# - titulo
# - autor
# - número de páginas
# - data de publicacao
# - emprestado

# Biblioteca:
# - nome
# - lista de livros disponiveis
# - lista de livros emprestados
# - emprestar(nome_do_livro)
# - devolver(nome_do_livro)

class Livro:
    def __init__(self, titulo, autor, npaginas, dtpub, emprestado):
        self.titulo = titulo
        self.autor = autor
        self.npaginas = npaginas
        self.dtpub = dtpub
        self.emprestado = emprestado
    def emprestar(self):
        self.emprestado = True
    def devolver(self):
        self.emprestado = False

class Biblioteca:
    def __init__(self, nome, livros):
        self.nome = nome
        self.livros = livros

    def livros_emprestados(self):
        emprestados = []
        for livro in self.livros:
            if livro.emprestado:
                emprestados.append(livro)
        return emprestados

    def livros_disponiveis(self):
        disponiveis = []
        for livro in self.livros:
            if not livro.emprestado:
                disponiveis.append(livro)
        return disponiveis

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.emprestado:
                    raise Exception('Livro já emprestado')
                else:
                    livro.emprestar()

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.devolver()


livros = [
    Livro('Titulo 1', 'Autor 1', 200, '01/10/2017', False),
    Livro('Titulo 2', 'Autor 2', 200, '01/10/2017', False),
    Livro('Titulo 3', 'Autor 3', 200, '01/10/2017', False),
    Livro('Titulo 4', 'Autor 4', 200, '01/10/2017', False),
    Livro('Titulo 5', 'Autor 5', 200, '01/10/2017', False),
    Livro('Titulo 6', 'Autor 6', 200, '01/10/2017', False),
    Livro('Titulo 7', 'Autor 7', 200, '01/10/2017', False),
    Livro('Titulo 8', 'Autor 8', 200, '01/10/2017', False),
    Livro('Titulo 9', 'Autor 9', 200, '01/10/2017', True),
    Livro('Titulo 10', 'Autor 10', 200, '01/10/2017', True),
    Livro('Titulo 11', 'Autor 11', 200, '01/10/2017', True),
]

b = Biblioteca('Bib do Alan', livros)
len(b.livros_emprestados())
len(b.livros_disponiveis())
b.emprestar('Titulo 3')
len(b.livros_emprestados())
len(b.livros_disponiveis())
b.emprestar('Titulo 2')
len(b.livros_disponiveis())
len(b.livros_emprestados())
b.devolver('Titulo 2')
len(b.livros_emprestados())
len(b.livros_disponiveis())
