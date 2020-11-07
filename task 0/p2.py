'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code DIST_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            DIST_PY.py
*  Created:             02/10/2020
*  Last Modified:       02/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
'''
 
# Import any required module/s
import math 

# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 +(y2-y1)**2)
    print('Distance: %.2f '%distance)


# Main function
if __name__ == '__main__':
    test_cases = int(input())
    if (test_cases >=1 and test_cases <=25):
        a=[]
        for i in range (test_cases):    
            b=[]                
            b=list(map(int, input().strip().split())) 
            a.append(b)

        count =0
        for i in range(test_cases): 
            for j in range (0,4):              
                if(a[i][j] >=-100 and a[i][j]<=100):
                    count+=1               
        for i in range(test_cases): 
                j=0
                if (count == (test_cases*4)):
                   compute_distance(a[i][j], a[i][j+1], a[i][j+2], a[i][j+3])
            