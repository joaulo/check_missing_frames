 
from os import listdir
from os.path import isfile, join

from itertools import groupby
from operator import itemgetter

path = "_cam_teaser_3600"
num_of_frames = 3600

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# print(onlyfiles)

rendered_frames = sorted([int(f[-8:-4]) for f in onlyfiles])

# print(rendered_frames)

full_seq = [n for n in range(1, num_of_frames + 1)]

# print(full_seq)

missing_frames = [f for f in full_seq if f not in rendered_frames]

# print(missing_frames)

missing_frames_list = []
with open("missing_frames.txt", "w") as f:
    for k, g in groupby(enumerate(missing_frames), lambda ix: ix[0] - ix[1]):
        missing_frames_range = list(map(itemgetter(1), g))
        f.write(', '.join(str(i) for i in missing_frames_range))
        f.write('\n')

        # print(missing_frames_range)

        if len(missing_frames_range) == 1:
            missing_frames_list.append(str(missing_frames_range[0]))
        else:
            missing_frames_list.append(str(missing_frames_range[0]) + "-" + str(missing_frames_range[-1]))
f.closed

with open("missing_frames_range.txt", "w") as f:
    f.write(', '.join(i for i in missing_frames_list))
f.closed

# print(missing_frames_list)
        