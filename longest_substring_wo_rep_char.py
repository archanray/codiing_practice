import numpy as np
import string 

def searchAround(s, i):
    length = 0
    palindrome = ""
    flag = 0
    if i == 0 or i == len(s)-1:
        length = 1
        palindrome = s[int(i)]
        return length, palindrome, flag
    for j in np.arange(0,i+0.5,0.5):
        base = int(np.ceil(i-j))
        top = int(np.floor(i+j))
        # print(base, top)
        if s[base] == s[top]:
            palindrome = s[base:top+1]
            length = len(palindrome)
        else:
            break
        if top == len(s)-1:
            flag = 1
            break
    return length, palindrome, flag

# LoLS:: length of longest subsequence O(1) space requirement
def centerLoLS(s):
    strLen = 0
    reqPal = ""
    flag = 0
    for i in np.arange(0,len(s)-0.5, 0.5):
        # print(s, i)
        length, maxpal, flag = searchAround(s,i)
        # print("algo output:", length, maxpal)
        if length >= strLen:
            # print("HERE", length, maxpal)
            strLen = length
            reqPal = maxpal
        if flag:
            return strLen, reqPal        
        # print("==========================================")
    return strLen, reqPal

# print(centerLoLS("babad"))
# print(centerLoLS("aab"))
# print(centerLoLS("trinitrophenylmethylnitramine"))
print(centerLoLS("trinityeeree"))
# print(centerLoLS("aacabdkacaa"))
# print(centerLoLS("hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
# print(centerLoLS("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"))
