from bs4 import BeautifulSoup
import graph

dicElements = {}  # responsavel por separar os elementos especificos (way, node...) dentro da função Find_tag_coord
dicWay = {}  # dicionario das tags Way
listWay = []  # lista que recebe todos os blocos XML da tag Way
# dicNode = {}
listNode = []  # lista que recebe os blocos XML sem a TAG name


def find_coord_stereotypes(list):
    flg = 0
    stereotypeList = []

    for nd in list.find_all('nd'):
        for coord in soup.find_all(id=str(nd.get('ref'))):
            # print coord
            dicElements["lat" + str(flg)] = coord.get('lat')
            dicElements["lon" + str(flg)] = coord.get('lon')
            flg = flg + 1
            stereotypeList.append(nd.get('ref'))

    # print(len(stereotypeList))
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
        # print(k)
    stereotypeList.clear()
    return


def find_tag_coord(test):
    if test.find(k="name"):
        find_coord_stereotypes(test)
        listWay.append(dicElements.copy())
    else:
        find_coord_stereotypes(test)
        listNode.append(dicElements.copy())
    dicElements.clear()
    return


def find_region_extent(list, ref):
    num = 0
    flgHi = list[ref+str(num)]
    flgLw = list[ref+str(num)]
    while ref+str(num) in list.keys():
        if flgHi < list[ref+str(num)]:
            flgHi = list[ref+str(num)]
        if flgLw > list[ref+str(num)]:
            flgLw = list[ref+str(num)]
        num += 1

    return flgHi, flgLw


#### LEITURA XML
with open('map.osm') as xml_file:
    soup = BeautifulSoup(xml_file, 'lxml')

#### PEGANDO TAGs WAY
dicWay = soup.find_all("way")

#### SINCRONIZANDO COORDENADAS E STEREOTYPES
for i in range(len(dicWay)):
    tagWay = BeautifulSoup(str(dicWay[i]), 'lxml')
    find_tag_coord(tagWay)

#### CONSTRUINDO ESQUEMA CONCEITUAL
print(graph.driveGraph(listWay))


#### RETANGULO ENVOLVENTE
#for i in listNode:
#    print(find_region_extent(i, 'lat'))
#    print(find_region_extent(i, 'lon'))
#    print()

#### GERAR SCRIP TABELAS
arqScript = open("script", 'w+')
for i in range(len(listWay)):
    arqScript.write(listWay[i]['name'])
    if "amenity" in listWay[i]:
        arqScript.write(" - " + listWay[i]['amenity'] + "\n")
    elif "highway" in listWay[i]:
        arqScript.write(" - " + listWay[i]['highway'] + "\n")
    elif "shop" in listWay[i]:
        arqScript.write(" - " + listWay[i]['shop'] + "\n")
    else:
        arqScript.write("\n")
arqScript.close()

###### GERAR RELATORIO
arqNode = open("relatorio", 'w+')

# for i in range(len(listNode)):
print(listNode[4].keys())
for i in range(len(listNode)):
    num = 0
    arqNode.write(listNode[i]["stereotype"] + "\n")
    while 'lat'+str(num) in listNode[i].keys():
        arqNode.write(str(listNode[i]['lat'+str(num)])+", "+str(listNode[i]['lon'+str(num)])+ "\n")
        num += 1
    latHi, latLw = find_region_extent(listNode[i], 'lat')
    lonHi, lonLw = find_region_extent(listNode[i], 'lon')
    arqNode.write(" -------------------------------------\n")
    arqNode.write("|\t\t\t "+str(latHi)+"\t\t\t  |\n")
    arqNode.write("|"+str(lonLw)+"\t\t\t "+str(lonHi)+"  |\n")
    arqNode.write("|\t\t\t " + str(latLw) + "\t\t\t  |\n")
    arqNode.write(" -------------------------------------\n\n\n")
arqNode.close()

# for i in range(len(listWay)):
#         for j in listWay[i].keys():
#             if "lat" not in j and "lon" not in j and "name" not in j:
#                 print(j, end="   ")
#             if j == "name":
#                 print(listWay[i]['name'], end="    ")
#         print()
