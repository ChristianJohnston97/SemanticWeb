import time 
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setReturnFormat(JSON)

sparql.setQuery("""

    PREFIX dbo: <http://dbpedia.org/ontology/>
	PREFIX dbp: <http://dbpedia.org/property/>
	SELECT distinct ?rugbyplayer
	FROM NAMED <http://dbpedia.org/ontology/>
	FROM NAMED <http://dbpedia.org/property/>

	WHERE
	{
	    
	    ?rugbyplayer dbo:birthDate|dbp:birthDate ?birthdate

		OPTIONAL
		{
			?rugbyplayer dbp:ruPosition <http://dbpedia.org/resource/Centre_(rugby_union)>	   
		}

		GRAPH <http://dbpedia.org/ontology>
		{
			OPTIONAL
			{
		    	?rugbyplayer dbo:birthPlace ?countryOfBirth
			}
		}
		GRAPH <http://dbpedia.org/property>
		{
			OPTIONAL
			{
		    	?rugbyplayer dbo:birthPlace ?countryOfBirth
			}
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
