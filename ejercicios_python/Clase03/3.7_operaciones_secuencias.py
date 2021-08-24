data = [4, 9, 1, 25, 16, 100, 49]
print(f'min(data):{min(data)}')
#1

print(f'max(data):{max(data)}')
#100
print(f'sum(data):{sum(data)}')
#204

for x in data:
    print(x,end=',')
print()

for n, x in enumerate(data):
    print(f'(n, x):({n},{x})')
print()

for n in range(len(data)):
    print(data[n],end=',')
print()    