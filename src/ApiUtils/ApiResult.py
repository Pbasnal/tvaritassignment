## This class is the object that helps in sharing results of 
# various functions and classes used by the FlaskApi.
class ApiResult:
    
    def __init__(self, isSuccess, errorCode, returnObject):
        self.IsSuccess = isSuccess
        self.ErrorCode = errorCode
        self.returnObject = returnObject
    
    @classmethod
    def Success(cls, returnObject):
        return ApiResult(True, 0, returnObject)
    
    @classmethod
    def Failed(cls, errorCode, returnObject):
        return ApiResult(False, errorCode, returnObject)

    def ToJson(self):
        return f"IsSuccess: {self.IsSuccess} ErrorCode: {self.ErrorCode} obj: {self.returnObject}"