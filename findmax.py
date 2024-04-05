s = list(map(int, input().split(" ")))
num = len(s) 

def find_max_iterative(s, num):
    max = s[0]  
    for i in range(1, num):  
        if s[i] > max:  
            max = s[i]  
    return max  

def find_max_recursive(s, num) :
    if num == 1 :
        return s[0]
    max = find_max_recursive(s, num-1)
    if max < s[num-1] :
        return s[num-1]
    else :
        return max