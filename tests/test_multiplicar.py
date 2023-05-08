from my_python_code import multiplicar
def test_multiplicar():
 assert multiplicar(2, 3) == 6
 assert multiplicar(0, 0) == 0
 assert multiplicar(-1, 1) == -1