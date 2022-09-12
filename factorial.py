t=0
globals()
def factorial():
    z = 1
    i = 1
    j = int(input("enter a number that you want to factorize: "))
    while i < (j + 1):
        z = z * i
        i = i + 1
    print(z)
def richard(ans):
    ans=(input("do you want to do another one ? (Y/N)")).upper()
    return ans
factorial()
richard()
while t<1000:
    if ans == "Y":
        factorial()
    if ans == "N"
        exit()
    else:
        richard()
