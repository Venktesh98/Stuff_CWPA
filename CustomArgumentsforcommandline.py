# include standard modules
import argparse
import copy
import pasteing

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--copydo", help="run get from copy", action="store_true")
parser.add_argument("-p", "--pastedo", help="run get from paste", action="store_true")

# read arguments from the command line
args = parser.parse_args()
print(args)

# check for --copy or -c
if args.copydo: 
    print("this is myprogram of copy")
    cp = copy.docopy()
    cp.get()

# check for --paste or -p
elif args.pastedo:
    print("This is paste program in testing")
    ps = pasteing.dopaste()
    ps.get()

else:
    print("None")

