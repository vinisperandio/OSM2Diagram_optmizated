from graphviz import Digraph, render

# HEALTH
global health
health = ['emergency']

global emergency
emergency = ['medical_rescue', 'firefighters', 'lifeguards', 'other_structure', 'other_station']
global medical_rescue
global firefighters
global lifeguards
global other_structure
global other_station
#---------------------------------------------PACKAGED SERVICES--------------------------------------------------------------------------
# SERVICES
global service
service = ['shop', 'amenity', 'craft']

global amenity
amenity = ['sustenance','education', 'transportation', 'financial', 'healthCare', 'entertainment', 'othersAmenity']
global sustenance
sustenance = ['bar','bbq','biergarten','cafe','drinking_water','fast_food','ice_cream','pub','restaurant']
global education
education = ['college', 'kindergarten', 'library', 'archive', 'public_bookcase', 'school', 'music_school',
             'driving_school', 'language_school', 'university', 'research_institute']
global transportation
transportation = ['bicycle_parking','bicycle_repair_station','bicycle_rental','boat_rental','bus_station', 'fuel',
                  'boat_sharing','bus_station','car_rental','car_sharing','car_wash','charging_station',
                  'ferry_terminal','grit_bin','motorcycle_parking','parking','parking_entrance','	parking_space',
                  'taxi','ticket_validator']
global financial
financial = ['atn','bank','bureau_de_change']
global healthCare
healthCare = ['baby_hatch','clinic','dentist','doctors','hospital','nursing_home','pharmacy','social_facility',
              'veterinary','blood_donation']
global entertainment
entertainment = ['arts_centre','brothel','casino','cinema','community_centre','fountain','gambling','nightclub',
                 'planetarium','social_centre','stripclub','studio','swingerclub','theatre']
global othersAmenity
othersAmenity = ['animal_boarding','animal_shelter','baking_oven','bench','clock','courthhouse','coworking_spece','creamtorium',
          'crypt','dive_centre','dojo','embassy','fire_station','game_feeding','grave_feeding','grave_yard','hunting_stand',
          'internet_cafe','kitchen','kneipp_water_cure','marketplace','photo_booth','place_of_worship','police','post_box',
          'post_office','prison','public_bath','ranger_station','recycling','rescue_station','sanitary_dump_station',
          'shelter','shower','table','telephone','toilets','townhall','vendingg_machine','wasted_disposal',
          'waste_transfer_station','watering_place','water_point']


global shop
shop = ['food_beverages','general_store','clothing_shoes_acessories','discountStore','health_beauty',
        'do_it_yourself','furniture_interior','eletronics','outdoors_sport','art_music_hobbies','stationery_gfits_books',
        'othersShop']
global food_beverages
food_beverages = ['alcohol','bakery','beverages','brewing_supplies','butcher','cheese', 'chocolate','chocolate','coffee',
                  'confectionery','convenience','deli','dairy','farm','frozen_food','greengrocer','health_food','ice_cream',
                  'pasta','pastry','seafood','spices','tea','water']
global general_store
general_store = ['department_sote','general','kiosk','mail','supermarket','wholesale']
global clothing_shoes_acessories
clothing_shoes_acessories = ['baby_goods','bag','boutique','clothes','fabric','fashion','jewelry','leather','sewing',
                             'shoes','tailor','watches']
global discountStore
discountStore = ['charity','second_hand','variety_store']
global health_beaty
health_beaty = ['beauty','chemist','cosmetics','erotic','hairdresser','hairdresser_supply','hearing_aids','herbalist',
                'massage','medical_supply','nutrition_supplements','optician','perfumery','tattoo']
global do_it_yourself
global furniture_interior
global eletronics
global outdoors_sport
global art_music_hobbies
global stationery_gfits_books
global othersShop
art_music_hobbies = ['camera', 'music', 'games']


global craft
craft = ['agricultura_engines', 'bakery', 'carpenter']
#-----------------------------------------------PACKAGE ROAD MESH----------------------------------------------------------------------
# ROAD MESH
global road_mesh
road_mesh = ['highway', 'aerialway', 'aeroway', 'railway', 'public_transportation', 'route']

global highway
highway = ['roads', 'special_road', 'path', 'linkRoads', 'lifecycle', 'othersHighway']
global roads
roads = ['residential', 'primary', 'motorway', 'unclassified']
global special_road
specialRoads = ['pedestrian', 'escape', 'raceway']
global path
path = ['steps', 'path', 'footway']

global aerialway
global aeroway

global railway
railway = ['tracks', 'station_and_shop', 'other_railway']

global public_transportation
global route

# STERIOTYPE
global line
line = ['highway']
global point
point = ['amenity', 'shop', '']
global polygon
polygon = ['amenity', 'shop', 'highway']

