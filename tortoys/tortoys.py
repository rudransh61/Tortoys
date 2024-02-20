import turtle
import argparse
import subprocess
import os

class EducationLanguageInterpreter:
    def __init__(self):
        self.turtle = turtle.Turtle()

    def execute(self, code):
        commands = code.split('\n')
        for command in commands:
            self.parse_command(command)

    def parse_command(self, command):
        tokens = command.split()
        if not tokens:
            return

        action = tokens[0].upper()

        if action == 'TURN':
            self.turn(tokens)
        elif action == 'MOVE':
            self.move(tokens)
        elif action == 'COLOR':
            self.set_color(tokens)
        elif action == 'MOVETO':
            self.move_to(tokens)
        else:
            print(f"Unknown command: {command}")

    def turn(self, tokens):
        if len(tokens) == 2:
            angle = float(tokens[1])
            self.turtle.left(angle)
        else:
            print("Invalid TURN command")

    def move(self, tokens):
        if len(tokens) == 2:
            distance = float(tokens[1])
            self.turtle.forward(distance)
        else:
            print("Invalid MOVE command")

    def set_color(self, tokens):
        if len(tokens) == 2:
            color = tokens[1].lower()
            self.turtle.color(color)
        else:
            print("Invalid COLOR command")

    def move_to(self, tokens):
        if len(tokens) == 3:
            x = float(tokens[1])
            y = float(tokens[2])
            self.turtle.goto(x, y)
        else:
            print("Invalid MOVETO command")


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
                print(file_contents)
                code = file_contents
        except:
            raise FileExistsError(f"File does not exist on path {file}.")
    

    interpreter = EducationLanguageInterpreter()
    interpreter.execute(code)
    turtle.done()

if __name__ == '__main__':
    main()

