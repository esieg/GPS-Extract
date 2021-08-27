Purpose: A small tool to add GPS coordinates of images to Google Maps

1. check py-version
  - min: 3.7
  - cli-command: python --version
  - @Linux: try python3 instead
  - Installer: https://www.python.org/downloads/
2. install requirements
  - <python/python3> -m pip install -r reqs.txt
3. (MacOS) export your pictures from Pictures
  - left-click first to export
  - shift + left-click last to mark every photo
  - use command + left-click, if you have separate sections to export
  - after every picture is marked: Shift + CMD + E
  - check "Location information"
  - export to a subdirectory in this project
4. Run the Script
  - run from terminal: <python/python3> gpsExport.py <yourSubdirName>
  - you should receive a File named "export.txt"
5. Add the GPS-Locations to Googlemaps
  - Login in your Map
  - open edit-mode
  - open your export-file
  - Proposal: Double-Click a line, CMD + X (@MacOS) to cut out the line, and include this text in Google maps
  - click on the green bubble in the map and add this point to the map
