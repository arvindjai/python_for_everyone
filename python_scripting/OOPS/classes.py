class MySampleClass:
    __myCode = ''
    def get_myCode(self):
        return self.__myCode
    
    def set_myCode(self,inValve):
        self.__myCode = inValve
    
    code = property(get_myCode,set_myCode)

    def reverseCode(self):
        return self.__myCode[::-1]
    
    def appendCode(self,inSuffix):
        self.__myCode = self.__myCode + inSuffix
        #  No return value