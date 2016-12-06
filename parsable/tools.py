'''turns string numbers into real numbers'''

def numberify(str_number, error=None):
    '''
    Method to turn a number-like string into a number
    Use error to return an error value other than None
    '''

    try:
        numb = round(float(str_number.replace(',', '')
                           .replace('(', '-').replace(')', '')
                           .replace('$', '')), 2)

    except:
        numb = error

    return numb
