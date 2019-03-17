import time 
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setReturnFormat(JSON)

sparql.setQuery("""

    PREFIX dbo: <http://dbpedia.org/ontology/>
	PREFIX dbp: <http://dbpedia.org/property/>
	SELECT distinct ?rugbyplayer
	WHERE
	{
	    
	    ?rugbyplayer dbo:birthDate|dbp:birthDate ?birthdate

		OPTIONAL
		{
			?rugbyplayer dbp:ruPosition <http://dbpedia.org/resource/Centre_(rugby_union)>	   
		}
		OPTIONAL
		{
		    ?rugbyplayer dbo:birthPlace ?countryOfBirth
		}
		OPTIONAL
		{
		   ?rugbyplayer dbp:ruNationalteam ?nationalteam
		}
		OPTIONAL
		{
		   ?nationalteam dbp:worldCupApps ?numworldcupappearances
		}
		OPTIONAL
		{
		 	?rugbyplayer a dbo:RugbyPlayer
		}
		OPTIONAL
		{
		 	?rugbyplayer dbp:ruNationalcaps ?numcaps.
		}
		OPTIONAL
		{
		 	?rugbyplayer dbo:birthDate|dbp:birthDate ?birthdate.
		}			
	}

	
""")

# average the time over 100 repeated trials
totalTime = 0
for i in range(0, 500):

	start = time.time()

	# fire query
	results = sparql.query()

	end = time.time()
	print(end - start)
	totalTime += (end - start)

finalAvg = totalTime/500
print totalTime
print finalAvg


'''



		OPTIONAL
		{
		    ?rugbyplayer dbo:height ?height.
		}
		OPTIONAL
		{
		   ?rugbyplayer dbo:weight ?weight.
		}
		OPTIONAL
		{
		 	?countryOfBirth dbo:populationTotal ?population.
		}

'''