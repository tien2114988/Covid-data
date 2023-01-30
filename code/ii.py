from main import*

ii = df[(df["location"] == 'Indonesia') | (
    df["location"] == 'Vietnam') | (df["location"] == 'Japan')]

idn = ii[ii["location"] == 'Indonesia']
jpg = ii[ii["location"] == 'Japan']
vnm = ii[ii["location"] == 'Vietnam']

idn.reset_index(drop=True, inplace=True)
jpg.reset_index(drop=True, inplace=True)
vnm.reset_index(drop=True, inplace=True)


def ii1():
    idn_max = list(idn[["new_cases", "new_deaths"]].max())
    jpg_max = list(jpg[["new_cases", "new_deaths"]].max())
    vnm_max = list(vnm[["new_cases", "new_deaths"]].max())

    idn_min = list(idn[["new_cases", "new_deaths"]].min())
    jpg_min = list(jpg[["new_cases", "new_deaths"]].min())
    vnm_min = list(vnm[["new_cases", "new_deaths"]].min())

    df1 = {"Indonesia": idn_max+idn_min, "Japan":
           jpg_max+jpg_min, "Vietnam": vnm_max+vnm_min}

    df1 = pandas.DataFrame(
        df1, index=["Max_cases", "Max_deaths", "Min_cases", "Min_deaths"])

    return df1