# VARIAVEIS CONTROLE
global contNode
global mother
contNode = 0
mother = {}


def driveGraph(listDic):
    listWay = listDic.copy()
    listService = []
    listRoadMesh = []
    listHealth = []

    if not listWay:
        return "Graph failed!"
    else:
        for i in range(len(listWay)):  # separate the entities according to packages
            for j in listWay[i].keys():
                if j in service:
                    if 'amenity' in listWay[i].keys():
                        if listWay[i]['amenity'] in healthCare:
                            listHealth.append(listWay[i].copy())
                        else:
                            listService.append(listWay[i].copy())
                    else:
                        listService.append(listWay[i].copy())
                if "highway" in j:
                    listRoadMesh.append(listWay[i].copy())

        arq = open("schema.gv", 'w+')
        arq.write("digraph structs { \n\tnode [shape=box]")

        serviceGraph(arq, listService)
        emergencyGraph(arq, listHealth)
        roadMeshGraph(arq, listRoadMesh)
        findRelation(arq)

        arq.write("\n\trankdir=BT\n\tsplines=ortho\n}")
        arq.close()

        render('dot', 'png', 'schema.gv')
    return "Graph checked!\n"


######################################################################################### CLASS_xml
def initPackage(name):
    return ("\n\tsubgraph cluster_" + name + " {" +
            "\n\t\tnode [color=black style=filled]" +
            "\n\t\tcolor=lightgrey style=filled" +
            "\n\t\tlabel=" + name)


def subGraph(arq, namePackage, package, list):
    flg = []
    global contNode  # HOW MANY NODES HAS IN THE SCHEMA
    global mother  # SAVE ALL CLASSES WITH YOUR KEYS, WILL USE FOR FIND RELATION
    listControlMain = []  # SECURITY FLAG, USED FOR TO KNOW IF MAINCLASS(AMENITY, SHOP, HIGHWAY) WAS GENERATED
    listControlSub = []
    listControlthird = []

    for k in package:
        for i in range(len(list)):  ##  TABLE NAME = university, third level
            if k in list[i] and list[i][k] not in listControlthird:
                arq.write(entityName(contNode, list[i][k], entityStereotype(list[i]["stereotype"])))
                mother[list[i][k]] = contNode
                flg.append(findClass(namePackage, list[i][k]))
                contNode = contNode + 1
                arq.write("\n\t\t\t<hr/>")
                for j in list[i].keys():  ##  TABLE ATT
                    if "stereotype" not in j and "lat" not in j and "lon" not in j and k not in j:
                        arq.write(entityAtt(j))
                arq.write(entityAtt("coordinates") + "\n\t\t\t</TABLE>>]")
                listControlthird.append(list[i][k])
                if k not in listControlMain:
                    arq.write(entityName(contNode, k, entityStereotype(
                        None)) + "\n\t\t\t</TABLE>>]")  ## MainClass = highway FIRST LEVEL
                    mother[k] = contNode
                    contNode = contNode + 1
                    listControlMain.append(k)

    for i in range(len(flg)):  ## SubClasses = roads, path SECOND LEVEL
        if flg[i] not in listControlSub:
            arq.write(entityName(contNode, flg[i], entityStereotype(None)) + "\n\t\t\t</TABLE>>]")
            mother[flg[i]] = contNode
            contNode = contNode + 1
            listControlSub.append(flg[i])
    arq.write("\n\t}")


def entityName(contNode, list, stereotype):
    return ("\n\t\t" + str(contNode) + "[style = \"filled, bold\" penwidth = \"1\" fillcolor=\"white\" label=<" +
            "\n\t\t\t<TABLE color=\"black\" border=\"0\">" +
            "\n\t\t\t <TR>" +
            "\n\t\t\t\t<TD align=\"center\"><font color=\"black\">" + str(list) + "</font>" +
            stereotype + "\n\t\t\t</TR>")


def entityStereotype(name):
    stereotype = "  "
    if name == "line":
        stereotype += "\n\t\t\t\t<font FACE=\"sigmoda\" POINT-SIZE=\"20.0\"> w</font>"
    if name == "point":
        stereotype += "\n\t\t\t\t<font FACE=\"sigmoda\" POINT-SIZE=\"20.0\"> b</font>"
    if name == "polygon":
        stereotype += "\n\t\t\t\t<font FACE=\"sigmoda\" POINT-SIZE=\"20.0\"> e</font>"

    stereotype += "</TD>"
    return stereotype


def entityAtt(valor):
    return ("\n\t\t\t<TR>" +
            "\n\t\t\t\t<TD align=\"left\">" + valor + "</TD>" +
            "\n\t\t\t </TR>")


