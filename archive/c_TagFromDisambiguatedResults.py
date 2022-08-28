import re, textwrap
import sys, os.path, shutil

# the script is designed to tag gazetteer items in a text from, by mapping
# disambiguated results

from datetime import datetime
startTime = datetime.now()

# main variables: files

textFolder = "./__texts_selected/"
textFile   = "0748Dhahabi.TarikhIslam.MGR20180917-ara1.mARkdownSimple"
textFilePath   = textFolder + textFile

rootFolder = "./_root_based_search/_extracted_data/"
rootFilePath   = rootFolder + textFile + ".RootList_PREACHING.csv"

topoFolder = "./_toponym_matching/_extracted_data/"
topoFilePath   = topoFolder + textFile + ".ToponymicData.csv"

# rootTag:

def loadRootDataIntoDic(rootDataFile):
    pass


topoClassDic = {
    "0" : "exclude",
    "book" : "grey",
    "dir" : "grey",
    "ethno" : "grey",
    "false" : "exclude",
    "general" : "exclude",
    "minor" : "grey",
    "new" : "exclude",
    "person" : "grey",
    "review" : "grey",
    "true" : "yellow", # "orange"
    "water" : "grey",
    "wrong" : "grey"
}

def loadTopoDataIntoDic(topoDataFile):
    with open(topoDataFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        TopoMatches = {}

        for d in data:
            d = d.split("\t")
            #  9 --- review status
            # 11 --- TXX tag
            # 12 --- index position
            # 13 --- URIs
            if topoClassDic[d[9]] != "exclude":
                tag = "%s@%s@-@%s@" % (d[11], d[13], d[9])
                TopoMatches[int(d[12])] = tag
                #input(TopoMatches)

    return(TopoMatches)

def loadRootDataIntoDic(rootDataFile):
    with open(rootDataFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        RootMatches = {}

        for d in data:
            d = d.split("\t")
            #  9 --- review status
            # 12 --- index position
            # 13 --- URIs (TAGS)
            if d[9] != "false":
                tag = "@MGR@%s@-@%s@" % (d[13], d[9])
                RootMatches[int(d[12])] = tag
                #input(RootMatches)

    return(RootMatches)

# global variables
splitter = "#META#Header#End#"
altSpaceRE = "[^ٱء-ي]+"
reflowLen = 68

import textwrap
# wraps long paragraphs: helps with viewing long files
def wrapPar(paragraph, lenSymb):
    wrapped = "\n".join(textwrap.wrap(paragraph, lenSymb))
    return(wrapped)

def reflowMain(main):
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


# 1. load main text
#       1. open main text
#       2. split into the list in the same manner as GazMatcher
# 2. load disambiguated results


# tagging with a taggingScheme

# REPORT STRUCTURE
#  0 : match          - complete match as a key
#  1 : display        - reformatted match for display
#  2 : ng1            - ngrams (tagged-3)
#  3 : ng2            - ngrams (tagged-2)
#  4 : ng3            - ngrams (tagged-1)
#  5 : tagged (ng4)   - ngrams (tagged-0)
#  6 : ng5            - ngrams (tagged+1)
#  7 : ng6            - ngrams (tagged+2)
#  8 : ng7            - ngrams (tagged+3)
#  9 : "status"       - status of review
# 10 : "probability"  - probabilities, based on ngram extrapolations
# 11 : "ngram"        - ngrams (numbers), for matches exclude/include
# 12 : "position"     - position in the text broken into list on space
# 13 : "middleTag"    - tagged item as it appears in the text
# 14 : "gazForm"      - gazetteer form of an item
# 15 : "fileName"     - the name of the file

# RE for TAGs

# ROOT MATCHES                           |  TOPO MATCHES
# @\w\w\w@\w+@General@-@00@ > grey       |  @TXX@Uri(,Uri)+@-@00@ > orange
#                                        |
# @\w\w\w@\w+@General@-@t[amt]@ > yellow |  << These are depricated
# @\w\w\w@\w+@General@-@f[amt]@ > orange |  << These are depricated 
#                                        |
# @\w\w\w@\w+@General@-@tr@ > green      |  @TXX@Uri@-@tr@ > green
# @\w\w\w@\w+@General@-@fr@ > red        |  FALSE: remove/delete
#                                        |
# @\w\w\w@\w+@\w+@-@tr@ > blue           |  @TXX@NOURI@-@00@ > yellow

def mappingDisResults(textFile, topoDataFile):
    print("="*80)
    print("===>now, starting mapping tags into the text (from disambiguated resutls):\n\t\t%s" % textFile)
    print("===>" + str(datetime.now() - startTime))
    print("="*80)

    TopoDataDic = loadTopoDataIntoDic(topoDataFile)
    RootDataDic = loadRootDataIntoDic(rootFilePath)   

    # open text file
    with open(textFile, "r", encoding="utf8") as f1:
        textOriginal = f1.read()
        text = textOriginal.split(splitter)

        header = text[0]
        main = text[1].strip()

        altSpaceRE = "[^ٱء-ي]+"
        main = re.split(r"(%s)" % altSpaceRE, main)

        for i in range(0, len(main), 1):
            if i in RootDataDic:
                main[i-1] = main[i-1] + " %s " % RootDataDic[i]

        for i in range(0, len(main), 1):
            if i in TopoDataDic:
                main[i-1] = main[i-1] + " %s " % TopoDataDic[i]

        main = reflowMain("".join(main))

        taggedText = header + splitter+ "\n\n\n" + main
        taggedText = re.sub(" +", " ", taggedText)
        taggedText = re.sub("\n +", "\n", taggedText)

    # save main text
    with open(textFile+".TEST", "w", encoding="utf8") as f9:
        f9.write(taggedText)

    # # TEST for consistency: text and taggedText    
    # altSpaceRE = "[^ٱء-ي]+"
    # textOriginal = re.sub(r"(%s)" % altSpaceRE, " ", textOriginal)
    # taggedText = re.sub(r"(%s)" % altSpaceRE, " ", taggedText)

    # print(len(textOriginal))
    # print(len(taggedText))

    # if textOriginal == taggedText:
    #     print("textOriginal == taggedText")
    # else:
    #     print("textOriginal != taggedText")

mappingDisResults(textFilePath, topoFilePath)
print("===>" + str(datetime.now() - startTime))

print("Done!")
