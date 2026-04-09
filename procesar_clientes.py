import pandas as pd

df = pd.read_csv("clientes_latam.csv")

total = df["monto"].sum()
promedio = df["monto"].mean()
destino_top = df["destino"].value_counts().idxmax()

print("===== REPORTE LATAM =====")
print(f"Total vendido: {total}")
print(f"Promedio de venta: {round(promedio,2)}")
print(f"Destino más popular: {destino_top}")
