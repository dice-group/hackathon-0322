from flask import Flask, request
from flask_cors import CORS, cross_origin
from elasticsearch7 import Elasticsearch

#elasticsearch indexing has to be done first
#currently a index is deployed on ea-test.cs.upb.de
#run generateRoberta.py first

import pickle

app = Flask(__name__)
cors = CORS(app)
es = Elasticsearch(["http://localhost:9200"])
model=pickle.load(open("roberta.sav", 'rb'))

def get_embeddings_neighbour(inputtext, index_name,size):
    query_embedding=model.encode(inputtext)
    res = es.search(index=index_name, size=size, query={

                "match": {"verbal": inputtext},
    }, _source=["subject", "predicate", "object"])
    '''
    res = es.search(index=index_name, size=size, query={

        "script_score": {
            "query": {
                "match": {"verbal": inputtext},
            },

            "script": {

                "source": "cosineSimilarity(params.queryVector, 'embeddings') + 1.0",
                "params": {
                    "queryVector": query_embedding
                }
            }
        }
    }, _source=["subject", "predicate", "object"]
                    )'''
    hits = res['hits']['hits']
    if len(hits) > 0:
        results = []
        for i in hits:
            results.append(i['_source'])
        return results
    return None
'''
    res = es.search(index=index_name,size=size,query={
        
        "script_score": {
            "query": {
                "bool": {
                }
            },
    
                "script": {
    
                    "source": "cosineSimilarity(params.queryVector, 'embeddings') + 1.0",
                    "params": {
                        "queryVector": query_embedding
                    }
                }
            }
        },_source=["subject","predicate","object"]
        )'''




@app.route('/get-triples-by-text', methods=['GET', 'POST'])
@cross_origin()
def get_triples_by_text():
    if "input-text" not in request.json:
        return "Invalid parameters", 400
    input_text = request.json["input-text"]
    index_name = request.json["indexname"]
    size = request.json["size"]
    neighbours = get_embeddings_neighbour(input_text, index_name,size)
    result = {
        "triples": neighbours
    }
    return result


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")