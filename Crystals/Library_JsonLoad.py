"""
SOURCE:
    http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python/6633651#6633651
DESCRIPTION:
    Loads a json into a python object
ARGS:
    CheckArguments
        Type:
            python boolean
        Description:
            if true, checks the arguments with conditions written in the function
            if false, ignores those conditions
    PrintExtra
        Type:
            python integer
        Description:
            if greater than 0, prints addional information about the function
            if 0, function is expected to print nothing to console
            Additional Notes:
                The greater the number, the more output the function will print
                Most functions only use 0 or 1, but some can print more depending on the number
    JsonString
        Type:
            <type 'NoneType'>
        Description:
    ForceAscii
        Type:
            <type 'NoneType'>
        Description:
    ForceUnicode
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import json
def Main(
    JsonString= None,
    ForceAscii= False,
    ForceUnicode= False,
    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None


    if ForceAscii is None:
        ForceAscii= False
    if ForceUnicode is None:
        ForceUnicode= False


    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)
    s = JsonString


    def byteify(input):
        if isinstance(input, dict):
            return {byteify(key): byteify(value)
                    for key, value in input.iteritems()}
        elif isinstance(input, list):
            return [byteify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input

    def deunicodify_hook(pairs):
        new_pairs = []
        for key, value in pairs:
            if isinstance(value, unicode):
                value = value.encode('utf-8')
            if isinstance(key, unicode):
                key = key.encode('utf-8')
            new_pairs.append((key, value))
        return dict(new_pairs)

    def _decode_list(data):
        rv = []
        for item in data:
            if isinstance(item, unicode):
                item = item.encode('utf-8')
            elif isinstance(item, list):
                item = _decode_list(item)
            elif isinstance(item, dict):
                item = _decode_dict(item)
            rv.append(item)
        return rv

    def _decode_dict(data):
        rv = {}
        for key, value in data.iteritems():
            if isinstance(key, unicode):
                key = key.encode('utf-8')
            if isinstance(value, unicode):
                value = value.encode('utf-8')
            elif isinstance(value, list):
                value = _decode_list(value)
            elif isinstance(value, dict):
                value = _decode_dict(value)
            rv[key] = value
        return rv

    if ForceAscii is False and ForceUnicode is False:
        ErrorMessage = 'Arg error: need either ForceAscii or ForceUnicode to not be `False`'
        raise Exception(ErrorMessage)
    elif ForceAscii is True and ForceUnicode is False:
        #do the ascii
        #print 'Forcing ascii'
        #obj = json.loads(s, object_hook=_decode_dict)
        obj = byteify(json.loads(s))
        #print 'obj', obj
        #obj = json.loads(s, object_hook=deunicodify_hook)
    elif ForceAscii is False and ForceUnicode is True:
        obj = json.loads(s)#by default the json loads method makes unicode things
    elif ForceAscii is True and ForceUnicode is True:
        ErrorMessage = 'Arg error: both ForceAscii ForceUnicode are not none- solution ambiguous'
        raise Exception(ErrorMessage)


    Result = obj
    return Result 
