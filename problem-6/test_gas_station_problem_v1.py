"""
The MIT License

Copyright 2025 Juliano Maciel.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import unittest
from gas_station_problem_v1 import gas_station


class TestGasStation(unittest.TestCase):
    def test_gas_station_found(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        self.assertEqual(gas_station(gas, cost), 3)  # add assertion here

    def test_gas_station_not_found(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        self.assertEqual(gas_station(gas, cost), -1)

    def test_empty_list(self):
        gas = []
        cost = []
        self.assertEqual(gas_station(gas, cost), -1)

    def test_single_station(self):
        gas = [5]
        cost = [4]
        self.assertEqual(gas_station(gas, cost), 0)

    def test_gas_equals_total_cost(self):
        gas = [1, 2, 3]
        cost = [2, 3, 1]
        self.assertEqual(gas_station(gas, cost), 2)

    def test_total_gas_less_than_total_cost(self):
        gas = [1, 2, 3]
        cost = [3, 4, 3]
        self.assertEqual(gas_station(gas, cost), -1)


if __name__ == '__main__':
    unittest.main()
