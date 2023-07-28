def is_anagram(str1, str2):
    for i in str1:
        if i not in str2:
            return False
    return True


s1 = "listen"
s2 = "silent"

print(is_anagram(s1, s2))