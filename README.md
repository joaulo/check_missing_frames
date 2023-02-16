**Check Missing Frames**

A simple script that read files list from a folder, the folder MUST contain files with this pattern:
filename+number(4 digits)+extension(4 digits including period).
Example: "render1214.jpg"
The script assume files to be in sequence and look for "holes" in the sequence.
Missing files are reported in two different documents:
1. _missing_frames.txt_ : comma separated values of every single frame number missing, separated in rows by sequences
2. _missing_frames_range.txt_ : comma separated couple values, each couple representing start and end (inclusive) of the range that is missing.

**How To**

Open check_missing_frames.py file and edit these variables on row 8 and 9:
- _path_ = "path_to_the_folder"
- _num_of_frames_ = number_of_total_frames_expected_in_that_folder
Then run the script with Python.

**Future improvements**

- pass folder to examine as command line parameter?
- manage output files path?
- maybe a GUI?
- maybe a self executable?
