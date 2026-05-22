import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def grafico_valores_perdidos(df):

    # Calcular valores perdidos
    missing = df.isnull().sum()

    # Porcentaje
    missing_percent = (missing / len(df)) * 100

    # Crear DataFrame resumen
    missing_df = pd.DataFrame({
        'Variable': missing.index,
        'Valores Perdidos': missing.values,
        'Porcentaje': missing_percent.values
    })

    # Filtrar solo columnas con nulos
    missing_df = missing_df[
        missing_df['Valores Perdidos'] > 0
    ]

    # Ordenar
    missing_df = missing_df.sort_values(
        by='Porcentaje',
        ascending=False
    )

    # Tamaño figura
    plt.figure(figsize=(12, 7))

    # Gráfico
    ax = sns.barplot(
        data=missing_df,
        x='Porcentaje',
        y='Variable'
    )

    # Título
    plt.title(
        'Valores Perdidos por Variable',
        fontsize=16,
        fontweight='bold'
    )

    plt.xlabel('Porcentaje (%)')
    plt.ylabel('Variables')

    # Etiquetas en barras
    for i, row in missing_df.iterrows():

        ax.text(
            row['Porcentaje'] + 0.5,
            i,
            f"{row['Valores Perdidos']} ({row['Porcentaje']:.1f}%)",
            va='center'
        )

    plt.tight_layout()

    plt.show()