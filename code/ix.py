from main import *
from ii import *
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split

timeline = ["1/2020", "4/2020", "6/2020", "8/2020",
            "11/2021", "12/2021", "6/2021", "8/2021", "1/2022"]


def ix1():
    idn_cases_sum = idn["new_cases"].sum()
    idn_cases = {}
    for i in [2020, 2021, 2022]:
        idn_y = idn[[int(x.strftime("%Y")) <= i for x in idn["date"]]]
        for j in [1, 4, 6, 8]:
            idn_cases[str(j)+"/"+str(i)] = idn_y[[(int(x.strftime("%Y")) < i) | (int(x.strftime("%m")) <= j)
                                                  for x in idn_y["date"]]]["new_cases"].sum()/idn_cases_sum
            if i == 2022:
                break

    idn_deaths_sum = idn["new_deaths"].sum()
    idn_deaths = {}
    for i in [2020, 2021, 2022]:
        idn_y = idn[[int(x.strftime("%Y")) <= i for x in idn["date"]]]
        for j in [1, 4, 6, 8]:
            idn_deaths[str(j)+"/"+str(i)] = idn_y[[(int(x.strftime("%Y")) < i) | (int(x.strftime("%m")) <= j)
                                                  for x in idn_y["date"]]]["new_deaths"].sum()/idn_deaths_sum
            if i == 2022:
                break

    idn_fig, idn_ax = plt.subplots()
    idn_ax.plot(idn_cases.keys(), idn_cases.values(),
                marker="o", label="new_cases")
    idn_ax.plot(idn_deaths.keys(), idn_deaths.values(),
                marker="o", label="new_deaths")
    idn_ax.set_xlabel("Timeline", color="y")
    idn_ax.set_ylabel("Values", color="y")
    idn_fig.suptitle(
        "The cumulative relative frequency plot of new_cases/new_deaths in Indonesia".upper(), color="#30D5C8")
    idn_ax.legend()

    jpg_cases_sum = jpg["new_cases"].sum()
    jpg_cases = {}
    for i in [2020, 2021, 2022]:
        jpg_y = jpg[[int(x.strftime("%Y")) <= i for x in jpg["date"]]]
        for j in [1, 4, 6, 8]:
            jpg_cases[str(j)+"/"+str(i)] = jpg_y[[(int(x.strftime("%Y")) < i) | (int(x.strftime("%m")) <= j)
                                                  for x in jpg_y["date"]]]["new_cases"].sum()/jpg_cases_sum
            if i == 2022:
                break

    jpg_deaths_sum = jpg["new_deaths"].sum()
    jpg_deaths = {}
    for i in [2020, 2021, 2022]:
        jpg_y = jpg[[int(x.strftime("%Y")) <= i for x in jpg["date"]]]
        for j in [1, 4, 6, 8]:
            jpg_deaths[str(j)+"/"+str(i)] = jpg_y[[(int(x.strftime("%Y")) < i) | (int(x.strftime("%m")) <= j)
                                                  for x in jpg_y["date"]]]["new_deaths"].sum()/jpg_deaths_sum
            if i == 2022:
                break

    jpg_fig, jpg_ax = plt.subplots()
    jpg_ax.plot(jpg_cases.keys(), jpg_cases.values(),
                marker="o", label="new_cases")
    jpg_ax.plot(jpg_deaths.keys(), jpg_deaths.values(),
                marker="o", label="new_deaths")
    jpg_ax.set_xlabel("Timeline", color="y")
    jpg_ax.set_ylabel("Values", color="y")
    jpg_fig.suptitle(
        "The cumulative relative frequency plot of new_cases/new_deaths in Japan".upper(), color="#30D5C8")
    jpg_ax.legend()

    vnm_cases_sum = vnm["new_cases"].sum()
    vnm_cases = {}
    for i in [2020, 2021, 2022]:
        vnm_y = vnm[[int(x.strftime("%Y")) <= i for x in vnm["date"]]]
        for j in [1, 4, 6, 8]:
            vnm_cases[str(j)+"/"+str(i)] = vnm_y[[(int(x.strftime("%Y")) < i) | (int(x.strftime("%m")) <= j)
                                                  for x in vnm_y["date"]]]["new_cases"].sum()/vnm_cases_sum
            if i == 2022:
                break

    vnm_deaths_sum = vnm["new_deaths"].sum()
    vnm_deaths = {}
    for i in [2020, 2021, 2022]:
        vnm_y = vnm[[int(x.strftime("%Y")) <= i for x in vnm["date"]]]
        for j in [1, 4, 6, 8]:
            vnm_deaths[str(j)+"/"+str(i)] = vnm_y[[(int(x.strftime("%Y")) < i) | (int(x.strftime("%m")) <= j)
                                                  for x in vnm_y["date"]]]["new_deaths"].sum()/vnm_deaths_sum
            if i == 2022:
                break

    vnm_fig, vnm_ax = plt.subplots()
    vnm_ax.plot(vnm_cases.keys(), vnm_cases.values(),
                marker="o", label="new_cases")
    vnm_ax.plot(vnm_deaths.keys(), vnm_deaths.values(),
                marker="o", label="new_deaths")
    vnm_ax.set_xlabel("Timeline", color="y")
    vnm_ax.set_ylabel("Values", color="y")
    vnm_fig.suptitle(
        "The cumulative relative frequency plot of new_cases/new_deaths in Vietnam".upper(), color="#30D5C8")
    vnm_ax.legend()

    plt.show()


