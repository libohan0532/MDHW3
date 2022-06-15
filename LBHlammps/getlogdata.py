
#cutup 截取片段开头行数
#cutdown 截取片段末尾行数+1

filein = input("输入.lammps文件当前名称(一般为log.lammps): ")
fileout = "out.txt"
data = open(filein,mode='r')
dout = open(fileout,mode='w')
f = data.readlines()

lnum = 0
for line in f:
    lnum += 1
    A = line.split()
    #print(A)
    for item in A:
        if item == 'Step':
            cutup = lnum
        if item == 'Loop':
            cutdown = lnum
act = f[cutup-1:cutdown-1]
print("输出文件名为：",dout.name)
dout.writelines(act)
dout.close()
data.close()

#print(cutup)
#print(cutdown)


