from SumEngine.SumOfNumbers import SumOfNumbers
from SumEngine.SumOutput import SumOutput

import sys
import logging

def SetupLogger():
    logging.basicConfig(filename="console.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    return logger

def main():
    logger = SetupLogger()

    sumOfNumbers = SumOfNumbers(3, logger)
    answer = sumOfNumbers.AddNumbers(sys.argv[1:])

    if answer.Status == SumOutput.StatusCode.Success:
        print(answer.Result)
        return
    
    print("Error Message -", answer.ErrorMessage)
    print(sumOfNumbers.HowToUseTip())


if __name__ == "__main__":
    main()