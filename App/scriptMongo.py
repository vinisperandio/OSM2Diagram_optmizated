
def coordinates(listAll, i):
    script = ""
    charStereotypeOpen = ["", "[ ", "[ [ "]
    charStereotypeClose = ["", " ]", " ] ]"]
    stereotypeFLG = 0
    num = 0
    stereotype = ""

    if listAll[i]['stereotype'] == 'Point':
        stereotype = "Point"
        stereotypeFLG = 0
    elif listAll[i]['stereotype'] == 'Line':
        stereotype = "LineString"
        stereotypeFLG = 1
    elif listAll[i]['stereotype'] == 'Polygon':
        stereotype = "Polygon"
        stereotypeFLG = 2

    script += "geometries: { type: " + "\"" + stereotype + "\","
    script += " coordinates: " + charStereotypeOpen[stereotypeFLG]
    while 'lat' + str(num) in listAll[i].keys():
        script += " [ "
        script += str(listAll[i]['lat' + str(num)]) + ", " + str(listAll[i]['lon' + str(num)])
        num += 1
        script += " ] ,"

    script = script[:-1]
    script += charStereotypeClose[stereotypeFLG] + " }\n"

    return script



def othersAtrib(listAll, i):
    script = ""
    remove = ["name","stereotype","amenity","highway","shop","building"]
    for j in listAll[i].keys():
        if j not in remove and "lat" not in j and "lon" not in j :
            script += j + " : " + listAll[i][j] + ", "

    return script



def scriptGeneration(listAll, mapName):
    arqScript = open("Resultado/script", 'w+')
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
            script += "name: "+ listAll[i]['name'] + ", "

        script += othersAtrib(listAll, i)
        script += coordinates(listAll, i)
        listScript.append(script)


    listScript.sort()
    arqScript.write("use "+ mapName +"\n\n")
    arrab = listScript[0].split(".")[1]
    for x in listScript:

        if x.split(".")[1] != arrab:
            arqScript.write("\n")
            arrab = x.split(".")[1]
        arqScript.write(x)

    arqScript.close()
    print("Script Table completed")

    return


# db.school.insert({name:"elfie holfs", locations: {type: "Point",coordinates: [123123, 123123]}});
