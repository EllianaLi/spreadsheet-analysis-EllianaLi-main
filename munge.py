# place your code to clean up the data file below.
import csv
f = open("/Users/wusiteng/Desktop/DB Design/spreadsheet-analysis-Log1c11/data/Capital_Budget.csv", 'r')
csv_reader = csv.DictReader(f)
# preparation for output
csvfile =  open('/Users/wusiteng/Desktop/DB Design/spreadsheet-analysis-Log1c11/data/clean_data.csv', 'w', newline='')
fieldnames = ["Project Type",'Budget Line', 'Budget Line Title','First Fiscal Year','Fiscal Year 1 Amount', 'Fiscal Year 2 Amount','Fiscal Year 3 Amount','Fiscal Year 4 Amount', 'Total Budget $']
writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
writer.writeheader()

# already a pretty clean data
for line in csv_reader:
# removing unnecessary columns e.g. funding type, project type name
    title1 = "Funding Type"
    title2 = "Project Type Name"
    title3 = "Published Date"
    del line[title1]
    del line[title2]
    del line[title3]
# add necessary columns, total budget for 4 fiscal year, ignoring time value of money
    l = ['Fiscal Year 1 Amount', 'Fiscal Year 2 Amount','Fiscal Year 3 Amount','Fiscal Year 4 Amount']
    total = 0
    for key in line.keys():
        if key in l:
            total += int(line[key])
    line['Total Budget $'] = str(total)
# export to clean_data.csv
    writer.writerow(line)
csvfile.close()