# Travel Audience Data Science Recruitment Challenge

Given a csv file, logs.csv, containing ad impressions as records with multiple fields ‘uuid’, ‘ts’, ‘useragent’, and ‘hashed_ip’, compute the following features for each record:
1.	highly_active: Whether the user is highly active, i.e. has a large number of events (True/False)
2.	multiple_days: Whether the user is active for multiple days (True/False)
3.	weekday_biz: Whether the user's traffic tends to occur during weekday business hours (True/False)
4.	One additional feature of my choice. (True/False, or numeric.)
device_type: To find which type of device the user has used. (Numeric)

## Infrastructure, Technologies and Libraries used
1. Windows 10
2. Python 3.5.2
3. Pandas
4. Numpy
5. Matplotlib

## Project File Structure

travel_audience_ds_task/&nbsp;&nbsp;<--------------- Project root <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;plots/&nbsp;&nbsp;<--------------------------------- Plots folder which contains the output graphs <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Highly_Active_Users_Plot.png&nbsp;&nbsp;<--- User's histogram based on number of days activity <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users_Histogram.png&nbsp;&nbsp;<------------ Visualization of highly active users <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config.py&nbsp;&nbsp;<----------------------------- Config file containing major constants used in codes <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_processing.py&nbsp;&nbsp;<------------------ Implementation of feature extraction, data visualization and its supporting functions <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;features_computation.py&nbsp;&nbsp;<------------ Main python file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;README.md <--------------------------- Readme file

## How to use

Run features_computation.py as below from command-line:
```sh/cmd
$ python features_computation.py logs.csv output.csv
```
Note: full file path is required. For example: "python features_computation.py ./data/logs.csv ./data/output.csv"

## Sample Console Result or Logs

Fetching data from input file and creating the DataProcessing Object...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DataProcessing object created<br>
Data visualization...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of highly active users - 273<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Other users count -- 257081<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Plots are generated in ./plots folder<br>
Extracting features...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extracted highly_active feature<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extracted multiple_days feature<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extracted weekday_biz feature<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extracted device_type feature<br>
Time (in minutes) taken to generate plots and extract required features and write the output into a file - 8.291095495563303<br>

## First 10 records of output.csv
uuid,highly_active,multiple_days,weekday_biz,device_type
313908E1F6825D28ADF3FCE451E5B5E5,False,False,True,1
C7F60E6140A59120D9C9854CA87758DF,False,False,False,3
2DC20DA3585AEDFD846E8679AE5C14C7,False,True,True,3
1C8B0E355480105C5C5B8B466399155F,False,True,True,3
86F243798AE16A55AFC1D3293279CCD5,False,True,True,3
42F14D0B0C6D827EDE671491904B5EBD,False,False,False,1
8DFC1B8495A5EF100CEA682AFB8C7D7C,False,True,False,3
9D758258C16B9A597D9E31249B2DF25C,False,True,False,3
BDBF7B79FF78AA95EBF7211B22E7E97D,False,False,False,1
...

## Author

Harish Kumar Govindaswamy Saravanam
