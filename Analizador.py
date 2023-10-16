2class SyntaxAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_token = None
        self.current_position = 0

    def get_next_token(self):
        if self.current_position < len(self.input_string):
            self.current_token = self.input_string[self.current_position]
            self.current_position += 1
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.get_next_token()
        else:
            raise SyntaxError(f"Expected {expected_token}, but found {self.current_token}")

    def factor(self):
        if self.current_token.isnumeric():
            self.match(self.current_token)
        else:
            self.match('(')
            self.expression()
            self.match(')')

    def term(self):
        self.factor()
        while self.current_token in ('*', '/'):
            self.match(self.current_token)
            self.factor()

    def expression(self):
        self.term()
        while self.current_token in ('+', '-'):
            self.match(self.current_token)
            self.term()

    def parse(self):
        self.get_next_token()
        self.expression()
        if self.current_token is None:
            print("Parsing successful!")

if __name__ == "__main__":
    input_string = input("Ingrese una expresión: ")
    analyzer = SyntaxAnalyzer(input_string)
    try:
        analyzer.parse()
    except SyntaxError as e:
        print(f"Error de sintaxis: {str(e)}")
