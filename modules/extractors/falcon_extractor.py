import urllib3
import json
def extract_resources(question:str, answers:list):
    result_ent_question, result_rel_question, result_ent_answer = [], [], []
    http = urllib3.PoolManager()
    data  = {"text":question}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request(
    'POST',
    'https://labs.tib.eu/falcon/api?mode=long',
    body=encoded_data,
    headers={'Content-Type': 'application/json'}
    )
    question_out = json.loads(r.data.decode('utf-8'))

    for ans in answers:
        data  = {"text":ans}
        encoded_data = json.dumps(data).encode('utf-8')
        r = http.request(
            'POST',
            'https://labs.tib.eu/falcon/api?mode=long',
            body=encoded_data,
            headers={'Content-Type': 'application/json'}
        )
        answer_out = json.loads(r.data.decode('utf-8'))
        for ent in answer_out['entities']:
            result_ent_answer.append(ent[0])

    for ent in question_out['entities']:
    result_ent_question.append(ent[0])

    for rel in question_out['relations']:
    result_rel_question.append(rel[0])  

    return result_ent_question, result_rel_question, result_ent_answer
