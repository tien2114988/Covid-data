from main import*
from ii import*

idn1468 = idn[[int(x.strftime("%m")) in [1, 4, 6, 8] for x in idn["date"]]]
idn20 = idn1468[[int(x.strftime("%Y")) == 2020 for x in idn1468["date"]]]
idn21 = idn1468[[int(x.strftime("%Y")) == 2021 for x in idn1468["date"]]]
idn22 = idn1468[[int(x.strftime("%Y")) == 2022 for x in idn1468["date"]]]

jpg1468 = jpg[[int(x.strftime("%m")) in [1, 4, 6, 8] for x in jpg["date"]]]
jpg20 = jpg1468[[int(x.strftime("%Y")) == 2020 for x in jpg1468["date"]]]
jpg21 = jpg1468[[int(x.strftime("%Y")) == 2021 for x in jpg1468["date"]]]
jpg22 = jpg1468[[int(x.strftime("%Y")) == 2022 for x in jpg1468["date"]]]

vnm1468 = vnm[[int(x.strftime("%m")) in [1, 4, 6, 8] for x in vnm["date"]]]
vnm20 = vnm1468[[int(x.strftime("%Y")) == 2020 for x in vnm1468["date"]]]
vnm21 = vnm1468[[int(x.strftime("%Y")) == 2021 for x in vnm1468["date"]]]
vnm22 = vnm1468[[int(x.strftime("%Y")) == 2022 for x in vnm1468["date"]]]

idn1112 = idn[[int(x.strftime("%m")) in [11, 12] for x in idn["date"]]]
idn_20 = idn1112[[int(x.strftime("%Y")) == 2020 for x in idn1112["date"]]]
idn_21 = idn1112[[int(x.strftime("%Y")) == 2021 for x in idn1112["date"]]]
idn_22 = idn[[int(x.strftime("%Y")) == 2022 for x in idn["date"]]]

jpg1112 = jpg[[int(x.strftime("%m")) in [11, 12] for x in jpg["date"]]]
jpg_20 = jpg1112[[int(x.strftime("%Y")) == 2020 for x in jpg1112["date"]]]
jpg_21 = jpg1112[[int(x.strftime("%Y")) == 2021 for x in jpg1112["date"]]]
jpg_22 = jpg[[int(x.strftime("%Y")) == 2022 for x in jpg["date"]]]

vnm1112 = vnm[[int(x.strftime("%m")) in [11, 12] for x in vnm["date"]]]
vnm_20 = vnm1112[[int(x.strftime("%Y")) == 2020 for x in vnm1112["date"]]]
vnm_21 = vnm1112[[int(x.strftime("%Y")) == 2021 for x in vnm1112["date"]]]
vnm_22 = vnm[[int(x.strftime("%Y")) == 2022 for x in vnm["date"]]]

idn20_ = idn[[int(x.strftime("%Y")) == 2020 for x in idn["date"]]]
idn21_ = idn[[int(x.strftime("%Y")) == 2021 for x in idn["date"]]]

jpg20_ = jpg[[int(x.strftime("%Y")) == 2020 for x in jpg["date"]]]
jpg21_ = jpg[[int(x.strftime("%Y")) == 2021 for x in jpg["date"]]]

vnm20_ = vnm[[int(x.strftime("%Y")) == 2020 for x in vnm["date"]]]
vnm21_ = vnm[[int(x.strftime("%Y")) == 2021 for x in vnm["date"]]]