def findClass(name, tag):
    if name == 'road_mesh':
        return findClassroad_mesh(tag)
    elif name == 'service':
        return findClassService(tag)
    elif name == 'health':
        return findClassHealth(tag)


######################################################################################### REALATION
def entityRelation(slave, master):
    return ("\n\t\t" + str(slave) + " -> " + str(master) + "[arrowhead=onormal]")


def findRelation(arq):
    global mother
    for i in mother:
        if i in education:
            arq.write(entityRelation(mother[i], mother['education']))
        elif i in transportation:
            arq.write(entityRelation(mother[i], mother['transportation']))
        elif i in entertainment:
            arq.write(entityRelation(mother[i], mother['entertainment']))
        elif i in healthCare:
            arq.write(entityRelation(mother[i], mother['healthCare']))
        elif i in amenity:
            arq.write(entityRelation(mother[i], mother['amenity']))
        elif i in art_music_hobbies:
            arq.write(entityRelation(mother[i], mother['art_music_hobbies']))
        elif i in shop:
            arq.write(entityRelation(mother[i], mother['shop']))
        elif i in roads:
            arq.write(entityRelation(mother[i], mother['roads']))
        elif i in highway:
            arq.write(entityRelation(mother[i], mother['highway']))
    return print("\nRelation checked!")


def packageRelation(arq, list, name):
    flg = []
    global contNode
    global mother

    for i in range(len(list)):  ##  NOME TABELA
        if name in list[i]:
            arq.write(entityName(contNode, list[i][name], entityStereotype(list[i]["stereotype"])))
            mother[list[i]['amenity']] = contNode
            flg.append(findClassHealth(list[i]['amenity']))
            contNode = contNode + 1
            arq.write("\n\t\t\t<hr/>")
            for j in list[i].keys():  ##  ATRIBUTOS TABELA
                if "stereotype" not in j and "lat" not in j and "lon" not in j and name not in j:
                    arq.write(entityAtt(j))
            arq.write(entityAtt("coordenadas") + "\n\t\t\t</TABLE>>]")

    for i in range(len(flg)):  ## SubClasses = HEALTHCARE .....
        arq.write(entityName(contNode, flg[i], entityStereotype(None)) + "\n\t\t\t</TABLE>>]")
        mother[flg[i]] = contNode
        contNode = contNode + 1


######################################################################################### HEALTH
def findClassHealth(tag):
    if tag in healthCare:
        return "healthCare"
    return


def emergencyGraph(arq, listHealth):
    arq.write(initPackage("HEALTH"))
    packageRelation(arq, listHealth, "amenity")  ##AMENITY
    subGraph(arq, "health", health, listHealth)

    return "HEALTH checked!"


######################################################################################### ROAD MESH
def findClassroad_mesh(tag):
    if tag in roads:
        return "roads"
    elif tag in path:
        return "path"
    elif tag in specialRoads:
        return "specialRoads"


def roadMeshGraph(arq, listRoadMesh):
    arq.write(initPackage("ROAD_MESH"))
    subGraph(arq, "road_mesh", road_mesh, listRoadMesh)

    return "road_mesh checked!"


######################################################################################### SERVICES
def findClassService(tag):
    if tag in education:
        return "education"
    elif tag in transportation:
        return "transportation"
    elif tag in art_music_hobbies:
        return "art_music_hobbies"


def serviceGraph(arq, listService):
    arq.write(initPackage("SERVICES"))
    subGraph(arq, "service", service, listService)

    return "Services checked!"

# def serviceGraph(arq, listService):
#     flg=[]
#     global contNode
#     global mother
#
#     arq.write(initPackage("SERVICES"))
#     ##AMENITY
#     for i in range(len(listService)):##  NOME TABELA
#         arq.write(entityName(contNode,listService[i]['amenity']))
#         mother[listService[i]['amenity']] =  contNode
#         flg.append(findClassService(listService[i]['amenity']))
#         contNode = contNode+1
#         for j in listService[i].keys():##  ATRIBUTOS TABELA
#             if "lat" not in j and "lon" not in j and "amenity" not in j:
#                 arq.write(entityAtt(j))
#         arq.write(entityAtt("coordenadas")+"\n\t\t\t</TABLE>>]")
#
#     for i in range(len(flg)):## SubClasses = transportation, education .....
#         arq.write(entityName(contNode,flg[i])+"\n\t\t\t</TABLE>>]")
#         mother[flg[i]] = contNode
#         contNode = contNode +1
#     arq.write(entityName(contNode,"amenity")+"\n\t\t\t</TABLE>>]"+"\n\t}") ## MainClass = amenity
#     mother['amenity'] = contNode
#     contNode = contNode+1
#
#     print(flg)
#     print(mother)
#     return "Services checked!"
