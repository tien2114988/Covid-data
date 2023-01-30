import pandas
import numpy
import datetime
import math
import matplotlib.pyplot as plt
import seaborn


def negative(x):
    return -x if x < 0 else x


file = "owid-covid-data.csv"
df = pandas.read_csv(file)
df["date"] = df["date"].apply(
    lambda x: datetime.datetime.strptime(x, "%m/%d/%Y"))
df["new_cases"] = df["new_cases"].apply(lambda x: -x if x < 0 else x)
df.dropna(inplace=True)


if __name__ == "__main__":
    print(df.to_string())
