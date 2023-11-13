# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que classes derivadasde uma superclasse
# tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz
# parte da assinatura).
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais.
# SOLID
# S - Single Responsability Principle (SRP) - Princípio da responsabilidade única
# O - Open-Closed Principle (OCP) - Princípio aberto-fechado
# L - Liskov Substitution Principle (LSP) - Princípio da substituição de Liskov
# I - Interface Segregation Principle (ISP) - Princípio da segregação de interfaces
# D - Dependency Inversion Principle (DIP) - Princípio da inversão de dependência
# SO"L"ID
# Princípio da substituição de Liskov
# Objetos de uma superclasse devem ser substituíveis por objetos de uma
# subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload) - Pyhton não suporta sobrecarga de métodos
# Sobreposição de métodos (override) - Python suporta sobreposição de métodos
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'Enviando e-mail: {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'Enviando SMS: {self.mensagem}')
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada com sucesso\n')
    else:
        print('Falha ao enviar notificação\n')


notificacao_email = NotificacaoEmail('Testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)
