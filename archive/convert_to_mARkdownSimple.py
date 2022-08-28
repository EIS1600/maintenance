import re, textwrap
import sys, os, shutil

sys.path.append("/Users/romanovienna/Dropbox/4.Research/PPE_Analysis/scripts/")
import ara, maintenance

magicValueOld = "######OpenITI#"
magivValueNew = "#OpenITI################################################"
metadataHeadO = "#META#Header#End#"
metaDataHeadN = "#METADATAEND############################################"

# main variables - files
textFolder = "./__texts_selected/retired/"
textFile = "0748Dhahabi.TarikhIslam.Shamela0035100-ara1.mARkdown"

reflowLen = 68

# the script removes tags from the text.

###############################################################################################
# FUNCTIONS ###################################################################################
###############################################################################################

from random import randint
def generate12IDs(iterations):
    IDs = []
    for i in range(0, iterations):
        IDs.append(str(randint(100000000000, 999999999999)))
    IDs = list(set(IDs))
    print("IDs: {:,}".format(len(IDs)))
    return(IDs)

import textwrap
# wraps long paragraphs: helps with viewing long files
def wrapPar(paragraph, lenSymb):
    wrapped = "\n".join(textwrap.wrap(paragraph, lenSymb))
    return(wrapped)

###############################################################################################

from datetime import datetime
startTime = datetime.now()

# convert from old mARkdown into new simplified

def fromOldToSimple(filePath, IDs):
    with open(filePath, "r", encoding="utf8") as f1:
        data = f1.read()

        data = data.replace(magicValueOld, magivValueNew)
        data = data.replace(metadataHeadO, metaDataHeadN)

        header = re.split(metaDataHeadN, data)[0]
        text   = re.split(metaDataHeadN, data)[1]

        sections = re.split("\n#", text)

        sectionsNew = []

        for s in sections[1:]:
            s = s.replace("\n~~", " ").strip()

            if s.startswith("#"):
                # header
                s = re.sub("^#+ ", "# ", s)
                
            else:
                # paragraph
                if "%~%" in s:
                    s = "===%s===" % s
                else:
                    s = wrapPar(s, reflowLen)


            sectionsNew.append(s.strip())


    data = "\n\n".join(sectionsNew)

    # joining poetry lines (there should be only one \n between the lines of the same poem)
    data = data.replace("===\n\n===", "\n")
    data = data.replace("===\n", "\n").replace("\n===", "\n")

    # REPLACE SOME ELEMENTS
    data = data.replace("Milestone300", "ms000")

    # ADD IDS
    data  = data.split("\n\n")
    dataNew = []

    for i in range(0, len(data)):
        passage = data[i]
        idnum   = IDs[i]

        if passage.startswith("#"):
            passage = passage.replace("#", "#$%s$#" % idnum)
        else:
            passage = "$%s$ ~\n" % idnum + passage

        dataNew.append(passage)

    data = "\n\n".join(dataNew)
    data = header + "\n%s\n\n" % metaDataHeadN + data

    # remove extra spaces
    data = re.sub("  +", " ", data).replace("\n ", "\n").replace(" \n", "\n")

    with open(filePath.replace(".mARkdown", ".mARkdownSimple_TEST"), "w", encoding="utf8") as f9:
        f9.write(data)


IDs = generate12IDs(5000000)
filePath = os.path.join(textFolder, textFile)
fromOldToSimple(filePath, IDs)

print("===>" + str(datetime.now() - startTime))
print("Done!")
