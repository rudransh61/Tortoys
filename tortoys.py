import turtle
import argparse
import subprocess
import os
import tortoys as lang

def main():
    subprocess.run('cls',shell=True)
    parser = argparse.ArgumentParser(description='Tortoys : A programming language made for kids')
    parser.add_argument('--f', help='Input file path')

    args = parser.parse_args()
    
    code = ""
    # Check if the 'f' argument is provided
    if args.f:
        file_path = args.f
        # Add your code logic here for handling the input file
        try :
            with open(file_path, 'r') as file:
                # Read the entire contents of the file
                file_contents = file.read()
                # print(file_contents)
                code = file_contents
        except:
            raise FileExistsError(f"File does not exist on path {file}.")
    

    interpreter = lang.Tortoys()
    interpreter.execute(code)

if __name__ == '__main__':
    main()