def v1(show=True):
    month = ["1", "4", "6", "8"]

    idn20_1 = idn20[[int(x.strftime("%m")) ==
                     1 for x in idn20["date"]]]["new_cases"].sum()
    idn20_4 = idn20[[int(x.strftime("%m")) ==
                     4 for x in idn20["date"]]]["new_cases"].sum()
    idn20_6 = idn20[[int(x.strftime("%m")) ==
                     6 for x in idn20["date"]]]["new_cases"].sum()
    idn20_8 = idn20[[int(x.strftime("%m")) ==
                     8 for x in idn20["date"]]]["new_cases"].sum()

    idn21_1 = idn21[[int(x.strftime("%m")) ==
                     1 for x in idn21["date"]]]["new_cases"].sum()
    idn21_4 = idn21[[int(x.strftime("%m")) ==
                     4 for x in idn21["date"]]]["new_cases"].sum()
    idn21_6 = idn21[[int(x.strftime("%m")) ==
                     6 for x in idn21["date"]]]["new_cases"].sum()
    idn21_8 = idn21[[int(x.strftime("%m")) ==
                     8 for x in idn21["date"]]]["new_cases"].sum()

    jpg20_1 = jpg20[[int(x.strftime("%m")) ==
                     1 for x in jpg20["date"]]]["new_cases"].sum()
    jpg20_4 = jpg20[[int(x.strftime("%m")) ==
                     4 for x in jpg20["date"]]]["new_cases"].sum()
    jpg20_6 = jpg20[[int(x.strftime("%m")) ==
                     6 for x in jpg20["date"]]]["new_cases"].sum()
    jpg20_8 = jpg20[[int(x.strftime("%m")) ==
                     8 for x in jpg20["date"]]]["new_cases"].sum()

    jpg21_1 = jpg21[[int(x.strftime("%m")) ==
                     1 for x in jpg21["date"]]]["new_cases"].sum()
    jpg21_4 = jpg21[[int(x.strftime("%m")) ==
                     4 for x in jpg21["date"]]]["new_cases"].sum()
    jpg21_6 = jpg21[[int(x.strftime("%m")) ==
                     6 for x in jpg21["date"]]]["new_cases"].sum()
    jpg21_8 = jpg21[[int(x.strftime("%m")) ==
                     8 for x in jpg21["date"]]]["new_cases"].sum()

    vnm20_1 = vnm20[[int(x.strftime("%m")) ==
                     1 for x in vnm20["date"]]]["new_cases"].sum()
    vnm20_4 = vnm20[[int(x.strftime("%m")) ==
                     4 for x in vnm20["date"]]]["new_cases"].sum()
    vnm20_6 = vnm20[[int(x.strftime("%m")) ==
                     6 for x in vnm20["date"]]]["new_cases"].sum()
    vnm20_8 = vnm20[[int(x.strftime("%m")) ==
                     8 for x in vnm20["date"]]]["new_cases"].sum()

    vnm21_1 = vnm21[[int(x.strftime("%m")) ==
                     1 for x in vnm21["date"]]]["new_cases"].sum()
    vnm21_4 = vnm21[[int(x.strftime("%m")) ==
                     4 for x in vnm21["date"]]]["new_cases"].sum()
    vnm21_6 = vnm21[[int(x.strftime("%m")) ==
                     6 for x in vnm21["date"]]]["new_cases"].sum()
    vnm21_8 = vnm21[[int(x.strftime("%m")) ==
                     8 for x in vnm21["date"]]]["new_cases"].sum()

    idn20_case = [idn20_1, idn20_4, idn20_6, idn20_8]
    idn21_case = [idn21_1, idn21_4, idn21_6, idn21_8]

    jpg20_case = [jpg20_1, jpg20_4, jpg20_6, jpg20_8]
    jpg21_case = [jpg21_1, jpg21_4, jpg21_6, jpg21_8]

    vnm20_case = [vnm20_1, vnm20_4, vnm20_6, vnm20_8]
    vnm21_case = [vnm21_1, vnm21_4, vnm21_6, vnm21_8]

    if show == True:
        fig, (idn_case, jpg_case, vnm_case) = plt.subplots(ncols=3, nrows=1)

        idn_case.plot(month, idn20_case, label="2020")
        idn_case.plot(month, idn21_case, label="2021")
        idn_case.set_xlabel("Month")
        idn_case.set_ylabel("new_cases")
        idn_case.set_title("Indonesia", color="#30D5C8")
        idn_case.legend()

        jpg_case.plot(month, jpg20_case, label="2020")
        jpg_case.plot(month, jpg21_case, label="2021")
        jpg_case.set_xlabel("Month")
        jpg_case.set_ylabel("new_cases")
        jpg_case.set_title("Japan", color="#30D5C8")
        jpg_case.legend()

        vnm_case.plot(month, vnm20_case, label="2020")
        vnm_case.plot(month, vnm21_case, label="2021")
        vnm_case.set_xlabel("Month")
        vnm_case.set_ylabel("new_cases")
        vnm_case.set_title("Vietnam", color="#30D5C8")
        vnm_case.legend()

        fig.suptitle(
            "The plot of new_cases for January, April, June, August in Indonesia, Japan, Vietnam".upper(), color="b")

        plt.show()

    return [idn20_case, idn21_case, jpg20_case, jpg21_case, vnm20_case, vnm21_case]


