import unittest
import sys
import os
from CLP_sorter import main

class TestCLP (unittest.TestCase):
    def test_sorter(self):
        with open("test_input.txt", "w") as f:
             f.write("3\n1\n2\n")

        try:
             sys.argv = ["CLP_sorter.py", "-r", "-o", "test_output.txt", "test_input.txt"]
             main()  

             with open("test_output.txt", "r") as f:
                  output_lines = f.read().splitlines()
                  self.assertEqual(output_lines, ["3", "2", "1"])

        finally:
             os.remove("test_input.txt")
             os.remove("test_output.txt")
 
if __name__ == "__main__":
 unittest.main()