from modules.knowledge_extraction import extract_resources
from modules.sparql_generator import generate_sparql


def create_sparql(text_question, text_answer):
    # Extract knowledge
    qa_pair = (text_question, text_answer)
    entity_list, relation_list = extract_resources(qa_pair)
    sparql = generate_sparql(entity_list, relation_list, )
    return sparql

# TODO: Read input from a file and write output to a file