def v2(show=True):
    month = ["1", "4", "6", "8"]

    idn20_1 = idn20[[int(x.strftime("%m")) ==
                     1 for x in idn20["date"]]]["new_deaths"].sum()
    idn20_4 = idn20[[int(x.strftime("%m")) ==
                     4 for x in idn20["date"]]]["new_deaths"].sum()
    idn20_6 = idn20[[int(x.strftime("%m")) ==
                     6 for x in idn20["date"]]]["new_deaths"].sum()
    idn20_8 = idn20[[int(x.strftime("%m")) ==
                     8 for x in idn20["date"]]]["new_deaths"].sum()

    idn21_1 = idn21[[int(x.strftime("%m")) ==
                     1 for x in idn21["date"]]]["new_deaths"].sum()
    idn21_4 = idn21[[int(x.strftime("%m")) ==
                     4 for x in idn21["date"]]]["new_deaths"].sum()
    idn21_6 = idn21[[int(x.strftime("%m")) ==
                     6 for x in idn21["date"]]]["new_deaths"].sum()
    idn21_8 = idn21[[int(x.strftime("%m")) ==
                     8 for x in idn21["date"]]]["new_deaths"].sum()

    jpg20_1 = jpg20[[int(x.strftime("%m")) ==
                     1 for x in jpg20["date"]]]["new_deaths"].sum()
    jpg20_4 = jpg20[[int(x.strftime("%m")) ==
                     4 for x in jpg20["date"]]]["new_deaths"].sum()
    jpg20_6 = jpg20[[int(x.strftime("%m")) ==
                     6 for x in jpg20["date"]]]["new_deaths"].sum()
    jpg20_8 = jpg20[[int(x.strftime("%m")) ==
                     8 for x in jpg20["date"]]]["new_deaths"].sum()

    jpg21_1 = jpg21[[int(x.strftime("%m")) ==
                     1 for x in jpg21["date"]]]["new_deaths"].sum()
    jpg21_4 = jpg21[[int(x.strftime("%m")) ==
                     4 for x in jpg21["date"]]]["new_deaths"].sum()
    jpg21_6 = jpg21[[int(x.strftime("%m")) ==
                     6 for x in jpg21["date"]]]["new_deaths"].sum()
    jpg21_8 = jpg21[[int(x.strftime("%m")) ==
                     8 for x in jpg21["date"]]]["new_deaths"].sum()

    vnm20_1 = vnm20[[int(x.strftime("%m")) ==
                     1 for x in vnm20["date"]]]["new_deaths"].sum()
    vnm20_4 = vnm20[[int(x.strftime("%m")) ==
                     4 for x in vnm20["date"]]]["new_deaths"].sum()
    vnm20_6 = vnm20[[int(x.strftime("%m")) ==
                     6 for x in vnm20["date"]]]["new_deaths"].sum()
    vnm20_8 = vnm20[[int(x.strftime("%m")) ==
                     8 for x in vnm20["date"]]]["new_deaths"].sum()

    vnm21_1 = vnm21[[int(x.strftime("%m")) ==
                     1 for x in vnm21["date"]]]["new_deaths"].sum()
    vnm21_4 = vnm21[[int(x.strftime("%m")) ==
                     4 for x in vnm21["date"]]]["new_deaths"].sum()
    vnm21_6 = vnm21[[int(x.strftime("%m")) ==
                     6 for x in vnm21["date"]]]["new_deaths"].sum()
    vnm21_8 = vnm21[[int(x.strftime("%m")) ==
                     8 for x in vnm21["date"]]]["new_deaths"].sum()

    idn20_death = [idn20_1, idn20_4, idn20_6, idn20_8]
    idn21_death = [idn21_1, idn21_4, idn21_6, idn21_8]

    jpg20_death = [jpg20_1, jpg20_4, jpg20_6, jpg20_8]
    jpg21_death = [jpg21_1, jpg21_4, jpg21_6, jpg21_8]

    vnm20_death = [vnm20_1, vnm20_4, vnm20_6, vnm20_8]
    vnm21_death = [vnm21_1, vnm21_4, vnm21_6, vnm21_8]

    if show == True:
        fig, (idn_death, jpg_death, vnm_death) = plt.subplots(ncols=3, nrows=1)

        idn_death.plot(month, idn20_death, label="2020")
        idn_death.plot(month, idn21_death, label="2021")
        idn_death.set_xlabel("Month")
        idn_death.set_ylabel("new_deaths")
        idn_death.set_title("Indonesia", color="#30D5C8")
        idn_death.legend()

        jpg_death.plot(month, jpg20_death, label="2020")
        jpg_death.plot(month, jpg21_death, label="2021")
        jpg_death.set_xlabel("Month")
        jpg_death.set_ylabel("new_deaths")
        jpg_death.set_title("Japan", color="#30D5C8")
        jpg_death.legend()

        vnm_death.plot(month, vnm20_death, label="2020")
        vnm_death.plot(month, vnm21_death, label="2021")
        vnm_death.set_xlabel("Month")
        vnm_death.set_ylabel("new_deaths")
        vnm_death.set_title("Vietnam", color="#30D5C8")
        vnm_death.legend()

        fig.suptitle(
            "The plot of new_deaths for January, April, June, August in Indonesia, Japan, Vietnam".upper(), color="b")

        plt.show()

    return [idn20_death, idn21_death, jpg20_death, jpg21_death, vnm20_death, vnm21_death]


