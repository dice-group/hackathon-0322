from modules.knowledge_extraction import extract_resources
from modules.sparql_generator import generate_sparql


def create_sparql(text_question, answer_list):
    # Extract knowledge
    q_entity_list, q_relation_list, a_entity_list = extract_resources(text_question, answer_list)
    sparql = generate_sparql(q_entity_list, q_relation_list, a_entity_list, text_question, answer_list)
    return sparql

# TODO: Read input from a file and write output to a file
