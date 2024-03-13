import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Bici Mad')



# definir argumentos de entrada, que luego voy a escribir en la terminal
parser.add_argument('-o', '--origin', type=str, help='Origen del usuario')
parser.add_argument('-d', '--destination', type=str, help='Destino del usuario')


# inicio el parser
parse_args = parser.parse_args()


origin = parse_args.origin
dest = parse_args.destination

print(origin, '---------', dest)

df = pd.read_csv('data/crop_yield.csv')

df = df[(df.Fert==origin) & (df.Water==dest)]

print(df)

print()

print(f'Hola, estas en {origin}, tu estacion mas cercana es {df.iloc[0]}')




