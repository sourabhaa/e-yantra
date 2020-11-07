'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code APLAM_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			APLAM_PY.py
*  Created:				04/10/2020
*  Last Modified:		04/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
# '''

    # Import reduce module
import functools 

def generate_AP(a1, d, n):
    AP_series = []
    for i in range (n):
        if i==0:
            AP_series.append(a1)
        AP_series.append(a1+i*d)

    return AP_series



    
# Main function
if __name__ == '__main__':
    T = int(input())
    if(T>=1 and T<=25 ):
        a=[]
        b=[]
        
        for i in range (T):
            a=list(map(int, input().strip().split()))
            count = 0
            for j in range(len(a)):
                
                if (a[j]>= 1 and a[j]<= 100):
                    count+=1
            if(count == len(a)):
                b.append(a)
        for i in range (T):
            AP = generate_AP(b[i][0], b[i][1], b[i][2])
            sqr_AP_series = list(map(lambda x: x ** 2 ,AP))
            print(*AP)
            print(*sqr_AP_series)            		    
            print (functools.reduce(lambda x,y:x+y,AP)) 

