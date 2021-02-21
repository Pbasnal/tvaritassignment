from ApiUtils.ApiResult import ApiResult
from SumEngine.SumOfNumbers import SumOfNumbers
from SumEngine.SumOutput import SumOutput

from flask import jsonify

## Handler methods are called from the API to process compute the result and handle
## result returned by the SumEngine. 
## They act as a layer of abstraction which hides the different actions which were 
## performed on different results of the SumEngine and return only the response to
## the api which should be returned to the client.
def ComputeSumOfInputNumbers(sumFinder, inputNumbers):
    result = sumFinder.AddNumbers(inputNumbers)

    if result.Status == SumOutput.StatusCode.Success:
        return ApiResult.Success(result.Result)

    elif result.Status == SumOutput.StatusCode.InputError: 
        return ApiResult.Failed(400, str({
                "ErrorMessage": result.ErrorMessage,
                "HowToUse": sumFinder.HowToUseTip()
            }))

    else:
        return ApiResult.Failed(400, result.ErrorMessage)