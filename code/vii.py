from main import *

code = ["1", "4", "6", "8"]
end = ["11", "12"]

df20 = df[[int(x.strftime("%Y")) == 2020 for x in df["date"]]]
df21 = df[[int(x.strftime("%Y")) == 2021 for x in df["date"]]]

df20_1 = df20[[int(x.strftime("%m")) == 1 for x in df20["date"]]]
df20_4 = df20[[int(x.strftime("%m")) == 4 for x in df20["date"]]]
df20_6 = df20[[int(x.strftime("%m")) == 6 for x in df20["date"]]]
df20_8 = df20[[int(x.strftime("%m")) == 8 for x in df20["date"]]]
df20_11 = df20[[int(x.strftime("%m")) == 11 for x in df20["date"]]]
df20_12 = df20[[int(x.strftime("%m")) == 12 for x in df20["date"]]]

df21_1 = df21[[int(x.strftime("%m")) == 1 for x in df21["date"]]]
df21_4 = df21[[int(x.strftime("%m")) == 4 for x in df21["date"]]]
df21_6 = df21[[int(x.strftime("%m")) == 6 for x in df21["date"]]]
df21_8 = df21[[int(x.strftime("%m")) == 8 for x in df21["date"]]]
df21_11 = df21[[int(x.strftime("%m")) == 11 for x in df21["date"]]]
df21_12 = df21[[int(x.strftime("%m")) == 12 for x in df21["date"]]]


def vii1():
    df20_cases = [df20_1["new_cases"].sum(), df20_4["new_cases"].sum(),
                  df20_6["new_cases"].sum(), df20_8["new_cases"].sum()]
    df21_cases = [df21_1["new_cases"].sum(), df21_4["new_cases"].sum(),
                  df21_6["new_cases"].sum(), df21_8["new_cases"].sum()]

    fig, ax = plt.subplots(ncols=2)

    ax[0].bar(code, df20_cases)
    ax[0].set_title("2020", color="orange")
    ax[0].set_xlabel("Month", color="b")
    ax[0].set_ylabel("new_cases", color="b")

    ax[1].bar(code, df21_cases)
    ax[1].set_title("2021", color="orange")
    ax[1].set_xlabel("Month", color="b")
    ax[1].set_ylabel("new_cases", color="b")

    fig.suptitle("the plot of new_cases in 2020, 2021".upper(),
                 color="r")
    plt.show()


def vii2():
    df20_deaths = [df20_1["new_deaths"].sum(), df20_4["new_deaths"].sum(),
                   df20_6["new_deaths"].sum(), df20_8["new_deaths"].sum()]
    df21_deaths = [df21_1["new_deaths"].sum(), df21_4["new_deaths"].sum(),
                   df21_6["new_deaths"].sum(), df21_8["new_deaths"].sum()]

    fig, ax = plt.subplots(ncols=2)

    ax[0].bar(code, df20_deaths)
    ax[0].set_title("2020", color="orange")
    ax[0].set_xlabel("Month", color="b")
    ax[0].set_ylabel("new_deaths", color="b")

    ax[1].bar(code, df21_deaths)
    ax[1].set_title("2021", color="orange")
    ax[1].set_xlabel("Month", color="b")
    ax[1].set_ylabel("new_deaths", color="b")

    fig.suptitle("the plot of new_deaths in 2020, 2021".upper(),
                 color="r")
    plt.show()


def vii3():
    df20_cases = [df20_11["new_cases"].sum(), df20_12["new_cases"].sum()]
    df21_cases = [df21_11["new_cases"].sum(), df21_12["new_cases"].sum()]

    fig, ax = plt.subplots(ncols=2)

    ax[0].bar(end, df20_cases)
    ax[0].set_title("2020", color="orange")
    ax[0].set_xlabel("Month", color="b")
    ax[0].set_ylabel("new_cases", color="b")

    ax[1].bar(end, df21_cases)
    ax[1].set_title("2021", color="orange")
    ax[1].set_xlabel("Month", color="b")
    ax[1].set_ylabel("new_cases", color="b")

    fig.suptitle("the plot of new_cases in 2020, 2021".upper(),
                 color="r")
    plt.show()


def vii4():
    df20_deaths = [df20_11["new_deaths"].sum(), df20_12["new_deaths"].sum()]
    df21_deaths = [df21_11["new_deaths"].sum(), df21_12["new_deaths"].sum()]

    fig, ax = plt.subplots(ncols=2)

    ax[0].bar(end, df20_deaths)
    ax[0].set_title("2020", color="orange")
    ax[0].set_xlabel("Month", color="b")
    ax[0].set_ylabel("new_deaths", color="b")

    ax[1].bar(end, df21_deaths)
    ax[1].set_title("2021", color="orange")
    ax[1].set_xlabel("Month", color="b")
    ax[1].set_ylabel("new_deaths", color="b")

    fig.suptitle("the plot of new_deaths in 2020, 2021".upper(),
                 color="r")
    plt.show()


def vii5():
    timeline = ["11/2020", "12/2020", "11/2021", "12/2021"]
    cases = [df20_11["new_cases"].sum(), df20_12["new_cases"].sum(
    ), df21_11["new_cases"].sum(), df21_12["new_cases"].sum()]
    sum_cases = sum(cases)
    d = {}
    rest = 0

    for i in range(4):
        d[timeline[i]] = cases[i]/sum_cases
        d[timeline[i]] += rest
        rest = d[timeline[i]]

    plt.bar(d.keys(), d.values())
    plt.xlabel("Timeline", color="y")
    plt.ylabel("% relative new_cases", color="y")
    plt.title(
        "the cumulative relative frequency plot of new_cases".upper(), color="red")
    plt.show()


def vii6():
    timeline = ["11/2020", "12/2020", "11/2021", "12/2021"]
    deaths = [df20_11["new_deaths"].sum(), df20_12["new_deaths"].sum(
    ), df21_11["new_deaths"].sum(), df21_12["new_deaths"].sum()]
    sum_deaths = sum(deaths)
    d = {}
    rest = 0

    for i in range(4):
        d[timeline[i]] = deaths[i]/sum_deaths
        d[timeline[i]] += rest
        rest = d[timeline[i]]

    plt.bar(d.keys(), d.values())
    plt.xlabel("Timeline", color="y")
    plt.ylabel("% relative new_deaths", color="y")
    plt.title(
        "the cumulative relative frequency plot of new_deaths".upper(), color="red")
    plt.show()


def main():
    f = [vii1, vii2, vii3, vii4, vii5, vii6]
    choice = int(input("enter the answer do you want to show : "))
    return f[choice-1]()


if __name__ == "__main__":
    main()
