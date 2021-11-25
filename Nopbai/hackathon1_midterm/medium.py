import re
def anagram_number(number):
    str1=str(number)
    reverse= str1[::-1]
    if reverse == str1 and re.match("^\d*$",str1): 
     return(True)
    return(False)

def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(s):
        #Bắt thằng IV, IX, XL.. trước
        if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
        else:
            num+=roman[s[i]]
            i+=1
    return(num)
    