# pholof

Generate a list of paths, metadata for files containing specified exif tag.

Sorting through hundreds or thousands of arbitrarily named files may require a considerable time investment. Use exising file exif metadata to find "low hanging fruit".

This module is intended for use with geolocation tags such

`Composite:GPSPosition: 43.0770722222222 -70.7521444444444`

## Requirements

-   ExifTool: http://www.sno.phy.queensu.ca/~phil/exiftool/
-   pyexiftool: https://github.com/smarnach/pyexiftool

## Usage

Call filesExifData=findExifFiles with:

-   directories: list of directories
-   tags: list of exif tags to search
-   exts: list of extenstion to include

Example:

## Example:

findExifFiles(['/tmp/photos4exif/']['gps longitude', 'gps latitude', 'gps position', 'composite:gpsposition'], ['.jpg', '.gif', '.jpeg', '.png'])

{"/tmp/photos4exif/img_0311-edited.jpg": {"Composite:GPSPosition": "43.0769916666667 -70.7520972222222"}, "/tmp/photos4exif/img_0312-edited.jpg": {"Composite:GPSPosition": "43.0770722222222 -70.7521444444444"}, "/tmp/photos4exif/img_0312.jpg": {"Composite:GPSPosition": "43.0770722222222 -70.7521444444444"}, "/tmp/photos4exif/img_0313-edited.jpg": {"Composite:GPSPosition": "43.0770722222222 -70.7521444444444"}, "/tmp/photos4exif/img_0314-edited.jpg": {"Composite:GPSPosition": "43.0770722222222 -70.7521444444444"} ...

## Notes

This is a simple tool which reads standard EXIF tags (see https://exiftool.org/TagNames/IPTC.html) It is primarily intended for extracting GPS data though any exif tag which exiftool can read should work.

## Other Interesting Projects

-   a simple ruby script which extracts GPS data from photos:

Digging into digital images: Extracting batch location data automatically: https://exposingtheinvisible.org/resources/image-digging
