import turtle
import re
import tortoys.terror as terror
class Tortoys:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.variables = {}
        self.turtle.screen.title("Welcome to Tortoys")

    def execute(self, code):
        commands = code.split('\n')
        for line_number, command in enumerate(commands, start=1):
            self.parse_command(command, line_number)

    def parse_command(self, command, line_number):
        # Ignore everything after the $ symbol for comments
        command = command.split('$')[0].strip()
        
        tokens = self.tokenize(command)
        if not tokens:
            return

        action = tokens[0].upper()

        if action == 'RIGHT':
            self.right(tokens, line_number)
        elif action == 'LEFT':
            self.left(tokens, line_number)
        elif action == 'MOVE':
            self.move(tokens, line_number)
        elif action == 'COLOR':
            self.set_color(tokens, line_number)
        elif action == 'MOVETO':
            self.move_to(tokens, line_number)
        elif action == 'SPEED':
            self.speed(tokens, line_number)
        elif action == 'TITLE':
            self.title(tokens, line_number)
        elif action == 'CLEAR':
            self.clear(line_number)
        elif action == 'SETX':
            self.set_x(tokens, line_number)
        elif action == 'SETY':
            self.set_y(tokens, line_number)
        elif action == 'PRINT':
            self.print(tokens, line_number)
        elif action == 'SET':
            self.set_variable(tokens, line_number)
        elif action == 'CLOSE':
            self.close(line_number)
        elif action == 'DONE':
            self.done(line_number)
        else:
            raise(f"Unknown command: {command} : On line number {line_number}")

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

    def right(self, tokens, line_number):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                distance = float(value)
            elif value in self.variables:
                distance = float(self.variables[value])
            else:
                raise(f"Undefined variable: {value} on line {line_number}")

            self.turtle.right(distance)
        else:
            raise(f"Invalid RIGHT command on line {line_number}")
            
    def left(self, tokens, line_number):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                angle = float(value)
            elif value in self.variables:
                angle = self.variables[value]
            else:
                raise(f"Undefined variable: {value} on line {line_number}")

            self.turtle.left(angle)
        else:
            raise(f"Invalid LEFT command on line {line_number}")

    def move(self, tokens, line_number):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                distance = float(value)
            elif value in self.variables:
                distance = float(self.variables[value])
            else:
                raise(f"Undefined variable: {value} on line {line_number}")

            self.turtle.forward(distance)
        else:
            raise(f"Invalid MOVE command on line {line_number}")

    def set_color(self, tokens, line_number):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                color = str(value)
            elif value in self.variables:
                color = self.variables[value]
            else:
                raise(f"Undefined variable: {value} on line {line_number}")

            self.turtle.color(color)
        else:
            raise(f"Invalid COLOR command on line {line_number}")

    def set_x(self, tokens, line_number):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                x = float(value)
            elif value in self.variables:
                x = self.variables[value]
            else:
                raise(f"Undefined variable: {value} on line {line_number}")
            self.turtle.set_x(x)
        else:
            raise(f"Invalid SETX command on line {line_number}")

    def set_y(self, tokens, line_number):
        if len(tokens) == 2:
            value = tokens[1]
            if value.isnumeric():
                y = float(value)
            elif value in self.variables:
                y = self.variables[value]
            else:
                raise(f"Undefined variable: {value} on line {line_number}")

            self.turtle.set_y(y)
        else:
            raise(f"Invalid SETY command on line {line_number}")

    def move_to(self, tokens, line_number):
        if len(tokens) == 3:
            x = float(tokens[1])
            y = float(tokens[2])
            self.turtle.goto(x, y)
        else:
            raise(f"Invalid MOVETO command on line {line_number}")

    def speed(self, tokens, line_number):
        if len(tokens) == 2:
            speed = float(tokens[1])
            self.turtle.speed(speed)
        else:
            raise(f"Invalid SPEED command on line {line_number}")

    def title(self, tokens, line_number):
        if len(tokens) == 2:
            title = str(tokens[1])
            self.turtle.screen.title(title)
        else:
            raise(f"Invalid TITLE command on line {line_number}")

    def print(self, tokens, line_number):
        if len(tokens) == 2:
            msg = str(tokens[1])
            # Replace variable names with their values inside curly braces
            msg = self.replace_variables(msg)
            # Simplify arithmetic expressions inside curly braces
            msg = self.simplify_arithmetic(msg)
            print(msg)
        else:
            raise(f"Invalid PRINT command on line {line_number}")

    
    def simplify_arithmetic(self, msg):
        # Simplify arithmetic expressions inside curly braces
        while '{' in msg and '}' in msg:
            start_index = msg.find('{')
            end_index = msg.find('}')
            expression = msg[start_index + 1:end_index]

            try:
                # Check if the expression contains a variable
                if any(char.isalpha() for char in expression):
                    result = str(eval(expression, {}, self.variables))
                else:
                    result = str(eval(expression))
            except Exception as e:
                print(f"Error evaluating expression: {expression} - {e}")
                break

            msg = msg[:start_index] + result + msg[end_index + 1:]

        return msg


    def clear(self, line_number):
        try :
            self.turtle.clear()
        except :
            raise(f"Error while running CLEAR on line number {line_number}")

    def set_variable(self, tokens , line_number):
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


    def replace_variables(self, expression):
        # Find all variable names inside curly braces
        placeholders = re.findall(r'\{([A-Za-z0-9_]+)\}', expression)
        
        # Replace each variable with its value
        for placeholder in placeholders:
            if placeholder in self.variables:
                variable_value = str(self.variables[placeholder])
                expression = expression.replace(f"{{{placeholder}}}", variable_value)
        
        return expression
            
        
    def close(self, line_number):
        try :
            self.turtle.screen.bye()
        except :
            raise(f"Error while running CLOSE on line {line_number}")
        
    def done(self, line_number):
        try :
            turtle.done()
        except :
            raise(f"Error while running DONE on line {line_number}")