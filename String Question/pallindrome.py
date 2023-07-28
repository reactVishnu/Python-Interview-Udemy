
def pallindrome(stringular):
    n = ''.join(filter(str.isalnum, stringular.lower()))
    k = n == n[::-1]
    return k


s = 'A man, a plan, a canal: Panama'
print(pallindrome(s))
