def print_cyan(skk): 
    print("\033[96m{}\033[00m".format(skk))
def log_error(skk): 
    print("\033[91m{}\033[00m".format(skk))
    quit()
def print_green(skk): 
    print("\033[92m{}\033[00m".format(skk))

print_cyan("Bank helper modules initialized!")