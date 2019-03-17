import time 
from SPARQLWrapper import SPARQLWrapper, JSON
start = time.time()

sparql = SPARQLWrapper("http://drugbank.bio2rdf.org/sparql")

sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	PREFIX db: <http://bio2rdf.org/drugbank_vocabulary:>
	SELECT ?drug_name ?dosage ?indication
	WHERE {
    ?drug a db:Drug .
    ?drug rdfs:label ?drug_name .
    OPTIONAL { ?drug db:dosage ?dosage . }
    OPTIONAL { ?drug db:indication ?indication . }
}
""")


sparql.setReturnFormat(JSON)
results = sparql.query().convert()

end = time.time()
print(end - start)