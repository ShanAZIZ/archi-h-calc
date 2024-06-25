
import os


VALID_OPERATIONS = ["+", "*"]

def valid_count_args(args):
    return len(args) == 3

def file_exists(filename):
    return os.path.isfile(filename) # TODO: valid csv

def is_valid_operation(operation): 
    return operation in VALID_OPERATIONS

def read_args(args):
    
    if(not valid_count_args(args)):
        raise ValueError("Vous devez passer deux arguments uniquement") 
    
    file_name = args[1]
    operation = args[2]

    if(not file_exists(file_name)):
        raise ValueError(f"Le fichier {file_name} n'existe pas")

    if(not is_valid_operation(operation)):
        raise ValueError(f"L'opération {operation} n'est pas pris en charge") # TODO: mieux gerer le *

    return {
        'filename': args[1],
        'operation': args[2] 
    }
