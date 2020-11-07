# Main function
if __name__ == '__main__':
    
    test_cases = int(input())
    n = []
    a=[]
    i=0
    for T in range(test_cases):
        elm = int(input())
        n.append(elm)
    for T in range(test_cases):        
        for i in range(0,n[T]):
            if i==0:
                a.append(i+3)
            elif i%2 == 0:
                a.append(i*2)
            else:
                a.append(i*i)
        for i in a: 
            print(i, end = ' ')
        a.clear()
        print(" ")
   
