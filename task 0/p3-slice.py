'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code SLICE_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            SLICE_PY.py
*  Created:             04/10/2020
*  Last Modified:       04/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
'''
 
# Main function
if __name__ == '__main__':
    test_cases = int(input())
    l=[]
    nn =[]
    Sum =[]
    summ=0
    if (test_cases>=1 and test_cases <= 25):
        for i in range(test_cases): 
            L = int(input())
            l.append(L)
            n =[]
            count =0
            if (L>=8 and L<=50):
                n = list(map(int,input().strip().split()))
            
                
                
            for j in range(len(n)):
                if (n[j]>= -100 and n[j]<= 100):
                    count+=1

            if (count == (len(n))):
                nn.append(n)
                summ=n[3]+n[4]+n[5]+n[6]+n[7]
                Sum.append(summ)

        m=[]
        c=[]
        d=[]
        for i in range(test_cases):
            a=[]
            b=[]
            for j in range (l[i]):
                
                if (j%3==0 and j>1):    
                    a.append(nn[i][j]+3)
                
                if (j%5==0 and j>1):
                    b.append(nn[i][j]-7)
           
            m=nn[i]
            m.reverse()   
            print(*m)
            print(*a)
            print(*b)
            print(Sum[i])
            
            
                
        
            




    




































