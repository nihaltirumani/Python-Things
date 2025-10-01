import random

def sort(li:list): 
    for i in range(1, len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li
                
list1 = [random.randint(-100, 100) for i in range(100)]
list2 = sort(list1)

print(list2)