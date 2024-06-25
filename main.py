import sys

from args_validation import read_args
from operations import output
from read_file import numbers_from_file

def main():
    arguments = read_args(sys.argv)
    numbers = numbers_from_file(arguments["filename"])
    output(numbers, arguments["operation"])

if __name__ == "__main__":
    main()

