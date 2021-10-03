def is_palindrom(n):
    '''
    Determină dacă un număr dat este palindrom
    :param n:Numarul verificat
    :return:
    bool:True in caz ca numarul este palindrom si False in caz ca nu este
    '''
    if n<10:
        return True
    palindrom=0
    uc=n
    while uc!=0:
        palindrom=uc%10+palindrom*10
        uc=uc//10
    if palindrom==n:
        return True
    return False
def test_is_palindom():
    assert is_palindrom(121) is True
    assert is_palindrom(123) is False
    assert is_palindrom(1) is True
test_is_palindom()
def is_superprime(n):
    '''
    Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.
    :param n: Numarul verificat
    :return:
    bool: True daca toate numerele sunt prime, False in caz contrar
    '''
    copie=n
    if n<2:
        return False
    if copie<10:
        for i in range (2,copie//2+1):
            if copie%i==0:
                return False
        return True
    p=0
    while copie!=0:
        copie=copie//10
        p=p+1
    copie=n
    while p!=0:
        for i in range (2,copie//2+1):
            if copie%i==0:
                return False
        copie=copie//10
        p=p-1
    return True
def test_is_superprime():
   assert is_superprime(237) is False
   assert is_superprime(1) is False
   assert is_superprime(233) is True
   assert is_superprime(8) is False
test_is_superprime()
"Realizarea meniului pentu utilizator"
sholdRun=True
while sholdRun:
    print("MENIU")
    print("1,Determinati daca un nr este palindrom ")
    print("2,Determinati daca un nr este superprim ")
    print("x.IESIRE")
    print("ALEGE O OPTIUNE! ")
    optiune=input()
    if optiune=="1":
        a=int (input("Dati nr pe care doriti sa verificati ca este palindrom "))
        if is_palindrom(a)==True:
            print("Da este palindrom ")
        else:
           print("Nu este palindrom ")
    elif optiune=="2":
        b=int (input("Dati nr pe care doriti sa verificati ca este superprim "))
        if is_superprime(b) == True:
            print("Da este numar superprim ")
        else:
           print("Nu este numar superprim ")
    elif optiune == "x":
        sholdRun=False
    else:
        print("Optiune Gresita! Reincercati ")