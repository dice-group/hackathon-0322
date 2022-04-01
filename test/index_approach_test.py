import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


from modules.extractors.index_based_extractor import extract_resources

test_text = "Which European countries have a constitutional monarchy?"
test_answer = ["Sweden", "Liechtenstein", "Belgium", "Denmark"]


q_ent_list, q_rel_list, a_ent_list = extract_resources(test_text, test_answer)

print("Question Entity List:", q_ent_list, '\n')
print("Question Relation List:", q_rel_list, '\n')
print("Answer Entity List:", a_ent_list, '\n')