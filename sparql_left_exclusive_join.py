import time 
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setReturnFormat(JSON)
sparql.setQuery("""
	
  	PREFIX dbo: <http://dbpedia.org/ontology/>
	PREFIX dbp: <http://dbpedia.org/property/>
	SELECT distinct ?rugbyplayer ?nationalteam ?numcaps ?countryOfBirth
	WHERE
	{
		{
			?rugbyplayer dbo:birthDate|dbp:birthDate ?birthdate
		}

		MINUS
		{
			?rugbyplayer dbp:ruPosition <http://dbpedia.org/resource/Centre_(rugby_union)>	   
		}
		MINUS
		{
		    ?rugbyplayer dbo:birthPlace ?countryOfBirth
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
MINUS
		{
		    ?rugbyplayer dbo:birthPlace ?countryOfBirth
		}

		MINUS
		{
		   ?rugbyplayer dbp:ruNationalteam ?nationalteam
		}
		MINUS
		{
		    ?rugbyplayer dbp:ruNationalcaps ?numcaps
		}

'''
