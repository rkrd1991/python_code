open('temp.txt','w').close()
open('temp2.txt','w').close()
open('PM_2cat.txt','w').close()
 
with open('cat'+str(n)+'.txt','r') as cat:
    for seq in cat.readlines():
        L=[int(x) for x in seq.split()]
        copyfile('cat'+str(L[0])+'.txt','temp.txt')
        open('temp2.txt','w').close()
        for i in range(1,len(L)):
            temp=open('temp.txt','a+')
            for t in temp.readlines():
                file2=open('cat'+str(i)+'.txt','r')
                for f2 in file2.readlines():
                    temp2=open('temp2.txt','a')
                    temp2.write(t.rstrip()+' '+f2)
                    temp2.close()
            copyfile('temp2.txt','temp.txt')
        temp=open('temp.txt','r')
        file=open('PM_2cat.txt','a')
        file.write(temp.read())
        file.close()
        temp.close()
