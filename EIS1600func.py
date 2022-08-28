###############################################################################
# PROJECT REUSABLE ATOMIC FUNCTIONS ###########################################
###############################################################################

import re

# VARIABLES ###################################################################

splitter  = "#META#Header#End#"
reflowLen = 70

# PARAGRAPH WRAPPER ###########################################################

import textwrap
# wraps long paragraphs: helps with viewing long files
def wrapPar(paragraph, lenSymb):
    wrapped = "\n".join(textwrap.wrap(paragraph, lenSymb))
    return(wrapped)

# ID GENERATOR ################################################################

from random import randint
def generate12IDs(iterations):
    IDs = []
    for i in range(0, iterations):
        IDs.append("$%s$" % str(randint(400000000000, 999999999999)))
        #input(IDs)
    IDs = list(set(IDs))
    #print("IDs: {:,}".format(len(IDs)))
    return(IDs)

# CONVERT MarKDOWN TO EIS1600 #################################################
# > takes the mARkdown text; returns the converted text #######################

def convertToEIS1600(inputText):
    text = inputText.split(splitter)

    IDs = generate12IDs(3000000)

    header = text[0]
    main = text[1]

    # fix
    main = main.replace("~\n", "\n")
    main = main.replace("\n~~", " ")

    #main = re.sub(r"(#~:\w+: *)", r"\n\1\n\n", main)

    main = re.sub(" +", " ", main)

    main = main.replace("\n###", "\n\n###")
    main = main.replace("\n# ", "\n\n")

    main = re.sub("\n{3,}", "\n\n", main)

    # fix poetry
    main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)
    main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)
    main = re.sub(r"(%~% [^\n]+\n)\n([^\n]+ %~%)", r"\1\2", main)

    main = main.split("\n\n")

    mainUpdated = []

    counter = 0
    for m in main:
        counter += 1
        if m.startswith("### "):
            m = m.replace("### ", "#%s " % IDs[counter])
            mainUpdated.append(m)
        elif "%~%" in m:
            m = "%s ::POETRY:: ~\n" % IDs[counter] + m
            mainUpdated.append(m)
        else:
            m = wrapPar(m, 60)
            m = "%s ::UNDEFINED:: ~\n" % IDs[counter] + m
            mainUpdated.append(m)

    main = "\n\n".join(mainUpdated)
    main = re.sub(r"\n(.{1,10})\n", r" \1\n", main)

    # spaces
    main = re.sub("\n +", "\n", main)

    # reassemble text
    final = header + splitter + "\n\n" + main
    return(final)
