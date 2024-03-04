import argparse


parser = argparse.ArgumentParser(description='BiciMad')

parser.add_argument('-o', '--origin', type=str, help='Origen de usuario')
parser.add_argument('-d', '--destination', type=str, help='Destino de usuario')

parser_args = parser.parse_args()

origin = parser_args.origin
destination = parser_args.destination

print(origin, destination)
