f = open("2000.txt", 'r', encoding = 'utf-8')
nf = open("test.txt", 'w')
idx = 1

while True:
    if idx % 40 == 1:
        nf.write("unit"+str((idx // 40) + 1)+"\n")
    idx +=1
    line = f.readline()
    nf.write(line)
    if not line: break
    print(line)
f.close()
nf.close()