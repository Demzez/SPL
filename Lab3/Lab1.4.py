import json


def calculate_firm_profit():
    firms_profit = {}
    total_profit = 0
    profitable_firms = 0

    with open("firms.txt", "r", encoding="utf-8") as file:
        for line in file:
            data = line.split()
            name = data[0]
            revenue = int(data[2])
            costs = int(data[3])

            profit = revenue - costs
            firms_profit[name] = profit

            # Считаем среднюю прибыль только для прибыльных фирм
            if profit > 0:
                total_profit += profit
                profitable_firms += 1


    average_profit = total_profit / profitable_firms if profitable_firms > 0 else 0

    result_list = [firms_profit, {"average_profit": round(average_profit)}] # округление

    # Сохраняем в JSON файл
    with open("firms_result.json", "w", encoding="utf-8") as json_file:
        json.dump(result_list, json_file, ensure_ascii=False, indent=4)

    print("Результат сохранен в firms_result.json")
    print(result_list)


calculate_firm_profit()