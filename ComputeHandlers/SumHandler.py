from ApiUtils.ApiResult import ApiResult
from sum import SumOfNumbers, SumOutput

from flask import jsonify

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