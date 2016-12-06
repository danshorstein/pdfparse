import ftfy


def read_text_file(filename):
    '''opens the text file and fixes any encoding issues'''
    filein = open(filename, 'br')
    filein = ftfy.fix_file(filein)
    data = [row.strip('\n') for row in filein]
    return data


def save_to_csv(stuff): #TODO - add a save to csv option/????
    '''saves the file to csv'''
    pass
