data = {}

with open('conf.txt','r') as f:
    for line in f:
        key,value = line.split('=')

data['a'] = str(input('Input a: '))
data['b'] = str(input('Input b: '))
data['c'] = str(input('Input c: '))

with open('conf.txt','w') as f:
    for value in sorted(data.items(),key=lambda item:item[1],reverse=True):
        f.write('%s = %s\n' % (value))

print(open('conf.txt','r').read())