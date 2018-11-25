from graphviz import Digraph, render
import os

#---------------------------------------------PACKAGE DELIMITATION-------------------------------------------------------------------------
global delimitation
delimitation = ['barrier', 'boundary']

global barrier
barrier = ['linear_barriers','access control on highways']
global linear_barriers
linear_barriers = ['cable_barrier','city_wall','ditch','fence','guard_rail','handrail','hedge','kerb','retaining_wall',
                   'tank_trap','wall']
global access_control_on_highways
access_control_on_highways = ['block','bollard','border_control','bump_gate','bus_trap','cattle_grid','chain','cycle_barrier',
                              'debris','entrance','full-height_turnstile','gate','hampshire_gate','height_restrictor',
                              'horse_stile','jersey_barrier','kent_carriage_gap','kissing_gate','lift_gate','log',
                              'motorcycle_barrier','rope','sally_port','spikes','stile','sump_buster','swing_gate',
                              'toll_booth','turnstile','yes']
global boundary
boundary = ['administrative','historic','maritime','national_park','political','postal_code','religious_administration','protected_area']

#---------------------------------------------PACKAGE MILITARY-------------------------------------------------------------------------
global Military
Military = ['Military']

global military
military = ['airfield','ammunition','bunker','barracks','checkpoint','danger_area','naval_base','nuclear_explosion_site',
            'obstacle_course','office','range','training_area','trench','launchpad']

#---------------------------------------------PACKAGE ELECTRICITY-------------------------------------------------------------------------
global electricity
electricity = ['power']

global power
power = ['plant','cable','compensator','converter','generator','heliostat','insulator','line','minor_line','pole','portal',
         'catenary_mast','substation','switch','terminal','tower','transformer']

#---------------------------------------------PACKAGE LANDUSE-------------------------------------------------------------------------
global Landuse
Landuse = ['landuse']

global landuse
landuse = ['commercial','construction','industrial','residential','retail','allotments','basin','brownfield','cemetery',
           'depot','farmland','farmyard','forest','garages','grass','greenfield','greenhouse_horticulture','landfill',
           'meadow','military','orchard','plant_nursery','port','quarry','railway','recreation_ground','religious','reservoir','salt_pond',
           'village_green','vineyard']

#---------------------------------------------PACKAGE LEISURE-------------------------------------------------------------------------
global Leisure
Leisure = ['leisure','historic','tourism','man_made','sport']

global leisure
leisure = ['adult_gaming_centre', 'amusement_arcade', 'beachj_resort', 'bandstand', 'bird_hide', 'common', 'dance',
           'disc_golf_course', 'dog_park', 'escape_game', 'firepit', 'fishing', 'fitness_centre', 'fitness_station',
           'garden', 'hackerspace', 'horse_riding', 'ice_rink', 'marina', 'miniature_golf', 'nature_reserve', 'park',
           'picnic_table', 'pitch', 'playground', 'slipway', 'sports_centre', 'stadium', 'summer_camp', 'swimming_area',
           'swimming_pool', 'track', 'water_park', 'wildlife_hide']
global historic
historic = ['aircraft', 'aqueduct', 'archaeological_site', 'battlefield', 'boundary_stone', 'building', 'cannon','castle',
            'castle_wall', 'church', 'city_gate', 'citywalls', 'farm', 'fort', 'gallows', 'highwater_mark', 'locomotive',
            'manor', 'memorial', 'milestone', 'monastery', 'monument', 'optical_telegraph', 'pillory', 'railway_car', 'ruins',
            'rune_stone', 'ship', 'tomb', 'tower', 'wayside_cross', 'wayside_shrine', 'wreck', 'yes']
global tourism
tourism = ['alpine_hut', 'apartment', 'aquarium', 'artwork', 'attraction', 'camp_site', 'caravan_site', 'chalet', 'gallery',
            'guest_house', 'hostel', 'hotel', 'information', 'motel', 'museum', 'picnic_site', 'theme_park', 'viewpoint',
            'wilderness_hut', 'zoo', 'yes']
global man_made
man_made = ['adit', 'beacon', 'breakwater', 'bridge', 'bunker_silo', 'campanile', 'chimney', 'communication_tower', 'crane',
            'cross', 'cutline', 'clearcut', 'dovecote', 'drinking_fountain', 'dyke', 'embankment','flagpole', 'gasometer',
            'groyne', 'guy', 'kiln', 'lighthouse', 'mast', 'mineshalft', 'monitoring_station', 'obelisk', 'observatory',
            'offshore_platform', 'petroleum_well', 'pier', 'pipeline', 'pumping_station', 'reservoir_covered', 'silo',
            'snow_fence', 'snow_net', 'storage_tank', 'street_cabinet', 'surveillance', 'survey_point', 'telescope', 'tower',
            'wastewater_plant', 'watermill', 'water_tower', 'water_well', 'water_tap', 'water_works', 'wildlife_crossing',
            'windmill', 'works', 'yes']
