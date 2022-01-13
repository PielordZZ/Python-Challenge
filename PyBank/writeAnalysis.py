from os.path import exists

def writeNewFile(filePath,filetext):
    if not exists(filePath):
        f = open(filePath, 'w')
        f.write(filetext)
        f.close()
    else:
        userInput= input('file exists overwrite with new data? (y/n)')
        if userInput == 'y':
            f = open(filePath, 'w')
            f.write(filetext)
            f.close()


