# Script to analyse NOS verkiezingen data

First the html from https://nos.nl/collectie/13860/artikel/2373037-bekijk-hier-de-uitslagen-van-de-verkiezingen was inspected
Based on the inspection it was determined that data is stored at https://d2vz64kg7un9ye.cloudfront.net/data/{cbscode gemeente}.json?v=1616023447
The cbscode of 'gemeentes' was downloaded from https://www.cbs.nl/-/media/_excel/2020/47/gemeenten-alfabetisch-2021.xlsx
The script `run.sh` downloads the election percentages data, the script `run_votes.sh` downloads the election votes. The downloaded file is a json file. 
The script stemmen.py and verkiezingen.py filter the data for party [5] (lijst 6: SP). If you are interested in other parties you need to change this filter.
The script barplot creates plots for every provence.

## Built with

- python 3.9.1
- pandas 15.1.0

## Run in the terminal

To get the percentage data for the Socialist Party 
```bash{}
bash run.sh
```
To get the votes e data for the Socialist Party 
```bash{}
bash run_votes.sh
```

To get the json file with all the info for gemeente cbs code 001
```bash{}
curl https://d2vz64kg7un9ye.cloudfront.net/data/001.json?v=1616023447 > 001.json
```

To create plots start jupyter notebooks and run barplot.ipynb


## Licence

<a href = "https://github.com/fenna/verkiezingen/blob/main/LICENSE"> Mozilla License </a>







