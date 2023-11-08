import multiprocessing
from clickhouse_driver import Client

# Функция для выполнения запросов
def execute_query(query):
    client = Client(
        host='g2.plzvpn.ru',
        user='default',
        password='1',
        port='9000',
        database='test',
        #settings={'use_numpy': True}
    )

    result = client.execute(query)
    for row in result:
        print(row)

if __name__ == '__main__':
    # Список запросов, которые вы хотите выполнить параллельно
    queries = [
        'SELECT * FROM Prodazhi LIMIT 6',
        'SELECT * FROM Goroda LIMIT 4',
    ]

    # Создайте пул процессов, равный количеству запросов
    pool = multiprocessing.Pool(processes=len(queries))

    # Запустите запросы параллельно
    pool.map(execute_query, queries)

    # Завершите пул
    pool.close()
    pool.join()