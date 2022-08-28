import re

# IDs are to be assigned only to major logical units (they start with `###`)
# In order to assign an ID to a new logical unit:
#     1. `###` must be changed into `###$IDHOLDER$#`
#     2. Run this script:
#       - it will pick IDs from the list of 100k IDs
#       - it will save a new file with all the IDs from the text (*uri*.IDs)


inputTextFile  = "__texts_selected/0902Sakhawi.DawLamic.JK003608-ara1.mARkdownSimple"
inputTextFile  = "/Users/romanovienna/_OpenITI/0925AH/data/0902Sakhawi/0902Sakhawi.DawLamic/0902Sakhawi.DawLamic.JK003608-ara1.mARkdownSimple"
outputTextFile = inputTextFile
textFileIDs    = inputTextFile+".IDs"

reflowLen = 68
splitter = "#META#Header#End#"

from random import randint
def generate12IDs():
    IDs = []
    for i in range(0, 2000000):
        IDs.append(randint(100000000000, 999999999999)) 
    IDs = list(set(IDs))
    return(IDs)

import textwrap
# wraps long paragraphs: helps with viewing long files
def wrapPar(paragraph, lenSymb):
    wrapped = "\n".join(textwrap.wrap(paragraph, lenSymb))
    return(wrapped)

def reflowMain(main, unusedIDs):
    # reflow main
    print("="*80)
    print("Reflowing, this may take a few moments...")
    main = main.split("\n\n")

    mainUpdated = []

    count = 0
    for m in main:
        if m.startswith("###"):
            if "$IDHOLDER$" in m:
                count += 1
                m = m.replace("$IDHOLDER$", "$%s$" % unusedIDs[count])
            # m = updateID(m, count)
            # if len(m) > reflowLen:
            #     print("%s is too long" % m[:15])
            m = m.replace("\n", " ")
            m = m.replace("  ", " ")
            m = wrapPar(m, reflowLen)
            mainUpdated.append(m)
        elif "%~%" in m:
            mainUpdated.append(m)
        else:
            m = m.replace("\n", " ")
            m = m.replace("  ", " ")
            m = wrapPar(m, reflowLen)
            mainUpdated.append(m)

    main = "\n\n".join(mainUpdated)
    main = re.sub(r"\n(.{1,10})\n", r" \1\n", main)

    # morphological tags fixed
    main = re.sub(r"(\n#~:\w+:)\n", r"\1", main)

    # fix poetry
    main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)
    main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)
    main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)

    # spaces
    main = re.sub("\n +", "\n", main)
    main = re.sub(" +", " ", main)

    # offset morphological tags
    main = re.sub(r"(\n#~:[\w/]+:) ?", r"\1\n", main)

    return(main)

from datetime import datetime
startTime = datetime.now()

# 1. [Re]Insert IDs into headers / Update, if exist and are different (report!)
# 2. Reflow the file

def processIDs(inputTextFile):
    print("="*80)
    print("Processing IDs in: %s" % inputTextFile.split("/")[-1])
    print("="*80)

    outputTextFile  = inputTextFile#+".TEST"
    IDsFullList = generate12IDs()

    with open(inputTextFile, "r", encoding="utf8") as f1:

        text = f1.read().split(splitter)

        header = text[0]
        main = text[1].strip()

        # in case there are no IDs yet
        main = re.sub(r"(^|\n)### ", r"\1###$IDHOLDER$# ", main)
        IDholders = re.findall("###\$IDHOLDER\$#", main)

        usedIDsList = []
        usedIDs = re.findall(r"\n###\$(\d{12})\$#", main)
        usedIDsList.extend(usedIDs)
        unusedIDs = list(set(IDsFullList)-set(usedIDsList))

        print("\tIDs already in use:\t%d" % len(usedIDsList))
        print("\tIDs still unused:\t%d" % len(unusedIDs))
        print("\tIDs to be updated:\t%d" % len(IDholders))

        # get unused IDs

        # # update IDHOLDERS
        # counter = 0
        # for i in re.finditer(r"\$IDHOLDER\$", main):
        #     counter += 1
        #     main = re.sub(i.group(0), "$%s$" % unusedIDs[counter], main)
            
        #     if counter == 100:
        #         break

        main = reflowMain(main, unusedIDs)

        # reassemble text
        final = header + splitter + "\n\n" + main
        with open(outputTextFile, "w", encoding="utf8") as f9:
            f9.write(final)

        # collect all used IDs
        IDs = re.findall("\$\d{5}\$", final)
        IDs = "\n".join(IDs).replace("$", "")
        with open(outputTextFile+".IDs", "w", encoding="utf8") as f9:
            f9.write(IDs)
    

processIDs(inputTextFile)




print("===>" + str(datetime.now() - startTime))
print("Done!")
