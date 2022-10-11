import pandas
res = dict()
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in nato_alphabet.iterrows():
    res[row.letter] = row.code
take_input = input("Enter your word here:\n")
result = list()
for i in take_input:
    result.append(res[i.upper()])
print("Şunları söyleyin:")
for i in result:
    print(f"{i}'nın {i[0]}'sı")
