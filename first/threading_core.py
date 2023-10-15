# Конкурентность (concurrency) - запуск выполнение сразу нескольких задач (необязательно в 1 момент времени
# выполняется несколько) . Зависит от ПО.

# Параллельность (parallel) - конкурентность, когда 2+ задачи выполняются одновременно. Зависит железа•
# thread-safe - потокобезопасность, означает что при работе с объектом не возникают известные проблемы при работе с конкурентностью
# GIL (Global Interpreter Lock) - глобальная блокировка интерпретатора


# Задачи могут быть:
# CPU-bound - зависит от мощности процессора
# I0-bound - зависит от системы ввода/ вывода
# threading - I0-bound задачи
# asyncia - I0-bound задачи
# multiprocessing - любые задачи
import threading
import time
import requests
def activity():
    # for e in range (1000_000):
    #     abs (round(e ** 2 / 122) + e * 3.14)
    requests.get("https://yandex.ru")


def run(threaded = False):
    start = time.time()
    if not threaded:
        for e in range(10):
            activity()
    else:
        threads = [threading.Thread(target=activity(), daemon = True) for _ in range(10)]
        for e in threads:
            e.start()
        for e in threads:
            e.join()
    end = time.time()
    print(f'Time {end - start} seconds')


if __name__ == '__main__':
    run()