layer_path = "/home/turkey/Desktop/GISdata/Data/CA_Counties_TIGER2016.shp"
#Defines layer path to file to be selected from
layer_name = "CA_Zipcodes"
#define layer name
vlayer = QgsVectorLayer(layer_path, layer_name, "ogr")
#Use QgsVectorLayer to load and define layer_name
QgsProject.instance().addMapLayer(vlayer)
# adds vlayer to map


ca_csv = 'file:////home/turkey/Desktop/GISdata/Data/0d9be83b-5027-41ff-97b2-6ca70238d778.csv'
#csv variable "FILE://PATHTOFILE/FILENAME.CSV" file// is needed before filepath"
csvLyr = QgsVectorLayer(ca_csv,'covid_stats','delimitedtext')
#csv layer
csvLyr.isValid()
#checks if CSV is valid
QgsProject.instance().addMapLayer(csvLyr)
#adds layer to map

csvField ='county'
shpField ='NAME'
#sets field names for CSV and SHP



joinObject=QgsVectorLayerJoinInfo()
joinObject.setJoinFieldName(csvField)
#Join field name from CSV
joinObject.setTargetFieldName(shpField)
#join target field name from shp

joinObject.setJoinLayerId(csvLyr.id())
joinObject.setUsingMemoryCache(True)
joinObject.setJoinLayer(csvLyr)
vlayer.addJoin(joinObject)

iface.mapCanvas().refresh()
#Refresh map Canvas
