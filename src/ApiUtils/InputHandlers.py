from ApiUtils.ApiResult import ApiResult

## This method helps in doing basic validation of the FlaskApi input
## After validation it also converts the input into an array 
## which can be then passed to the SumEngine
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

## Helper method to convert the string of numbers in an array of strings
## Example input: 'b{[1, 2, 3]}' -> returns: ['1', '2', '3']
def ConvertInputToArray(input):
    # Taking only 4 to -3 because the input will contain 'b{[' at the begining
    #  and ']}' at the end
    input = str(input)[4: -3]
    
    return input.split(',')    