def ix2():
    lr = lm.LinearRegression()

    idn21 = idn[[int(x.strftime("%Y")) == 2021 for x in idn["date"]]]
    idn_fig, idn_ax = plt.subplots(ncols=3)

    for i in [2020, 2021, 2022]:
        idn_ = idn[[int(x.strftime("%Y")) == i for x in idn["date"]]]
        x = numpy.array([idn_["new_cases"]]).T
        y = numpy.array(idn_["new_deaths"])

        lr.fit(x, y)
        yp = lr.predict(x)

        idn_ax[i-2020].scatter(x, y, color="red", label="collected data")
        idn_ax[i-2020].plot(x, yp, label="linear regression")
        idn_ax[i-2020].set_xlabel("new_cases", color="y")
        idn_ax[i-2020].set_ylabel("new_deaths", color="y")
        idn_ax[i-2020].set_title(str(i))
        idn_ax[i-2020].legend()
        idn_fig.suptitle(
            f"The correlation between new_cases/new_deaths in Indonesia".upper(), color="g")

    jpg21 = jpg[[int(x.strftime("%Y")) == 2021 for x in jpg["date"]]]
    jpg_fig, jpg_ax = plt.subplots(ncols=3)

    for i in [2020, 2021, 2022]:
        jpg_ = jpg[[int(x.strftime("%Y")) == i for x in jpg["date"]]]
        x = numpy.array([jpg_["new_cases"]]).T
        y = numpy.array(jpg_["new_deaths"])

        lr.fit(x, y)
        yp = lr.predict(x)

        jpg_ax[i-2020].scatter(x, y, color="red", label="collected data")
        jpg_ax[i-2020].plot(x, yp, label="linear regression")
        jpg_ax[i-2020].set_xlabel("new_cases", color="y")
        jpg_ax[i-2020].set_ylabel("new_deaths", color="y")
        jpg_ax[i-2020].set_title(str(i))
        jpg_ax[i-2020].legend()
        jpg_fig.suptitle(
            f"The correlation between new_cases/new_deaths in Japan".upper(), color="g")

    vnm21 = vnm[[int(x.strftime("%Y")) == 2021 for x in vnm["date"]]]
    vnm_fig, vnm_ax = plt.subplots(ncols=3)

    for i in [2020, 2021, 2022]:
        vnm_ = vnm[[int(x.strftime("%Y")) == i for x in vnm["date"]]]
        x = numpy.array([vnm_["new_cases"]]).T
        y = numpy.array(vnm_["new_deaths"])

        lr.fit(x, y)
        yp = lr.predict(x)

        vnm_ax[i-2020].scatter(x, y, color="red", label="collected data")
        vnm_ax[i-2020].plot(x, yp, label="linear regression")
        vnm_ax[i-2020].set_xlabel("new_cases", color="y")
        vnm_ax[i-2020].set_ylabel("new_deaths", color="y")
        vnm_ax[i-2020].set_title(str(i))
        vnm_ax[i-2020].legend()
        vnm_fig.suptitle(
            f"The correlation between new_cases/new_deaths in Vietnam".upper(), color="g")

    plt.show()


