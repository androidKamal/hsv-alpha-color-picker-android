import re

files = ["../README.md", "../colorpicker/build.gradle", "../demo_app/build.gradle"]

new_version_code = "30001"
new_version_string = "3.0.1"

for file in files:
    with open(file, "rb") as f:
        old = f.read()
    new = old
    new = re.sub("versionCode \d+", "versionCode "+new_version_code, new)
    new = re.sub("versionName '[\d.]+'", "versionName '{}'".format(new_version_string), new)
    new = re.sub("libraryVersion = '[\d.]+'", "libraryVersion = '{}'".format(new_version_string), new) 
    new = re.sub("implementation 'com.rarepebble:colorpicker:[\d.]+'",
        "compile 'com.rarepebble:colorpicker:{}'".format(new_version_string), new)

    with open(file, "wb") as f:
        f.write(new)