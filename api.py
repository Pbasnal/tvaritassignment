from sum import SumOfNumbers
from Common.LoggingSetup import SetupLogger
from ApiUtils.InputHandlers import BasicInputValidationAndParsing
from ComputeHandlers.SumHandler import ComputeSumOfInputNumbers

from flask import Flask, request, jsonify, abort
import json


app = Flask(__name__)
logger = None

@app.route('/sum', methods=['PUT'])
def SumOf3Numbers():
    try:
        sumFinder = SumOfNumbers(3)
        basicValidationResult = BasicInputValidationAndParsing(request.data, logger)
        
        if basicValidationResult.IsSuccess == False:
            abort(basicValidationResult.ErrorCode, basicValidationResult.returnObject)
        
        result = ComputeSumOfInputNumbers(sumFinder, basicValidationResult.returnObject)

        logger.debug(result.ToJson())
        if result.IsSuccess:
            return jsonify(result.returnObject)
        
        else:
            abort(result.ErrorCode, result.returnObject)

    except Exception as ex:
        logger.exception("Exception")
        raise


if __name__ == '__main__':
    logger = SetupLogger()
    app.run(host='0.0.0.0', debug=True)

