


def strStr(haystack, needle):
    if not needle:
        return 0

    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1


print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))

print ('foo'bar')