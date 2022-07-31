import pandas
import datetime

file = "owid-covid-data.csv"
df = pandas.read_csv(file)
df["date"] = df["date"].apply(
    lambda x: datetime.datetime.strptime(x, "%m/%d/%Y"))
