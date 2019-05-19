# Author: Thomas Hollis
# Date: 19/05/2019
# Purpose: Extract top speed from all Strava .gpx files (they don't give it to you because they don't want to encourage
#          any 'dangerous' behaviour...

# 0. Import libraries
import gpxpy
import pandas as pd

# 1. Set up data structures
gpx_files = []
top_speeds = []
total_rides = 112  # add your total number of rides (.gpx files here)

# 2. Import data from folder
print("Importing all {} .gpx files ...".format(total_rides))

for i in range(0, total_rides):
    gpx_files.append(gpxpy.parse(open('Ride{}.gpx'.format(i),)))
    print("Imported {} .gpx files".format(i))

print("All {} gpx files successfully imported.".format(len(gpx_files)))

# 3. Extract top speed of all Strava rides (note: GPS glitches must be smoothed for reliable top speed)

# Experiments:

for j in range(0, len(gpx_files)):
    print("Processing Ride{}...".format(j))

    print("{} track(s)".format(len(gpx_files[j].tracks)))
    track = gpx_files[j].tracks[0]

    print("{} segment(s)".format(len(track.segments)))
    segment = track.segments[0]

    print("{} point(s)".format(len(segment.points)))

    data = []
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        data.append([point.longitude, point.latitude,
                     point.elevation, point.time, segment.get_speed(point_idx)])

    columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
    df = pd.DataFrame(data, columns=columns)
    top_speeds.append(max(df.Speed))

top = (max(top_speeds)/1000)*3600

print("================== Data analysis complete ==================")
print("Top speed of all analysed rides is: {:.2f} km/h.".format(top))
