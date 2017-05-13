from unnecessary_math import multiply, add
 
def test_numbers_3_4():
    assert multiply(3,4) == 12 

def test_strings_a_3():
    assert multiply('a',3) == 'aaa' 

def test_numbers_1_2():
    assert add(1,2) == 3

def test_numbers_1_minus_1():
    assert add(1,-1) == 0

def test_numbers_1_1():
    assert add(1,1) == 2