global sport
sport = ['9pin','10pin','american_football','aikido','archery','athletics','australian_football','badminton','bandy',
         'base','baseball','basketball','beachvolleyball','	billiards','bmx','bobsleigh','boules','bowls','bowling_alley','boxing',
         'canadian_football','canoe','chess','cliff_diving','climbing','climbing_adventure','cockfighting','cricket',
         'croquet','curling','cycling','darts','dog_racing','equestrian','fencing','field_hockey','free_flying','futsal',
         'gaelic_games','golf','gymnastics','handball','hapkido','horseshoes','horse_racing','ice_hockey','ice_skating',
         'ice_stock','judo','karate','karting','kitesurfing','korfball','lacrosse','model_aerodrome','motocross','motor',
         'multi','netball','obstacle_course','orienteering','paddle_tennis','padel','parachuting','paragliding','pelota',
         'racquet','rc_car','roller_skating','rowing','rugby_league','rugby_union','running','sailing','scuba_diving',
         'shooting','skateboard','soccer','sumo','surfing','swimming','table_tennis','table_soccer','taekwondo','tennis',
         'toboggan','volleyball','water_polo','water_ski','weightlifting','wrestling','yoga']

#---------------------------------------------PACKAGE HEALTH-------------------------------------------------------------------------
global health
health = ['emergency']

global emergency
emergency = ['medical_rescue', 'firefighters', 'lifeguards', 'other_Structure', 'other_Station']
global medical_rescue
medical_rescue = ['ambulance_station', 'defibrilator', 'first_aid_kit', 'landing_site', 'emergency_ward_entrance']
global firefighters
firefighters = ['dry_riser_inlet', 'fire_alarm_box', 'fire_extinguisher', 'fire_flapper', 'fire_hose',
                       'fire_hydrant', 'water_tank', 'fire_water_pond', 'suction_point']
global lifeguards
lifeguards = ['lifeguard', 'lifeguard_base', 'lifeguard_tower', 'lifeguard_platform', 'life_ring']
global other_Structure
other_Structure = ['mountain_rescue', 'ses_station']
global other_Station
other_Station = ['assembly_point', 'access_point', 'phone', 'rescue_box', 'siren']

#---------------------------------------------PACKAGED SERVICES--------------------------------------------------------------------------
global service
service = ['shop', 'amenity', 'craft']

global amenity
amenity = ['sustenance','education', 'transportation', 'financial', 'healthcare', 'entertainment', 'other_Amenity']
global sustenance
sustenance = ['bar','bbq','biergarten','cafe','drinking_water','fast_food','food_court','ice_cream','pub','restaurant']
global education
education = ['college', 'kindergarten', 'childcare', 'library', 'archive', 'public_bookcase', 'school', 'music_school',
             'driving_school', 'language_school', 'university', 'research_institute']
global transportation
transportation = ['bicycle_parking','bicycle_repair_station','bicycle_rental','boat_rental','bus_station', 'fuel',
                  'boat_sharing','bus_station','car_rental','car_sharing','car_wash','charging_station',
                  'ferry_terminal','grit_bin','motorcycle_parking','parking','parking_entrance','	parking_space',
                  'taxi','ticket_validator']
global financial
financial = ['atm','bank','bureau_de_change']
global healthcare
healthcare = ['baby_hatch','clinic','dentist','doctors','hospital','nursing_home','pharmacy','social_facility',
              'veterinary','blood_donation']
global entertainment
entertainment = ['arts_centre','brothel','casino','cinema','community_centre','fountain','gambling','nightclub','love_hotel',
                 'planetarium','social_centre','stripclub','studio','swingerclub','theatre']
global other_Amenity
other_Amenity = ['animal_boarding','animal_shelter','baking_oven','bench','clock','courthouse','coworking_spece','creamtorium',
          'crypt','dive_centre','dojo','embassy','fire_station','game_feeding','grave_feeding','grave_yard','hunting_stand',
          'internet_cafe','kitchen','kneipp_water_cure','marketplace','photo_booth','place_of_worship','police','post_box',
          'post_office','prison','public_bath','public_building','ranger_station','recycling','rescue_station','sanitary_dump_station',
          'shelter','shower','table','telephone','toilets','townhall','vendingg_machine','wasted_disposal',
          'waste_transfer_station','watering_place','water_point']


global shop
shop = ['food_beverages','general_store','clothing_shoes_acessories','discount Store','health and beauty',
        'do_it_yourself','furniture_interior','eletronics','outdoors_sport','art_music_hobbies','stationery_gifts_books',
        'other_Shop']
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
do_it_yourself= ['agraria','appliance','bathoroom_furnishing','doityourself','electrical','energy','fireplace',
                         'florist','garden_centre','garden_furniture','gas','glaziery','hardware','houseware','locksmith',
                         'paint','security','trade']
global furniture_interior
furniture_interior = ['antique','bed','candles','carpet','curtain','doors','flooring','furniture','interior_decoration',
                      'kitchen','lamps','tiles','window_blind']
global eletronics
eletronics = ['computer','robot','electronics','hifi','mobile_phone','radiotechnics','vacuum_cleaner']
global outdoors_sport
outdoors_sport = ['atv','bicycle','boat','car','car_repair','car_parts','fuel','fishing','free_flying','hunting','jetski',
                  'motorcycle','outdoor','scuba_diving','ski','snowmobile','sports','swimming_pool','tyres']
