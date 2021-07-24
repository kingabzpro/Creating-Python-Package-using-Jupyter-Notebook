
import unittest
from distributions.binomial import Binomial

class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('data/binary.txt')

    def test_initialization(self):
        self.assertEqual(self.binomial.p, 0.4, 'p value incorrect')
        self.assertEqual(self.binomial.n, 20, 'n value incorrect')

    def test_readdata(self):
        self.assertEqual(self.binomial.data,\
         [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1], 'data not read in correctly')
    
    def test_calculatemean(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 8)
    
    def test_calculatestdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev,2), 2.19)
        
    def test_replace_stats_with_data(self):
        p, n = self.binomial.replace_stats_with_data()
        self.assertEqual(round(p,3), 0.471)
        self.assertEqual(n, 17)
        
    def test_pdf(self):
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.01235)
    
        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.06923)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00963)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two
        
        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)
        
    
if __name__ == '__main__':
    unittest.main()