def v3():
    month = ["1", "4", "6", "8"]
    case = v1(False)
    death = v2(False)

    idn_fig, (idn20, idn21) = plt.subplots(nrows=1, ncols=2)

    idn20_case, idn20_death = case[0], death[0]
    idn20.plot(month, idn20_case, label="new_cases")
    idn20.plot(month, idn20_death, label="new_deaths")
    idn20.legend()
    idn20.set_xlabel("Month")
    idn20.set_ylabel("Values")
    idn20.set_title("2020", color="r")

    idn21_case, idn21_death = case[1], death[1]
    idn21.plot(month, idn21_case, label="new_cases")
    idn21.plot(month, idn21_death, label="new_deaths")
    idn21.legend()
    idn21.set_xlabel("Month")
    idn21.set_ylabel("Values")
    idn21.set_title("2021", color="r")

    idn_fig.suptitle(
        "The plot of the new_cases and new_deaths for January, April, June, August in Indonesia".upper(), color="b")

    jpg_fig, (jpg20, jpg21) = plt.subplots(nrows=1, ncols=2)

    jpg20_case, jpg20_death = case[2], death[2]
    jpg20.plot(month, jpg20_case, label="new_cases")
    jpg20.plot(month, jpg20_death, label="new_deaths")
    jpg20.legend()
    jpg20.set_xlabel("Month")
    jpg20.set_ylabel("Values")
    jpg20.set_title("2020", color="r")

    jpg21_case, jpg21_death = case[3], death[3]
    jpg21.plot(month, jpg21_case, label="new_cases")
    jpg21.plot(month, jpg21_death, label="new_deaths")
    jpg21.legend()
    jpg21.set_xlabel("Month")
    jpg21.set_ylabel("Values")
    jpg21.set_title("2021", color="r")

    jpg_fig.suptitle(
        "The plot of the new_cases and new_deaths for January, April, June, August in Japan".upper(), color="b")

    vnm_fig, (vnm20, vnm21) = plt.subplots(nrows=1, ncols=2)

    vnm20_case, vnm20_death = case[4], death[4]
    vnm20.plot(month, vnm20_case, label="new_cases")
    vnm20.plot(month, vnm20_death, label="new_deaths")
    vnm20.legend()
    vnm20.set_xlabel("Month")
    vnm20.set_ylabel("Values")
    vnm20.set_title("2020", color="r")

    vnm21_case, vnm21_death = case[5], death[5]
    vnm21.plot(month, vnm21_case, label="new_cases")
    vnm21.plot(month, vnm21_death, label="new_deaths")
    vnm21.legend()
    vnm21.set_xlabel("Month")
    vnm21.set_ylabel("Values")
    vnm21.set_title("2021", color="r")

    vnm_fig.suptitle(
        "The plot of the new_cases and new_deaths for January, April, June, August in Vietnam".upper(), color="b")

    plt.show()