global art_music_hobbies
art_music_hobbies = ['atr','collector','craft','frame','games','model','music','musical_instrument','photo','camera',
                     'trophy','video','video_games']
global stationery_gifts_books
stationery_gifts_books = ['anime','books','gift','lottery','newsagent','stationery','ticket']
global other_Shop
other_Shop = ['bookmaker','copyshop','dry_cleaning','e-cigarette','funeral_directors','laundry','money_lender','party',
              'pawnbroker','pet','pyrotechnics','religion','storage_rental','tobacco','toys','travel_agency','vacant',
              'weapons','user_defined']

global craft
craft = ['agricultura_engines', 'bakery','basket_maker','beekeeper','blacksmith','boatbuilder','bookbinder','brewery',
         'builder','cabinet_maker','car_repair','carpenter','carpet_layer','caterer','chimney_sweeper','clockmaker',
         'confectionery','cooper','dental_technician','distillery','dressmaker','electronics_repair','embroiderer',
         'electrician','engraver','floorer','gardener','glaziery','grinding_mill','handicraft','hvac','insulation',
         'jeweller','joiner','key_cutter','locksmith','metal_construction','mint','musical_instrument','oil_mill',
         'optician','organ_builder','painter','parquet_layer','photographer','photographic_laboratory','piano_tuner',
         'plasterer','plumber','pottery','printmaker','rigger','roofer','saddler','sailmaker','sawmill','scaffolder',
         'sculptor','shoemaker','stand_builder','stonemason','sun_protection','tailor','tiler','tinsmith','toolmaker',
         'turner','upholsterer','watchmaker','window_construction','winery']

#-----------------------------------------------PACKAGE ROAD MESH----------------------------------------------------------------------
global road_mesh
road_mesh = ['highway', 'aerialway', 'aeroway', 'railway', 'public_transportation', 'route']

global aerialway
aerialway = ['cable_car','gondola','chair_lift','mixed_lift','drag_lift','t-bar','j-bar','rope_tow','magic_carpet','zip_line']

global aeroway
aeroway = ['aerodrome','apron','gate','hangar','helipad','heliport','navigationaid','runway','spaceport','taxilane',
           'taxiway','terminal','windsock']

global highway
highway = ['roads', 'link roads','special roads', 'Path', 'lifecycle', 'other highway features']
global roads
roads = ['motorway','trunk','primary','secondary','tertiary','unclassified','residential','service']
global linkRoads
linkRoads = ['motorway_link','trunk_link','primary_link','secondary_link','tertiary_link']
global special_road
special_road = ['living_street','pedestrian','track','bus_guideway','escape','raceway','road']
global Path
Path = ['footway','bridleway','steps','path','cycleway','busway']
global lifecycle
lifecycle = ['proposed','construction']
global other_Highway
other_Highway = ['bus_stop','crossing','elevator','emergency_access_point','give_way','phone','mini_roundabout','motorway_junstion',
                'passing_place','rest_area','speed_camera','street_lamp','services','stop','traffic_signals','turning_circle',
                'User Defined']

global railway
railway = ['tracks','station and shop','other Railways']
global tracks
tracks = ['abandoned','construction','disused','funicular','light_rail','miniature','monorail','narrow_gauge','preserved',
          'rail','subway','tram']
global station_and_shop
station_and_shop = ['halt','stop_position','platform','station','subway_entrance','tram_stop']
global other_Railways
other_Railways = ['buffer_stop','derail','crossing','level_crossing','signal','switch','railway_crossing','turntable',
                 'roundhouse','traverser','wash','user defined']

global public_transportation
public_transportation = ['stop_position','platform','station','stop_area']

global route
route = ['bicycle','bus','canoe','detour','ferry','fitness_trail','hiking','horse','inline_skates','light_rail','mtb',
         'nordic_walking','pipeline','piste','power','Railway','road','running','ski','train','tram','User defined']


#-----------------------------------------------PACKAGE EDIFICATION--------------------------------------------------------------------
global edification
edification = ['place','office','building']

global place
place = ['administratively_declared_places','populated_settlements_urban','populated_settlements_urban_and_rural','other_places']
global administratively_declared_places
administratively_declared_places = ['country','state','region','province','district','county','municipality']
global populated_settlements_urban
populated_settlements_urban = ['city','borough','suburb','quarter','neighbourhood','city_block','plot']
global populated_settlements_urban_and_rural
populated_settlements_urban_and_rural = ['town','village','hamlet','isolated_dwelling','farm','allotments']
global other_places
other_places = ['continent','archipelago','island','islet','square','locality']

global office
office = ['accountant','adoptin_agency','advertising_agency','architect','association','charity','company','education_institution',
          'employment_agency','energy_supplier','estate_agent','forestry','foundation','government','guide','healer','insurance',
          'it','lawyer','logistic','moving_company','newspaper','ngo','notary','physician','political_party','private_investigator'
          'property_management','quango','real_estate_agent','religion','research','surveyor','tax','tax_advisor','telecommunications'
          'therapist','travel_agent','water_utility']

