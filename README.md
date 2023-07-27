# Sunrise and Sunset Times in Austin
This Python script retrieves sunrise and sunset times for Austin, Texas using the Sunrise-Sunset API (https://sunrise-sunset.org/api). The retrieved data is then written to a CSV file.

## How it works
1. The script uses the `requests` library to send a GET request to the Sunrise-Sunset API.
2. The latitude and longitude of Austin (30.267153, -97.743057) are specified in the request.
3. The response from the API is a JSON object containing the sunrise and sunset times, as well as other solar-related data.
4. The script parses this response to extract the sunrise and sunset times.
5. These times are then written to a CSV file named 'sunrise_sunset_austin.csv'.

## Prerequisites
Ensure that you have the following installed:
* Python 3
* The `requests` library. If you don't have it installed, you can install it using pip:
```shell
pip install requests
```

## Usage
Run the script with Python:
```shell
python3 <script_name>.py
```
Replace `<script_name>` with the name of the Python file.

After running the script, you'll find a file named 'sunrise_sunset_austin.csv' in your current directory. The file will contain the sunrise and sunset times.

## Important note
This script is set to get sunrise and sunset times for the year 2021 and the city of Austin, Texas. You may need to modify the parameters in the script to suit your needs.

## Author
Inhyeok Lee

## Created on
Sat Nov 6 2021
