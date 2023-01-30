from ii import*


def iii1():
    idn_cases = idn_deaths = jpg_cases = jpg_deaths = vnm_cases = vnm_deaths = 0

    for i in range(1, idn.shape[0]):
        if idn["new_cases"].loc[i] == idn["new_cases"].loc[i-1]:
            idn_cases += 1
        if idn["new_deaths"].loc[i] == idn["new_deaths"].loc[i-1]:
            idn_deaths += 1

    for i in range(1, jpg.shape[0]):
        if jpg["new_cases"].loc[i] == jpg["new_cases"].loc[i-1]:
            jpg_cases += 1
        if jpg["new_deaths"].loc[i] == jpg["new_deaths"].loc[i-1]:
            jpg_deaths += 1

    for i in range(1, vnm.shape[0]):
        if vnm["new_cases"].loc[i] == vnm["new_cases"].loc[i-1]:
            vnm_cases += 1
        if vnm["new_deaths"].loc[i] == vnm["new_deaths"].loc[i-1]:
            vnm_deaths += 1

    df1 = {"Indonesia": [idn_cases, idn_deaths],
           "Japan": [jpg_cases, jpg_deaths], "Vietnam": [vnm_cases, vnm_deaths]}
    df1 = pandas.DataFrame(df1, index=["new_cases", "new_deaths"])
    return df1


def iii2():
    idn_cases = idn_deaths = jpg_cases = jpg_deaths = vnm_cases = vnm_deaths = 0
    idn_cases_min, idn_deaths_min = idn[["new_cases", "new_deaths"]].min()
    jpg_cases_min, jpg_deaths_min = jpg[["new_cases", "new_deaths"]].min()
    vnm_cases_min, vnm_deaths_min = vnm[["new_cases", "new_deaths"]].min()

    for i in range(idn.shape[0]):
        if idn["new_cases"].loc[i] == idn_cases_min:
            if i == 0 or idn["new_cases"].loc[i] != idn["new_cases"].loc[i-1]:
                idn_cases += 1
        if idn["new_deaths"].loc[i] == idn_deaths_min:
            if i == 0 or idn["new_deaths"].loc[i] != idn["new_deaths"].loc[i-1]:
                idn_deaths += 1

    for i in range(jpg.shape[0]):
        if jpg["new_cases"].loc[i] == jpg_cases_min:
            if i == 0 or jpg["new_cases"].loc[i] != jpg["new_cases"].loc[i-1]:
                jpg_cases += 1
        if jpg["new_deaths"].loc[i] == jpg_deaths_min:
            if i == 0 or jpg["new_deaths"].loc[i] != jpg["new_deaths"].loc[i-1]:
                jpg_deaths += 1

    for i in range(vnm.shape[0]):
        if vnm["new_cases"].loc[i] == vnm_cases_min:
            if i == 0 or vnm["new_cases"].loc[i] != vnm["new_cases"].loc[i-1]:
                vnm_cases += 1
        if vnm["new_deaths"].loc[i] == vnm_deaths_min:
            if i == 0 or vnm["new_deaths"].loc[i] != vnm["new_deaths"].loc[i-1]:
                vnm_deaths += 1

    df2 = {"Indonesia": [idn_cases, idn_deaths],
           "Japan": [jpg_cases, jpg_deaths], "Vietnam": [vnm_cases, vnm_deaths]}
    df2 = pandas.DataFrame(df2, index=["new_cases", "new_deaths"])
    return df2


def iii3():
    idn_cases = idn_deaths = jpg_cases = jpg_deaths = vnm_cases = vnm_deaths = 0
    idn_cases_max, idn_deaths_max = idn[["new_cases", "new_deaths"]].max()
    jpg_cases_max, jpg_deaths_max = jpg[["new_cases", "new_deaths"]].max()
    vnm_cases_max, vnm_deaths_max = vnm[["new_cases", "new_deaths"]].max()

    for i in range(idn.shape[0]):
        if idn["new_cases"].loc[i] == idn_cases_max:
            if i == 0 or idn["new_cases"].loc[i] != idn["new_cases"].loc[i-1]:
                idn_cases += 1
        if idn["new_deaths"].loc[i] == idn_deaths_max:
            if i == 0 or idn["new_deaths"].loc[i] != idn["new_deaths"].loc[i-1]:
                idn_deaths += 1

    for i in range(jpg.shape[0]):
        if jpg["new_cases"].loc[i] == jpg_cases_max:
            if i == 0 or jpg["new_cases"].loc[i] != jpg["new_cases"].loc[i-1]:
                jpg_cases += 1
        if jpg["new_deaths"].loc[i] == jpg_deaths_max:
            if i == 0 or jpg["new_deaths"].loc[i] != jpg["new_deaths"].loc[i-1]:
                jpg_deaths += 1

    for i in range(vnm.shape[0]):
        if vnm["new_cases"].loc[i] == vnm_cases_max:
            if i == 0 or vnm["new_cases"].loc[i] != vnm["new_cases"].loc[i-1]:
                vnm_cases += 1
        if vnm["new_deaths"].loc[i] == vnm_deaths_max:
            if i == 0 or vnm["new_deaths"].loc[i] != vnm["new_deaths"].loc[i-1]:
                vnm_deaths += 1

    df3 = {"Indonesia": [idn_cases, idn_deaths],
           "Japan": [jpg_cases, jpg_deaths], "Vietnam": [vnm_cases, vnm_deaths]}
    df3 = pandas.DataFrame(df3, index=["new_cases", "new_deaths"])
    return df3


