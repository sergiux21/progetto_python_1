
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column, hue=None): #hue sarà la colonna di confronto
    plt.figure(figsize=(8, 4))
    sns.histplot(data=df, x=column, hue=hue, kde=True)
    plt.title(f"Distribuzione dei valori di {column}")
    plt.tight_layout()
    plt.show()

def plot_boxplot(df, x, y): #prima la categorica e poi la numerica
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=x, y=y, data=df)
    plt.title(f"{y} rispetto a {x}")
    plt.tight_layout()
    plt.show()

def plot_heatmap(df):
    plt.figure(figsize=(12, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Matrice di Correlazione")
    plt.tight_layout()
    plt.show()
    