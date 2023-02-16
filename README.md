Check Missing Frames

A simple script that read files list from a folder, the folder MUST contain files with this pattern:
filename+number(4 digits)+extension(4 digits including period).
Example: "render1214.jpg"
The script assume files to be in sequence and look for "holes" in the sequence.
Missing files are reported in two different documents:
1. missing_frames.txt : comma separated values of every single frame number missing, separated in rows by sequences
2. missing_frames_range.txt : comma separated couple values, each couple representing start and end (inclusive) of the range that is missing.