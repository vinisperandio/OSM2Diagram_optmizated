from bs4 import BeautifulSoup
import graph

dicElements = {} #responsavel por separar os elementos especificos (way, node...) dentro da função Find_tag_coord
dicWay = {} #dicionario das tags Way
listWay = [] #lista que recebe todos os blocos XML da tag Way
#dicNode = {}
#listNode = []


def Find_tag_coord(test):
    flg = 0
    stereotypeList=[]
    if test.find(k="name"):
        flg = 0
        for nd in test.find_all('nd'):
            for coord in soup.find_all(id=str(nd.get('ref'))):
                #print coord
                dicElements["lat" + str(flg)] = coord.get('lat')
                dicElements["lon" + str(flg)] = coord.get('lon')
                flg = flg + 1
                stereotypeList.append(nd.get('ref'))

        print(len(stereotypeList))
        if len(stereotypeList) == 1:
            dicElements["stereotype"] = "point"
        elif stereotypeList[0] == stereotypeList[len(stereotypeList)-1]:
            dicElements["stereotype"] = "polygon"
        else:
            dicElements["stereotype"] = "line"

        for tag in test.find_all('tag'):
            k = tag.get('k')
            v = tag.get('v')
            dicElements[k] = v
            #print(k)
        listWay.append(dicElements.copy())
        stereotypeList.clear()
        dicElements.clear()
    return



#### LEITURA XML
with open ('map.osm') as xml_file:
    soup = BeautifulSoup(xml_file, 'lxml')

#### PEGANDO TAGs WAY
dicWay = soup.find_all("way")

#### SINCRONIZANDO COORDENADAS
for i in range(len(dicWay)):
    tagWay = BeautifulSoup(str(dicWay[i]), 'lxml')
    Find_tag_coord(tagWay)

#### CONSTRUINDO ESQUEMA CONCEITUAL
print(graph.driveGraph(listWay))

#### GERAR SCRIP TABELAS
arq = open("script",'w+')
for i in range(len(listWay)):
    arq.write(listWay[i]['name'])
    if "amenity" in listWay[i]:
        arq.write (" - "+listWay[i]['amenity']+"\n")
    elif "highway" in listWay[i]:
        arq.write(" - " + listWay[i]['highway'] + "\n")
    else:
        arq.write ("\n")
arq.close()

# for i in range(len(listWay)):
#         for j in listWay[i].keys():
#             if "lat" not in j and "lon" not in j and "name" not in j:
#                 print(j, end="   ")
#             if j == "name":
#                 print(listWay[i]['name'], end="    ")
#         print()
