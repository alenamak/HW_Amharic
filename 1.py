
f = open('alph.csv', 'r', encoding='utf-8')

d = {}
line1 = []
x = 1
y = 0

for line in f:
    line = line.strip()
    l = line.split('\t')
    if 'u' in l:
        for i in l:
            line1.append(i)
    else:
        for i in l:
            if x < 8:
                key = l[x]
                d[key] = l[0] + line1[x-1]
                x += 1
            else:
                x = 1
                
            
print(d)

f.close()

text = open('text.txt', 'r', encoding='utf-8')
transl = open('transl.txt', 'w', encoding='utf-8')

for line in text:
    for letter in line:
        if letter in d:
            transl.write(d[letter])
        else:
            transl.write(letter)

text.close()
transl.close()
