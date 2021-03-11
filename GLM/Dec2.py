
with open('input2.txt') as f:
    doc = f.read()

lines = doc.split('\n')
items = [line.split(' ') for line in lines if line != '']
lens = [len(item) for item in items]
objects = [{'low': int(item[0].split('-')[0]), 'high':int(item[0].split('-')[1]), 'char': item[1].strip(':'), 'pwd': item[2] } for item in items if len(item)==3]

nok = 0
for obj in objects:
    n = obj['pwd'].count(obj['char'])
    if n <= obj['high'] and n >= obj['low']:
        nok += 1

print(nok)

nok = 0
for obj in objects:
    if (obj['pwd'][obj['high']-1] == obj['char'] and not obj['pwd'][obj['low']-1] == obj['char']) or (not obj['pwd'][obj['high']-1] == obj['char'] and obj['pwd'][obj['low']-1] == obj['char']):
        nok += 1

print(nok)

nok = 0
for obj in objects:
    sum = 0
    if obj['pwd'][obj['low']-1] == obj['char']:
        sum += 1
    if obj['pwd'][obj['high']-1] == obj['char']:
        sum += 1
    if sum == 1:
        nok += 1


print(nok)
print('hej')
