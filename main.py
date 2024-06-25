import sys

from args_validation import read_args
from operations import operate
from read_file import numbers_from_file

def main():
    arguments = read_args(sys.argv)
    numbers = numbers_from_file(arguments["filename"])
    print(operate(numbers, arguments["operation"]))

if __name__ == "__main__":
    main()

