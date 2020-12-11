import pandas as pd
penguins = pd.read_csv('penguins_cleaned.csv')


df = penguins.copy()
target = 'sex'
encode = ['species', 'island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]


target_mapper = {'Adeline': 0, 'Chinstrap': 1, 'Gentoo': 2}


def target_encode(val):
    return target_mapper[val]


df['species'] = df['species'].aply(target_encode)
