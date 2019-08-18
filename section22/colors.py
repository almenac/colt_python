from termcolor import colored
import colorama

colorama.init()

text = colored("Hi there", color="cyan")

print(text)