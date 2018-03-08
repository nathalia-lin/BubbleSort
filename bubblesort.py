def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-1):
            a = lst[j]
            b = lst[j+1]
            if a > b:
                lst[j] = b
                lst[j+1] = a
                #lst[j],lst[j+1] = lst[j+1],lst[j]
            
    return lst

print(bubble_sort([1,3,4,2,5,6,3,4]))

def bubble_sort_optimize(lst):
# why is this more optimized? 

    n = len(lst)
    swap = 0

    while n != 0:
        for j in range(n-1):
            a = lst[j]
            b = lst[j+1]
            if a > b:
                lst[j] = b
                lst[j+1] = a
                swap += 1
                print (swap)
        if swap == 0:
            break
          
    return lst
print(bubble_sort_optimize([1,2,3,4,5,6]))


    
        
