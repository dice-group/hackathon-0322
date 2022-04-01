def extract_resources(text_question, answer_list):
    q_entity_list = list()
    q_relation_list = list()
    a_entity_list = list()
    
    NER = spacy.load("en_core_web_sm")
    #raw_text="How much did Pulp Fiction cost?"
    text1= NER(text_question)
    text2= NER(answer_list)
    for word in text1.ents:
        print(word.text,word.label_)
        q_entity_list.append(word.text)
    for word in text2.ents:
        print(word.text,word.label_)
        a_entity_list.append(word.text)
    return q_entity_list, q_relation_list, a_entity_list
