
kopi = open(r"C:\Users\user\OneDrive\Desktop\Visual Studio Code\Python\kopi_susu.txt", "w") #writing the textfile

kopi.write("Koleksi Kopi-Kopi Tempatan\n")
leng = "Koleksi Kopi-Kopi Tempatan"
kopi.write("=" * len(leng))

kopi.write("Kopi O\n")
kopi.write("Kopi Tarik\n")
kopi.write("Kopi Susu Tambah\n")
kopi.write("Kopi Milo Ais\n")
kopi.write("Kopi Mak\n")
kopi.write("Kopi Gula")

kopi.close()
print("Completed")
'''
k = open("kopisusu.txt", "r")
list1 = k.readlines()
print(list1[3])

'''
'''
print(k.readline(2)) #same as read(2)
print(k.readline())

print(k.read(7)) #it will continue after the 7 char including the space
print(k.read(8))
'''