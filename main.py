from modules.knowledge_extraction import extract_resources
from modules.sparql_generator import generate_sparql


def create_sparql(text_question, answer_list):
    # Extract knowledge
    entity_list, relation_list = extract_resources(text_question, answer_list)
    sparql = generate_sparql(entity_list, relation_list, text_question, answer_list)
    return sparql

# TODO: Read input from a file and write output to a file
