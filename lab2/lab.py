# NO IMPORTS ALLOWED!

import json

def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    return any({i, j} == {actor_id_1, actor_id_2} for i, j, _ in data)

def make_data_dict(data):
    db = {}
    for datum in data:
        if datum[0] in db:
            db[datum[0]].add(datum[1])
        else:
            db[datum[0]] = {datum[1]}
        if datum[1] in db:
            db[datum[1]].add(datum[0])
        else:
            db[datum[1]] = {datum[0]}
    return db

def add_new_level(db, actors, backtrack):
    '''
    takes db dictionary, set of actors in previous level, and parent pointer dictionary,
    returns tuple (new_level, updated dictionary)
    '''
    level = set()
    d = {}
    for actor in actors:
        for child in db[actor]:
            if child not in backtrack:
                backtrack[child] = actor
                level.add(child)
    return (level, backtrack)

def get_actors_with_bacon_number(data, n):
    db = make_data_dict(data)
    actors = {4724}
    backtrack = {4724:None}
    i = 0
    while i < n:
        actors, backtrack = add_new_level(db, actors, backtrack)
        i += 1
    return actors

def get_bacon_path(data, target):
    return get_path(data, 4724, target)

def get_path(data, actor_id_1, actor_id_2):
    levels = {0:set([actor_id_1])}
    backtrack = {actor_id_1:None}
    db = make_data_dict(data)
    if actor_id_1 not in db or actor_id_2 not in db:
        return None
    number = 0
    while levels[number] != set():
        level, backtrack = add_new_level(db, levels[number], backtrack)
        number += 1
        levels[number] = level
        if actor_id_2 in level:
            break
    path = [actor_id_2]
    while path[-1] != actor_id_1:
        path += [backtrack[path[-1]]]
    return path[::-1]

if __name__ == '__main__':
    with open('resources/large.json') as f:
        db = json.load(f)
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    print(get_bacon_path(db, 197897))
    pass
