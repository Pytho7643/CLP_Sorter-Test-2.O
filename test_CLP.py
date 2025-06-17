import unittest
import tempfile
import sys
import os
from CLP_sorter import main

class TestCLP (unittest.TestCase):
    def test_sorter(self):
        with tempfile.NamedTemporaryFile(mode="w+", delete = False) as input_file:        
             input_file.write("3\n1\n2\n")
             input_file_name = input_file.name
             input_file.flush()

        with tempfile.NamedTemporaryFile(mode="w+", delete = False) as output_file:
             output_file_name = output_file.name

        try:
             sys.argv = ["CLP_sorter.py", "-r", "-o", output_file_name, input_file_name]
             main()  

             with open(output_file_name, "r") as f:
                output_lines = f.read().splitlines()
                self.assertEqual(output_lines, ["3", "2", "1"])
        finally:
                os.remove(input_file_name)
                os.remove(output_file_name) 
if __name__ == "__main__":
 unittest.main()