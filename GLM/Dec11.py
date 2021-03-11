


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


def pathfinder(edges, sp, route, sok, totcost, Nvisited, Nwh_used, Ndouble_visits):
    if sp == 'S':
        sok = True
    #if Nvisited >= 9 and sp == 'N' and totcost < 26:
    #    print(Nvisited)
    #    print(totcost)
    #    print(Nwh_used)
    #    print(route)
    if sp == 'N' and sok and totcost <= 24:
        print('Found route!!')
        print(route)
        print (totcost)
        print('hej')
    else:
        edges_copy = [edge.copy() for edge in edges]
        # moves = [edge for edge in edges_copy if sp in edge['nodes'] and not edge['used'] and not (edge['wh'] and not sok) and not (edge['wh'] and Nwh_used == 2)] # 1
        #moves = [edge for edge in edges_copy if sp in edge['nodes'] and not edge['used']] # 1b
        possible_moves = [edge for edge in edges_copy if sp in edge['nodes']] # 2
        possible_moves = [move for move in possible_moves if not move['used']]


        for move in possible_moves:
            for node in move['nodes']:
                if node != sp:
                    next_sp = node
            if next_sp in route:
                if Ndouble_visits < 10:
                    new_Ndouble_visits = Ndouble_visits + 1
                else:
                    continue
            else:
                new_Ndouble_visits = Ndouble_visits 
            move['used'] = True
            if sok and move['wh'] and Nwh_used < 2:
                new_totcost = totcost - move['cost']
                Nwh_used += 1
            else:
                new_totcost = totcost + move['cost']
            pathfinder(edges_copy, next_sp, [*route, next_sp], sok, new_totcost, Nvisited + 1, Nwh_used, new_Ndouble_visits)
            move['used'] = False






sp = 'N'
pathfinder(edges, sp, [], False, 0, 0, 0, 0)






