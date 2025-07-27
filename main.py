#importiamo le nostre librerie e metodi
from app.loader import load_data
from app.statistics import t_test_between_groups
from app.descrizioni import describe_columns
from app.grafici import plot_boxplot, plot_heatmap, plot_histogram

def main():
    path = "data/heart_cleveland_upload.csv"
    #carichiamo i dati
    df = load_data(path)
    #descriviamo i dati
    print("Info Dati:")
    describe_columns(df)
    #facciamo un test statistico
    print("\nT-test su colesterolo tra sani e malati")
    t_chol, p_chol, m0, m1 = t_test_between_groups(df, 'chol', 'condition', 0, 1)
    print(f"T_stat di colesterolo:  {t_chol:.2f}") 
    print(f"P_value di colesterolo:  {p_chol:.3f}")
    print(f"Sani: media colesterolo =  {m0:.3f}")
    print(f"Malati: media colesterolo =  {m1:.3f}")

    #mostriamo i grafici
    plot_histogram(df, 'age', hue='condition')
    plot_boxplot(df, 'condition', 'chol')
    plot_heatmap(df)





if __name__ == "__main__":
    main()