import requests
import sparql
from functools import reduce

def extract_resources(question:str, answer:list):
    r1 = requests.get('https://tagme.d4science.org/tagme/tag?lang=en&include_abstract=true&include_categories=true&gcube-token=27df9d89-f3f8-4fbb-9f1a-060fc53e81f1-843339462&text='\
                     +question)
    r2 = requests.get('https://tagme.d4science.org/tagme/tag?lang=en&include_abstract=true&include_categories=true&gcube-token=27df9d89-f3f8-4fbb-9f1a-060fc53e81f1-843339462&text='\
                     +reduce(lambda ans1, ans2: ans1+' '+ans2, answer))
    
    entities_question = []
    entities_answer = []
    
    clean_question = r1.text.replace('{', '').replace('}', '').replace('[', '').replace(']', '')
    tokens_question = r1.text.split(' ')
    
    clean_answer = r2.text.replace('{', '').replace('}', '').replace('[', '').replace(']', '')
    tokens_answer = r2.text.split(' ')
    
    for tk in clean_question.split(','):
        if '"id"' in tk:
            id = tk.strip().split(':')[-1]
            q = ('SELECT DISTINCT ?uri WHERE {?uri dbo:wikiPageID ?id . FILTER (?id=534366)} LIMIT 1'.replace('id=534366', f'id={id}'))
            result = sparql.query('http://dbpedia.org/sparql', q)
            for ent in result:
                entities_question.append(ent[0].n3().strip('<>'))
                
    for tk in clean_answer.split(','):
        if '"id"' in tk:
            id = tk.strip().split(':')[-1]
            q = ('SELECT DISTINCT ?uri WHERE {?uri dbo:wikiPageID ?id . FILTER (?id=534366)} LIMIT 1'.replace('id=534366', f'id={id}'))
            result = sparql.query('http://dbpedia.org/sparql', q)
            for ent in result:
                entities_answer.append(ent[0].n3().strip('<>'))
    return entities_question, [], entities_answer
    
