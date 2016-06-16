def nightRoute(city):
    for connections in city:
        for city2, bridge_value in enumerate(connections):
            if bridge_value != -1:

    # destination_connections = []
    # total_city = len(city[0])
    # start_idx = 0
    # end_idx = len(city[0]) - 1
    # for i, j in zip(city[len(city[0]) - 1], range(0, end_idx)):
    #	if i != -1:
    #			destination_connections.append(j)
    # compute_cost()


# def compute_cost():
    # pass


if __name__ == '__main__':
    city = [[-1, -1, 19, 8, 18, -1, -1, -1, -1, -1],
            [10, 6, 4, 7, 0, 10, 18, -1, 0, -1],
            [-1, -1, 15, -1, 17, 3, -1, 14, 16, 3],
            [4, 19, 3, 15, 8, 4, 6, 11, 5, 8],
            [5, 3, 10, -1, 0, 14, 15, 1, 16, 5],
            [-1, 8, -1, -1, 5, -1, 5, 0, 1, -1],
            [-1, 18, -1, 19, 2, -1, 10, -1, 8, 6],
            [14, 8, 12, 16, -1, -1, 0, 16, 15, 17],
            [4, 5, 1, 12, 0, 4, 8, 15, 1, -1],
            [13, 7, 17, -1, 4, 13, 16, 3, 12, 9]]
    nightRoute(city)
