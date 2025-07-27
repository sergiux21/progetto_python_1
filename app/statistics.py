from scipy import stats
#t-testt tra due gruppi di una variabile categorica (condition)
#per una colonna numerica
def t_test_between_groups(df, numeric_col, group_col, group1_val, group2_val):
    group1 = df[df[group_col] == group1_val][numeric_col].dropna()
    group2 = df[df[group_col] == group2_val][numeric_col].dropna()
    t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
    return t_stat, p_value, group1.mean(), group2.mean()