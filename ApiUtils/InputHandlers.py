from ApiUtils.ApiResult import ApiResult

def BasicInputValidationAndParsing(rawInput, logger):
    input = str(rawInput)
    logger.debug("Input values " + input)

    if len(input) <= 7:
        return ApiResult.Failed(400, str({
                "ErrorMessage": "Input not fomatted properly",
                "HowToUse": "Provide exactly 3 numbers in the format '{[1, 2, 3]}'"
            }))

    inputNumbers = ConvertInputToArray(input)

    return ApiResult.Success(inputNumbers)

def ConvertInputToArray(input):
    input = str(input)[4: -3]
    return input.split(',')    