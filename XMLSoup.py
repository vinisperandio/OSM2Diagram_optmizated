from bs4 import BeautifulSoup
import graph

dicElements = {}  # responsavel por separar os elementos especificos (way, node...) dentro da função Find_tag_coord
dicWay = {}    # dicionario das tags Way
listWay = []   # lista que recebe todos os blocos XML da tag Way
dicNode = {}   # dicionario das tags Node
listNode = []   # lista que recebe todos os blocos XML da tag Node
listIncom = []  # lista que recebe os blocos XML sem a TAG name
listAllEntities = [] # lista que contem todos os elementos das Tags NODE, WAY e Relations que serão modelados

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
        dicElements["stereotype"] = "point"
    elif stereotypeList[0] == stereotypeList[len(stereotypeList) - 1]:
        dicElements["stereotype"] = "polygon"
    else:
        dicElements["stereotype"] = "line"

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

    dicElements["stereotype"] = "point"
    return


def find_tag_coord(test, tagType):
    if tagType == 'way':
        if test.find(k="name"):
            find_coord_stereotypes_Way(test)
            listWay.append(dicElements.copy())
        else:
            find_coord_stereotypes_Way(test)
            listIncom.append(dicElements.copy())

    elif tagType == 'node':
        if test.find('tag'):
            find_coord_stereotypes_Node(test)
            listNode.append(dicElements.copy())
        else:
            None

    else:
        print('RELATIONS')

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
with open('map_ladeira.osm') as xml_file:
    soup = BeautifulSoup(xml_file, 'lxml')

#### PEGANDO TAGs WAY
dicWay = soup.find_all("way")
dicNode = soup.find_all("node")

#### SINCRONIZANDO COORDENADAS E STEREOTYPES
for i in range(len(dicWay)):
    tagWay = BeautifulSoup(str(dicWay[i]), 'lxml')
    find_tag_coord(tagWay, 'way')

for i in range(len(dicNode)):
    find_tag_coord(dicNode[i], 'node')

#### CONSTRUINDO ESQUEMA CONCEITUAL
listAllEntities = listNode + listWay
print(graph.driveGraph(listAllEntities))


#### GERAR SCRIP TABELAS
arqScript = open("script", 'w+')
for i in range(len(listAllEntities)):
    if "name" in listAllEntities[i]:
        arqScript.write(listAllEntities[i]['name'])
    if "amenity" in listAllEntities[i]:
        arqScript.write(" - " + listAllEntities[i]['amenity'])
    if "highway" in listAllEntities[i]:
        arqScript.write(" - " + listAllEntities[i]['highway'])
    if "shop" in listAllEntities[i]:
        arqScript.write(" - " + listAllEntities[i]['shop'])
    else:
        arqScript.write("\n")
print("Script Table completed")
arqScript.close()


###### GERAR RELATORIO
arqNode = open("relatorio", 'w+')
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


# for i in range(len(listWay)):
#         for j in listWay[i].keys():
#             if "lat" not in j and "lon" not in j and "name" not in j:
#                 print(j, end="   ")
#             if j == "name":
#                 print(listWay[i]['name'], end="    ")
#         print()
