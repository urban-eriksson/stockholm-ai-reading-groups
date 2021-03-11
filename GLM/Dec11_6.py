""" Mathekalender 2020-12-11
"""

edges = [
{'nodes': ('N','C') , 'cost': 6, 'used': False, 'wh': False},
{'nodes': ('N','B') , 'cost': 5, 'used': False, 'wh': False},
{'nodes': ('N','A') , 'cost': 7, 'used': False, 'wh': False},
{'nodes': ('A','B') , 'cost': 5, 'used': False, 'wh': True},
{'nodes': ('A','D') , 'cost': 7, 'used': False, 'wh': False},
{'nodes': ('B','C') , 'cost': 3, 'used': False, 'wh': False},
{'nodes': ('B','E') , 'cost': 4, 'used': False, 'wh': False},
{'nodes': ('B','D') , 'cost': 6, 'used': False, 'wh': False},
{'nodes': ('C','H') , 'cost': 4, 'used': False, 'wh': True},
{'nodes': ('C','E') , 'cost': 3, 'used': False, 'wh': False},
{'nodes': ('D','F') , 'cost': 6, 'used': False, 'wh': True},
{'nodes': ('D','G') , 'cost': 2, 'used': False, 'wh': False},
{'nodes': ('E','H') , 'cost': 5, 'used': False, 'wh': False},
{'nodes': ('E','F') , 'cost': 3, 'used': False, 'wh': False},
{'nodes': ('F','S') , 'cost': 8, 'used': False, 'wh': False},
{'nodes': ('F','G') , 'cost': 5, 'used': False, 'wh': False},
{'nodes': ('G','S') , 'cost': 3, 'used': False, 'wh': False},
{'nodes': ('H','S') , 'cost': 7, 'used': False, 'wh': False},
]

def pathfinder(edges, sp, route, visits, sok, totcost, Nwh, Ndouble_visits, conditions):

    # Terminating condition
    if sp == 'N' and sok:
        success = True
        if 'O1' in conditions:
            success = success and totcost <= 24
        if 'O2' in conditions:
            pass # Condition used in algorithm
        if 'O3' in conditions:
            pass # Condition used in algorithm
        if 'O4' in conditions:
            success = success and len(set(route)) == 10 # Unique nodes == 10
        if 'O5' in conditions:
            success = success and Ndouble_visits <= 1
        if 'O6' in conditions:
            success = success and Ndouble_visits >= 1

        if success:
            return True, route, visits, totcost, Nwh, Ndouble_visits
        else:
            return False, [], {}, 0, 0, 0
    else:
        if sp == 'S':
            sok = True

        if sok:
            direction = 'return'
        else:
            direction = 'outward'

        edges_copy = [edge.copy() for edge in edges]
        if 'O3' in conditions:
            possible_moves = [edge for edge in edges_copy if sp in edge['nodes'] and not edge['used']]
        else:
            possible_moves = [edge for edge in edges_copy if sp in edge['nodes']]

        for move in possible_moves:
            # Find next standpoint
            for node in move['nodes']:
                if node != sp:
                    next_sp = node

            # Don't return prematurely
            if next_sp == 'N' and not sok:
                continue

            if sok and move['wh'] and (not 'O2' in conditions or Nwh < 3):
                cost_delta = - move['cost']
                Nwh_delta = 1
            else:
                cost_delta = move['cost']
                Nwh_delta = 0

            Ndouble_visits_delta = 0
            if next_sp in visits:
                if visits[next_sp] == 'outward' and direction == 'return':
                    Ndouble_visits_delta = 1
                # Avoid going through the same node twice on outward and return
                # Not explicitly given I think
                elif visits[next_sp] == direction:
                    continue 

            # edges_copy update by reference
            move['used'] = True

            success, route_hat, visits_hat, totcost_hat, Nwh_hat, Ndouble_visits_hat = pathfinder(
                edges_copy,
                next_sp,
                [*route, next_sp],
                {**visits, next_sp: direction},
                sok,
                totcost + cost_delta,
                Nwh + Nwh_delta,
                Ndouble_visits + Ndouble_visits_delta,
                conditions
                )

            if success:
                return True, route_hat, visits_hat, totcost_hat, Nwh_hat, Ndouble_visits_hat 
            
            move['used'] = False

        return False, [], {}, 0, 0, 0 

test_cases = [
    ['O1','O2','O3'],
    ['O1','O2','O5'],
    ['O1','O2','O6'],
    ['O1','O3','O5'],
    ['O1','O3','O6'],
    ['O1','O4','O5'],
    ['O1','O5','O6'],
    ['O1','O4','O6'],
    ['O2','O3','O4'],
    ['O4','O5','O6'],
]

sp = 'N'
for test_case, i in zip(test_cases, range(len(test_cases))):
    success, route, visits, totcost, Nwh, Ndouble_visits = pathfinder(edges, sp, [], {}, False, 0, 0, 0, test_case)
    print('\n*** Test case ' + str(i+1) + ' (' + ','.join(test_case) + ') ***')
    if success:
        print('Route: ' + ','.join(route))
        print('Duration: ' + str(totcost) + ' hours')
        print('Worm holes used: ' + str(Nwh))
        print('Number of places visited both on outward and return: ' + str(Ndouble_visits))
    else:
        print('Did not find any solution for the given conditions')







