import unittest
import sys
from speciallecture.CSVPrinter import CSVPrinter

# sys.path.append("../speciallecture")
class TestCSVPrinter(unittest.TestCase):

  def test_read1(self):
    printer = CSVPrinter('./tests/sample.csv')
    line = printer.read()
    self.assertEqual(2,len(line))

  def test_read2(self):
    printer = CSVPrinter('./tests/sample.csv')
    line = printer.read()
    self.assertEqual("aaa1",line[0][0])

  def test_read3(self):
    try:
      printer = CSVPrinter('./tests/Sample.csv')
      printer.read()
      unittest.TestCase.fail("This line should not be invoked")
    except Exception as e:
      print("Input file does not exist")
