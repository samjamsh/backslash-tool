def write_file(filename,data):
    try:
        with open(filename,'w') as file:
            file.write(data)

    except Exception as err:
        sys.exit(err)

def byte(filename):
    try:
        with open(filename,"rb") as file:
            return file.read()

    except Exception as err:
        sys.exit(err)

def parameters():
    try:
        if len(sys.argv) > 2 or len(sys.argv) == 1:
            sys.exit("arguments error: try passing a parameter as argument")

        else:
            if sys.argv[1] == "-ff" or sys.argv[1] == "--file-to-file":
                filename = input("filename: ") # file to convert
                target_file = input("destination file: ")
                file_bytes = byte(filename)
                return (file_bytes,target_file), 'ff'

            elif sys.argv[1] == "-ft" or sys.argv[1] == "--file-to-text":
                filename = input("filename: ") # file to convert
                file_bytes = byte(filename)
                return file_bytes, 'ft'

            elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
                help_message = f"""Backslashes Conversor to On and Off  1.0 ../10/2022\nThis tool enables and disables backslashes into a file\nyou can turn on/enable backslashes into all the file content/data or into all text content\n\nParameters Usage:\n   -ft or --file-to-text: file to text (from file to text) \n   -ff or --file-to-file: file to file (from file to file) \n   -h or --help: shows this message\n\nProgram identificators:\n   ft: file as input and output to the screen (output is printed on the screen as text) \n   ff: file as input and output to file (output is redirected to a destination file) \n\nExamples:\n    python3 {sys.argv[0]} -ft: asks the user to input the filename and show the output on the screen\n    python3 {sys.argv[0]} -ff: asks the user to input the filename and output filename, and writes the output on the output file\n    filename: [file with the data to be converted]\n    output filename: [file to wirte the output]\n"""
                sys.exit(help_message)

            else:
                sys.exit("invalid argument")

    except Exception as err:
        sys.exit(err)

    except KeyboardInterrupt as err:
        sys.exit()


def backslash_on():
    try:
        data, mode = parameters()
        string = str(data)[2:-1]

        if mode == "ff":
            # file to file mode
            file_data, target_filename = data
            string = str(file_data)[2:-1] # conversion of bytes to string
            write_file(target_filename,string)

        elif mode == "ft":
            # file to text/screen mode
            print(string)

        else:
            sys.exit("unknown error: something with the option/mode went wrong")

    except Exception as err:
        sys.exit(err)

import sys
backslash_on()
