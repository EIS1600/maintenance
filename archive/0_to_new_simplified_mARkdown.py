# the script converts from OpenITI mARkdown into simplified version of OpenITI mARkdownSimple

import re

inputFile = "/Users/romanovienna/_OpenITI/0925AH/data/0902Sakhawi/0902Sakhawi.DawLamic/0902Sakhawi.DawLamic.JK003608-ara1.inProgress"
outputFile = "/Users/romanovienna/_OpenITI/0925AH/data/0902Sakhawi/0902Sakhawi.DawLamic/0902Sakhawi.DawLamic.JK003608-ara1.mARkdownSimple"

inputFile = "/Users/romanovienna/_OpenITI/1350AH/data/1339IsmacilBashaBaghdadi/1339IsmacilBashaBaghdadi.HadiyatCarifin/1339IsmacilBashaBaghdadi.HadiyatCarifin.Shia003362Vols-ara1.mARkdown"
outputFile = "./__texts_selected/1339IsmacilBashaBaghdadi.HadiyatCarifin.Shia003362Vols-ara1.mARkdownSimple"

#inputFile = "/Users/romanovienna/_OpenITI/1350AH/data/1339IsmacilBashaBaghdadi/1339IsmacilBashaBaghdadi.HadiyatCarifin/1339IsmacilBashaBaghdadi.HadiyatCarifin.Shia003362Vols-ara1.mARkdown"
#outputFile = "./__texts_selected/1339IsmacilBashaBaghdadi.HadiyatCarifin.Shia003362Vols-ara1.mARkdownSimple"

splitter = "#META#Header#End#"

import textwrap
# wraps long paragraphs: helps with viewing long files
def wrapPar(paragraph, lenSymb):
    wrapped = "\n".join(textwrap.wrap(paragraph, lenSymb))
    return(wrapped)

def convertToEIS1600(inputFile, outputFile):
    
    with open(inputFile, "r", encoding="utf8") as f1:

        text = f1.read().split(splitter)

        header = text[0]
        main = text[1]

        # fix
        main = main.replace("~\n", "\n")
        main = main.replace("\n~~", " ")

        main = re.sub(r"(#~:\w+: *)", r"\n\1\n\n", main)

        main = re.sub(" +", " ", main)

        main = main.replace("\n###", "\n\n###")
        main = main.replace("\n# ", "\n\n")

        main = re.sub("\n{3,}", "\n\n", main)

        main = main.split("\n\n")

        mainUpdated = []

        for m in main:
            if m.startswith("###"):
                mainUpdated.append(m)
            elif "%~%" in m:
                mainUpdated.append(m)
            else:
                m = wrapPar(m, 60)
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

        # reassemble text
        final = header + splitter + "\n\n" + main
        with open(outputFile, "w", encoding="utf8") as f9:
            f9.write(final)
    


