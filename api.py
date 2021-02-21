from flask import Flask, request, jsonify, abort
import json
import logging
from sum import SumOfNumbers, SumOutput

app = Flask(__name__)

logging.basicConfig(filename="api.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/sum', methods=['PUT'])
def summer():
    # try:
    input = str(request.data)
    logger.debug("Input values " + input)
    sumFinder = SumOfNumbers(3)

    if len(input) <= 7:
        abort(400, jsonify({
                    "ErrorMessage": "Input is invalid ",
                    "HowToUse": sumFinder.HowToUseTip()
                }))

    inputNumbers = ConvertInputToArray(input)

    for num in inputNumbers:
        logger.debug("num: " + str(num))

    result = sumFinder.AddNumbers(inputNumbers)

    if result.Status == SumOutput.StatusCode.Success:
        return jsonify(result.Result)
    elif result.Status == SumOutput.StatusCode.InputError: 
        abort(400, str({
                "ErrorMessage": result.ErrorMessage,
                "HowToUse": sumFinder.HowToUseTip()
            }))
    else:
        abort(400, result.ErrorMessage)

    # except Exception as ex:
    #     logger.exception("Exception ")
    
    # abort(500, "Failed to compute the result")

def ConvertInputToArray(input):

    input = str(input)[4: -3]
    return input.split(',')    

if __name__ == '__main__':
   app.run(host='0.0.0.0')
