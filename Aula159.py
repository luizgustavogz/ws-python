# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos
# como __init__(), __repr__(), __eq__() (entre outros) em classes definidas
# pelo usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    # idade: int

    @property
    def nome_completo(self) -> str:
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, nome_completo: str) -> None:
        self.nome, self.sobrenome = nome_completo.split(' ', maxsplit=1)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Cunha')
    p1.nome_completo = 'Luiz Gustavo de Oliveira Cunha'
    print(p1)
    print(p1.nome_completo)
