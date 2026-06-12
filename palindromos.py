def isPalindrome(str):
    i = 0
    j = len(str)-1

    clean_str = str.lower()

    while i < j:
        if clean_str[i] != clean_str[j]:
            return False

        i += 1
        j -= 1

    return True

if __name__ == '__main__':
    inputStr = input()
    print(isPalindrome(inputStr))