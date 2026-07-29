mail = 'hey! how are youdoing all hope everyone is doing good'
f = open("myfiles.txt", "w")
f.write(mail)
data = f.read()
print(data)
f.close()