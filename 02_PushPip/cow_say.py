import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('message')
parser.add_argument('-c', '--character', default='default')
parser.add_argument('-l', '--list', action='store_false')
args = parser.parse_args()

if args.list:
    print(cowsay.list_cows())
else:
    print(cowsay.cowsay(args.message, cow=args.character))
