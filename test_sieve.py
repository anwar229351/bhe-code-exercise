import unittest
from sieve import nth_prime

class TestSieve(unittest.TestCase):

    def test_0th_prime(self):
        self.assertEqual(nth_prime(0), 2)
    
    def test_19th_prime(self):
        self.assertEqual(nth_prime(19), 71)
    
    def test_99th_prime(self):
        self.assertEqual(nth_prime(99), 541)
    
    def test_10000000th_prime(self):
        self.assertEqual(nth_prime(10000000), 179424691)
    
    def test_additional_primes(self):
        self.assertEqual(nth_prime(1), 3)
        self.assertEqual(nth_prime(2), 5)
        self.assertEqual(nth_prime(3), 7)
        self.assertEqual(nth_prime(4), 11)
        self.assertEqual(nth_prime(5), 13)
        self.assertEqual(nth_prime(6), 17)

if __name__ == '__main__':
    unittest.main()