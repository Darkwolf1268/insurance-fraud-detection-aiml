import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(path):

    df = pd.read_csv(path)

    df = df.dropna()

    le = LabelEncoder()

    for col in df.select_dtypes(include="object"):
        df[col] = le.fit_transform(df[col])

    return df
