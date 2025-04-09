group = open("BoyGroup.txt","w")
group.write("Stray Kids\n")
group.write("Enhypen\n")
group.write("TXT")
group.close()

group = open("BoyGroup.txt","r")
print(group.read())
group.close()

group = open("BoyGroup.txt","r")
print(group.read(4))
print(group.read(10))
group.close()

group = open("BoyGroup.txt","r")
print(group.readline())
print(group.readline())
print(group.readline())
group.close()

group = open("BoyGroup.txt","r")
print(group.readlines())
group.close()

group = open("BoyGroup.txt","r")
for line in group:
  print(line)
group.close()

group = open("BoyGroup.txt","a")
group.write("\nATEEZ\n")
group.close()