import re, textwrap
import sys, os.path, shutil

sys.path.append("/Users/romanovienna/Dropbox/4.Research/PPE_Analysis/scripts/")
import ara, maintenance

# main variables - files
textFolder = "./__texts_selected/"
textFile = "0748Dhahabi.TarikhIslam.MGR20180917-ara1.mARkdownSimple"

# the script removes tags from the text.

from datetime import datetime
startTime = datetime.now()

def cleanTags(file, pattern):
    with open(file, "r", encoding="utf8") as f1:
        data = f1.read()

        data = re.sub(pattern, "", data)

        with open(file, "w", encoding="utf8") as f9:
            f9.write(data)


cleanTags(textFolder+textFile, "@[^ ]+@")

#import subprocess
#subprocess.call("cd .. && python3 a_Insert_IDs.py", shell=True)

print("===>" + str(datetime.now() - startTime))
print("Done!")
