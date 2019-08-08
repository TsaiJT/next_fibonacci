def nextFibonacci(num_list):
    """Show the next Fibonacci number for the element in the list."""
    """ex. input => [1, 22, 9], output => [2, 34, 13]"""

    # Initial the result list to store the next permutaion num.
    result_list = [0] * len(num_list)

    # Create a fibonacci list.
    max_num = max(num_list)
    fib_list = creatFibList(max_num)

    for index, item in enumerate(num_list):    
    # Find the fib number which is great than the item comparing to the element in fib_list.
        for fib_num in fib_list:
            if item < fib_num:
                result_list[index] = fib_num
                break
    return result_list

def creatFibList(max_num):
    """Create a fibonacci list which the last item is greater than max_num"""
    fib_list = [0, 1, 1]

    while fib_list[len(fib_list)-1] <= max_num:
        fib_list.append(fib_list[len(fib_list)-1]+fib_list[len(fib_list)-2])

    return fib_list

def main():
    result = nextFibonacci([1, 22, 9])
    print(result)

if __name__ == '__main__':
    main()