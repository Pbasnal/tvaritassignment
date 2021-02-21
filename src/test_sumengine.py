import unittest
import random
import string
import logging

# Module to be tested
from SumEngine.SumOfNumbers import SumOfNumbers
from SumEngine.SumOutput import SumOutput

def NewSumEngine():
    logging.basicConfig(filename="console.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    return SumOfNumbers(3, logger)

class TestSum_AdditionOf2Numbers(unittest.TestCase):

    def test_Add2Numbers_HasCommutativeProperty(self):
        sumOf3 = NewSumEngine()

        numa = random.randint(0, 10000)
        numb = random.randint(0, 10000)

        self.assertEqual(sumOf3.Add2Numbers(numa, numb),
                         sumOf3.Add2Numbers(numb, numa))

    def test_Add2Numbers_HasIdentityProperty(self):
        sumOf3 = NewSumEngine()

        numa = random.randint(0, 10000)
        self.assertEqual(numa, sumOf3.Add2Numbers(numa, 0))

    def test_Add2Numbers_HasAssociativeProperty(self):
        sumOf3 = NewSumEngine()

        numa = random.randint(0, 10000)
        numb = random.randint(0, 10000)
        numc = random.randint(0, 10000)

        lhs = sumOf3.Add2Numbers(sumOf3.Add2Numbers(numa, numb), numc)
        rhs = sumOf3.Add2Numbers(numa, sumOf3.Add2Numbers(numb, numc))

        self.assertEqual(lhs, rhs)


class TestSum_NumberIsATeen(unittest.TestCase):

    def test_IsTheNumberATeen_IdentifiesTeenCorrectly(self):
        sumOf3 = NewSumEngine()

        teens = [13, 14, 17, 18, 19]

        for num in range(0, 10000):
            if num in teens:
                self.assertEqual(sumOf3.IsTheNumberATeen(num), True)
                continue

            self.assertEqual(sumOf3.IsTheNumberATeen(num), False)


class TestSum_AddNumbers(unittest.TestCase):

    def test_HasCommutativeProperty(self):
        sumOf3 = NewSumEngine()

        numa = str(random.randint(0, 10000))
        numb = str(random.randint(0, 10000))
        numc = str(random.randint(0, 10000))

        result = sumOf3.AddNumbers([numa, numb, numc])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)

        self.assertEqual(result.Result, sumOf3.AddNumbers(
            [numb, numa, numc]).Result)
        self.assertEqual(result.Result, sumOf3.AddNumbers(
            [numc, numa, numb]).Result)

    def test_AddNumbers_HasIdentityProperty_ForNumbersGreaterThan20(self):
        sumOf3 = NewSumEngine()

        numa = str(random.randint(20, 10000))
        numb = str(random.randint(20, 10000))

        result = sumOf3.AddNumbers([numa, numb, '0'])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)
        self.assertEqual(
            result.Result, sumOf3.Add2Numbers(int(numb), int(numa)))

        result = sumOf3.AddNumbers([numa, '0', '0'])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)
        self.assertEqual(result.Result, int(numa))

    def test_AddNumbers_HasIdentityProperty_ForNumbersLessThan13(self):
        sumOf3 = NewSumEngine()

        numa = str(random.randint(0, 13))
        numb = str(random.randint(0, 13))

        result = sumOf3.AddNumbers([numa, numb, '0'])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)
        self.assertEqual(
            result.Result, sumOf3.Add2Numbers(int(numb), int(numa)))

        result = sumOf3.AddNumbers([numa, '0', '0'])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)
        self.assertEqual(result.Result, int(numa))

    def test_AddNumbers_HasIdentityProperty_ForTeens(self):
        sumOf3 = NewSumEngine()
        teens = [13, 14, 17, 18, 19]

        numa = str(random.choice(teens))
        numb = str(random.randint(20, 10000))

        result = sumOf3.AddNumbers([numa, numb, '0'])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)
        self.assertEqual(result.Result, int(numb))

        result = sumOf3.AddNumbers([numa, '0', '0'])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)
        self.assertEqual(result.Result, 0)

    def test_AddNumbers_UsingNumbersInsteadOfStrings(self):
        sumOf3 = NewSumEngine()

        numa = random.randint(0, 13)
        numb = random.randint(0, 13)

        result = sumOf3.AddNumbers([numa, numb, '0'])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)
        self.assertEqual(result.Result, sumOf3.Add2Numbers(numb, numa))

        result = sumOf3.AddNumbers([numa, '0', '0'])
        self.assertEqual(result.Status, SumOutput.StatusCode.Success)
        self.assertEqual(result.Result, numa)

class TestSum_AddNumbers_Validations(unittest.TestCase):
    
    def test_AddNumbers_ShouldOnlyTake3Numbers(self):
        sumOf3 = NewSumEngine()

        result = sumOf3.AddNumbers([1, 2, 3, 4])
        self.assertEqual(result.Status, SumOutput.StatusCode.InputError)

        result = sumOf3.AddNumbers([1, 2])
        self.assertEqual(result.Status, SumOutput.StatusCode.InputError)

    def test_AddNumbers_ShouldFailIfCharacterIsPovided(self):
        sumOf3 = NewSumEngine()

        result = sumOf3.AddNumbers([1, 2, 'a'])
        self.assertEqual(result.Status, SumOutput.StatusCode.InputError)
        result = sumOf3.AddNumbers([1, 'basd', 'a'])
        self.assertEqual(result.Status, SumOutput.StatusCode.InputError)

if __name__ == '__main__':
    unittest.main()