global building
building = ['accommodation','Commercial','Religious','civic_amenity','other_building', 'yes', 'supermarket']
global accommodation
accommodation = ['apartments','farm','hotel','house','detached','residential','dormitory','terrace','houseboat','bungalow','static_caravan']
global Commercial
Commercial = ['commercial','office','industrial','retail','warehouse','kiosk','cabin']
global religious
religious = ['religious','cathedral','chapel','church','mosque','temple','synagogue','shrine']
global civic_amenity
civic_amenity = ['bakehouse','kindergarten','civic','hospital','school','stadium','train_station','transportation','university',
                 'grandstand','public']
global other_building
other_building = ['barn','bridge','bunker','carport','convervatory','construction','crowshed','digester','farm_auxiliary','garage','garages',
                  'garbages_shed','greenhouse','hangar','hut','pavilion','parking','riding_hall','roof','shed','stable','sty','transformer_tower',
                  'services','ruins','water_tower','user defined']


#-----------------------------------------------PACKAGE VEGETATION--------------------------------------------------------------------
global vegetation
vegetation = ['natural','geological']

global natural
natural = ['vegetation_surface_related','water_related','landform_related']

global vegetation_surface_related
vegetation_surface_related = ['wood','tree_row','tree','scrub','heath','moor','grassland','fell','bare_rock','scree',
                              'shingle','sand','mud']
global water_related
water_related = ['water','wetland','glacier','bay','cape','beach','coastline','spring','hot_spring','geyser','blowhole']
global landform_related
landform_related = ['peak','volcano','valley','ridge','arete','cliff','saddle','rock','stone','sinkhole','cave_entrance']

global geological
geological = ['moraine','outcrop','palaeontological_site']


#-----------------------------------------------PACKAGE HYDROGRAPHY--------------------------------------------------------------------
global hydrography
hydrography = ['waterway']

global waterway
waterway = ['natural_watercourses','man_made_waterways','facilities','barriers_on_waterways','other_features_on_waterways']
global natural_watercourses
natural_watercourses = ['river','riverbank','stream','wadi','drystream']
global man_made_waterways
man_made_waterways = ['canal','drain','ditch','fairway']
global facilities
facilities = ['dock','boatyard']
global barriers_on_waterways
barriers_on_waterways = ['dam','weir','stream_end','waterfall','lock_gate']
global other_features_on_waterways
other_features_on_waterways = ['turning_point','water_point','fuel']


#-----------------------------------------------VARIAVEIS CONTROLE-----------------------------------------------------------
global contNode
global mother
global superClass
global subClass
global entity
contNode = 0
mother = {}
superClass = {}
subClass = {}
entity = {}
controllerPackages = {}
#-----------------------------------------------------------------------------------------------------------------------------

def driveGraph(listDic):
    listWay = listDic.copy()
    listService = []
    listRoadMesh = []
    listHealth = []
    listLeisure = []
    listEdification = []
    listLandUse = []
    listElectricity = []
    listMilitary = []
    listDelimitation = []
    listVegetation = []
    listHydrography = []


    if not listWay:
        return "Graph failed!"
    else:
        for i in range(len(listWay)):  # separate the entities according to packages
            for j in listWay[i].keys():
                if j in service:
                    if 'amenity' in listWay[i].keys():
                        if listWay[i]['amenity'] in healthcare:
                            listHealth.append(listWay[i].copy())
                            j = 0
                            i += i
                            break
                        elif listWay[i]['amenity'] in entertainment:
                            listLeisure.append(listWay[i].copy())
                        else:
                            listService.append(listWay[i].copy())
                if j in road_mesh:
                    listRoadMesh.append(listWay[i].copy())
                if j in health:
                    listHealth.append(listWay[i].copy())
                if j in edification:
                    listEdification.append(listWay[i].copy())
                if j in Leisure:
                    listLeisure.append(listWay[i].copy())
                if j in Landuse:
                    listLandUse.append(listWay[i].copy())
                if j in electricity:
                    listElectricity.append(listWay[i].copy())
                if j in Military:
                    listMilitary.append(listWay[i].copy())
                if j in delimitation:
                    listDelimitation.append(listWay[i].copy())
                if j in vegetation:
                    if 'natural' in listWay[i].keys():
                        if listWay[i]['natural'] in water_related:
                            listHydrography.append(listWay[i].copy())
                        else:
                            listVegetation.append(listWay[i].copy())
                if j in hydrography:
                    listHydrography.append(listWay[i].copy())

        arq = open("Resultado/schema.gv", 'w+')
        arq.write("digraph structs { \n\tnode [shape=box]")

        landUseGraph(arq, listLandUse)
        leisureGraph(arq, listLeisure)
        serviceGraph(arq, listService)
        emergencyGraph(arq, listHealth)
        print(listHealth)
        roadMeshGraph(arq, listRoadMesh)
        edificationGraph(arq, listEdification)
        electricityGraph(arq, listElectricity)
        delimitationGraph(arq, listDelimitation)
        militaryGraph(arq, listMilitary)
        hydrographyGraph(arq, listHydrography)
        vegetationGraph(arq, listVegetation)
        findRelation(arq)
        print("\nnumero de entidades:"+ str(len(entity)))

        arq.write("\n\trankdir=BT\n\tsplines=ortho\n}")
        arq.close()

        render('dot', 'png', 'Resultado/schema.gv')
        os.remove("Resultado/schema.gv")
    return "Graph checked!"


