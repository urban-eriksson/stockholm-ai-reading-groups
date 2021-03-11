""" Mathekalender 2020-12-17
"""
import numpy as np

edges = [
    {'nodes': ('N','4') , 'cost': 28, 'used': False},
    {'nodes': ('N','5') , 'cost': 28, 'used': False},
    {'nodes': ('N','7') , 'cost': 22, 'used': False},
    {'nodes': ('N','9') , 'cost': 30, 'used': False},
    {'nodes': ('N','8') , 'cost': 28, 'used': False},
    {'nodes': ('1','5') , 'cost': 36, 'used': False},
    {'nodes': ('1','4') , 'cost': 22, 'used': False},
    {'nodes': ('1','3') , 'cost': 28, 'used': False},
    {'nodes': ('1','2') , 'cost': 41, 'used': False},
    {'nodes': ('2','3') , 'cost': 22, 'used': False},
    {'nodes': ('2','6') , 'cost': 32, 'used': False},
    {'nodes': ('2','10') , 'cost': 60, 'used': False},
    {'nodes': ('3','4') , 'cost': 10, 'used': False},
    {'nodes': ('3','6') , 'cost': 22, 'used': False},
    {'nodes': ('4','5') , 'cost': 40, 'used': False},
    {'nodes': ('4','8') , 'cost': 40, 'used': False},
    {'nodes': ('4','6') , 'cost': 28, 'used': False},
    {'nodes': ('5','7') , 'cost': 30, 'used': False},
    {'nodes': ('6','8') , 'cost': 28, 'used': False},
    {'nodes': ('6','10') , 'cost': 32, 'used': False},
    {'nodes': ('7','9') , 'cost': 28, 'used': False},
    {'nodes': ('8','9') , 'cost': 22, 'used': False},
    {'nodes': ('8','11') , 'cost': 20, 'used': False},
    {'nodes': ('8','10') , 'cost': 32, 'used': False},
    {'nodes': ('9','11') , 'cost': 22, 'used': False},
    {'nodes': ('10','11') , 'cost': 32, 'used': False},
]

# nodes = [
#     {'post_office': 1, 'letters': 38, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 2, 'letters': 76, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 3, 'letters': 4, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 4, 'letters': 61, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 5, 'letters': 37, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 6, 'letters': 19, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 7, 'letters': 2, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 8, 'letters': 3, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 9, 'letters': 5, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 10, 'letters': 18, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False},
#     {'post_office': 11, 'letters': 23, 'empty': False, 'visited_by_steffan': False, 'visisted_by_ralph': False}
# ]

nodes = {
    'N': {'letters': 0, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '1': {'letters': 38, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '2': {'letters': 76, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '3': {'letters': 4, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '4': {'letters': 61, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '5': {'letters': 37, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '6': {'letters': 19, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '7': {'letters': 2, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '8': {'letters': 3, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '9': {'letters': 5, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '10': {'letters': 18, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False},
    '11': {'letters': 23, 'empty': False, 'visited_by_steffan': False, 'visited_by_ralph': False}
}


Nmax = 143
tmax = 204

letters = np.array([nodes[key]['letters'] for key in nodes.keys() if not key=='N'])
offices = np.array([key for key in nodes.keys() if not key=='N'])


res = []

for j in range(2048):
    selector = np.array(list(np.binary_repr(j).zfill(11))).astype(np.bool)
    if np.sum(letters[selector]) == Nmax:
        res.append(selector)


def pathfinder(sp, edges, nodes, route, letters, totcost, node_list):
    #if sp == 'N' and letters == 143:
    if sp == 'N' and letters == 143 and totcost == tmax:
        print('hej')
        return True, [{'route': route, 'time': totcost}]
    elif sp == 'N' and totcost > 0:
        return False, [{}]
    elif totcost >=300:
        return False, [{}]
    else:
        edges_copy = [edge.copy() for edge in edges]
        nodes_copy = {key:value.copy() for key,value in nodes.items()}
        possible_moves = [edge for edge in edges_copy if sp in edge['nodes']]
        res = []
        for move in possible_moves:
            # Find next standpoint
            for node in move['nodes']:
                if node != sp:
                    next_sp = node
            if nodes_copy[next_sp]['visited_by_ralph']:
                continue
            else:
                nodes_copy[next_sp]['visited_by_ralph'] = True 

            cost_delta = move['cost']

            if next_sp in node_list:
                letters_delta = nodes[next_sp]['letters']
            else:
                letters_delta = 0

            success, res_hat = pathfinder(
                next_sp,
                edges_copy,
                nodes_copy,
                [*route, next_sp],
                letters + letters_delta,
                totcost + cost_delta,
                node_list
                )

            if success:
                res.extend(res_hat)
            nodes_copy[next_sp]['visited_by_ralph'] = False

        return len(res) > 0, res 



def pathfinder2(sp, edges, nodes, route, letters, totcost, node_list):
    #if sp == 'N' and letters == 143:
    if sp == 'N' and letters == 143 and totcost < tmax:
        print('hej')
        return True, [{'route': route, 'time': totcost}]
    elif sp == 'N' and totcost > 0:
        return False, [{}]
    elif totcost >=300:
        return False, [{}]
    else:
        edges_copy = [edge.copy() for edge in edges]
        nodes_copy = {key:value.copy() for key,value in nodes.items()}
        possible_moves = [edge for edge in edges_copy if sp in edge['nodes']]
        res = []
        for move in possible_moves:
            # Find next standpoint
            for node in move['nodes']:
                if node != sp:
                    next_sp = node
            if nodes_copy[next_sp]['visited_by_ralph']:
                continue
            else:
                nodes_copy[next_sp]['visited_by_ralph'] = True 

            cost_delta = move['cost']

            if next_sp in node_list:
                letters_delta = nodes[next_sp]['letters']
            else:
                letters_delta = 0

            success, res_hat = pathfinder2(
                next_sp,
                edges_copy,
                nodes_copy,
                [*route, next_sp],
                letters + letters_delta,
                totcost + cost_delta,
                node_list
                )

            if success:
                res.extend(res_hat)
            nodes_copy[next_sp]['visited_by_ralph'] = False

        return len(res) > 0, res 


for selector in res:
    node_list = offices[selector]
    success, res_hat = pathfinder('N', edges, nodes, [], 0, 0, node_list)
    if success:
        print(selector)
        node_list2 = offices[np.logical_not(selector)]
        success, res_hat2 = pathfinder2('N', edges, nodes, [], 0, 0, node_list2)
        print('hej')
