import random, sys, string, secrets
print('=================================================')
print("=             GePass 1-0 (by nikpro)            =")
print('=================================================')
print("HELLO! It's a program that generates password")
print('type length of password')
a=int(input()) #value of characters
if a==0 :
    print ('good joke, BYE :))))))')
    sys.exit()
print('Choose level of security and type number of level')
print('1---light (only numbers) :::::::: 2---Hard(numbers+letters) :::::::: 3---MEGA(punctuation + numbers + letters)')
l=int(input())
if l<=0:
    print('good joke, BYE :))))))')
    sys.exit()
#-----------------------level 1-------------------------------
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
if l==1:
    i=0
    while i<a:
        print(random.choice(list1), end="")
        i+=1
#---------------------------------level 2---------------------
if l==2 :
    def generate_alphanum_crypt_string(a):
        letters_and_digits = string.ascii_letters + string.digits
        crypt_rand_string = ''.join(secrets.choice(letters_and_digits) for i in range(a))
        print("Your password is:", crypt_rand_string)
    generate_alphanum_crypt_string(a)
#---------------------level 3---------------
if l==3:
    d=0
    while d<a:
        print(secrets.choice(string.printable), end="")
        d+=1
