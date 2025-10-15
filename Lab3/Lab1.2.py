def process_bank_clients():
    best_clients = []
    with open("bank_clients.txt", "r") as bank_clients_file:
        best_client = bank_clients_file.readline().split()

        for line in bank_clients_file:
            data_line = line.split()

            if int(best_client[1]) < int(data_line[1]):
                best_client = data_line

            if int(data_line[1]) > 1000:
                best_clients.append(' '.join(data_line))

        print("Лучший клиент - " + ' '.join(best_client))
        print("Список всех богатых:\n" + '\n'.join(best_clients))

process_bank_clients()