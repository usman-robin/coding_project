# open file
f = open("example.txt", 'r')
print(f.read())
for line in f:
    print line

counter = 0
while f.readline():
    counter += 1
    print (counter)



f.close()

#fw = open("example.txt", "a") #opens file with name of "test.txt"
#fw.write("Adding a line")
#fw.close()