def v4(show=True):
    timeline = ["11/2020", "12/2020", "11/2021",
                "12/2021", "1/2022", "2/2022"]

    idn20_11 = idn_20[[int(x.strftime("%m")) ==
                       11 for x in idn_20["date"]]]["new_cases"].sum()
    idn20_12 = idn_20[[int(x.strftime("%m")) ==
                       12 for x in idn_20["date"]]]["new_cases"].sum()
    idn21_11 = idn_21[[int(x.strftime("%m")) ==
                       11 for x in idn_21["date"]]]["new_cases"].sum()
    idn21_12 = idn_21[[int(x.strftime("%m")) ==
                       12 for x in idn_21["date"]]]["new_cases"].sum()
    idn22_1 = idn_22[[int(x.strftime("%m")) ==
                     1 for x in idn_22["date"]]]["new_cases"].sum()
    idn22_2 = idn_22[[int(x.strftime("%m")) ==
                      2 for x in idn_22["date"]]]["new_cases"].sum()
    idn2 = [idn20_11, idn20_12, idn21_11, idn21_12, idn22_1, idn22_2]

    jpg20_11 = jpg_20[[int(x.strftime("%m")) ==
                       11 for x in jpg_20["date"]]]["new_cases"].sum()
    jpg20_12 = jpg_20[[int(x.strftime("%m")) ==
                       12 for x in jpg_20["date"]]]["new_cases"].sum()
    jpg21_11 = jpg_21[[int(x.strftime("%m")) ==
                       11 for x in jpg_21["date"]]]["new_cases"].sum()
    jpg21_12 = jpg_21[[int(x.strftime("%m")) ==
                       12 for x in jpg_21["date"]]]["new_cases"].sum()
    jpg22_1 = jpg_22[[int(x.strftime("%m")) ==
                     1 for x in jpg_22["date"]]]["new_cases"].sum()
    jpg22_2 = jpg_22[[int(x.strftime("%m")) ==
                      2 for x in jpg_22["date"]]]["new_cases"].sum()
    jpg2 = [jpg20_11, jpg20_12, jpg21_11, jpg21_12, jpg22_1, jpg22_2]

    vnm20_11 = vnm_20[[int(x.strftime("%m")) ==
                       11 for x in vnm_20["date"]]]["new_cases"].sum()
    vnm20_12 = vnm_20[[int(x.strftime("%m")) ==
                       12 for x in vnm_20["date"]]]["new_cases"].sum()
    vnm21_11 = vnm_21[[int(x.strftime("%m")) ==
                       11 for x in vnm_21["date"]]]["new_cases"].sum()
    vnm21_12 = vnm_21[[int(x.strftime("%m")) ==
                       12 for x in vnm_21["date"]]]["new_cases"].sum()
    vnm22_1 = vnm_22[[int(x.strftime("%m")) ==
                     1 for x in vnm_22["date"]]]["new_cases"].sum()
    vnm22_2 = vnm_22[[int(x.strftime("%m")) ==
                      2 for x in vnm_22["date"]]]["new_cases"].sum()
    vnm2 = [vnm20_11, vnm20_12, vnm21_11, vnm21_12, vnm22_1, vnm22_2]

    if show == True:
        idn_fig, idn_ax = plt.subplots()
        idn_ax.bar(timeline, idn2, color="#30D5C8")
        idn_ax.set_xlabel("Time", c="b")
        idn_ax.set_ylabel("new_cases", c="b")
        idn_ax.set_title(
            "The plot of the new_cases for the last 2 months of the year in Indonesia".upper(), c="r")

        jpg_fig, jpg_ax = plt.subplots()
        jpg_ax.bar(timeline, jpg2, color="#30D5C8")
        jpg_ax.set_xlabel("Time", c="b")
        jpg_ax.set_ylabel("new_cases", c="b")
        jpg_ax.set_title(
            "The plot of the new_cases for the last 2 months of the year in Japan".upper(), c="r")

        vnm_fig, vnm_ax = plt.subplots()
        vnm_ax.bar(timeline, vnm2, color="#30D5C8")
        vnm_ax.set_xlabel("Time", c="b")
        vnm_ax.set_ylabel("new_cases", c="b")
        vnm_ax.set_title(
            "The plot of the new_cases for the last 2 months of the year in Vietnam".upper(), c="r")

        plt.show()

    return [idn2, jpg2, vnm2]


