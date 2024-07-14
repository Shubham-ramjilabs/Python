import csv
file="C:/Users/shubh/Downloads/8317_Age and sex by ethnic group (grouped total responses), for census night population counts, 2006, 2013, and 2018 Censuses (RC, TA, SA2, DHB)\DimenLookupEthnic8317.csv"
with open(file) as f:
    reader_file=csv.reader(f,delimiter='-')
    for row in reader_file:
        print(row)