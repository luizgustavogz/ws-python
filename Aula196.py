from threading import Lock, Thread
from time import sleep

"""
# (Parte 1) Threads - Executando processamentos em paralelo
class MeuThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""

"""
# (Parte 2) Threads - Executando processamentos em paralelo
def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""

# (Parte 3) Threads - Executando processamentos em paralelo
class Ingressos:
    def __init__(self, estoque: int):
        self.estoque = estoque
        self.lock = Lock()  # Criando um lock

    def comprar(self, quantidade: int):
        self.lock.acquire()  # Bloqueia o método

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()  # Libera o método
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        self.lock.release()  # Libera o método


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print('Ingressos em estoque =', ingressos.estoque)
