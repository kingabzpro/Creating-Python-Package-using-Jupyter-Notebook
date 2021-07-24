
import unittest
from distributions.gaussian import Gaussian

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(35, 6)
        self.gaussian.read_data_file('data/random.txt')

    def test_initialization(self): 
        self.assertEqual(self.gaussian.mean, 35, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 6, 'incorrect standard deviation')

    def test_readdata(self):
        self.assertEqual(self.gaussian.data,\
         [10, 23, 45, 12, 23, 45, 67, 100, 300, 250, 45, 68, 29, 59, 239, 934, 12, 321, 12, 32, 1], 'data not read in correctly')

    def test_meancalculation(self):
        self.assertEqual(self.gaussian.calculate_mean(),\
         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 210.77, 'sample standard deviation incorrect')
        self.assertEqual(round(self.gaussian.calculate_stdev(0), 2), 205.69, 'population standard deviation incorrect')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.01658,\
         'pdf function does not give expected result') 
        self.gaussian.calculate_mean()
        self.gaussian.calculate_stdev()
        self.assertEqual(round(self.gaussian.pdf(75), 5), 0.00184,\
        'pdf function after calculating mean and stdev does not give expected result')      

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two
        
        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)

if __name__ == '__main__':
    unittest.main()
