import json
from builtins import print

from bs4 import BeautifulSoup
from App import graph
import time
from App import scriptMongo
import re
import os
import sys

dicMain = {}     # arquivo osm inteiro carregado
dicElements = {}  # responsavel por separar as caracteristicas (name, coordinates...) dentro da funcao Find_tag_coord
global dicWay
dicWay = {}    # dicionario das tags Way
listWay = []   # lista que recebe todos os blocos XML da tag Way
dicNode = {}   # dicionario das tags Node
listNode = []   # lista que recebe todos os blocos XML da tag Node
dicRelation = {}
listRelation = []
listIncom = []  # lista que recebe os blocos XML sem a TAG name
listAllEntities = [] # lista que contem todos os elementos das Tags NODE, WAY e Relations que serao modelados
idMultipolygon = [] #guarda os ID dos multipolygons, para que eles nao entrem no arquivo RELATORIO


def replace_attr(value):
    return value.replace('/', '_').replace('\u010c', 'C').replace('\u200e', '').replace('\"', '').replace(' ', '_')


def find_coord_stereotypes_Way(list):
    flg = 0
    stereotypeList = []

    for nd in list.find_all('nd'):
        refID = nd.get('ref')
        dicElements["lat" + str(flg)] = dicMain[refID][0]
        dicElements["lon" + str(flg)] = dicMain[refID][1]
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
        dicElements[k] = replace_attr(v)
    stereotypeList.clear()
    return


def find_coord_stereotypes_Node(list):
    flg = 0

    dicElements["lat" + str(flg)] = list.get('lat')
    dicElements["lon" + str(flg)] = list.get('lon')

    for tag in list.find_all('tag'):
        k = tag.get('k')
        v = tag.get('v')
        dicElements[k] = replace_attr(v)

    dicElements["stereotype"] = "Point"
    return


def find_coord_stereotypes_Relation(list):
    flg = 0

    for member in list.find_all('member'):
        refMember = member.get('ref')
        idMultipolygon.append(refMember)

        if refMember in dicWay:

            for nd in dicWay[refMember].find_all('nd'):
                refID = nd.get('ref')
                dicElements["lat" + str(flg)] = dicMain[refID][0]
                dicElements["lon" + str(flg)] = dicMain[refID][1]
                flg = flg + 1


    dicElements["stereotype"] = "Polygon"

    for tag in list.find_all('tag'):
        if tag.get('k') == 'type':
            None
        else:
            k = tag.get('k')
            v = tag.get('v')
            dicElements[k] = replace_attr(v)
    return


def find_ID(list):
    id_soup = BeautifulSoup(str(list), 'lxml')
    return id_soup.way['id']


def find_tag_coord(test, tagType):
    if tagType == 'way':
        find_coord_stereotypes_Way(test)
        if test.find('tag'):
            listWay.append(dicElements.copy())
        #else:
        if not test.find(k="name"):
            if find_ID(test) in idMultipolygon:
                None
            else:
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


def insert_key_dic(dic):
    list = []
    auxDic = {}

    for i in range(len(dic)):
        list.append(dic[i])
        inID = str(list[0]).find("id=")
        endID = str(list[0]).rfind("\"", inID, inID + 15)
        st = str(list[0])[inID + 4:endID]
        auxDic[st] = list[0]
        list.clear()

    dic.clear()
    dic = auxDic.copy()
    return dic


def shp_generation(listNames):
    linestring = 0
    multipolygon = 0
    point = 0

    for i in listNames:
        # print(i)
        with open("Resultado/" + i + ".geojson") as file:  # , encoding='windows-1252'
            arq = json.load(file, strict=False)
        data = json.dumps(arq)

        linestring = data.count('LineString')
        multipolygon = data.count('Polygon')
        point = data.count('Point')
        # print(linestring)
        # print(multipolygon)
        # print(point)
        # print(i)
        # print()

        if linestring > (multipolygon and point):
            os.system("ogr2ogr -nlt LINESTRING -skipfailures Resultado/" + i + ".shp Resultado/" + i + ".geojson")
        elif multipolygon > (linestring and point):
            os.system("ogr2ogr -nlt MULTIPOLYGON -skipfailures Resultado/" + i + ".shp Resultado/" + i + ".geojson")
        else:
            os.system("ogr2ogr -f \"ESRI Shapefile\" Resultado/" + i + ".shp Resultado/" + i + ".geojson")
    return


def report_generation():
    arqNode = open("Resultado/relatorio", 'w+')
    for i in range(len(listIncom)):
        num = 0
        arqNode.write(listIncom[i]["stereotype"] + "\n")
        while 'lat' + str(num) in listIncom[i].keys():
            arqNode.write(str(listIncom[i]['lat' + str(num)]) + ", " + str(listIncom[i]['lon' + str(num)]) + "\n")
            num += 1
        latHi, latLw = find_region_extent(listIncom[i], 'lat')
        lonHi, lonLw = find_region_extent(listIncom[i], 'lon')
        arqNode.write(" -------------------------------------\n")
        arqNode.write("|\t\t\t " + f'{lonHi:.7f}' + "\t\t\t  |\n")
        arqNode.write("|" + f'{latLw:.7f}' + "\t\t\t " + f'{latHi:.7f}' + "  |\n")
        arqNode.write("|\t\t\t " + f'{lonLw:.7f}' + "\t\t\t  |\n")
        arqNode.write(" -------------------------------------\n\n\n")

    print("Arq Incomplete nodes checked!")
    arqNode.close()
    return

def start(arq):

    #### LEITURA XML
    #with open(sys.argv[1]) as xml_file:
    ini = time.time()
    global dicWay
    global dicNode
    global dicRelation

    with open(arq) as xml_file: #, encoding='UTF-8'
        soup = BeautifulSoup(xml_file, 'lxml')

    #### PEGANDO TAGs WAY
    for tag in soup.find_all(re.compile("^node")):
        dicMain[tag.get('id')] = [tag.get('lat'),tag.get('lon')]

    dicRelation = soup.find_all("relation")
    dicRelation = insert_key_dic(dicRelation)

    dicWay = soup.find_all("way")
    dicWay = insert_key_dic(dicWay)

    dicNode = soup.find_all("node")
    dicNode = insert_key_dic(dicNode)


    #### SINCRONIZANDO COORDENADAS E STEREOTYPES
    for i in dicRelation:
        find_tag_coord(dicRelation[i], 'relation')


    for i in dicWay:
        find_tag_coord(dicWay[i], 'way')

    for i in dicNode:
        find_tag_coord(dicNode[i], 'node')


    #### CONSTRUINDO ESQUEMA CONCEITUAL
    listAllEntities = listNode + listWay + listRelation

    print(graph.driveGraph(listAllEntities))


    #### GERAR SCRIP TABELAS
    fileName = xml_file.name
    listNames = scriptMongo.scriptGeneration(listAllEntities, fileName[4:])
    listNames = sorted(set(listNames))
    # print(listNames)

    #### GERAR SHP
    shp_generation(listNames)


    ###### GERAR RELATORIO
    report_generation()


    end = time.time()
    clock = round(end-ini, 3)
    print(str(clock)+" ms")
    print(str(clock/60)+" min")