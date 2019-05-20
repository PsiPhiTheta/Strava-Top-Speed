# Strava-Top-Speed
A mini repo containing scripts to extract top speed from Strava .gpx data

## Step 0. Download your Strava data

- Go to: ```Settings > My Account > Download or Delete Your Account > Get Started > Request your archive``` 
- You will receive an email with a ```.zip``` file
- Extract the file and keep all the ```.gpx``` files
- Place the files in the same directory as the [main Python script](https://github.com/PsiPhiTheta/Strava-Top-Speed/blob/master/StravaTopSpeed.py) you downloaded from this repo
- Edit the Python script on line 13 to change the number of ```total_rides``` to the total number of ```.gpx``` files you have (in my case 112)

## Step 1. Download and install Python + libraries

- Download Python [here](https://www.python.org/downloads/)
- To install the libraries: ```pip install pandas``` and ```pip install gpxpy```

## Step 2. Run 

- Run the script and examine the output
