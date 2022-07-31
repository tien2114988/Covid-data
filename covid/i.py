from main import*


def ex1():
    df1 = df["date"].apply(lambda x: x.strftime("%Y"))
    df1 = list(df1[df1.duplicated() == False])
    print("the data is collected through the years", df1)


def ex2():
    df2 = df[["iso_code", "location"]]
    df2 = df2[(["OWID" not in x for x in df2["iso_code"]])
              & (df2["iso_code"].duplicated() == False)].head(10)
    df2 = df2.reset_index(drop=True)
    print(df2)


def ex3():
    df3 = df["continent"]
    df3 = df3[(df3.duplicated() == False) & (df3.notna())]
    df3 = df3.reset_index(drop=True)
    print(df3)


def ex4():
    continent = list(df["continent"].value_counts(sort=False).keys())
    continent.append("Total")
    observation = list(df["continent"].value_counts(sort=False).values)
    observation.append(sum(observation))
    df4 = {"Continent": continent,
           "Observation": observation}
    df4 = pandas.DataFrame(df4)
    print(df4)


def ex5():
    df5 = df["location"][df["location"] != "World"]
    country = list(df5.value_counts(sort=False).tail(10).keys())
    country.append("Total")
    observation = list(df5.value_counts(sort=False).tail(10).values)
    observation.append(sum(observation))
    df5 = {"Country": country,
           "Observation": observation}
    df5 = pandas.DataFrame(df5)
    print(df5)


def ex6():
    df6 = df["continent"].value_counts()
    df6 = dict(df6.head(1))
    print("the continent has the most dataset :", df6)


def ex7():
    df7 = df["continent"].value_counts()
    df7 = dict(df7.tail(1))
    print("the continent has the least dataset :", df7)


def ex8():
    df8 = df["location"].value_counts()
    df8 = dict(df8.head(1))
    print("the country has the most dataset :", df8)


def ex9():
    df9 = df["location"].value_counts()
    df9 = dict(df9.tail(1))
    print("the country has the least dataset :", df9)


def ex10():
    df10 = df["date"].value_counts()
    df10 = dict(df10.head(1))
    print("the date has the most dataset :", df10)


def ex11():
    df11 = df["date"].value_counts()
    df11 = dict(df11.tail(1))
    print("the date has the least dataset :", df11)


def ex12():
    print("i dont understand the question")


def ex13():
    df13 = dict(df[["continent", "date"]].value_counts().head(1))
    print("the date and the continent has the most dataset :", df13)


def ex14():
    df14 = dict(df[["continent", "date"]].value_counts().tail(1))
    print("the date and the continent has the most dataset :", df14)


def ex15():
    k = input("enter the date you want to show data : ")
    t = input("enter continent you want to show data : ")
    df15 = df[["continent", "date"]].value_counts()
    print(df15[(t, k)])


def ex16():
    df16 = pandas.DataFrame(
        df["iso_code"][[len(x) <= 3 for x in df["iso_code"]]]).value_counts()
    observation = df16[df16.duplicated() == False]
    df16 = dict(df16)
    ex16 = {}
    for i in observation:
        ex16[i] = []
    for x, y in df16.items():
        ex16[y].append(x)
    df16 = ex16.copy()
    for x, y in ex16.items():
        if len(y) == 1:
            df16.pop(x)
    for i in df16.values():
        print(i)


def ex17():
    df17 = df[["iso_code", "location"]][[
        len(x) > 3 for x in df["iso_code"]]].value_counts(sort=False)
    df17.reset_index(drop=True)
    print(df17)


def main():
    f = [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9,
         ex10, ex11, ex12, ex13, ex14, ex15, ex16, ex17]
    choice = int(input("what answer do you want to show : "))
    f[choice-1]()


if __name__ == "__main__":
    main()
