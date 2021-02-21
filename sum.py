import sys
import logging
from enum import Enum

class SumOutput:
    class StatusCode(Enum):
        Success = 0
        InputError = 1
        InternalException = 2

    def __init__(self, status : StatusCode, errorMessage : str, result : int):
        self.Status = status
        self.ErrorMessage = errorMessage
        self.Result = result

class SumOfNumbers:
    def __init__(self, numberOfArgumentsToAccept, logger = None):

        if logger == None:
            logging.basicConfig(filename="sumofnumbers.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')

            self.logger = logging.getLogger()
            self.logger.setLevel(logging.DEBUG)
        else: 
            self.logger = logger
        self.NumberOfArgumentsToAccept = numberOfArgumentsToAccept

    def HowToUseTip(self):
        howToUse = """
        =============================================================
        * How to use
        * Provide 3 numbers which needs to be added. If any of the  *
        * number belongs to the list [13, 14, 17, 18, 19] then that *
        * number will be treated as 0.                              *
        =============================================================
        """

        return howToUse

    def ValidateNumberOfArguments(self, inputs):
        # argv[0] is the name of the script
        totalNumberOfArguments = len(inputs)
        if totalNumberOfArguments != self.NumberOfArgumentsToAccept:
            return SumOutput(SumOutput.StatusCode.InputError, 
                    f'Exactly {self.NumberOfArgumentsToAccept} numbers are required', 
                    0)
        
        return SumOutput(SumOutput.StatusCode.Success, '', 0)

    def Add2Numbers(self, numa, numb):
        return numa + numb

    def IsTheNumberATeen(self, num):
        if num in [13, 14, 17, 18, 19]:
            return True
        return False

    def ConvertArgToInputNumber(self, arg):
        try:
            convertedNum = int(arg)
            if self.IsTheNumberATeen(convertedNum):
                convertedNum = 0
                
            return SumOutput(SumOutput.StatusCode.Success, '', convertedNum)

        except:
            self.logger.debug(f"Input value {arg} is not an intger")            
            return SumOutput(SumOutput.StatusCode.InputError, 
                            f'All arguments should be numbers', 
                            0)

    def AddNumbers(self, inputs):
        try:
            self.logger.debug("Input values " + str(inputs))
            validationResult = self.ValidateNumberOfArguments(inputs)
            if validationResult.Status != SumOutput.StatusCode.Success:
                return validationResult    
        
            sum = 0
            for i in range(self.NumberOfArgumentsToAccept):
                conversionOutput = self.ConvertArgToInputNumber(inputs[i])
                if conversionOutput.Status != SumOutput.StatusCode.Success:
                    return conversionOutput

                self.logger.debug(f"Adding {conversionOutput.Result} to {sum}")
                sum = self.Add2Numbers(sum, conversionOutput.Result)

        except Exception as err:
            self.logger.exception("Internal exception")
            return SumOutput(SumOutput.StatusCode.InternalException, 
                            f'An internal error has occured.', 
                            0)

        self.logger.debug(f"Result {sum}")
        return SumOutput(SumOutput.StatusCode.Success, '', sum)

def main():
    sumOfNumbers = SumOfNumbers(3)
    answer = sumOfNumbers.AddNumbers(sys.argv[1:])

    if answer.Status == SumOutput.StatusCode.Success:
        print(answer)
    elif answer.Status == SumOutput.StatusCode.InputError:
        print(sumOfNumbers.HowToUseTip())
    else:
        print(answer.ErrorMessage)


if __name__ == "__main__":
    main()
