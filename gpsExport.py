#!/usr/bin/env python
import os
import argparse
from exif import Image

def create_parser():
    '''create the parser'''
    parser = argparse.ArgumentParser()
    parser.add_argument('subdir')
    args = parser.parse_args()
    return(args.subdir)

def get_files(path):
    '''get all files in directory'''
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return(files)

def get_coords(file):
    '''get exif data from pic'''
    with open(file, 'rb') as inf:
        img = Image(inf)
    if img.has_exif:
        lats = img.gps_latitude
        lat = str(int(lats[0])) + '°' + str(int(lats[1])) + "'" + str(lats[2]) + f'"{img.gps_latitude_ref}'
        lons = img.gps_longitude
        lon = str(int(lons[0])) + '°' + str(int(lons[1])) + "'" + str(lons[2]) + f'"{img.gps_longitude_ref}'
        return({'lat': lat, 'lon': lon})
    else:
        return(None)

def write(lat, lon, csv):
    if(csv):
        with open('export.csv', 'a') as outf:
            outf.write(f'{str(lat)}; {str(lon)}\r\n')
    else:
        with open('export.txt', 'a') as outf:
            outf.write(f'{str(lat)} {str(lon)}\r\n')

if(__name__ == '__main__'):
    '''main_function'''
    subdir = create_parser()
    dir = os.path.join(os.getcwd(), subdir)
    files = get_files(dir)
    for file in files:
        file_path = os.path.join(dir, file)
        coords = get_coords(file_path)
        if(coords == None):
            continue
        write(coords['lat'], coords['lon'], False)
