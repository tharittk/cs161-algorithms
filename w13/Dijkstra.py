from Johnson import *

def dijkstra(G, node_start = 1):
    # initialization
    vtx_explored = [node_start]
    vtx_unexplored = list(G.thc.keys()) # all node that has incoming edges

    try:
        vtx_unexplored.remove(node_start)
    except:
        pass # the start node has no incoming

    last_point_score = {}
    last_point_score[node_start]  = 0
    is_exhausted = False

    while not is_exhausted:
        current_min_score = float('inf')
        is_exhausted = True # must invalidate this in loop

        for node in vtx_explored:
            try:
                for dest in list(G.htc[node].keys()):
                    if dest not in vtx_explored:
                        is_exhausted = False
                        # calculate
                        currScore = (last_point_score[node] + G.thc[dest][node])
                        if currScore < current_min_score:
                            current_min_score = currScore
                            current_dest = dest
            except:# no outgoing edge
                pass
            # get the edge wanted
        if is_exhausted:
             break

        last_point_score[current_dest]= current_min_score
        vtx_explored.append(current_dest)
        vtx_unexplored.remove(current_dest)


    # for those unreachable
    for node in vtx_unexplored:
        last_point_score[node] = float('inf')

    return last_point_score



if __name__ == "__main__":
    g = Graph()
    #g.read_text_input('./small_g.txt')
    g.read_legacy_dijkstra('./DijkstraData.txt')
    last_point_score = dijkstra(g)
    #print(last_point_score)

    Ans = ''
    toAns = [7,37,59,82,99,115,133,165,188,197]
    for id in toAns:
        Ans += (str(last_point_score[id]) +',')
    print('>> Ans: ', Ans)