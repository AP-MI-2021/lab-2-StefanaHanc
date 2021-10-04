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
def get_n_choose(n,k):
    '''
    Calculează combinări de n luate câte k
    :param n:
    :param k:
    :return: Se returneaza calculul combinarilor n luate cate k
    '''
    x=1
    for i in range(n-k+1,n+1):
        x=x*i
    y=1
    for i in range(2,k+1):
        y*=i
    return x/y
def test_get_n_choose():
    assert get_n_choose(4,1)==4
    assert get_n_choose(4,4)==1
    assert get_n_choose(5,0)==1
    assert get_n_choose(4,3)==4
test_get_n_choose()
def main():
    print("Realizarea meniului pentu utilizator")
sholdRun=True
while sholdRun:
    print("MENIU")
    print("1,Determinati daca un nr este palindrom ")
    print("2,Determinati daca un nr este superprim ")
    print("3,Calculează combinări de n luate câte k ")
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
    elif optiune == "3":
        c = int(input("Dati nr n "))
        v= int(input("Dati nr k "))
        print("Combinări de n luate câte k este ")
        print(int (get_n_choose(c,v)))
    elif optiune == "x":
        sholdRun=False
    else:
        print("Optiune Gresita! Reincercati ")
if _name_=="_main_":
    main()