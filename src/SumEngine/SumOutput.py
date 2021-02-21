from enum import Enum

## This class is the object that helps in sharing results of various functions inside the SumOfNumbers.py class
## This class is also used to communicate result with any other class which uses SumOfNumbers.py functionality
class SumOutput:
    class StatusCode(Enum):
        Success = 0
        InputError = 1
        InternalException = 2

    def __init__(self, status : StatusCode, errorMessage : str, result : int):
        self.Status = status
        self.ErrorMessage = errorMessage
        self.Result = result