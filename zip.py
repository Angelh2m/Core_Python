midterms = [80, 90, 78]
finals = [98, 89, 53]
studens = ['John', 'Jane', 'Rail']

# final_grades = zip(midterms, finals)

final_grades = {t[0]: max(t[1], t[2])
                for t in zip(studens, midterms, finals)}

print(final_grades)

scores = map(
    lambda pair: max(pair),
    zip(midterms, finals)
)
print(scores)
