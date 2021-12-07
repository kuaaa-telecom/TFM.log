import sys

def winner(records):
    book = {}
    for record in records:
        winner = record.split("\n")[0].split(" ")[1]
        if winner not in book:
            book[winner] = 1
        else:
            book[winner] += 1
    return book 

def moster(records):
    book = {}
    for record in records:
        rows = record.split("\n")
        for row in rows:
            corp = row.split(" ")[1]
            if corp not in book:
                book[corp] = 1
            else:
                book[corp] += 1
    return book 


filename = sys.argv[1]

raw = open(filename, 'r').read()
records = raw.split("\n\n")

print(winner(records))
print(moster(records))