######################################################################################### HYDROGRAPHY
def findClassHydrography(tag):
    if tag in natural_watercourses:
        return "natural_watercourses"
    elif tag in facilities:
        return "facilities"
    elif tag in man_made_waterways:
        return "man_made_waterways"
    elif tag in barriers_on_waterways:
        return "barriers_on_waterways"
    elif tag in other_features_on_waterways:
        return "other_features_on_waterways"
    elif tag in water_related:
        return "water_related"
    return


def hydrographyGraph(arq, listhydrography):
    arq.write(initPackage("HYDROGRAPHY"))
    packageRelation(arq, listhydrography, "vegetation", "hydrography")  ##VEGETATION
    subGraph(arq, "hydrography", hydrography, listhydrography)

    return "HYDROGRAPHY checked!"


######################################################################################### VEGETATION
def findClassVegetation(tag):
    if tag in vegetation_surface_related:
        return "vegetation_surface_related"
    elif tag in landform_related:
        return "landform_related"

    elif tag in geological:
        return "geological"
    return


def vegetationGraph(arq, listVegetation):
    arq.write(initPackage("VEGETATION"))
    subGraph(arq, "vegetation", vegetation, listVegetation)

    return "VEGETATION checked!"


######################################################################################### DELIMITATION
def findClassDelimitation(tag):
    if tag in linear_barriers:
        return "linear_barriers"
    elif tag in access_control_on_highways:
        return "access_control_on_highways"

    elif tag in boundary:
        return "boundary"
    return


def delimitationGraph(arq, listDelimitation):
    arq.write(initPackage("DELIMITATION"))
    subGraph(arq, "delimitation", delimitation, listDelimitation)

    return "DELIMITATION checked!"


######################################################################################### MILITARY
def findClassMilitary(tag):
    if tag in military:
        return "Military"
    return


def militaryGraph(arq, listMilitary):
    arq.write(initPackage("MILITARY"))
    subGraph(arq, "Military", Military, listMilitary)

    return "MILITARY checked!"


######################################################################################### ELECTRICITY
def findClassElectricity(tag):
    if tag in power:
        return "power"
    return


def electricityGraph(arq, listElectricity):
    arq.write(initPackage("ELECTRICITY"))
    subGraph(arq, "electricity", electricity, listElectricity)

    return "ELECTRICITY checked!"


######################################################################################### LANDUSE
def findClassLanduse(tag):
    if tag in landuse:
        return "landuse"
    return


def landUseGraph(arq, listLandUse):
    arq.write(initPackage("LANDUSE"))
    subGraph(arq, "Landuse", Landuse, listLandUse)

    return "LANDUSE checked!"


######################################################################################### LEISURE
def findClassLeisure(tag):
    if tag in entertainment:
        return "entertainment"
    elif tag in leisure:
        return "leisure"
    elif tag in historic:
        return "historic"
    elif tag in tourism:
        return "tourism"
    elif tag in man_made:
        return "man_made"
    elif tag in sport:
        return "sport"
    return


def leisureGraph(arq, listLeisure):
    arq.write(initPackage("LEISURE"))
    packageRelation(arq, listLeisure, "amenity", "Leisure")  ##AMENITY
    subGraph(arq, "Leisure", Leisure, listLeisure)

    return "Leisure checked!"


######################################################################################### HEALTH
def findClassHealth(tag):
    if tag in healthcare:
        return "healthcare"
    elif tag in medical_rescue:
        return "medical_rescue"
    elif tag in firefighters:
        return "firefighters"
    elif tag in lifeguards:
        return "lifeguards"
    elif tag in other_Station:
        return "other_Station"
    elif tag in other_Structure:
        return "other_Structure"
    return


def emergencyGraph(arq, listHealth):
    arq.write(initPackage("HEALTH"))
    packageRelation(arq, listHealth, "amenity", "health")  ##AMENITY
    subGraph(arq, "health", health, listHealth)


    return "HEALTH checked!"


######################################################################################### ROAD MESH
def findClassroad_mesh(tag):
    if tag in roads:
        return "roads"
    elif tag in Path:
        return "Path"
    elif tag in linkRoads:
        return "link roads"
    elif tag in lifecycle:
        return "life cycle"
    elif tag in special_road:
        return "special roads"
    elif tag in other_Highway:
        return "other highway features"

    elif tag in tracks:
        return "tracks"
    elif tag in station_and_shop:
        return "station and shop"
    elif tag in other_Railways:
        return "other Railways"

    elif tag in aerialway:
        return "aerialway"

    elif tag in aeroway:
        return "aeroway"

    elif tag in route:
        return "route"

    elif tag in public_transportation:
        return "public transportation"

def roadMeshGraph(arq, listRoadMesh):
    arq.write(initPackage("ROAD_MESH"))
    subGraph(arq, "road_mesh", road_mesh, listRoadMesh)

    return "road_mesh checked!"


