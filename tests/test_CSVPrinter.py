import unittest
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
  def test_read(self):
    printer = 'sample.csv'
    l = printer.read()
    self.assertEqual(2,len(l))

  def test_read1(self):
    printer = CSVPrinter('sample.csv')
    line = printer.read()
    print(line)
    self.assertEqual(2,len(line))

  def test_read2(self):
    printer = CSVPrinter('sample.csv')
    line = printer.read()
    print(line)
    self.assertEqual("sample.csv",len[0][0])

  def test_read3(self):
    try:
      printer = CSVPrinter('sample.csv')
      printer.read()
      unittest.TestCase.fail("This line should not be invoked")
    except Exception as e:
      self.assertEqual("Input file does not exist")
