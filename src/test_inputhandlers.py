from ApiUtils.InputHandlers import BasicInputValidationAndParsing

import logging
import unittest

logging.basicConfig(filename="console.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TestSum_AdditionOf2Numbers(unittest.TestCase):
    
    def test_BasicValidation_SuccessScenarios(self):

        inputs = [
            '{[1, 2, 3]}',
            'b{[1, "2", 3]}',
            'b{[1, 13, "3"]}',
            'b{["1", "2", 15]}',
            'b{["1", "2", abc]}',
            'b{["1", "2", 15,,',
            'b[1, 2]}',
        ]

        for input in inputs: 
            basicValidationResult = BasicInputValidationAndParsing(input, logger)
            self.assertEqual(basicValidationResult.IsSuccess, True)
            self.assertIsInstance(basicValidationResult.returnObject, list, input) 

    def test_BasicValidation_FailureScenarios(self):
    
        inputs = [
            'b[1, 2]'
        ]

        for input in inputs: 
            basicValidationResult = BasicInputValidationAndParsing(input, logger)
            self.assertEqual(basicValidationResult.IsSuccess, False, input)

if __name__ == '__main__':
    unittest.main()