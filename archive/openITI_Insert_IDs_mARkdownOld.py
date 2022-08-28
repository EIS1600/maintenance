import re, sys

inputFile = "0748Dhahabi.TarikhIslam.MGR20180917-ara1.mARkdownSimple"
outputFile = inputFile

reflowLen = 68

splitter = "#META#Header#End#"

import textwrap
# wraps long paragraphs: helps with viewing long files
def wrapPar(paragraph, lenSymb):
    wrapped = "\n~~".join(textwrap.wrap(paragraph, lenSymb))
    return(wrapped)

from datetime import datetime
startTime = datetime.now()

# 1. [Re]Insert IDs into headers / Update, if exist and are different (report!)
# 2. Reflow the file

def updateID(passage, count):
    newID = "###$%09d$#" % count
    if "### " in passage:
        passage = passage.replace("### ", "%s " % newID)
        #input(passage)
    elif "%s " % newID in passage:
        pass
        #print("\t- Passage ID has not changed: %s" % newID)
    elif "###$"  in passage:
        print("Passage ID has changed:")
        oldID = re.search(r"(###\$\d+\$#)", passage).group(1)
        print("\twas: %s" % oldID)
        print("\tnew: %s" % newID)
        passage = passage.replace(oldID, newID)
        print("="*80)
        print(passage)
        print("="*80)
        input()

    return(passage)


def reflowMdSimple(inputFile):
    with open(inputFile, "r", encoding="utf8") as f1:

        text = f1.read().split(splitter)

        header = text[0]
        main = text[1].strip()

        main = main.replace("\n~~", " ")

        # [re]insert IDs
        altSpaceRE = "[^ٱء-ي]+"
        main = re.split(r"(%s)" % altSpaceRE, main)

        length = len(main)-1

        #print(main[length-1])
        #input(main[length])

        newText = []
        for i in range(0, length):
            item = updateID(main[i], i)
            newText.append(item)
            

        main = "".join(newText)

        # reflow main
        main = main.split("\n")

        mainUpdated = []

        count = 0

        for m in main:
            count += 1
            if "%~%" in m:
                mainUpdated.append(m)
            else:
                m = wrapPar(m, reflowLen)
                mainUpdated.append(m)

        main = "\n".join(mainUpdated)
        main = re.sub(r"\n(.{1,10})\n", r" \1\n", main)

        # morphological tags fixed
        main = re.sub(r"(\n#~:\w+:)\n", r"\1", main)

        # fix poetry
        #main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)
        #main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)
        #main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)

        # spaces
        main = re.sub("\n +", "\n", main)
        main = re.sub(" +", " ", main)

        # offset morphological tags
        main = re.sub(r"(\n#~:[\w/]+:) ?", r"\1\n", main)

        # reassemble text
        final = header + splitter + "\n\n" + main
        with open(outputFile, "w", encoding="utf8") as f9:
            f9.write(final)
    

#reflowMdSimple(inputFile)

# # The following function checks if a file gets messed up or not: test is passed!
# def compare(file):
#     with open(file, "r", encoding="utf8") as f1:
#         text1 = f1.read()
#         text1 = re.sub("###(\$\d+\$#)?", "", text1)
#         text1 = re.sub("###", "", text1)
#         text1 = re.sub("\s+", "", text1)

#     with open(file+"_TEST", "r", encoding="utf8") as f2:
#         text2 = f2.read()
#         text2 = re.sub("###(\$\d+\$#)?", "", text2)
#         text2 = re.sub("\s+", "", text2)

#     if text1 == text2:
#         print("Text1 == Text2")
#     else:
#         print("Text1 != Text2")

# compare(inputFile)

def main():
    if len(sys.argv) == 2:
        reflowMdSimple(sys.argv[1])
    else:
        print("Wrong command! It should be:")
        print("\tpython3 openITI_Insert_IDs_mARkdownOld.py path_to_file")

main()


print("===>" + str(datetime.now() - startTime))
print("Done!")
