import sys
import math
import csv

'''
Alex Cooper
09/2024
Tool for engine calculations
Takes commandline arguments:
    1. Target data csv
    2. Intended column in csv
If no column argument is given, default to last column
'''

#SHELL ARGUMENTS

#Open csv and read contents to multidimensional array
with open(sys.argv[1]) as file:
    try:
        csvIn = csv.reader(file)
        data = list(csvIn)
        print("---Data Loaded---")
    except:
        print("###Data not ok###")

#Check for user defined engine selection at command line
try:
    sys.argv[2]
except IndexError:
    selected = (len(data)-1)
    print("---Last Engine Selected---")
else:
    selected = int(sys.argv[2])
    print("---Engine Selected---")

#FUNCTIONS

#SelectEngine takes the relevant column headers and data for the selected engine
def selectEngine(data, selected):
    engine = {}
    x = 0
    while x < len(data[0]):
        try:
            engine.update({data[0][x]:float(data[selected][x])})
        except:
            engine.update({data[0][x]:data[selected][x]})
        x += 1
    listEngine(engine)
    return engine

#CompleteEngine finds the gaps in the data and attempts to fill them
def completeEngine(engine):

    print("---Calculating Engine---")

    if engine.get("Swept Displacement") == "":
        try:
            engine.update({"Swept Displacement" : Vd(engine["Bore"], engine["Stroke"])})
        except Exception as err:
            print("Failed", err)

    if engine.get("Total Swept Displacement") == "":
        try:
            engine.update({"Total Swept Displacement" : cc(engine["Swept Displacement"], engine["Cylinders"])})
        except:
            print("Failed", err)

    if engine.get("Compression Ratio") == "" and engine.get("Clearance Volume") == "":
        print("Please provide Compression Ratio or Clearance Volume")
    elif engine.get("Clearance Volume") == "":
        try:
            engine.update({"Clearance Volume" : Vc(engine["Swept Displacement"], engine["Compression Ratio"])})
        except:
            print("Failed", err)
    elif engine.get("Compression Ratio") == "":
        try:
            engine.update({"Compression Ratio" : rc(engine["Swept Displacement"], engine["Clearance Volume"])})
        except:
            print("Failed", err)
    listEngine(engine)

# Neatly lists the engine spec
def listEngine(engine):
    for a,b in engine.items():
        if b == "":
            b = "N/A"
        elif isinstance(b, float):
            b = round(b, 2)
        print(a,":",b)
#CALCULATIONS

#Vd Swept Displacement volume
def Vd(B, L):
    Vd = (math.pi * ((B/2) ** 2) * L)
    return Vd

def Vc(Vd, rc):
    Vc = Vd / (rc - 1) 
    return Vc

#rc Compression Ratio
def rc(Vd, Vc):
    rc = (Vd + Vc)/Vc
    return rc

#cc total displacement of engine
def cc(Vd, cyl):
    cc = Vd * cyl
    return cc

#CODE

engine = selectEngine(data, selected)
completeEngine(engine)

