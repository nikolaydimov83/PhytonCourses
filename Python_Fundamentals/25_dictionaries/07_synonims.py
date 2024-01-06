synonyms_count=int(input())
dictionary={}

for i in range(synonyms_count):
    key=input()
    value=input()
    if key in dictionary.keys():
        dictionary[key].append(value)
    else:
        dictionary[key]=[value]

for word,synonims in dictionary.items():
    print(f"{word} - {', '.join(synonims)}")