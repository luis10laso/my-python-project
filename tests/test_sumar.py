import sys
import os
sys.path.append(os.path.dirname(os.path.abspath("my_python_code.py")))

from src.my_python_code import sumar
def test_sumar():
 assert sumar(2, 3) == 5
 assert sumar(0, 0) == 0
 assert sumar(-1, 1) == 0