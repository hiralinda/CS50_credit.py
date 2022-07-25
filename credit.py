sum_odd_list = []
while True:
    card_number = input("Number: ")
    numbers = [int(d) for d in card_number]
    # print(numbers)
    odd_num = numbers[::2]
    # print(odd_num)
    even_num = numbers[1::2]
    # print(even_num)
    for i in range (0, len(odd_num)):
        odd_num[i] = int(odd_num[i])
    for i in range (0, len(even_num)):
        even_num[i] = int(even_num[i])

    odd_num = [i * 2 for i in odd_num]
    # print(odd_num)
    for i in odd_num:
        sum_odd = 0
        for digit in str(i):
            sum_odd += int(digit)
        sum_odd_list.append(sum_odd)
    # print(sum_odd_list)
    # print(sum(sum_odd_list))
    resultado = (sum(sum_odd_list) + sum (even_num))
    #print(resultado)
    if (resultado % 10) != 0:
        print("INVALID")

    elif numbers[0] == 3:
        if numbers[1] == 4 or 7:
            print("AMEX")

    elif numbers[0] == 5:
        if numbers[1] == 1 or 2 or 3 or 4 or 5:
            print("MASTERCARD")

    elif numbers[0] == 4:
        print("VISA")

    quit()
