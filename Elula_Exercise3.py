def print_diamond(n):
    #Ensure the n is an odd number
    if n % 2 == 0:
        print("Error: Please enter an odd number.")
        return
    
    #Calculate the midpoint of  diamond
    mid = n // 2

    #Top half of the diamond (including the middle row)
    for i in range(mid + 1):
        print(' ' * (mid - i) + '*' * (2 * i + 1))

    #Bottom half of the diamond
    for i in range(mid -1, -1, -1):
        print(' ' * (mid - i) + '*' * (2 * i + 1))

n = int(input("Enter an odd integer: "))
print_diamond(n)
