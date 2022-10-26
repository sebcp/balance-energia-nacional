import pandas as pd

df = pd.read_csv("files/bne_balance_nacional.csv", sep=";")
df["tcal"] = df["tcal"].apply(lambda string: int(string.split(",")[0]))
df_consumo = df[df["item"] == "CONSUMO FINAL"]
categorias_mineria = ["Cobre", "Salitre", "Hierro", "Minas Varias"]
categorias_industrial = ["Papel y Celulosa", "Siderurgia", "Petroquímica", "Cemento", "Azúcar", "Pesca", "Industrias Varias"]
categorias_transporte = ["Terrestre", "Ferroviario", "Marítimo", "Aéreo"]
categorias_no_inustriales = ["Comercial", "Público", "Residencial", "Sanitarias"]

df_mineria = df_consumo[df_consumo["categoria"].isin(categorias_mineria)]
df_industrial = df_consumo[df_consumo["categoria"].isin(categorias_industrial)]
df_transporte = df_consumo[df_consumo["categoria"].isin(categorias_transporte)]
df_no_industriales = df_consumo[df_consumo["categoria"].isin(categorias_no_inustriales)]

df_mineria_grouped = df_mineria.groupby(["anio", "seccion"])["tcal"].sum()
df_industrial_grouped = df_industrial.groupby(["anio", "seccion"])["tcal"].sum()
df_transporte_grouped = df_transporte.groupby(["anio", "seccion"])["tcal"].sum()
df_no_industriales_grouped = df_no_industriales.groupby(["anio", "seccion"])["tcal"].sum()

print(df_mineria_grouped)