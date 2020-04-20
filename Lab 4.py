#Steven Littel, 10 April 2020, GEOG 682 Lab 4
crime = "S:/682/Spring20/slittel/Lab 4/Crime/Crime_Incidents_in_2017/Crime_Incidents_in_2017.shp"
districts = "S:/682/Spring20/slittel/Lab 4/Districts/Police_Districts/Police_Districts.shp"
iface.addVectorLayer(crime,"crime","ogr")
iface.addVectorLayer(districts,"districts","ogr")
processing.run("qgis:joinbylocationsummary", {'INPUT':districts,'JOIN':crime,'PREDICATE':1,'SUMMARIES':0,'OUTPUT':"S:/682/Spring20/slittel/Lab 4/Lab_4_join.shp"})
joindata = "S:/682/Spring20/slittel/Lab 4/Lab_4_join.shp"
iface.addVectorLayer(joindata,"joindata","ogr")
#The 3rd Police District had the most crime with a count if 5,970