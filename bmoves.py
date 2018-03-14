import os,sys,getpass

listdir = os.listdir()

if len(sys.argv) == 3:
    extArg = sys.argv[1]
    dirArg = sys.argv[2]

else:
    print("""

options:

    '1' = .png
    '2' = .exe
    '3' = .docx'
    '4' = .mp4'
    '5' = .jpg'
    '6' = .py'
    '7' = .txt'
    '8' = .pdf'
    '9' = .url'

    Make sure to include a '\\' behind the specified directory

example:
    bmoves.py <option> <directory>


    """)
    sys.exit()


def main():

    #Feel free to add more extensions to the option dictionary
    extOptions = {
        '1':'.png',
        '2':'.exe',
        '3':'.docx',
        '4':'.mp4',
        '5':'.jpg',
        '6':'.py',
        '7':'.txt',
        '8':'.pdf',
        '9':'.url'

    }

    for bestand in listdir:
        filename, file_extension = os.path.splitext('{}'.format(bestand))
        a = sys.path[0]
        tempPath = '{dir}{file}{ext}'.format(dir=dirArg,file=filename,ext=extOptions[extArg])

        #png
        if file_extension.lower() == extOptions[extArg]:
            os.rename(filename+extOptions[extArg], tempPath )
            print("File {a} moved to {b}".format(a=filename+extOptions[extArg],b=tempPath))
