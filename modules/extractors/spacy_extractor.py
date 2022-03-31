def extract_resources(text_question, answer_list):
    entity_list =  list()
    relation_list = list()
    """
    Knowledge Extraction logic here
    """
    NER = spacy.load("en_core_web_sm")
    #raw_text="How much did Pulp Fiction cost?"
    text1= NER(text_question)
    text2= NER(answer_list)
    for word in text1.ents:
        print(word.text,word.label_)
        entity_list.append(word.text)
    for word in text1.ents:
        print(word.text,word.label_)
        entity_list.append(word.text)
    return entity_list relation_list
