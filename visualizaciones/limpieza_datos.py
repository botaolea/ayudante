{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "ySMguRGJOeaj"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "def grafico_valores_perdidos(df):\n",
        "\n",
        "    # Calcular valores perdidos\n",
        "    missing = df.isnull().sum()\n",
        "\n",
        "    # Porcentaje\n",
        "    missing_percent = (missing / len(df)) * 100\n",
        "\n",
        "    # Crear DataFrame resumen\n",
        "    missing_df = pd.DataFrame({\n",
        "        'Variable': missing.index,\n",
        "        'Valores Perdidos': missing.values,\n",
        "        'Porcentaje': missing_percent.values\n",
        "    })\n",
        "\n",
        "    # Filtrar solo columnas con nulos\n",
        "    missing_df = missing_df[\n",
        "        missing_df['Valores Perdidos'] > 0\n",
        "    ]\n",
        "\n",
        "    # Ordenar\n",
        "    missing_df = missing_df.sort_values(\n",
        "        by='Porcentaje',\n",
        "        ascending=False\n",
        "    )\n",
        "\n",
        "    # Tamaño figura\n",
        "    plt.figure(figsize=(12, 7))\n",
        "\n",
        "    # Gráfico\n",
        "    ax = sns.barplot(\n",
        "        data=missing_df,\n",
        "        x='Porcentaje',\n",
        "        y='Variable'\n",
        "    )\n",
        "\n",
        "    # Título\n",
        "    plt.title(\n",
        "        'Valores Perdidos por Variable',\n",
        "        fontsize=16,\n",
        "        fontweight='bold'\n",
        "    )\n",
        "\n",
        "    plt.xlabel('Porcentaje (%)')\n",
        "    plt.ylabel('Variables')\n",
        "\n",
        "    # Etiquetas en barras\n",
        "    for i, row in missing_df.iterrows():\n",
        "\n",
        "        ax.text(\n",
        "            row['Porcentaje'] + 0.5,\n",
        "            i,\n",
        "            f\"{row['Valores Perdidos']} ({row['Porcentaje']:.1f}%)\",\n",
        "            va='center'\n",
        "        )\n",
        "\n",
        "    plt.tight_layout()\n",
        "\n",
        "    plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Tr4A1klVOnkM"
      },
      "execution_count": 5,
      "outputs": []
    }
  ]
}