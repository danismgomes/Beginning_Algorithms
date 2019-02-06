# isPalindrome
# It verifies if a integer number is Palindrome or not

answer = int(input("Type a integer number: "))

answer_list = []

while answer != 0:  # putting every digit of the number in a list
    answer_list.append(answer % 10)  # get the first digit
    answer = answer // 10  # remove the first digit


def is_palindrome(a_list):

    for i in range(0, len(a_list)//2):

        if a_list[i] != a_list[len(a_list)-i-1]:  # verifying if some element of the list is not palindrome
            return "It is not Palindrome."

    return "It is Palindrome."


print(is_palindrome(answer_list))
