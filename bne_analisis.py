import pandas as pd

# Se lee el archivo base, se transoforma la columna de teracalorías y se definen las categorías mayores
df = pd.read_csv("files/bne_balance_nacional.csv", sep=";")
df["tcal"] = df["tcal"].apply(lambda string: int(string.split(",")[0]))
df_consumo = df[df["item"] == "CONSUMO FINAL"]
df_consumo.pop("item")
df_consumo.pop("combustible")
categorias_mineria = ["Cobre", "Salitre", "Hierro", "Minas Varias"]
categorias_industrial = ["Papel y Celulosa", "Siderurgia", "Petroquímica", "Cemento", "Azúcar", "Pesca", "Industrias Varias"]
categorias_transporte = ["Terrestre", "Ferroviario", "Marítimo", "Aéreo"]
categorias_no_inustriales = ["Comercial", "Público", "Residencial", "Sanitarias"]

# Se separan en dataframes por categoría y se eliminan las filas correspondientes a gastos energéticos nulos
df_mineria = df_consumo[df_consumo["categoria"].isin(categorias_mineria)]
df_mineria = df_mineria.loc[df_mineria["tcal"]!=0]

df_industrial = df_consumo[df_consumo["categoria"].isin(categorias_industrial)]
df_industrial = df_industrial.loc[df_industrial["tcal"]!=0]

df_transporte = df_consumo[df_consumo["categoria"].isin(categorias_transporte)]
df_transporte = df_transporte.loc[df_transporte["tcal"]!=0]

df_no_industriales = df_consumo[df_consumo["categoria"].isin(categorias_no_inustriales)]
df_no_industriales = df_no_industriales.loc[df_no_industriales["tcal"]!=0]

# Se agrupa por año y sección energética, se suma el consumo y se exporta a csv
df_mineria_grouped_secciones = df_mineria.groupby(["anio", "seccion"])["tcal"].sum()
df_mineria_grouped_secciones.reset_index().to_csv('files/bne_mineria_secciones.csv', index=False)

df_industrial_grouped_secciones = df_industrial.groupby(["anio", "seccion"])["tcal"].sum()
df_industrial_grouped_secciones.reset_index().to_csv('files/bne_industrial_secciones.csv', index=False)

df_transporte_grouped_secciones = df_transporte.groupby(["anio", "seccion"])["tcal"].sum()
df_transporte_grouped_secciones.reset_index().to_csv('files/bne_transporte_secciones.csv', index=False)

df_no_industriales_grouped_secciones = df_no_industriales.groupby(["anio", "seccion"])["tcal"].sum()
df_no_industriales_grouped_secciones.reset_index().to_csv("files/bne_no_industriales_secciones.csv", index=False)

# Se agrupa por año, se suma el consumo y se vuelven a juntar en un solo df y se exporta a csv
df_mineria_no_seccionado = df_mineria.drop(["seccion","categoria"], axis=1)
df_mineria_grouped_total = df_mineria_no_seccionado.groupby("anio").sum()
df_mineria_grouped_total = df_mineria_grouped_total.reset_index()
df_mineria_grouped_total["categoria"] = "Minería"

df_industrial_no_seccionado = df_industrial.drop(["seccion","categoria"], axis=1)
df_industrial_grouped_total = df_industrial_no_seccionado.groupby("anio").sum()
df_industrial_grouped_total = df_industrial_grouped_total.reset_index()
df_industrial_grouped_total["categoria"] = "Industrial"

df_transporte_no_seccionado = df_transporte.drop(["seccion","categoria"], axis=1)
df_transporte_grouped_total = df_transporte_no_seccionado.groupby("anio").sum()
df_transporte_grouped_total = df_transporte_grouped_total.reset_index()
df_transporte_grouped_total["categoria"] = "Transporte"

df_no_industriales_no_seccionado = df_no_industriales.drop(["seccion","categoria"], axis=1)
df_no_industriales_grouped_total = df_no_industriales_no_seccionado.groupby("anio").sum()
df_no_industriales_grouped_total = df_no_industriales_grouped_total.reset_index()
df_no_industriales_grouped_total["categoria"] = "Público, residencial, comercial y sanitaria"

frames = [df_mineria_grouped_total, df_industrial_grouped_total, df_transporte_grouped_total, df_no_industriales_grouped_total]
df_total_categorico_anio = pd.concat(frames)
df_total_categorico_anio.to_csv("files/bne_total_categorico_anio.csv", index=False)