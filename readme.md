# Tools for personal use

It was for the purpose of learning `Python`.

```commandline
python3 -V
Python 3.10.12
```

## Tool `img_by_folder`

I needed to transfer files from my smartphone to my computer. 
All media files on the smartphone are in one folder such as photos, panoramas and videos.

File names on the smartphone are stored as:

POCO X4 Pro
```
IMG_20230917_082434.jpg
VID_20230917_071501.mp4
PANO_20230511_185250.jpg
```
or 

Realme 6, Redmi 5+
```
IMG20230917082434.jpg
VID20230917071501.mp4
```

After copying these files from the smartphone, I would like to have a folder structure 
with the dates: 
```
2023-05
2023-09
``` 
and in them the files corresponding to this date.

### Move files to directories 

`photos.py` - takes all file names from the specified directory. 

Files must have the format `prefix_YYYYMMDD_HHMMSS`. 

Creates a directory named `YYYY-MM` from the file name and moves files 
corresponding to the year and month there. 

`prefix_` can be 4 or 5 characters long. For example, `IMG_`, `VID_`, `PANO_`.

### Move files from directories 

`photos_undo.py` - is the inverse of the previous operation. Takes all files in subdirectories of the specified directory and moves the files into it. The subdirectories are deleted.

**Disclaimer**

The author of the scripts is not responsible for any damages or issues 
arising from the use of the scripts. It is recommended to create backups 
of your data and folders before using the scripts to avoid data loss.