def v5(show=True):
    timeline = ["11/2020", "12/2020", "11/2021",
                "12/2021", "1/2022", "2/2022"]

    idn20_11 = idn_20[[int(x.strftime("%m")) ==
                       11 for x in idn_20["date"]]]["new_deaths"].sum()
    idn20_12 = idn_20[[int(x.strftime("%m")) ==
                       12 for x in idn_20["date"]]]["new_deaths"].sum()
    idn21_11 = idn_21[[int(x.strftime("%m")) ==
                       11 for x in idn_21["date"]]]["new_deaths"].sum()
    idn21_12 = idn_21[[int(x.strftime("%m")) ==
                       12 for x in idn_21["date"]]]["new_deaths"].sum()
    idn22_1 = idn_22[[int(x.strftime("%m")) ==
                     1 for x in idn_22["date"]]]["new_deaths"].sum()
    idn22_2 = idn_22[[int(x.strftime("%m")) ==
                      2 for x in idn_22["date"]]]["new_deaths"].sum()
    idn2 = [idn20_11, idn20_12, idn21_11, idn21_12, idn22_1, idn22_2]

    jpg20_11 = jpg_20[[int(x.strftime("%m")) ==
                       11 for x in jpg_20["date"]]]["new_deaths"].sum()
    jpg20_12 = jpg_20[[int(x.strftime("%m")) ==
                       12 for x in jpg_20["date"]]]["new_deaths"].sum()
    jpg21_11 = jpg_21[[int(x.strftime("%m")) ==
                       11 for x in jpg_21["date"]]]["new_deaths"].sum()
    jpg21_12 = jpg_21[[int(x.strftime("%m")) ==
                       12 for x in jpg_21["date"]]]["new_deaths"].sum()
    jpg22_1 = jpg_22[[int(x.strftime("%m")) ==
                     1 for x in jpg_22["date"]]]["new_deaths"].sum()
    jpg22_2 = jpg_22[[int(x.strftime("%m")) ==
                      2 for x in jpg_22["date"]]]["new_deaths"].sum()
    jpg2 = [jpg20_11, jpg20_12, jpg21_11, jpg21_12, jpg22_1, jpg22_2]

    vnm20_11 = vnm_20[[int(x.strftime("%m")) ==
                       11 for x in vnm_20["date"]]]["new_deaths"].sum()
    vnm20_12 = vnm_20[[int(x.strftime("%m")) ==
                       12 for x in vnm_20["date"]]]["new_deaths"].sum()
    vnm21_11 = vnm_21[[int(x.strftime("%m")) ==
                       11 for x in vnm_21["date"]]]["new_deaths"].sum()
    vnm21_12 = vnm_21[[int(x.strftime("%m")) ==
                       12 for x in vnm_21["date"]]]["new_deaths"].sum()
    vnm22_1 = vnm_22[[int(x.strftime("%m")) ==
                     1 for x in vnm_22["date"]]]["new_deaths"].sum()
    vnm22_2 = vnm_22[[int(x.strftime("%m")) ==
                      2 for x in vnm_22["date"]]]["new_deaths"].sum()
    vnm2 = [vnm20_11, vnm20_12, vnm21_11, vnm21_12, vnm22_1, vnm22_2]

    if show == True:
        idn_fig, idn_ax = plt.subplots()
        idn_ax.bar(timeline, idn2, color="#30D5C8")
        idn_ax.set_xlabel("Time", c="b")
        idn_ax.set_ylabel("new_deaths", c="b")
        idn_ax.set_title(
            "The plot of the new_deaths for the last 2 months of the year in Indonesia".upper(), c="r")

        jpg_fig, jpg_ax = plt.subplots()
        jpg_ax.bar(timeline, jpg2, color="#30D5C8")
        jpg_ax.set_xlabel("Time", c="b")
        jpg_ax.set_ylabel("new_deaths", c="b")
        jpg_ax.set_title(
            "The plot of the new_deaths for the last 2 months of the year in Japan".upper(), c="r")

        vnm_fig, vnm_ax = plt.subplots()
        vnm_ax.bar(timeline, vnm2, color="#30D5C8")
        vnm_ax.set_xlabel("Time", c="b")
        vnm_ax.set_ylabel("new_deaths", c="b")
        vnm_ax.set_title(
            "The plot of the new_deaths for the last 2 months of the year in Vietnam".upper(), c="r")

        plt.show()

    return [idn2, jpg2, vnm2]


