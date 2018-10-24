from bs4 import BeautifulSoup
import graph
import time
import scriptMongo
import sys

dicElements = {}  # responsavel por separar as caracteristicas (name, coordinates...) dentro da funcao Find_tag_coord
dicWay = {}    # dicionario das tags Way
listWay = []   # lista que recebe todos os blocos XML da tag Way
dicNode = {}   # dicionario das tags Node
listNode = []   # lista que recebe todos os blocos XML da tag Node
dicRelation = {}
listRelation = []
listIncom = []  # lista que recebe os blocos XML sem a TAG name
listAllEntities = [] # lista que contem todos os elementos das Tags NODE, WAY e Relations que serao modelados
idMultipolygon = [] #guarda os ID dos multipolygons, para que eles nao entrem no arquivo RELATORIO

def find_coord_stereotypes_Way(list):
    flg = 0
    stereotypeList = []

    for nd in list.find_all('nd'):
        for coord in soup.find_all(id=str(nd.get('ref'))):
            dicElements["lat" + str(flg)] = coord.get('lat')
            dicElements["lon" + str(flg)] = coord.get('lon')
            flg = flg + 1
            stereotypeList.append(nd.get('ref'))

    if len(stereotypeList) == 1:
        dicElements["stereotype"] = "Point"
    elif stereotypeList[0] == stereotypeList[len(stereotypeList) - 1]:
        dicElements["stereotype"] = "Polygon"
    else:
        dicElements["stereotype"] = "Line"

    for tag in list.find_all('tag'):
        k = tag.get('k')
        v = tag.get('v')
        dicElements[k] = v
    stereotypeList.clear()
    return

def find_coord_stereotypes_Node(list):
    flg = 0

    dicElements["lat" + str(flg)] = list.get('lat')
    dicElements["lon" + str(flg)] = list.get('lon')

    for tag in list.find_all('tag'):
        k = tag.get('k')
        v = tag.get('v')
        dicElements[k] = v

    dicElements["stereotype"] = "Point"
    return

def find_coord_stereotypes_Relation(list):
    flg = 0

    for member in list.find_all('member'):
        idMultipolygon.append(member.get('ref'))
        for way in soup.find_all(id=str(member.get('ref'))):
            for nd in way.find_all('nd'):
                for coord in soup.find_all(id=str(nd.get('ref'))):
                    dicElements["lat" + str(flg)] = coord.get('lat')
                    dicElements["lon" + str(flg)] = coord.get('lon')
                    flg = flg + 1

    dicElements["stereotype"] = "Polygon"

    for tag in list.find_all('tag'):
        if tag.get('k') == 'type':
            None
        else:
            k = tag.get('k')
            v = tag.get('v')
            dicElements[k] = v
    return

def find_ID(list):
    id_soup = BeautifulSoup(str(list), 'lxml')
    return id_soup.way['id']


def find_tag_coord(test, tagType):
    if tagType == 'way':
        if test.find('tag'):
            find_coord_stereotypes_Way(test)
            listWay.append(dicElements.copy())
        #else:
        if not test.find(k="name"):
            if find_ID(test) in idMultipolygon:
                None
            else:
                find_coord_stereotypes_Way(test)
                listIncom.append(dicElements.copy())

    elif tagType == 'node':
        if test.find('tag') and not(test.find(k="source")):
            find_coord_stereotypes_Node(test)
            listNode.append(dicElements.copy())
        else:
            None

    elif tagType == 'relation':
        if test.find(v="multipolygon"):
            find_coord_stereotypes_Relation(test)
            listRelation.append(dicElements.copy())
        else:
            None

    else:
        print('NEW TAG')

    dicElements.clear()
    return

def find_region_extent(list, ref):
    num = 0
    flgHi = float(list[ref+str(0)])
    flgLw = float(list[ref+str(0)])
    while ref+str(num) in list.keys():
        flg = float(list[ref+str(num)])
        flgHi = max(flgHi, flg)
        flgLw = min(flgLw, flg)
        num += 1
    return flgHi, flgLw


#### LEITURA XML
#with open(sys.argv[1]) as xml_file:
ini = time.time()

with open("App/map_vicosa2.osm", encoding='utf-8') as xml_file:
    soup = BeautifulSoup(xml_file, 'lxml')

#### PEGANDO TAGs WAY
dicWay = soup.find_all("way")
dicNode = soup.find_all("node")
dicRelation = soup.find_all("relation")


#### SINCRONIZANDO COORDENADAS E STEREOTYPES
for i in range (len(dicRelation)):
    find_tag_coord(dicRelation[i], 'relation')

for i in range(len(dicWay)):
    find_tag_coord(dicWay[i], 'way')

for i in range(len(dicNode)):
    find_tag_coord(dicNode[i], 'node')


#### CONSTRUINDO ESQUEMA CONCEITUAL
listAllEntities = listNode + listWay + listRelation
print(graph.driveGraph(listAllEntities))


#### GERAR SCRIP TABELAS
fileName = xml_file.name
scriptMongo.scriptGeneration(listAllEntities, fileName[4:])

###### GERAR RELATORIO
arqNode = open("Resultado/relatorio", 'w+')
for i in range(len(listIncom)):
    num = 0
    arqNode.write(listIncom[i]["stereotype"] + "\n")
    while 'lat'+str(num) in listIncom[i].keys():
        arqNode.write(str(listIncom[i]['lat'+str(num)])+", "+str(listIncom[i]['lon'+str(num)])+ "\n")
        num += 1
    latHi, latLw = find_region_extent(listIncom[i], 'lat')
    lonHi, lonLw = find_region_extent(listIncom[i], 'lon')
    arqNode.write(" -------------------------------------\n")
    arqNode.write("|\t\t\t "+f'{lonHi:.7f}'+"\t\t\t  |\n")
    arqNode.write("|"+f'{latLw:.7f}'+"\t\t\t "+f'{latHi:.7f}'+"  |\n")
    arqNode.write("|\t\t\t " + f'{lonLw:.7f}' + "\t\t\t  |\n")
    arqNode.write(" -------------------------------------\n\n\n")

print("Arq Incomplete nodes")
arqNode.close()
end = time.time()
print(str(round(end-ini, 4))+" ms")

# for i in range(len(listWay)):
#         for j in listWay[i].keys():
#             if "lat" not in j and "lon" not in j and "name" not in j:
#                 print(j, end="   ")
#             if j == "name":
#                 print(listWay[i]['name'], end="    ")
#         print()