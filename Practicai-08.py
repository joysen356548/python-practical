def numbers():
    yield 10
    yield 20
    yield 30

for n in numbers():
    print(n)