def ii2():
    idn_med2 = list(idn[["new_cases", "new_deaths"]].median())
    jpg_med2 = list(jpg[["new_cases", "new_deaths"]].median())
    vnm_med2 = list(vnm[["new_cases", "new_deaths"]].median())

    idn_sort_case = idn.sort_values("new_cases")
    idn_sort_death = idn.sort_values("new_deaths")
    jpg_sort_case = jpg.sort_values("new_cases")
    jpg_sort_death = jpg.sort_values("new_deaths")
    vnm_sort_case = vnm.sort_values("new_cases")
    vnm_sort_death = vnm.sort_values("new_deaths")

    idn_med1_case = idn_sort_case["new_cases"][:idn.shape[0]//2].median()
    idn_med1_death = idn_sort_death["new_deaths"][:idn.shape[0]//2].median()
    jpg_med1_case = jpg_sort_case["new_cases"][:jpg.shape[0]//2].median()
    jpg_med1_death = jpg_sort_death["new_deaths"][:jpg.shape[0]//2].median()
    vnm_med1_case = vnm_sort_case["new_cases"][:vnm.shape[0]//2].median()
    vnm_med1_death = vnm_sort_death["new_deaths"][:vnm.shape[0]//2].median()

    idn_med3_case = idn_sort_case["new_cases"][idn.shape[0]//2+1:].median()
    idn_med3_death = idn_sort_death["new_deaths"][idn.shape[0]//2+1:].median()
    jpg_med3_case = jpg_sort_case["new_cases"][jpg.shape[0]//2+1:].median()
    jpg_med3_death = jpg_sort_death["new_deaths"][jpg.shape[0]//2+1:].median()
    vnm_med3_case = vnm_sort_case["new_cases"][vnm.shape[0]//2+1:].median()
    vnm_med3_death = vnm_sort_death["new_deaths"][vnm.shape[0]//2+1:].median()

    df2 = {"Indonesia": [idn_med1_case, idn_med1_death]+idn_med2+[idn_med3_case, idn_med3_death],
           "Japan": [jpg_med1_case, jpg_med1_death]+jpg_med2+[jpg_med3_case, jpg_med3_death],
           "Vietnam": [vnm_med1_case, vnm_med1_death]+vnm_med2+[vnm_med3_case, vnm_med3_death]}

    df2 = pandas.DataFrame(
        df2, index=["Q1_cases", "Q1_deaths", "Q2_cases", "Q2_deaths", "Q3_cases", "Q3_deaths"])

    return df2


def ii3():
    idn_mean = idn[["new_cases", "new_deaths"]].mean()
    jpg_mean = jpg[["new_cases", "new_deaths"]].mean()
    vnm_mean = vnm[["new_cases", "new_deaths"]].mean()

    df3 = {"Indonesia": list(idn_mean), "Japan":
           list(jpg_mean), "Vietnam": list(vnm_mean)}

    df3 = pandas.DataFrame(df3, index=["Average_cases", "Average_deaths"])

    return df3


def ii4():
    idn_std = idn[["new_cases", "new_deaths"]].std()
    jpg_std = jpg[["new_cases", "new_deaths"]].std()
    vnm_std = vnm[["new_cases", "new_deaths"]].std()

    df4 = {"Indonesia": list(idn_std), "Japan":
           list(jpg_std), "Vietnam": list(vnm_std)}

    df4 = pandas.DataFrame(df4, index=["Std_cases", "Std_deaths"])

    return df4


def ii5():
    Q1 = ii2()[0:2]
    Q2 = ii2()[2:4]
    Q3 = ii2()[4:6]

    idn_IQR_case = Q3["Indonesia"][0]-Q1["Indonesia"][0]
    idn_IQR_death = Q3["Indonesia"][1]-Q1["Indonesia"][1]
    idn_out_case = idn["new_cases"][(idn["new_cases"] < Q1["Indonesia"][0]-1.5*idn_IQR_case)
                                    | (idn["new_cases"] > Q3["Indonesia"][0]+1.5*idn_IQR_case)].count()
    idn_out_death = idn["new_deaths"][(idn["new_deaths"] < Q1["Indonesia"][1]-1.5*idn_IQR_death)
                                      | (idn["new_deaths"] > Q3["Indonesia"][1]+1.5*idn_IQR_death)].count()

    jpg_IQR_case = Q3["Japan"][0]-Q1["Japan"][0]
    jpg_IQR_death = Q3["Japan"][1]-Q1["Japan"][1]
    jpg_out_case = jpg["new_cases"][(jpg["new_cases"] < Q1["Japan"][0]-1.5*jpg_IQR_case)
                                    | (jpg["new_cases"] > Q3["Japan"][0]+1.5*jpg_IQR_case)].count()
    jpg_out_death = jpg["new_deaths"][(jpg["new_deaths"] < Q1["Japan"][1]-1.5*jpg_IQR_death)
                                      | (jpg["new_deaths"] > Q3["Japan"][1]+1.5*jpg_IQR_death)].count()

    vnm_IQR_case = Q3["Vietnam"][0]-Q1["Vietnam"][0]
    vnm_IQR_death = Q3["Vietnam"][1]-Q1["Vietnam"][1]
    vnm_out_case = vnm["new_cases"][(vnm["new_cases"] < Q1["Vietnam"][0]-1.5*vnm_IQR_case)
                                    | (vnm["new_cases"] > Q3["Vietnam"][0]+1.5*vnm_IQR_case)].count()
    vnm_out_death = vnm["new_deaths"][(vnm["new_deaths"] < Q1["Vietnam"][1]-1.5*vnm_IQR_death)
                                      | (vnm["new_deaths"] > Q3["Vietnam"][1]+1.5*vnm_IQR_death)].count()

    df5 = {"Indonesia": [idn_out_case, idn_out_death], "Japan": [
        jpg_out_case, jpg_out_death], "Vietnam": [vnm_out_case, vnm_out_death]}
    df5 = pandas.DataFrame(df5, index=["Outlier_cases", "Outlier_deaths"])

    return df5


def ii6():
    Countries = ["Indonesia", "Japan", "Vietnam"]
    Max_cases, Max_deaths, Min_cases, Min_deaths = list(ii1().values)
    Q1_cases, Q1_deaths, Q2_cases, Q2_deaths, Q3_cases, Q3_deaths = list(
        ii2().values)
    Average_cases, Average_deaths = list(ii3().values)
    Std_cases, Std_deaths = list(ii4().values)
    Outlier_cases, Outlier_deaths = list(ii5().values)

    df6_case = {"Countries": Countries, "Min": Min_cases, "Q1": Q1_cases, "Q2": Q2_cases, "Q3": Q3_cases,
                "Max": Max_cases, "Avg": Average_cases, "Std": Std_cases, "Outlier": Outlier_cases}
    df6_death = {"Countries": Countries, "Min": Min_deaths, "Q1": Q1_deaths, "Q2": Q2_deaths, "Q3": Q3_deaths,
                 "Max": Max_deaths, "Avg": Average_deaths, "Std": Std_deaths, "Outlier": Outlier_deaths}

    df6_case = pandas.DataFrame(df6_case)
    df6_death = pandas.DataFrame(df6_death)

    return f"\t\t\t\tnew_cases\n{df6_case}\n\n\t\t\t\tnew_deaths\n{df6_death}"


def ii7():
    fig, (case, death) = plt.subplots(nrows=1, ncols=2)
    seaborn.boxplot(data=ii, x="location", y="new_cases", ax=case)
    seaborn.boxplot(data=ii, x="location", y="new_deaths", ax=death)
    fig.suptitle(
        "The new_cases/new_deaths boxplot in Indonesia , Japan and Vietnam".upper(), c="b")
    return plt.show()


def main():
    f = [ii1, ii2, ii3, ii4, ii5, ii6, ii7]
    choice = int(input("enter the answer do you want to show : "))
    print(f[choice-1]())


if __name__ == "__main__":
    main()
