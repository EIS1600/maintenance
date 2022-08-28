###############################################################################
# PROJECT REUSABLE FUNCTIONS ##################################################
###############################################################################

import EIS1600func

fromPath = "./texts_mARkdown/"
toPath   = "./texts_EIS1600/"

file = "0795IbnRajabHanbali.DhaylTabaqatHanabila.Shamela0031366-ara1.mARkdown"
file = "0526IbnAbiYacla.TabaqatHanabila.JK000213-ara1.mARkdown"

inputFile = fromPath + file
outputFile = toPath + file.replace(".mARkdown", ".EIS1600")


# RUNNING CODE ################################################################

"""
1. convert mARkdown files into EIS1600
2. insert IDs into EIS1600 files
3. split EIS1600 into MUI files, and generate IDs file (keeps the order of MUI)
-- "manual" work at the pieces of text / digital analyses of MUI
4. reassembles the EIS1600 file from the MUIs, inserts missing IDs > rerun [3] > repeat the "work cycle"

* MUI - minimal unit of information
"""

with open(inputFile, "r", encoding = 'utf8') as f1:
    text = EIS1600func.convertToEIS1600(f1.read())
    # INSERT IDS
    #text = EIS1600func.
    with open(outputFile, "w", encoding = "utf8") as f9:\
        f9.write(text)


