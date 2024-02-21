import turtle

class Tortoys:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.variables = {}

    def execute(self, code):
        commands = code.split('\n')
        for line_number, command in enumerate(commands, start=1):
            self.parse_command(command, line_number)

    def parse_command(self, command, line_number):
        tokens = self.tokenize(command)
        if not tokens:
            return

        action = tokens[0].upper()

        if action == 'RIGHT':
            self.right(tokens)
        elif action == 'LEFT':
            self.left(tokens)
        elif action == 'MOVE':
            self.move(tokens)
        elif action == 'COLOR':
            self.set_color(tokens)
        elif action == 'MOVETO':
            self.move_to(tokens)
        elif action == 'SPEED':
            self.speed(tokens)
        elif action == 'TITLE':
            self.title(tokens)
        elif action == 'CLEAR':
            self.clear()
        elif action == 'SETX':
            self.set_x(tokens)
        elif action == 'SETY':
            self.set_y(tokens)
        elif action == 'PRINT':
            self.print(tokens)
        elif action == 'SET':
            self.set_variable(tokens)
        else:
            print(f"Unknown command: {command} : On line number {line_number}")

    def tokenize(self, command):
        # Combine tokens inside double quotes as a single token
        tokens = []
        current_token = ''
        inside_quotes = False

        for char in command:
            if char == '"':
                inside_quotes = not inside_quotes
            elif char == ' ' and not inside_quotes:
                tokens.append(current_token)
                current_token = ''
            else:
                current_token += char

        if current_token:
            tokens.append(current_token)

        return tokens

    def right(self, tokens):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                distance = float(value)
            elif value in self.variables:
                distance = float(self.variables[value])
            else:
                print(f"Undefined variable: {value}")
                return

            self.turtle.right(distance)
        else:
            print("Invalid RIGHT command")
            
    def left(self, tokens):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                angle = float(value)
            elif value in self.variables:
                angle = self.variables[value]
            else:
                print(f"Undefined variable: {value}")
                return

            self.turtle.left(angle)
        else:
            print("Invalid LEFT command")

    def move(self, tokens):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                distance = float(value)
            elif value in self.variables:
                distance = float(self.variables[value])
            else:
                print(f"Undefined variable: {value}")
                return

            self.turtle.forward(distance)
        else:
            print("Invalid MOVE command")

    def set_color(self, tokens):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                color = str(value)
            elif value in self.variables:
                color = self.variables[value]
            else:
                print(f"Undefined variable: {value}")
                return

            self.turtle.color(color)
        else:
            print("Invalid COLOR command")

    def set_x(self, tokens):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                x = float(value)
            elif value in self.variables:
                x = self.variables[value]
            else:
                print(f"Undefined variable: {value}")
                return

            self.turtle.set_x(x)
        else:
            print("Invalid SETX command")

    def set_y(self, tokens):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                y = float(value)
            elif value in self.variables:
                y = self.variables[value]
            else:
                print(f"Undefined variable: {value}")
                return

            self.turtle.set_y(y)
        else:
            print("Invalid SETY command")

    def move_to(self, tokens):
        if len(tokens) == 3:
            x = float(tokens[1])
            y = float(tokens[2])
            self.turtle.goto(x, y)
        else:
            print("Invalid MOVETO command")

    def speed(self, tokens):
        if len(tokens) == 2:
            speed = float(tokens[1])
            self.turtle.speed(speed)
        else:
            print("Invalid SPEED command")

    def title(self, tokens):
        if len(tokens) == 2:
            title = str(tokens[1])
            self.turtle.screen.title(title)
        else:
            print("Invalid TITLE command")

    def print(self, tokens):
        if len(tokens) == 2:
            msg = str(tokens[1])
            print(msg)
        else:
            print("Invalid PRINT command")

    def clear(self):
        self.turtle.clear()

    def set_variable(self, tokens):
        if len(tokens)==3:
            variable_name = tokens[1]
            value = tokens[2]

            if value:
                self.variables[variable_name] = str(value)
            elif value in self.variables:
                self.variables[variable_name] = str(self.variables[value])
            else:
                print(f"Undefined variable value: {value}")
        else:
            print("Invalid SET command")

