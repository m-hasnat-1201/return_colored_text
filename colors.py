class ColorText:
    """
    This class is for coloring the output text.
    """
    color = {
        'white': "\033[1;37m",
        'yellow': "\033[1;33m",
        'green': "\033[1;32m",
        'blue': "\033[1;34m",
        'cyan': "\033[1;36m",
        'red': "\033[1;31m",
        'magenta': "\033[1;35m",
        'black': "\033[1;30m",
        'darkwhite': "\033[0;37m",
        'darkyellow': "\033[0;33m",
        'darkgreen': "\033[0;32m",
        'darkblue': "\033[0;34m",
        'darkcyan': "\033[0;36m",
        'darkred': "\033[0;31m",
        'darkmagenta': "\033[0;35m",
        'darkblack': "\033[0;30m",
        'off': "\033[0;0m"
    }

    def __init__(self):
        super(ColorText, self).__init__()

    def color_line(self, text, input_color):
        """
        This function will color the current text output and
            stops to color when it is done.
        The next output(s) will print in default system color.
        :param text: The text to be colored
        :param input_color: The color to apply to the text
        :return: Text with input color if it is available in the class
                If the color is not available system default will be used.
        """
        return f'{self.color.get(input_color.lower(), "")}{text}{self.color["off"]}'

    def color_lines(self, text, input_color):
        """
        This function will color the current text output and
            continues to color all other output(s)
        :param text: The text to be colored
        :param input_color: The color to apply to the text
        :return: Text with input color if it is available in the class
                If the color is not available system default will be used.
        """
        return f'{self.color.get(input_color.lower(), "")}{text}'


if __name__ == "__main__":
    # Testing the output
    print(ColorText().color_line('Hello everyone!', 'Blue'))
    print('Done executing...')
    print(ColorText().color_lines('Hello everyone!', 'RED'))
    print('Closing file...')