def v6():
    timeline = ["11/2020", "12/2020", "11/2021",
                "12/2021", "1/2022", "2/2022"]
    idn_case, jpg_case, vnm_case = v4(False)
    idn_death, jpg_death, vnm_death = v5(False)

    idn_fig, idn_ax = plt.subplots()
    idn_ax.plot(timeline, idn_case, label="new_cases")
    idn_ax.plot(timeline, idn_death, label="new_deaths")
    idn_ax.set_xlabel("Timeline", c="r")
    idn_ax.set_ylabel("Values", c="r")
    idn_ax.set_title(
        "The plot of the new_cases and new_deaths for the last 2 months of the year in Indonesia", c="b")
    idn_ax.legend()

    jpg_fig, jpg_ax = plt.subplots()
    jpg_ax.plot(timeline, jpg_case, label="new_cases")
    jpg_ax.plot(timeline, jpg_death, label="new_deaths")
    jpg_ax.set_xlabel("Timeline", c="r")
    jpg_ax.set_ylabel("Values", c="r")
    jpg_ax.set_title(
        "The plot of the new_cases and new_deaths for the last 2 months of the year in Japan", c="b")
    jpg_ax.legend()

    vnm_fig, vnm_ax = plt.subplots()
    vnm_ax.plot(timeline, vnm_case, label="new_cases")
    vnm_ax.plot(timeline, vnm_death, label="new_deaths")
    vnm_ax.set_xlabel("Timeline", c="r")
    vnm_ax.set_ylabel("Values", c="r")
    vnm_ax.set_title(
        "The plot of the new_cases and new_deaths for the last 2 months of the year in Vietnam", c="b")
    vnm_ax.legend()

    plt.show()


def v7():
    idn2020, idn2021, jpg2020, jpg2021, vnm2020, vnm2021 = {}, {}, {}, {}, {}, {}
    idn2020_cmlt = idn2021_cmlt = jpg2020_cmlt = jpg2021_cmlt = vnm2020_cmlt = vnm2021_cmlt = 0
    for i in range(1, 13):
        idn2020[i] = idn20_[
            [int(x.strftime("%m")) == i for x in idn20_["date"]]]["new_cases"].sum()+idn2020_cmlt
        idn2020_cmlt = idn2020[i]
        idn2021[i] = idn21_[
            [int(x.strftime("%m")) == i for x in idn21_["date"]]]["new_cases"].sum()+idn2021_cmlt
        idn2021_cmlt = idn2021[i]

        jpg2020[i] = jpg20_[
            [int(x.strftime("%m")) == i for x in jpg20_["date"]]]["new_cases"].sum()+jpg2020_cmlt
        jpg2020_cmlt = jpg2020[i]
        jpg2021[i] = jpg21_[
            [int(x.strftime("%m")) == i for x in jpg21_["date"]]]["new_cases"].sum()+jpg2021_cmlt
        jpg2021_cmlt = jpg2021[i]

        vnm2020[i] = vnm20_[
            [int(x.strftime("%m")) == i for x in vnm20_["date"]]]["new_cases"].sum()+vnm2020_cmlt
        vnm2020_cmlt = vnm2020[i]
        vnm2021[i] = vnm21_[
            [int(x.strftime("%m")) == i for x in vnm21_["date"]]]["new_cases"].sum()+vnm2021_cmlt
        vnm2021_cmlt = vnm2021[i]

    idn_fig, idn_ax = plt.subplots(ncols=2)
    idn_ax[0].bar(idn2020.keys(), idn2020.values())
    idn_ax[0].set_xlabel("Month", c="y")
    idn_ax[0].set_ylabel("new_cases", c="y")
    idn_ax[0].set_title("2020", color="r")
    idn_ax[1].bar(idn2021.keys(), idn2021.values())
    idn_ax[1].set_xlabel("Month", c="y")
    idn_ax[1].set_ylabel("new_cases", c="y")
    idn_ax[1].set_title("2021", color="r")
    idn_fig.suptitle(
        "The cumulative plot for new_cases in Indonesia".upper(), c="b")

    jpg_fig, jpg_ax = plt.subplots(ncols=2)
    jpg_ax[0].bar(jpg2020.keys(), jpg2020.values())
    jpg_ax[0].set_xlabel("Month", c="y")
    jpg_ax[0].set_ylabel("new_cases", c="y")
    jpg_ax[0].set_title("2020", color="r")
    jpg_ax[1].bar(jpg2021.keys(), jpg2021.values())
    jpg_ax[1].set_xlabel("Month", c="y")
    jpg_ax[1].set_ylabel("new_cases", c="y")
    jpg_ax[1].set_title("2021", color="r")
    jpg_fig.suptitle(
        "The cumulative plot for new_cases in Japan".upper(), c="b")

    vnm_fig, vnm_ax = plt.subplots(ncols=2)
    vnm_ax[0].bar(vnm2020.keys(), vnm2020.values())
    vnm_ax[0].set_xlabel("Month", c="y")
    vnm_ax[0].set_ylabel("new_cases", c="y")
    vnm_ax[0].set_title("2020", color="r")
    vnm_ax[1].bar(vnm2021.keys(), vnm2021.values())
    vnm_ax[1].set_xlabel("Month", c="y")
    vnm_ax[1].set_ylabel("new_cases", c="y")
    vnm_ax[1].set_title("2021", color="r")
    vnm_fig.suptitle(
        "The cumulative plot for new_cases in Vietnam".upper(), c="b")

    plt.show()


