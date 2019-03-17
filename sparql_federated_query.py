import time 
from SPARQLWrapper import SPARQLWrapper, JSON
start = time.time()

# http://drugbank.bio2rdf.org/sparql
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

sparql.setQuery("""

    PREFIX dbo: <http://dbpedia.org/ontology/>
	SELECT ?name 
	WHERE
	{ 
		SERVICE SILENT <http://dbdpedia.org/sparql>
		{
			SELECT ?name WHERE
			{
				?pais a dbo:Country.
				?pais rdfs:label ?name.
			}
		}
	}

""")


sparql.setReturnFormat(JSON)
results = sparql.query().convert()

end = time.time()
print(end - start)