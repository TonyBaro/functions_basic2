def countdown(num):
    while num>0:
        print(num)
        num=num-1

countdown(5)

def print_and_return(num_arr):
    print(num_arr[0])
    return num_arr[1]

print(print_and_return([4,5]))

def first_plus_length(num_arr):
    return num_arr[0]+len(num_arr)

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(num_arr):
    new_arr = []
    for x in num_arr:
        if x > num_arr[1]:
            new_arr.append(x)
    print(len(new_arr))
    return new_arr

print(values_greater_than_second([5,2,3,2,1,4]))

def length_and_value(num1,num2):
    new_arr=[]
    for x in range(num1):
        new_arr.append(num2)
    return new_arr

print(length_and_value(4,7))
print(length_and_value(6,2))




