
def coordinates(listAll, i):
    scriptStereotype = ""
    scriptCoordinates = ""
    script = ""
    charStereotypeOpen = ["", "[ ", "[ [ "]
    charStereotypeClose = ["", " ]", " ] ]"]
    stereotypeFLG = 0
    num = 1
    stereotype = ""
    flgMulti = ""
    charVirgula = [",", ""]
    flgVirgula = 0

    if listAll[i]['stereotype'] == 'Point':
        stereotype = "Point"
        stereotypeFLG = 0
    elif listAll[i]['stereotype'] == 'Line':
        stereotype = "LineString"
        stereotypeFLG = 1
    elif listAll[i]['stereotype'] == 'Polygon':
        stereotype = "Polygon"
        stereotypeFLG = 2

    scriptCoordinates = " coordinates: " + charStereotypeOpen[stereotypeFLG]
    flgLat = listAll[i]['lat0']
    flgLon = listAll[i]['lon0']
    scriptCoordinates += " [ "
    scriptCoordinates += str(listAll[i]['lat0']) + ", " + str(listAll[i]['lon0'])
    scriptCoordinates += " ] "
    while 'lat' + str(num) in listAll[i].keys():
        scriptCoordinates += charVirgula[flgVirgula] +" [ "
        scriptCoordinates += str(listAll[i]['lat' + str(num)]) + ", " + str(listAll[i]['lon' + str(num)])
        scriptCoordinates += " ] "
        flgVirgula = 0
        if flgLat == listAll[i]['lat'+str(num)] and flgLon == listAll[i]['lon'+str(num)]:
            if 'lat' + str(num+1) in listAll[i].keys():
                scriptCoordinates += charStereotypeClose[stereotypeFLG] + ", " + charStereotypeOpen[stereotypeFLG]
                flgLat = listAll[i]['lat'+str(num)]
                flgLon = listAll[i]['lon'+str(num)]
                flgMulti = "Multi"
                flgVirgula = 1

        num += 1

    stereotype = flgMulti + stereotype
    scriptStereotype = "geometries: { type: " + "\"" + stereotype + "\","
    script = scriptStereotype + scriptCoordinates
    script += charStereotypeClose[stereotypeFLG] + " }})\n"

    return script



def othersAtrib(listAll, i):
    script = ""
    remove = ["name","stereotype","amenity","highway","shop","building"]
    for j in listAll[i].keys():
        if j not in remove and "lat" not in j and "lon" not in j :
            script += j + " : \"" + listAll[i][j] + "\", "

    return script.replace("addr:", "")

def openJSON(listScript):
    dotA = listScript.find('.') + 1
    dotB = listScript.find('.', dotA)
    arqJSON = open("Resultado/" + str(listScript[dotA:dotB]) + ".json", 'w+')

    return arqJSON

def scriptGeneration(listAll, mapName):
    arqScript = open("Resultado/script.txt", 'w+')
    listScript = []
    script = ""

    for i in range(len(listAll)):

        if "amenity" in listAll[i]:
            script = "db."+listAll[i]['amenity']+".insert({ "

        elif "highway" in listAll[i]:
            script = "db."+listAll[i]['highway']+".insert({ "

        elif "shop" in listAll[i]:
            script = "db."+listAll[i]['shop']+".insert({ "

        elif "building" in listAll[i]:
            script = "db."+listAll[i]['building']+".insert({ "


        if "name" in listAll[i]:
            script += "name: \""+ listAll[i]['name'] + "\", "

        script += othersAtrib(listAll, i)
        script += coordinates(listAll, i)
        listScript.append(script)


    listScript.sort()
    arqScript.write("use "+ mapName +"\n\n")
    arrabN = listScript[0].split(".")[1]
    arqJSON = openJSON(listScript[0])
    for x in listScript:

        if x.split(".")[1] != arrabN:
            arqJSON.close()
            arqJSON = openJSON(x)
            arqScript.write("\n")
            arrabN = x.split(".")[1]

        arqScript.write(x)
        arqJSON.write(x[x.find('{'):x.find(')')]+"\n")

    arqScript.close()
    arqJSON.close()

    print("Script Table completed")
    # asd = listScript[0].find('.')
    # print(asd)
    # print(listScript[0].find('.', asd+1))
    # print(listScript[0][3:11])
    # print(listScript[0].find('{'))
    # print(listScript[0][19:])
    return