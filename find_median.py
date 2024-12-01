import math

def find_median(arr: list[int]) -> int:
    arr.sort()
    length = len(arr)
    middle_index = math.floor(length/2)
    median = 0
    if length % 2 == 0: # list has even number
        median = (arr[middle_index-1] + arr[middle_index])/2
    else:
        median = arr[middle_index]
    return median

if __name__=="__main__":
    numbers = input("Enter comma seperated numbers as input: ")
    num_list = [int(num) for num in numbers.split(",")]
    
    median = find_median(num_list)
    print(f"The median of the {num_list} is {median}")  
