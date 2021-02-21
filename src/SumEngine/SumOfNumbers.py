from SumEngine.SumOutput import SumOutput

class SumOfNumbers:

    ## Constructor - Takes number of integers to add and logger
    def __init__(self, numberOfArgumentsToAccept, logger):
        self.logger = logger
        self.NumberOfArgumentsToAccept = numberOfArgumentsToAccept

    def HowToUseTip(self):
        howToUse = "How to use - Provide 3 numbers which needs to be added. If any of the number belongs to the list [13, 14, 17, 18, 19] then that number will be treated as 0."

        return howToUse

    def ValidateNumberOfArguments(self, inputs):
        totalNumberOfArguments = len(inputs)

        # Number of arguments in the input should be equal to the 
        # number of integers set in the constructor
        if totalNumberOfArguments != self.NumberOfArgumentsToAccept:
            return SumOutput(SumOutput.StatusCode.InputError, 
                    f'Exactly {self.NumberOfArgumentsToAccept} numbers are required', 
                    0)
        
        return SumOutput(SumOutput.StatusCode.Success, '', 0)

    # Simple addition of 2 numbers.
    # This function has been created to test the addition function of the class.
    # Since all the addition happens with this code, testing this function will 
    # ensure that addition will happen properly.
    def Add2Numbers(self, numa, numb):
        return numa + numb

    # Function to check if a number is a teen or not.
    def IsTheNumberATeen(self, num):
        if num in [13, 14, 17, 18, 19]:
            return True
        return False

    # This method takes in the an object and converts it to an integer.
    # If the input object is not an integer, it'll return error.
    # If the number is a 'Teen' then it returns 0
    # Example input: 1   -> returns 1
    #                '1' -> returns 1
    #                'a' -> returns error
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

    # This function takes the array of input objects and computes their sum.
    # Example input: [1, 'a', '#$', '3'] -> returns error
    #              : [1, '2', '3'] -> returns 6
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
