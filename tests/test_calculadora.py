from Calculadora import somar

def testSomar2Mais3():
    assert somar(2,3) == 5

def testSomar2Mais8():
    assert somar(2,8) == 10

from Calculadora import multiplicar

def testMultiplicar2Mais3():
    assert multiplicar(2,3) == 6

def testMultiplicar2Mais8():
    assert multiplicar(2,8) == 16

    from Calculadora import subtrair

def testSubtrair5Menos3():
    assert subtrair(5,3) == 2

def testSubtrair10Menos4():
    assert subtrair(10,4) == 6

    from Calculadora import dividir

def testDividir10Por2():
    assert dividir(10,2) == 5

def testDividir10Por0():
    try:
        dividir(10,0)
        assert False, "Deveria lançar uma exceção de divisão por zero"
    except ZeroDivisionError:
        assert True