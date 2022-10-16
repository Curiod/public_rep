import csv
import json
import datetime


def display(res, number):
    formatted_row = '{:<5} {:<15} {:<12} {:<10} {:<9}'
    print(formatted_row.format("Место", "Нагрудный номер", "Имя", "Фамилия", "Результат"))
    for j in range(number):
        print(formatted_row.format(*res[j]))


with open('results_RUN.txt', 'r') as file1, open("competitors2.json", encoding="utf-8") as file2:
    data = csv.reader(file1, delimiter=' ')
    competitors = json.load(file2)
    results = []
    i = -1
    for row in data:
        if row[1] == 'start':
            i += 1
            start = row
            results.append([row[0], competitors[row[0]]['Surname'],
                           competitors[row[0]]['Name'], 0])
        if row[1] == 'finish':
            t1 = datetime.datetime.strptime(start[2], "%H:%M:%S,%f")
            t2 = datetime.datetime.strptime(row[2], "%H:%M:%S,%f")
            results[i][3] = str(t2-t1)[2:-4]
    results = sorted(results, key=lambda x: x[3])
    for i in range(len(results)):
        results[i].insert(0, i + 1)
        
display(results, 10)
