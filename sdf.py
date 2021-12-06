def intr(l1,n,l2,m):
    i,j=0,0
    while i<n and j<m:
        if(l1[i]<l2[j]):
            i+=1
        elif l2[j]<l1[i]:
             j+=1
        else:
            print(l1[i])
            i+=1
            j+=1
             
l1 = [1, 2, 4,4,4,4, 5, 6]
l2 = [2, 3,4,4,4,4,4, 5, 7]
n = len(l1)
m = len(l2)
intr(l1, n, l2, m)

  
