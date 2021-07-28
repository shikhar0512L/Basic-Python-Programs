from time import time



def func1(a, b):

    #Rohan Das

    return a + b


def func2(a, b):

    #By CodeWithHarry

    num1 = a

    num2 = b

    if(a>b and a!=3):

        pass

    sum([4,3])

    return a+b


jls_extract_var = '__main__'
if _name_ == jls_extract_var:
    init = time()

    for i in range(0, 100000):

        func1(3,5)



    for i in range(0, 100000):

        func2(3,5)

    print("Overall Time: ", time() - init) 