######################################################################################### EDIFICATION
def findClassEdification(tag):
    if tag in office:
        return "office"

    elif tag in accommodation:
        return "accommodation"
    elif tag in Commercial:
        return "Commercial"
    elif tag in religious:
        return "Religious"
    elif tag in building:
        return "building"
    elif tag in civic_amenity:
        return "civic_amenity"
    elif tag in other_building:
        return "other_building"

    elif tag in administratively_declared_places:
        return "administratively_declared_places"
    elif tag in populated_settlements_urban:
        return  "populated_settlements_urban"
    elif tag in populated_settlements_urban_and_rural:
        return "populated_settlements_urban_and_rural"
    elif tag in other_places:
        return "other_places"

    else:
        return "building"


def edificationGraph(arq, listEdification):
    arq.write(initPackage("EDIFICATION"))
    subGraph(arq, "edification", edification, listEdification)

    return "EDIFICATION checked!"


######################################################################################### SERVICES
def findClassService(tag):
    if tag in education:
        return "education"
    elif tag in transportation:
        return "transportation"
    elif tag in sustenance:
        return "sustenance"
    elif tag in financial:
        return "financial"
    elif tag in other_Amenity:
        return "other_Amenity"

    elif tag in general_store:
        return "general_store"
    elif tag in do_it_yourself:
        return "do_it_yourself"
    elif tag in eletronics:
        return "eletronics"
    elif tag in health_beaty:
        return "health and beauty"
    elif tag in food_beverages:
        return "food_beverages"
    elif tag in furniture_interior:
        return "furniture_interior"
    elif tag in outdoors_sport:
        return "outdoors_sport"
    elif tag in discountStore:
        return "discount_Store"
    elif tag in clothing_shoes_acessories:
        return "clothing_shoes_acessories"
    elif tag in art_music_hobbies:
        return "art_music_hobbies"
    elif tag in stationery_gifts_books:
        return "stationary_gifts_books"


def serviceGraph(arq, listService):
    arq.write(initPackage("SERVICES"))
    subGraph(arq, "service", service, listService)

    return "Services checked!"


######################################################################################### CLASS_xml
def initPackage(name):
    return ("\n\tsubgraph cluster_" + name + " {" +
            "\n\t\tnode [color=black style=filled]" +
            "\n\t\tcolor=lightgrey style=filled" +
            "\n\t\tlabel=" + name)


def subGraph(arq, namePackage, package, list):
    flg = []
    global superClass
    global subClass
    global entity
    global contNode  # HOW MANY NODES HAS IN THE SCHEMA
    global mother  # SAVE ALL CLASSES WITH YOUR KEYS, WILL USE FOR FIND RELATION
    listControlMain = []  # SECURITY FLAG, USED FOR TO KNOW IF MAINCLASS(AMENITY, SHOP, HIGHWAY) WAS GENERATED
    listControlSub = []
    listControlthird = []

    for k in package:
        for i in range(len(list)):  ##  TABLE NAME = university, third level
            if k in list[i] and list[i][k] not in listControlthird:
                arq.write(entityName(contNode, list[i][k], entityStereotype(list[i]["stereotype"])))
                mother[contNode] = list[i][k]
                entity[contNode] = list[i][k]
                controllerPackages[contNode] = namePackage
                flg.append(findClass(namePackage, list[i][k]))
                #print(list[i][k])
                contNode = contNode + 1
                arq.write("\n\t\t\t<hr/>")
                for j in list[i].keys():  ##  TABLE ATT
                    if "stereotype" not in j and "lat" not in j and "lon" not in j and k not in j:
                        arq.write(entityAtt(j))
                arq.write(entityAtt("coordinates") + "\n\t\t\t</TABLE>>]")
                listControlthird.append(list[i][k])
                if k not in listControlMain:
                    arq.write(entityName(contNode, k, entityStereotype(None)) + "\n\t\t\t</TABLE>>]")  ## MainClass = highway FIRST LEVEL
                    mother[contNode] = k
                    superClass[contNode] = k
                    controllerPackages[contNode] = namePackage
                    contNode = contNode + 1
                    listControlMain.append(k)

    for i in range(len(flg)):  ## SubClasses = roads, path SECOND LEVEL
        if flg[i] in road_mesh or flg[i] in Leisure or flg[i] in service or flg[i] in edification or flg[i] in Landuse \
                or flg[i] in electricity or flg[i] in Military or flg[i] in delimitation or flg[i] in vegetation or flg[i] in vegetation:
            None
        else:
            if flg[i] not in listControlSub:
                arq.write(entityName(contNode, flg[i], entityStereotype(None)) + "\n\t\t\t</TABLE>>]")
                mother[contNode] = flg[i]
                subClass[contNode] = flg[i]
                controllerPackages[contNode] = namePackage
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
    if name == "Line":
        stereotype += "\n\t\t\t\t<font FACE=\"sigmoda\" POINT-SIZE=\"20.0\"> w</font>"
    if name == "Point":
        stereotype += "\n\t\t\t\t<font FACE=\"sigmoda\" POINT-SIZE=\"20.0\"> b</font>"
    if name == "Polygon":
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
    elif name == 'Leisure':
        return findClassLeisure(tag)
    elif name == 'edification':
        return findClassEdification(tag)
    elif name == 'Landuse':
        return findClassLanduse(tag)
    elif name == 'electricity':
        return findClassElectricity(tag)
    elif name == 'Military':
        return findClassMilitary(tag)
    elif name == 'delimitation':
        return findClassDelimitation(tag)
    elif name == 'vegetation':
        return findClassVegetation(tag)
    elif name == 'hydrography':
        return findClassHydrography(tag)


