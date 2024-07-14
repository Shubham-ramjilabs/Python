import csv
import csv

csv.register_dialect('custom_dialect',
    delimiter='|',
    quotechar='"',
    doublequote=True,
    skipinitialspace=True,
    lineterminator='\n',
    quoting=csv.QUOTE_MINIMAL
)

# Using the custom dialect
file='C:/Users/shubh/Downloads/8317_Age and sex by ethnic group (grouped total responses), for census night population counts, 2006, 2013, and 2018 Censuses (RC, TA, SA2, DHB)\DimenLookupEthnic8317.csv'
with open(file, 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='custom_dialect')
    for row in reader:
        print(row)
