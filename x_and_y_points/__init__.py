import requests

class GetInfo:

    def __init__(self, function=None, x_range=None, x_value=None, y_value=None):
        self.function = function
        self.x_range = x_range

        self.x_value = x_value
        self.y_value = y_value

    def get_user_input(self):
        fake_range = ''

        if self.function is None:
            self.function = input('enter the function equation (use Y as the function and X as the independent variable): ')
            check_function = list(self.function)
            if self.function == '' or 'Y' not in check_function or '=' not in check_function or 'X' not in check_function:
                self.function = None
                print('the input was not in accepted format, or the independent variable was not capitalized\n')
                self.get_user_input()

        if self.function is not None and self.x_range is None:
            self.x_range = input('enter the domain of the independent variable X (in the format ( __ , __ ) ) (use -& for infinite small and +& for infinite big, ( -& , +& ) for infinite): ')
            self.x_range = self.x_range.split(' ')
            if self.x_range == '' or len(self.x_range) != 5:
                self.x_range = None
                print('the input was not in accepted format')
                self.get_user_input()

        if self.x_range[0] == '(' and self.x_range[1] != '-&':
            self.x_range.remove('(')
            number1 = int(self.x_range[0]) + 1
            self.x_range.remove(self.x_range[0])
            self.x_range.insert(0, str(number1))
        elif self.x_range[0] == '(' and self.x_range[1] == '-&':
            self.x_range.remove('(')
        elif self.x_range[0] == '[':
            self.x_range.remove('[')

        if self.x_range[-1] == ')' and self.x_range[-2] != '+&':
            self.x_range.remove(')')
            number2 = int(self.x_range[-1]) - 1
            self.x_range.remove(self.x_range[-1])
            self.x_range.append(str(number2))
        elif self.x_range[-1] == ')' and self.x_range[-2] == '+&':
            self.x_range.remove(')')
        elif self.x_range[-1] == ']':
            self.x_range.remove(']')

        for value in self.x_range:
            fake_range += value

        check_range = fake_range.split(',')

        if len(check_range) != 2:
            self.x_range = None
            print('the input was not in accepted format')
            self.get_user_input()

        self.make_the_x_values(fake_range)

    def make_the_x_values(self, x):
        self.x_range_list = x.split(',')

        if self.x_range_list != ['-&', '+&']:
            try:
                if self.x_range_list[0] == '-&':
                    self.x_value = [x for x in range(-100000, int(self.x_range_list[1]) + 1)]
                elif self.x_range_list[1] == '+&':
                    self.x_value = [x for x in range(int(self.x_range_list[0]), 100001)]
                else:
                    self.x_value = [x for x in range(int(self.x_range_list[0]), int(self.x_range_list[1]) + 1)]
            except IndexError:
                self.get_user_input()
        else:
            self.x_value = [x for x in range(-100000, 100001)]

        self.make_y_value(self.function, self.x_value)

    def make_y_value(self, equation, xs, actual_equation=''):
        processable_equation = equation.replace('^', '**')
        processable_equation = processable_equation.replace('x', '*')
        processable_equation = processable_equation.split(' ')
        processable_equation = processable_equation[2:]

        for value in processable_equation:
            actual_equation += value + ' '

        actual_equation = actual_equation.strip()

        if type(xs) == list:
            for value in xs:
                X = value
                self.y_value.append(eval(actual_equation))
        if type(xs) == int or type(xs) == float:
            X = xs

            return eval(actual_equation)
