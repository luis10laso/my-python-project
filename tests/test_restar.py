import sys
import os
sys.path.append(os.path.dirname(os.path.abspath("my_python_code.py")))

from src.my_python_code import restar
def test_restar():
 assert restar(5, 2) == 3
 assert restar(0, 0) == 0
 assert restar(-1, 1) == -2