def ix3():
    idn_cases, idn_deaths = list(idn["new_cases"]), list(idn["new_deaths"])
    for i in range(idn.shape[0]):
        if i < 7:
            idn_cases[i] = round(idn["new_cases"].iloc[0:i+1].sum() /
                                 (i+1))
            idn_deaths[i] = round(idn["new_deaths"].iloc[0:i+1].sum() /
                                  (i+1))
        else:
            idn_cases[i] = round(idn["new_cases"].iloc[i-6:i+1].sum() /
                                 7)
            idn_deaths[i] = round(idn["new_deaths"].iloc[i-6:i+1].sum() /
                                  7)
    idn["new_cases"], idn["new_deaths"] = idn_cases, idn_deaths

    jpg_cases, jpg_deaths = list(jpg["new_cases"]), list(jpg["new_deaths"])
    for i in range(jpg.shape[0]):
        if i < 7:
            jpg_cases[i] = round(jpg["new_cases"].iloc[0:i+1].sum() /
                                 (i+1))
            jpg_deaths[i] = round(jpg["new_deaths"].iloc[0:i+1].sum() /
                                  (i+1))
        else:
            jpg_cases[i] = round(jpg["new_cases"].iloc[i-6:i+1].sum() /
                                 7)
            jpg_deaths[i] = round(jpg["new_deaths"].iloc[i-6:i+1].sum() /
                                  7)
    jpg["new_cases"], jpg["new_deaths"] = jpg_cases, jpg_deaths

    vnm_cases, vnm_deaths = list(vnm["new_cases"]), list(vnm["new_deaths"])
    for i in range(vnm.shape[0]):
        if i < 7:
            vnm_cases[i] = round(vnm["new_cases"].iloc[0:i+1].sum() /
                                 (i+1))
            vnm_deaths[i] = round(vnm["new_deaths"].iloc[0:i+1].sum() /
                                  (i+1))
        else:
            vnm_cases[i] = round(vnm["new_cases"].iloc[i-6:i+1].sum() /
                                 7)
            vnm_deaths[i] = round(vnm["new_deaths"].iloc[i-6:i+1].sum() /
                                  7)
    vnm["new_cases"], vnm["new_deaths"] = vnm_cases, vnm_deaths

    lr = lm.LinearRegression()

    idn21 = idn[[int(x.strftime("%Y")) == 2021 for x in idn["date"]]]
    idn_fig, idn_ax = plt.subplots(ncols=3)

    for i in [2020, 2021, 2022]:
        idn_ = idn[[int(x.strftime("%Y")) == i for x in idn["date"]]]
        x = numpy.array([idn_["new_cases"]]).T
        y = numpy.array(idn_["new_deaths"])

        lr.fit(x, y)
        yp = lr.predict(x)

        idn_ax[i-2020].scatter(x, y, color="red", label="collected data")
        idn_ax[i-2020].plot(x, yp, label="linear regression")
        idn_ax[i-2020].set_xlabel("new_cases", color="y")
        idn_ax[i-2020].set_ylabel("new_deaths", color="y")
        idn_ax[i-2020].set_title(str(i))
        idn_ax[i-2020].legend()
        idn_fig.suptitle(
            f"The correlation between new_cases/new_deaths in Indonesia".upper(), color="g")

    jpg21 = jpg[[int(x.strftime("%Y")) == 2021 for x in jpg["date"]]]
    jpg_fig, jpg_ax = plt.subplots(ncols=3)

    for i in [2020, 2021, 2022]:
        jpg_ = jpg[[int(x.strftime("%Y")) == i for x in jpg["date"]]]
        x = numpy.array([jpg_["new_cases"]]).T
        y = numpy.array(jpg_["new_deaths"])

        lr.fit(x, y)
        yp = lr.predict(x)

        jpg_ax[i-2020].scatter(x, y, color="red", label="collected data")
        jpg_ax[i-2020].plot(x, yp, label="linear regression")
        jpg_ax[i-2020].set_xlabel("new_cases", color="y")
        jpg_ax[i-2020].set_ylabel("new_deaths", color="y")
        jpg_ax[i-2020].set_title(str(i))
        jpg_ax[i-2020].legend()
        jpg_fig.suptitle(
            f"The correlation between new_cases/new_deaths in Japan".upper(), color="g")

    vnm21 = vnm[[int(x.strftime("%Y")) == 2021 for x in vnm["date"]]]
    vnm_fig, vnm_ax = plt.subplots(ncols=3)

    for i in [2020, 2021, 2022]:
        vnm_ = vnm[[int(x.strftime("%Y")) == i for x in vnm["date"]]]
        x = numpy.array([vnm_["new_cases"]]).T
        y = numpy.array(vnm_["new_deaths"])

        lr.fit(x, y)
        yp = lr.predict(x)

        vnm_ax[i-2020].scatter(x, y, color="red", label="collected data")
        vnm_ax[i-2020].plot(x, yp, label="linear regression")
        vnm_ax[i-2020].set_xlabel("new_cases", color="y")
        vnm_ax[i-2020].set_ylabel("new_deaths", color="y")
        vnm_ax[i-2020].set_title(str(i))
        vnm_ax[i-2020].legend()
        vnm_fig.suptitle(
            f"The correlation between new_cases/new_deaths in Vietnam".upper(), color="g")

    plt.show()


def ml():
    idn20 = idn[[int(x.strftime("%Y")) == 2020 for x in idn["date"]]]
    x = numpy.array([idn20["new_cases"]]).T
    y = numpy.array(idn20["new_deaths"])
    xtrain, xtest, ytrain, ytest = train_test_split(
        x, y, train_size=0.7, random_state=7)
    lr = lm.LinearRegression()
    lr.fit(xtrain, ytrain)
    yp = lr.predict(xtest)
    for i in range(len(ytest)):
        print(ytest[i], " ", yp[i])
    plt.scatter(xtest, ytest, color="r")
    plt.plot(xtest, yp)
    plt.show()


def main():
    f = [ix1, ix2, ix3]
    choice = int(input("enter the answer do you want to show : "))
    return f[choice-1]()


if __name__ == "__main__":
    main()
