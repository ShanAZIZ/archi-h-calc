import csv


def numbers_from_file(filename):
    numbers = []
    with open(filename) as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
         numbers.append(int(row[0]))
    return numbers