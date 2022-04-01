from multiprocessing import Manager, Process
import extractors.dbpediaspotlight_extractor as dbps
import extractors.falcon_extractor as fal
import extractors.index_based_extractor as ind
import extractors.spacy_extractor as spa
import extractors.tagme_extractor as tag


def extract_resources(text_question, answer_list):
    q_entity_list = list()
    q_relation_list = list()
    a_entity_list = list()
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
            sol = res_dict[key]
            q_ent_list = sol[0]
            q_rel_list = sol[1]
            a_ent_list = sol[2]
            q_entity_list.extend(q_ent_list)
            q_relation_list.append(q_rel_list)
            a_entity_list.append(a_ent_list)

        # Indexing Based
        proc_ind = Process(target=parallel_wrapper,
                           args=('ind', ind.extract_resources, [text_question, a_entity_list], res_dict))
        proc_ind.start()
        proc_ind.join()
        q_ent_list, q_rel_list, a_ent_list = res_dict['ind']
        q_entity_list.extend(q_ent_list)
        q_relation_list.append(q_rel_list)

    return q_entity_list, q_relation_list, a_entity_list


def parallel_wrapper(key, func, args, res):
    res1, res2, res3 = func(*args)
    res[key] = (res1, res2, res3)
