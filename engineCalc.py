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
    listEngine(engine)

# Neatly lists the engine spec
class listClass:
    def listEngine(engine):
        for a,b in engine.items():
            if b == "":
                b = "N/A"
            print(a,":",b)
    def listEngine(engine, lines):
        print("wa")
#CALCULATIONS

#Vd Swept Displacement volume
def Vd(B, L):
    Vd = (math.pi * ((B/2) ** 2) * L)
    return Vd

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


'''
#Define variables for maths equations based on selected engine
Model = (engine[selected][iMODEL]) #Model Name
B = float(engine[selected][iB]) #Bore
L = float(engine[selected][iL]) #Stroke
cyl = int(engine[selected][iCYL]) #Cyl No
Vd = float(engine[selected][iVD]) #Swept Displacement
cc = float(engine[selected][iCC]) #Total swept displacement
Vc = float(engine[selected][iVC]) #Clearance volume
rc = float(engine[selected][RC]) #Compression Ratio


#cc = cc(Vd, cyl)
#rc = rc(Vd, Vc) 

#Print obtained data for selected engine
print(Model, B, L, cyl,Vd, round(cc,3), Vc, round(rc,1))


#Old code for intersecting the data with a dictionary.
#Import data and populate dictionary
columnHeaders = (Name, Bore, Stroke, Cylinders, compressionRatio, clearanceVolume)
#Define dictionary column names
Name = 'Name' #Expect string name
Bore = "Bore" #Expect cc in cm
Stroke = "Stroke" #Expect stroke in cm
Cylinders = "Cylinders" #Expect number of cylinders in count
compressionRatio = "Compression Ratio" #Expect CR as 1pd 12.1
clearanceVolume = "Clearance Volume" #Expect clearance volume in cm^3

#Create dictionary
engine = {Name:[], Bore:[], Stroke:[], Cylinders:[], compressionRatio:[], clearanceVolume:[]}
data = csv.reader(open(sys.argv[1]))

for row in data:
    for column in columnHeaders:
        for value in row:
            engine[column].append(value)
            print(engine)

engine[Name].append(row[0])
engine[Bore].append(row[1])
engine[Stroke].append(row[2])
engine[Cylinders].append(row[3])
engine[compressionRatio].append(row[4])
engine[clearanceVolume].append(row[5])

#Show entire dictionary
print(engine[Name])
print(engine[Bore])
print(engine[Stroke])
print(engine[Cylinders])
print(engine[compressionRatio])
print(engine[clearanceVolume])
'''