######################################################################################### REALATION
def entityRelation(slave, master):
    return ("\n\t\t" + str(slave) + " -> " + str(master) + "[arrowhead=onormal]")


def valueKey(dic, val):
    for k, v in dic.items():
        if v == val:
            return k


def findRelation(arq):
    global mother
    # print(mother)
    # print(controllerPackages)
    # print(superClass)
    # print(subClass)
    # print(entity)

    for k,v in mother.items():
        #print(v + " - " + controllerPackages[k])
        if v in entertainment and controllerPackages[k] == 'Leisure':
            arq.write(entityRelation(k, valueKey(mother,'entertainment')))
        elif v in healthcare and controllerPackages[k] == 'health':
            arq.write(entityRelation(k, valueKey(mother,'healthcare')))
        elif v in education and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother,'education')))
        elif v in transportation and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother,'transportation')))
        elif v in financial and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother,'financial')))
        elif v in sustenance and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother,'sustenance')))
        elif v in other_Amenity and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother,'other_Amenity')))
        elif (v in amenity and controllerPackages[k] == 'service') or (v in amenity and controllerPackages[k] == 'health') or (v in amenity and controllerPackages[k] == 'Leisure'):
            arq.write(entityRelation(k, valueKey(mother,'amenity')))

        elif v in food_beverages and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'food_beverages')))
        elif v in general_store and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'general_store')))
        elif v in clothing_shoes_acessories and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'clothing_shoes_acessories')))
        elif v in discountStore and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'discount')))
        elif v in health_beaty and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'health and beauty')))
        elif v in do_it_yourself and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'do_it_yourself')))
        elif v in furniture_interior and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'furniture_interior')))
        elif v in eletronics and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'eletronics')))
        elif v in outdoors_sport and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'outdoors_sport')))
        elif v in art_music_hobbies and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'art_music_hobbies')))
        elif v in stationery_gifts_books and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'stationery_gifts_books')))
        elif v in other_Shop and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'other_Shop')))
        elif v in shop and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'shop')))

        elif v in craft and controllerPackages[k] == 'service':
            arq.write(entityRelation(k, valueKey(mother, 'craft')))

        elif v in leisure and controllerPackages[k] == 'Leisure':
            arq.write(entityRelation(k, valueKey(mother,'leisure')))

        elif v in historic and controllerPackages[k] == 'Leisure':
            arq.write(entityRelation(k, valueKey(mother,'historic')))

        elif v in tourism and controllerPackages[k] == 'Leisure':
            arq.write(entityRelation(k, valueKey(mother,'tourism')))

        elif v in man_made and controllerPackages[k] == 'Leisure':
            arq.write(entityRelation(k, valueKey(mother,'man_made')))

        elif v in sport and controllerPackages[k] == 'Leisure':
            arq.write(entityRelation(k, valueKey(mother,'sport')))

        elif v in landuse and controllerPackages[k] == 'Landuse':
            arq.write(entityRelation(k, valueKey(mother,'landuse')))

        elif v in power and controllerPackages[k] == 'electricity':
            arq.write(entityRelation(k, valueKey(mother,'power')))

        elif v in military and controllerPackages[k] == 'Military':
            arq.write(entityRelation(k, valueKey(mother,'Military')))

        elif v in linear_barriers and controllerPackages[k] == 'delimitation':
            arq.write(entityRelation(k, valueKey(mother,'linear_barriers')))
        elif v in access_control_on_highways and controllerPackages[k] == 'delimitation':
            arq.write(entityRelation(k, valueKey(mother,'access_control_on_highways')))
        elif v in barrier and controllerPackages[k] == 'delimitation':
            arq.write(entityRelation(k, valueKey(mother, 'barrier')))

        elif v in boundary and controllerPackages[k] == 'delimitation':
            arq.write(entityRelation(k, valueKey(mother,'boundary')))

        elif v in medical_rescue and controllerPackages[k] == 'health':
            arq.write(entityRelation(k, valueKey(mother,'medical_rescue')))
        elif v in firefighters and controllerPackages[k] == 'health':
            arq.write(entityRelation(k, valueKey(mother,'firefighters')))
        elif v in lifeguards and controllerPackages[k] == 'health':
            arq.write(entityRelation(k, valueKey(mother,'lifeguards')))
        elif v in other_Station and controllerPackages[k] == 'health':
            arq.write(entityRelation(k, valueKey(mother, 'other_Station')))
        elif v in other_Structure and controllerPackages[k] == 'health':
            arq.write(entityRelation(k, valueKey(mother, 'other_Structure')))
        elif v in emergency and controllerPackages[k] == 'health':
            arq.write(entityRelation(k, valueKey(mother, 'emergency')))

        elif v in other_Highway and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'other highway features')))
        elif v in roads and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'roads')))
        elif v in linkRoads and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'link roads')))
        elif v in special_road and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'special roads')))
        elif v in Path and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'Path')))
        elif v in lifecycle and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'lifecycle')))
        elif v in highway and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'highway')))

        elif v in other_Railways and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'other Railways')))
        elif v in station_and_shop and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'station and shop')))
        elif v in tracks and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'tracks')))
        elif v in railway and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'railway')))

        elif v in aerialway and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'aerialway')))

        elif v in aeroway and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'aeroway')))

        elif v in route and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'route')))

        elif v in public_transportation and controllerPackages[k] == 'road_mesh':
            arq.write(entityRelation(k, valueKey(mother, 'public_transportation')))

        elif v in office and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'office')))

        elif v in accommodation and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'accommodation')))
        elif v in Commercial and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'Commercial')))
        elif v in religious and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'Religious')))
        elif v in civic_amenity and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'civic_amenity')))
        elif v in other_building and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'other_building')))
        elif v in building and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'building')))

        elif v in administratively_declared_places and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'administratively_declared_places')))
        elif v in populated_settlements_urban and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'populated_settlements_urban')))
        elif v in populated_settlements_urban_and_rural and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'populated_settlements_urban_and_rural')))
        elif v in other_places and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'other_places')))
        elif v in place and controllerPackages[k] == 'edification':
            arq.write(entityRelation(k, valueKey(mother, 'place')))

        elif v in landform_related and controllerPackages[k] == 'vegetation':
            arq.write(entityRelation(k, valueKey(mother, 'landform_related')))
        elif v in vegetation_surface_related and controllerPackages[k] == 'vegetation':
            arq.write(entityRelation(k, valueKey(mother, 'vegetation_surface_related')))
        elif v in geological and controllerPackages[k] == 'vegetation':
            arq.write(entityRelation(k, valueKey(mother, 'geological')))
        elif (v in natural and controllerPackages[k] == 'vegetation') or (v in natural and controllerPackages[k] == 'hydrography'):
            arq.write(entityRelation(k, valueKey(mother,'natural')))

        if v in water_related and controllerPackages[k] == 'hydrography':
            arq.write(entityRelation(k, valueKey(mother,'water_related')))
        if v in natural_watercourses and controllerPackages[k] == 'hydrography':
            arq.write(entityRelation(k, valueKey(mother,'natural_watercourses')))
        if v in facilities and controllerPackages[k] == 'hydrography':
            arq.write(entityRelation(k, valueKey(mother,'facilities')))
        if v in barriers_on_waterways and controllerPackages[k] == 'hydrography':
            arq.write(entityRelation(k, valueKey(mother,'barriers_on_waterways')))
        if v in other_features_on_waterways and controllerPackages[k] == 'hydrography':
            arq.write(entityRelation(k, valueKey(mother, 'other_features_on_waterways')))
        if v in waterway and controllerPackages[k] == 'hydrography':
            arq.write(entityRelation(k, valueKey(mother,'waterway')))
        else:
            arq.write(entityRelation())



