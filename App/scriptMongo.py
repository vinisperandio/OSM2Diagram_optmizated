
def coordinates(listAll, i):
    charStereotypeOpen = ["", "[ ", "[ [ "]
    charStereotypeClose = ["", " ]", " ] ]"]
    stereotypeFLG = 0
    num = 1
    stereotype = ""
    flgMulti = ""
    charVirgula = [",", ""]
    flgVirgula = 0
    flgCoord = 0

    if listAll[i]['stereotype'] == 'Point':
        stereotype = "Point"
        stereotypeFLG = 0
    elif listAll[i]['stereotype'] == 'Line':
        stereotype = "LineString"
        stereotypeFLG = 1
    elif listAll[i]['stereotype'] == 'Polygon':
        stereotype = "Polygon"
        stereotypeFLG = 2

    scriptCoordinates = " \"coordinates\": " + charStereotypeOpen[stereotypeFLG]
    flgLat = listAll[i]['lat0']
    flgLon = listAll[i]['lon0']
    scriptCoordinates += " [ "
    scriptCoordinates += str(listAll[i]['lon0']) + ", " + str(listAll[i]['lat0'])
    scriptCoordinates += " ] "
    while 'lat' + str(num) in listAll[i].keys():
        scriptCoordinates += charVirgula[flgVirgula] +" [ "
        scriptCoordinates += str(listAll[i]['lon' + str(num)]) + ", " + str(listAll[i]['lat' + str(num)])
        scriptCoordinates += " ] "
        flgVirgula = 0
        if flgLat == listAll[i]['lat'+str(num)] and flgLon == listAll[i]['lon'+str(num)]:
            if flgCoord == 0:
                if 'lat' + str(num+1) in listAll[i].keys():
                    scriptCoordinates += charStereotypeClose[stereotypeFLG] + ", " + charStereotypeOpen[stereotypeFLG]
                    flgLat = listAll[i]['lat'+str(num+1)]
                    #print(flgLat)
                    flgLon = listAll[i]['lon'+str(num+1)]
                    flgMulti = "Multi"
                    flgVirgula = 1
                    flgCoord = 1
            else:
                flgCoord = 0
        num += 1

    if flgMulti != "":
        chr = scriptCoordinates.find("[")
        scriptCoordinates = scriptCoordinates[:chr] + "[" + scriptCoordinates[chr:]
        scriptCoordinates += "]"

    stereotype = flgMulti + stereotype
    scriptStereotype = "\"type\": \"Feature\",\"geometry\": { \"type\": " + "\"" + stereotype + "\","
    script = scriptStereotype + scriptCoordinates
    script += charStereotypeClose[stereotypeFLG] + " }})\n"

    return script



def othersAtrib(listAll, i):
    script = ""
    remove = ["name","stereotype","amenity","highway","shop","building"]
    for j in listAll[i].keys():
        if j not in remove and "lat" not in j and "lon" not in j :
            script += "\"" + j + "\"" + " : \"" + listAll[i][j] + "\", "

    return script.replace("addr:", "")

def openJSON(listScript):
    dotA = listScript.find('.') + 1
    dotB = listScript.find('.', dotA)
    arqJSON = open("Resultado/" + str(listScript[dotA:dotB]) + ".geojson", 'w+')

    return arqJSON

def scriptGeneration(listAll, mapName):
    arqScript = open("Resultado/script.txt", 'w+')
    listScript = []
    scriptInsert = ""
    scriptJson = ""
    flgGeneric = 0


    for i in range(len(listAll)):
        if "amenity" in listAll[i]:
            script = "db."+listAll[i]['amenity']+".insert({ "
        elif "shop" in listAll[i]:
            script = "db."+listAll[i]['shop']+".insert({ "
        elif "craft" in listAll[i]:
            script = "db."+listAll[i]['craft']+".insert({ "

        elif "emergency" in listAll[i]:
            script = "db."+listAll[i]['emergency']+".insert({ "

        elif "leisure" in listAll[i]:
            script = "db." + listAll[i]['leisure'] + ".insert({ "
        elif "tourism" in listAll[i]:
            script = "db." + listAll[i]['tourism'] + ".insert({ "
        elif "historic" in listAll[i]:
            script = "db." + listAll[i]['historic'] + ".insert({ "
        elif "man_made" in listAll[i]:
            script = "db." + listAll[i]['man_made'] + ".insert({ "
        elif "sport" in listAll[i]:
            script = "db." + listAll[i]['sport'] + ".insert({ "

        elif "landuse" in listAll[i]:
            script = "db." + listAll[i]['landuse'] + ".insert({ "

        elif "military" in listAll[i]:
            script = "db." + listAll[i]['military'] + ".insert({ "

        elif "power" in listAll[i]:
            script = "db." + listAll[i]['power'] + ".insert({ "

        elif "barrier" in listAll[i]:
            script = "db." + listAll[i]['barrier'] + ".insert({ "
        elif "boundary" in listAll[i]:
            script = "db." + listAll[i]['boundary'] + ".insert({ "

        elif "highway" in listAll[i]:
            script = "db."+listAll[i]['highway']+".insert({ "

        elif "aerialway" in listAll[i]:
            script = "db."+listAll[i]['aerialway']+".insert({ "

        elif "aeroway" in listAll[i]:
            script = "db."+listAll[i]['aeroway']+".insert({ "

        elif "railway" in listAll[i]:
            script = "db."+listAll[i]['railway']+".insert({ "

        elif "route" in listAll[i]:
            script = "db."+listAll[i]['route']+".insert({ "

        elif "public_transportation" in listAll[i]:
            script = "db."+listAll[i]['public_transportation']+".insert({ "

        elif "building" in listAll[i]:
            script = "db."+listAll[i]['building']+".insert({ "
        elif "place" in listAll[i]:
            script = "db."+listAll[i]['place']+".insert({ "
        elif "office" in listAll[i]:
            script = "db." + listAll[i]['office'] + ".insert({ "

        elif "waterway" in listAll[i]:
            script = "db." + listAll[i]['waterway'] + ".insert({ "

        elif "natural" in listAll[i]:
            script = "db." + listAll[i]['natural'] + ".insert({ "
        elif "geological" in listAll[i]:
            script = "db." + listAll[i]['geological'] + ".insert({ "

        else:
            flgGeneric = 1

        if flgGeneric != 1:
            if "name" in listAll[i]:
                script += "\"name\": \""+ listAll[i]['name'] + "\", "

            script += othersAtrib(listAll, i)
            script += coordinates(listAll, i)
            listScript.append(script)
        flgGeneric = 0

    listScript.sort()
    arqScript.write("use "+ mapName +"\n\n")
    arrabN = listScript[0].split(".")[1]
    arqJSON = openJSON(listScript[0])
    scriptJson = "{\"type\": \"FeatureCollection\", \"features\": [\n"
    for x in listScript:

        if x.split(".")[1] != arrabN:
            scriptJson = scriptJson[:-2] + "\n"
            scriptJson += "]}"
            arqJSON.write(scriptJson)
            arqJSON.close()
            arqJSON = openJSON(x)
            scriptJson = "{\"type\": \"FeatureCollection\", \"features\": [\n"
            arrabN = x.split(".")[1]
            arqScript.write("\n")

        arqScript.write(x)
        scriptJson += x[x.find('{'):x.rfind(')')]+",\n"

    arqScript.close()
    scriptJson = scriptJson[:-2] + "\n"
    scriptJson += "]}"
    arqJSON.write(scriptJson)
    arqJSON.close()

    print("Script Table completed")
    return