from main import *
from ii import *


def iv1():
    continent = df["continent"].value_counts(sort=False)
    goal = ["5000", "10000", "20000", "40000"]
    df1 = {}
    for i in goal:
        df1[i] = len([x for x in continent.values if x <= int(i)])
    plt.bar(df1.keys(), df1.values(), color="#30D5C8")
    plt.xlabel("Goal of amount of the countries", color="b")
    plt.ylabel("Amount of continents in the range", color="b")
    plt.title(
        "country cumulative frequency histogram for continents".upper(), color="b")
    plt.show()


def iv2():
    country = df["location"].value_counts().size
    continent = list(df["continent"].value_counts(sort=False).keys())
    df2 = {}

    for i in continent:
        df2[i] = df[df["continent"] == i]["location"].value_counts().size / \
            country

    plt.bar(df2.keys(), df2.values(), color="#30D5C8")
    plt.grid(True, axis="y")
    plt.ylabel("% country/total", color="b")
    plt.xlabel("Continent", color="b")
    plt.title(
        "country relative frequency histogram for continents".upper(), color="b")
    plt.show()


def iv3():
    fig1, idn_case = plt.subplots()
    fig2, jpg_case = plt.subplots()
    fig3, vnm_case = plt.subplots()
    idn_case.bar(idn["date"].tail(
        7), idn["new_cases"].tail(7), color="#30D5C8")
    idn_case.set_xlabel("Last 7 days of 2022", color="b")
    idn_case.set_ylabel("new_cases", color="b")
    idn_case.set_title(
        "new_cases in the last 7 days of 2022 in Indonesia".upper(), color="b")
    jpg_case.bar(jpg["date"].tail(
        7), jpg["new_cases"].tail(7), color="#30D5C8")
    jpg_case.set_xlabel("Last 7 days of 2022", color="b")
    jpg_case.set_ylabel("new_cases", color="b")
    jpg_case.set_title(
        "new_cases in the last 7 days of 2022 in Japan".upper(), color="b")
    vnm_case.bar(vnm["date"].tail(
        7), vnm["new_cases"].tail(7), color="#30D5C8")
    vnm_case.set_xlabel("Last 7 days of 2022", color="b")
    vnm_case.set_ylabel("new_cases", color="b")
    vnm_case.set_title(
        "new_cases in the last 7 days of 2022 in Vietnam".upper(), color="b")
    plt.show()


def iv4():
    fig1, idn_death = plt.subplots()
    fig2, jpg_death = plt.subplots()
    fig3, vnm_death = plt.subplots()
    idn_death.bar(idn["date"].tail(
        7), idn["new_deaths"].tail(7), color="#30D5C8")
    idn_death.set_xlabel("Last 7 days of 2022", color="b")
    idn_death.set_ylabel("new_deaths", color="b")
    idn_death.set_title(
        "new_deaths in the last 7 days of 2022 in Indonesia".upper(), color="b")
    jpg_death.bar(jpg["date"].tail(
        7), jpg["new_deaths"].tail(7), color="#30D5C8")
    jpg_death.set_xlabel("Last 7 days of 2022", color="b")
    jpg_death.set_ylabel("new_deaths", color="b")
    jpg_death.set_title(
        "new_deaths in the last 7 days of 2022 in Japan".upper(), color="b")
    vnm_death.bar(vnm["date"].tail(
        7), vnm["new_deaths"].tail(7), color="#30D5C8")
    vnm_death.set_xlabel("Last 7 days of 2022", color="b")
    vnm_death.set_ylabel("new_deaths", color="b")
    vnm_death.set_title(
        "new_deaths in the last 7 days of 2022 in Vietnam".upper(), color="b")
    plt.show()


def iv5():
    outliers = ii5()
    plt.bar(outliers.columns, outliers.iloc[0].values, color="#30D5C8")
    plt.xlabel("Country", color="b")
    plt.ylabel("Outliers", color="b")
    plt.title(
        "The plot of outliers for new_cases in Indonesia, Japan, Vietnam".upper(), color="b")
    plt.show()


def iv6():
    outliers = ii5()
    plt.bar(outliers.columns, outliers.iloc[1].values, color="#30D5C8")
    plt.xlabel("Country", color="b")
    plt.ylabel("Outliers", color="b")
    plt.title(
        "The plot of outliers for new_deaths in Indonesia, Japan, Vietnam".upper(), color="b")
    plt.show()


def main():
    f = [iv1, iv2, iv3, iv4, iv5, iv6]
    choice = int(input("enter the answer do you want to show : "))
    f[choice-1]()


if __name__ == "__main__":
    main()
