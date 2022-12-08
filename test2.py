import pandas as pd

data = pd.read_csv("GlassdoorGenderPayGap.csv")
data.sort_values(by="Education", inplace=True)

def extractEducation(df, Education):
    new_df = pd.DataFrame()
    for i in range(len(data)):
        if (df.loc[i, "Education"]) == Education:
            new_df = pd.concat([new_df, df.loc[i].to_frame().T])
        else:
            continue
    return new_df

high_school_graduates = extractEducation(data, "High School")
college_graduates = extractEducation(data, "College")
masters_graduates = extractEducation(data, "Masters")
phd_graduates = extractEducation(data, "PhD")

hs_basepay_avg = high_school_graduates["BasePay"].mean()
college_basepay_avg = college_graduates["BasePay"].mean()
masters_basepay_avg = masters_graduates["BasePay"].mean()
phd_basepay_avg = phd_graduates["BasePay"].mean()

print(hs_basepay_avg)
print(college_basepay_avg)
print(masters_basepay_avg)
print(phd_basepay_avg)