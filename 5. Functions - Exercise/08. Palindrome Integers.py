number_list_str = input().split(",")


def palindrome(num_list):
    for i in num_list:
        result = int(i) == int(i[::-1])
        print(result)


palindrome(number_list_str)