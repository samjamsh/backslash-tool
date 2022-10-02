def file_bytes(filename,option,data):
    try:
        import sys
        if option == "encode":
            with open(filename,"r") as file:
                return file.read()
        elif option == "writes":
            with open(filename,"w") as file:
                file.write(data)
    except Exception as err:
        sys.exit(err)


def user_inputs():
    import sys
    try:
        parameters = len(sys.argv)
        if parameters != 2:
            sys.exit("parameter error: only one parameter is required!")
        else:
            pass

        option = sys.argv[1]
        if option == "-fs" or option == "-ft" or option == "--file-to-screen" or option == "--file-to-text": # fs (file to screen), ft (file to text). its same thing
            filename = input("filename: ")
            file_data = file_bytes(filename,'encode','')
            return file_data, "text_on_screen"

        elif option == "-ff" or option == "--file-to-file": # ff (file to file)
            filename = input("filename: ")
            output_filename = input("output filename: ")
            file_data = file_bytes(filename,"encode",'')
            return (file_data,output_filename), "file_to_file"

        elif option == "-h" or option == "--help":
            help_msg = f"""Backslashes Conversor to On and Off  1.0 ../10/2022\nThis tool enables and disables backslashes into a file text\nyou can turn on/enable backslashes into all the file content/data or into all text content\n\nParameters Usage:\n   -ft or --file-to-text: file to text (from file to text) \n   -fs or --file-to-screen: file to texton screen (from file to text) \n   -ff or --file-to-file: file to file (from file to file) \n   -h or --help: shows this message\n\nProgram identificators:\n   ft: file as input and output to the screen (output is printed on the screen as text) \n   fs: file as input and output to the screen (output is printed on the screen as text) \n   ff: file as input and output to file (output is redirected to a destination file) \n\nExamples:\n    python3 {sys.argv[0]} -ft: asks the user to input the filename and show the output on the screen\n    python3 {sys.argv[0]} -ff: asks the user to input the filename and output filename, and writes the output on the output file\n    filename: [file with the data to be converted]\n    output filename: [file to wirte the output]\n"""
            sys.exit(help_msg)

        else:
            sys.exit("option error: invalid option!")

    except Exception as err:
        sys.exit(err)
        
    except KeyboardInterrupt:
        sys.exit()

def formula(file_content):
    __file_data__ = ['']
    for char in file_content:

        if __file_data__[-1]+char == "\\n":
            char='\n'
            __file_data__[-1] = char
        else:
            __file_data__.append(char)

    updated_file_content=""
    for _char_ in __file_data__[1:]:
        updated_file_content += _char_

    return updated_file_content


def backslash_off():
    try:
        data, mode = user_inputs()
        if mode == "text_on_screen":
            data_converted = formula(data) # convertes the file data to backslash off
            print(data_converted) # prints the output on screen

        elif mode == "file_to_file":
            output_file = data[1]
            data = data[0]
            data_converted = formula(data) # convertes the file data to backslash off
            file_bytes(output_file,"writes",data_converted) # writes the output on output file
            print("done")

        else:
            sys.exit("unknown error: something is wrong with the mode/option")

    except Exception as err:
        sys.exit(err)


backslash_off()
