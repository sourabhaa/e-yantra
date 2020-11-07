'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code D2BIN_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			D2BIN_PY.py
*  Created:				04/10/2020
*  Last Modified:		04/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
'''

# Function to calculate Euclidean distance between two points

def dec_to_binary(n):
    if n==0:
        return 0
    else:    
        return (n % 2 + 10 * dec_to_binary(int(n// 2)))
    
    


# Main function
if __name__ == '__main__':
    test_cases = int(input())
    nn=[]
    if(test_cases >=1 and test_cases <=25):
        for case in range(1,test_cases+1):
            a = [0,0,0,0,0,0,0,0]
            n = int(input())
            if(n>=0 and n<=255):
                nn.append(n)
        for case in range(len(nn)):
                
            bin_num = dec_to_binary(nn[case])        
            count=0
            t=0
            t=bin_num
            while(bin_num>0):
                count=count+1
                bin_num=bin_num//10
                i=0
            for i in range (count):
                a[7-i] = t%10
                t=int(t/10)
            c=0
            for i in a:
                c+=1
                l=0
                if(c%8==0 and l <test_cases):
                    l+=1
                    print(i,end="\n")
                else:
                    print(i,end="")
                    

            



      