def v8():
    idn2020, idn2021, jpg2020, jpg2021, vnm2020, vnm2021 = {}, {}, {}, {}, {}, {}
    idn2020_cmlt = idn2021_cmlt = jpg2020_cmlt = jpg2021_cmlt = vnm2020_cmlt = vnm2021_cmlt = 0
    for i in range(1, 13):
        idn2020[i] = idn20_[
            [int(x.strftime("%m")) == i for x in idn20_["date"]]]["new_deaths"].sum()+idn2020_cmlt
        idn2020_cmlt = idn2020[i]
        idn2021[i] = idn21_[
            [int(x.strftime("%m")) == i for x in idn21_["date"]]]["new_deaths"].sum()+idn2021_cmlt
        idn2021_cmlt = idn2021[i]

        jpg2020[i] = jpg20_[
            [int(x.strftime("%m")) == i for x in jpg20_["date"]]]["new_deaths"].sum()+jpg2020_cmlt
        jpg2020_cmlt = jpg2020[i]
        jpg2021[i] = jpg21_[
            [int(x.strftime("%m")) == i for x in jpg21_["date"]]]["new_deaths"].sum()+jpg2021_cmlt
        jpg2021_cmlt = jpg2021[i]

        vnm2020[i] = vnm20_[
            [int(x.strftime("%m")) == i for x in vnm20_["date"]]]["new_deaths"].sum()+vnm2020_cmlt
        vnm2020_cmlt = vnm2020[i]
        vnm2021[i] = vnm21_[
            [int(x.strftime("%m")) == i for x in vnm21_["date"]]]["new_deaths"].sum()+vnm2021_cmlt
        vnm2021_cmlt = vnm2021[i]

    idn_fig, idn_ax = plt.subplots(ncols=2)
    idn_ax[0].bar(idn2020.keys(), idn2020.values())
    idn_ax[0].set_xlabel("Month", c="y")
    idn_ax[0].set_ylabel("new_deaths", c="y")
    idn_ax[0].set_title("2020", color="r")
    idn_ax[1].bar(idn2021.keys(), idn2021.values())
    idn_ax[1].set_xlabel("Month", c="y")
    idn_ax[1].set_ylabel("new_deaths", c="y")
    idn_ax[1].set_title("2021", color="r")
    idn_fig.suptitle(
        "The cumulative plot for new_deaths in Indonesia".upper(), c="b")

    jpg_fig, jpg_ax = plt.subplots(ncols=2)
    jpg_ax[0].bar(jpg2020.keys(), jpg2020.values())
    jpg_ax[0].set_xlabel("Month", c="y")
    jpg_ax[0].set_ylabel("new_deaths", c="y")
    jpg_ax[0].set_title("2020", color="r")
    jpg_ax[1].bar(jpg2021.keys(), jpg2021.values())
    jpg_ax[1].set_xlabel("Month", c="y")
    jpg_ax[1].set_ylabel("new_deaths", c="y")
    jpg_ax[1].set_title("2021", color="r")
    jpg_fig.suptitle(
        "The cumulative plot for new_deaths in Japan".upper(), c="b")

    vnm_fig, vnm_ax = plt.subplots(ncols=2)
    vnm_ax[0].bar(vnm2020.keys(), vnm2020.values())
    vnm_ax[0].set_xlabel("Month", c="y")
    vnm_ax[0].set_ylabel("new_deaths", c="y")
    vnm_ax[0].set_title("2020", color="r")
    vnm_ax[1].bar(vnm2021.keys(), vnm2021.values())
    vnm_ax[1].set_xlabel("Month", c="y")
    vnm_ax[1].set_ylabel("new_deaths", c="y")
    vnm_ax[1].set_title("2021", color="r")
    vnm_fig.suptitle(
        "The cumulative plot for new_deaths in Vietnam".upper(), c="b")

    plt.show()


def main():
    f = [v1, v2, v3, v4, v5, v6, v7, v8]
    choice = int(input("enter the answer do you want to show : "))
    return f[choice-1]()


if __name__ == "__main__":
    main()
