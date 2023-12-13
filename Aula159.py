# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos
# como __init__(), __repr__(), __eq__() (entre outros) em classes definidas
# pelo usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    # def __init__(self, nome, sobrenome) -> None:
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self) -> None:
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self) -> str:
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, nome_completo: str) -> None:
    #     self.nome, self.sobrenome = nome_completo.split(' ', maxsplit=1)


if __name__ == '__main__':
    # lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    # print(ordenadas)
    p1 = Pessoa('Luiz', 'Cunha')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
