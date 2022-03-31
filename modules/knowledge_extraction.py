from multiprocessing import Manager, Process
import extractors.dbpediaspotlight_extractor as dbps
import extractors.falcon_extractor as fal
import extractors.index_based_extractor as ind
import extractors.spacy_extractor as spa
import extractors.tagme_extractor as tag


def extract_resources(text_question, answer_list):
    entity_list = list()
    relation_list = list()
    """
    Knowledge Extraction
    """

    res_map = dict()
    with Manager() as manager:
        res_dict = manager.dict()
        process_list = list()
        # DBpedia Spotlight
        process_list.append(Process(target=parallel_wrapper,
                                    args=('dbps', dbps.extract_resources, [text_question, answer_list], res_dict)))
        # Falcon
        process_list.append(Process(target=parallel_wrapper,
                                    args=('fal', fal.extract_resources, [text_question, answer_list], res_dict)))
        # Indexing Based
        process_list.append(Process(target=parallel_wrapper,
                                    args=('ind', ind.extract_resources, [text_question, answer_list], res_dict)))
        # Spacy
        process_list.append(Process(target=parallel_wrapper,
                                    args=('spa', spa.extract_resources, [text_question, answer_list], res_dict)))
        # TagMe
        process_list.append(Process(target=parallel_wrapper,
                                    args=('tag', tag.extract_resources, [text_question, answer_list], res_dict)))

        # Start all processes
        for proc in process_list:
            proc.start()
        # Wait for all processes to finish
        for proc in process_list:
            proc.join()
        # copy all the results from the shared managed object
        for key in res_dict:
            ent_list, rel_list = res_dict[key]
            entity_list.extend(ent_list)
            relation_list.append(rel_list)
    return entity_list, relation_list


def parallel_wrapper(key, func, args, res):
    res[key] = func(*args)
