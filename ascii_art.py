from pyfiglet import figlet_format
from termcolor import colored

text = input('What message do you want to print?')
color = input('What colors?')

# if color == 'red' or color == 'green' or color == 'blue' or color == 'magenta' or color == 'cyan':
#     ascii_art = termcolor.colored(pyfiglet.figlet_format(text), color=color)
# else:
#     ascii_art = termcolor.colored(pyfiglet.figlet_format(text), color='magenta')

valid_color = ['red', 'green', 'yellow', 'blue, magenta', 'cyan', 'white']
if color not in valid_color:
    color = 'magenta'

ascii_art = colored(figlet_format(text), color=color)
print(ascii_art)


# text = colored("HI THERE!", color="magenta", on_color="on_yellow", attrs=["blink"])
