# Para ejecutar este codigo:
# python tuto_argparse.py -o A -d High -f 30 

# o bien:
# python tuto_argparse.py --origin A --destination High --filter 30 



import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='BiciMad')


# definicion de argumentos
parser.add_argument('-o', '--origin', type=str, help='Origen de usuarios')
parser.add_argument('-d', '--destination', type=str, help='Destino de usuarios')


parser.add_argument('-f', '--filter', type=float, help='Filtro para pruebas')



parser_args = parser.parse_args()

# variables que le paso por terminal, nombre viene del --nombre
origin = parser_args.origin
destination = parser_args.destination

filtro = parser_args.filter



df = pd.read_csv('data/crop_yield.csv')


if filtro > 15:
    print(df[(df.Fert==origin) & (df.Water==destination) & (df.Yield>filtro)])
    
else:
    print(df[(df.Fert==origin) & (df.Water==destination)])
