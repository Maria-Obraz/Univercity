import csv


def get_books(filename: str, name: str):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='|')

        resultat = [[]]
        resultat.clear()

        for row in reader:
            if ''.join(row).__contains__(name):
                resultat.append(row)

        return resultat

def get_totals(data: [[]], sum = 0, add = 0):
    resultat = [[]]
    resultat.clear()

    for row in data:
        count = int(row[3]) * float(row[4])
        if count < sum:
            sum += add
        resultat.append([row[0], count])

    return resultat


books = get_books("file.csv", "Python")
result = get_totals(books)

for i in result:
    print(i)