def iii4():
    no_new_report = iii1().T
    no_new_report.columns = ["Infections", "Deaths"]
    idn_new_report = idn.shape[0]-numpy.array(no_new_report.loc["Indonesia"])
    jpg_new_report = jpg.shape[0]-numpy.array(no_new_report.loc["Japan"])
    vnm_new_report = vnm.shape[0]-numpy.array(no_new_report.loc["Vietnam"])
    new_report = {"Indonesia": idn_new_report,
                  "Japan": jpg_new_report, "Vietnam": vnm_new_report}
    new_report = pandas.DataFrame(new_report, index=["Infections", "Deaths"]).T
    return "no_new_report :\n"+str(no_new_report)+"\n\nnew_report :\n"+str(new_report)


def iii5():
    pass


def iii6():
    pass


def iii7():
    idn_count = jpg_count = vnm_count = 0
    idn_min, jpg_min, vnm_min = idn.shape[0], jpg.shape[0], vnm.shape[0]

    for i in range(idn.shape[0]):
        if idn["new_cases"].loc[i] == 0:
            idn_count += 1
        elif i != 0 and idn["new_cases"].loc[i-1] == 0:
            if idn_count < idn_min:
                idn_min = idn_count
            idn_count = 0

    for i in range(jpg.shape[0]):
        if jpg["new_cases"].loc[i] == 0:
            jpg_count += 1
        elif i != 0 and jpg["new_cases"].loc[i-1] == 0:
            if jpg_count < jpg_min:
                jpg_min = jpg_count
            jpg_count = 0

    for i in range(vnm.shape[0]):
        if vnm["new_cases"].loc[i] == 0:
            vnm_count += 1
        elif i != 0 and vnm["new_cases"].loc[i-1] == 0:
            if vnm_count < vnm_min:
                vnm_min = vnm_count
            vnm_count = 0

    if idn_min == idn.shape[0]:
        idn_min = 0
    if jpg_min == jpg.shape[0]:
        jpg_min = 0
    if vnm_min == vnm.shape[0]:
        vnm_min = 0

    df7 = {"Indonesia": idn_min, "Japan": jpg_min, "Vietnam": vnm_min}
    df7 = pandas.DataFrame(df7, index=["min_date_no_case"])

    return df7


def iii8():
    idn_count = jpg_count = vnm_count = idn_max = jpg_max = vnm_max = 0

    for i in range(idn.shape[0]):
        if idn["new_cases"].loc[i] == 0:
            idn_count += 1
        elif i != 0 and idn["new_cases"].loc[i-1] == 0:
            if idn_count > idn_max:
                idn_max = idn_count
            idn_count = 0

    for i in range(jpg.shape[0]):
        if jpg["new_cases"].loc[i] == 0:
            jpg_count += 1
        elif i != 0 and jpg["new_cases"].loc[i-1] == 0:
            if jpg_count > jpg_max:
                jpg_max = jpg_count
            jpg_count = 0

    for i in range(vnm.shape[0]):
        if vnm["new_cases"].loc[i] == 0:
            vnm_count += 1
        elif i != 0 and vnm["new_cases"].loc[i-1] == 0:
            if vnm_count > vnm_max:
                vnm_max = vnm_count
            vnm_count = 0

    df7 = {"Indonesia": idn_max, "Japan": jpg_max, "Vietnam": vnm_max}
    df7 = pandas.DataFrame(df7, index=["min_date_no_case"])

    return df7


def main():
    f = [iii1, iii2, iii3, iii4, iii5, iii6, iii7, iii8]
    choice = int(input("enter the ex do you want to show : "))
    print(f[choice-1]())


if __name__ == "__main__":
    main()
