
def sum(x, y):
    with open("/dev/random", 'rb') as file:
        data = file.read(1024)
        file.close()
        print(data)
    return x + y

with open("/dev/random", 'rb') as file:
    data = file.read(1024)
    file.close()


print(sum(3, 4))