def packageRelation(arq, list, name, packageName):
    flg = []
    flgremove = []
    listControlthird = []
    listControlSecond = []
    global contNode
    global mother
    global entity
    i = 0


    while i < len(list):  ##  NOME TABELA
        #print(str(i) + " - " + str(len(list)))
        if name in list[i]:
            if (list[i]['amenity'] or list[i]['vegetation']) not in listControlthird:
                arq.write(entityName(contNode, list[i][name], entityStereotype(list[i]["stereotype"])))
                mother[contNode] = list[i][name]
                controllerPackages[contNode] = packageName
                if packageName == 'health':
                    flg.append(findClassHealth(list[i]['amenity']))
                elif packageName == 'Leisure':
                    flg.append(findClassLeisure(list[i]['amenity']))
                elif packageName == 'hydrography':
                    flg.append(findClassHydrography(list[i]['vegetation']))

                contNode = contNode + 1
                arq.write("\n\t\t\t<hr/>")
                for j in list[i].keys():  ##  ATRIBUTOS TABELA
                    if "stereotype" not in j and "lat" not in j and "lon" not in j and name not in j:
                        arq.write(entityAtt(j))
                arq.write(entityAtt("coordinates") + "\n\t\t\t</TABLE>>]")
                listControlthird.append(list[i][name])
                entity[contNode] = list[i][name]
                flgremove.append(i)

            else:
                del list[i]
                i -= 1

        i += 1


    for j in range(len(flg)):  ## SubClasses = HEALTHCARE .....
        if flg[j] not in listControlSecond:
            arq.write(entityName(contNode, flg[j], entityStereotype(None)) + "\n\t\t\t</TABLE>>]")
            mother[contNode] = flg[j]
            listControlSecond.append(flg[j])
            controllerPackages[contNode] = packageName
            contNode = contNode + 1
        else:
            None


