# Spreadsheet Analysis
A little assignment to practice finding data, munging it, and analyzing it in a spreadsheet program.
# Notice
## This is a joint assignment between Siteng Wu(sw4351) and Binxi Li (EllianaLi bl3134).

# Data set details
The data was found on [New York City OpenData](https://data.cityofnewyork.us/City-Government/Capital-Budget/46m8-77gv/data).

This dataset contains capital appropriation data by project type, budget line and source of funds. Amounts are in whole dollars. Data is created three times per year for the Preliminary Budget, Executive Budget and Adopted Budget to match appropriation numbers in the Capital Budget publication.

The original file is in CSV format, and the column names are included in the first row of data.
Display the head of data.

|Published Date|Project Type|Project Type Name|Budget Line|Budget Line Title|Funding Type|First Fiscal Year|Fiscal Year 1 Amount|Fiscal Year 2 Amount|Fiscal Year 3 Amount|Fiscal Year 4 Amount|
|---|---|---|---|---|---|---|---|---|---|---|
|20180201|AG|DEPARTMENT FOR THE AGING|AG 0001|"IMPROVEMENTS TO PROPERTY USED BY DEPARTMENT FOR THE AGING, CITYWIDE"|C|2019|3306783|3479000|2178000|1253000|
|20180201|AG|DEPARTMENT FOR THE AGING|AG 0002|"PURCHASE OF AUTOS, COMPUTERS, OTHER EQUIP FOR THE AGING, CITYWIDE"|C|2019|0|2342111|1403000|0|
|20180201|AG|DEPARTMENT FOR THE AGING|AG MN235|"LENOX HILL NEIGHBORHOOD HOUSE, INC."|C|2019|50000|0|0|0|
|20180201|BR|WATERWAY BRIDGES|BR 0231|"QUEENSBORO BRIDGE, REHABILITATION"|C|2019|141151222|0|0|0|
|20180201|BR|WATERWAY BRIDGES|BR 0253|RECONSTRUCTION OF WILLIAMSBURG BRIDGE|C|2019|0|0|273760919|0|
|20180201|BR|WATERWAY BRIDGES|BR 0270|REHABILITATION OF BROOKLYN BRIDGE|C|2019|289984124|0|0|15000000|
|20180201|BR|WATERWAY BRIDGES|BR 0287|RECONSTRUCTION: MACOMBS DAM BRIDGE OVER HARLEM RIVER|C|2019|0|93499|0|0|
|20180201|C|CORRECTION|C  0075|"CORRECTION FACILITIES, CONSTRUCTION, RECONS & IMPROVEMENTS, CITYWIDE"|C|2019|134751470|23330000|41300000|49384000|
|20180201|C|CORRECTION|C  0101|"SECURITY SYSTEMS, VARIOUS FACILITIES"|C|2019|0|0|1649995|0|
|20180201|C|CORRECTION|C  0112|PURCHASE OF EQUIPMENT FOR USE BY THE DEPT. OF CORRECTION|C|2019|4160367|4277000|3761000|3599000|
|20180201|C|CORRECTION|C  0114|"ACQUISITION, CONSTR., ETC. SUPPLEMENTARY HOUS. PROG. AND SUPPORT FACIL"|C|2019|82877375|0|0|0|
|20180201|CO|COURTS|CO 0080|27 MADISON AVE. - MANHATTAN APPELLATE DIVISION COURTHOUSE - 1ST DEPT.|C|2019|488500|0|0|0|
|20180201|CO|COURTS|CO 0081|31 CHAMBERS ST. - MANHATTAN SURROGATE'S COURT|C|2019|16689624|0|0|0|

The original data is already in a usable format, so we decided to modify the data a little bit to better suit the analysis part.

We removed several unnecessary columns first and then add one additional column summing the budget for each project across 4 fiscal years.

```
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
```

# Spreadsheet Analysis
Analysis:

Describe each of the aggregate statistic you have calculated - include a description of each 
and describe any insights the statistic shows that may not be obvious to someone just viewing the raw data.
If using a pivot table for analysis, include a Markdown table showing a sample of the results of the pivot table 
(no more than 20 rows, please), along with a short description of what the results show and any insights they offer.
If using a chart for visualization, include the chart image in the report, with a short description of what the image shows 
and any insights it offers. See the Markdown guide linked above for details of showing an image.

## Analysis Part 

In the Microsoft Excel, we did some analysis for the clean data of capital budget in sheet 1 amd sheet named
pivot_table and chart_table. 

### - Aggregated Statistics  
for the aggregate statistics, I have calculated the total amount of different budget titles in fiscal year 1,
fiscal year2, fiscal year 3, fiscal year 4 and the sum of 4 fiscal years. The budget amount in fiscal year 4 
is the largest. 
The amount is very large and Excel displays the number in scientific notation. Also, I have used the MAX() 
function to find the max budget amount and mean budget amount for each budget title (exclude those 0 records) 
in each fiscal year. We can see that the mean amount of each budget title is increasing from fiscal year 1 
to fiscal year 4.  
Since the base fiscal year differs from 2019 to 2023, I split the total amount in each fiscal year into 5 rows, 
resulting in a total budget amount starting at different years , from 2019 to 2023, in the specific 
fiscal year under that column. In each row, I also calculated the mean amount of budget for the specific budget line title ( excluding 0).  
In addition, I extract 15 different project types and calculated the total budget, occurrence times of each 
project type. The project type in short of "PV", which is about the culture investment and reconstruction of culture is
mentioned most frequently, while the project type in short of "L" is mentioned the least. Besides, I also found the max fiscal budget amount in fiscal year 1 under each program type.  

### - Pivot Table
sample:  
|.|AG|.|.|.|BR|.|.|.|  
|---|---|---|---|---|---|---|---|---|  
|row_label|Fiscal_Year1_Amount|Fiscal_Year2_Amount|Fiscal_Year3_Amount|Fiscal_Year4_Amount|Fiscal_Year1_Amount|Fiscal_Year2_Amount|Fiscal_Year3_Amount|Fiscal_Year4_Amount|
|2019|4833783|17614677|10071222|10679000|1159449992|132641499|810882757|47000000|  
|2020|4057000|1505111|16122095|2544000|353798427|148404000|43011116|827767688|  
|2021|4030000|11871228|387000|18999000|45546293|404427688|0|0|  
|2022|6503000|0|14793406|20115994|389922323|2227962|103852371|392728307|  
|2023|15383912|8496236|31944000|2675000|645868008|8888000|149811749|35000000|  
|total|34807695|39483648|73317723|55012994|2594585043|696589149|1107557993|1302495995|   

The pivot table shows that under different project categories, starting at 2019,2020,2021,2022,2023,
the total amount of each fiscal year. We can see that except 0, the fiscal budget in each fiscal year 
is millions!


### -Chart
Chart  
![Chart](/截屏2022-10-02 下午7.10.47.png)

<img height="200" src="/Users/libinxi/Desktop/大三/Database/workshhop/spreadsheet-analysis-EllianaLi-main/截屏2022-10-02 下午7.10.47.png" title="fiscal budget amount starting from differen years" width="300"/>(/Users/libinxi/Desktop/大三/Database/workshhop/spreadsheet-analysis-EllianaLi-main/截屏2022-10-02 下午7.10.47.png)


The image shows that starting from different years, the budget amount in fiscal year 1-4. Starting 
from 2019 to 2022, each fiscal year, the budget is below or around 5E+10, however, there is a significant 
increase when the starting year is 2023. The fiscal amount in each budget year
is 5-6 times than starting at years between 2019 to 2022.

# Extra Credit 
We think we deserve the extra credit as we choose to tackle with data tables which contain thousands of rows. It adds difficulty 
to munge data and do the analysis. Moreover, we choose to use the data visualization in two ways: pivot table and chart, which
contain different information. Your extra credit to this assignment would motivate us to continuously rise to 
more challenging work!



