from contextlib import nullcontext
import math as m



def rsa(plainText,n,e):
    print("plainText")
    print(n, e)
    CipherText= []
    codechart = "abcdefghijklmnopqrstuvwxyz"
    chaine = ""

    for key in codechart:
        for i in plainText:
            if key == i:
                char = codechart.index(key) 
                c = int(m.pow(char,e) % n)
                CipherText.append(c)
                truechaine = chaine.join([str(item) for item in CipherText])            
                
    return truechaine


      

# def dech_rsa(cryptedText,d,n):
#     plainText = ""
#     codechart = "abcdefghijklmnopqrstuvwxyz"
#     char = nullcontext
#     for i in cryptedText:
#         char = m.pow(i,d) % n
#         for i in range (len(codechart)):
#             if i == char:
#                 plainText == codechart[i]
#     return plainText

# message =("Two one Nine Two")
# print("encrypt message is :",rsa(message,3,5))

