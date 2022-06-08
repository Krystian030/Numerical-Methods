def lagrange(x, sample):
    length = len(sample)
    result = 0
    for i in range(length):
        tmp = 1.0
        for j in range(length):
            if i != j:
                tmp *= (x-sample[j][0])/(sample[i][0]-sample[j][0])
        result += tmp * sample[i][1]
    return result


def lagrange_interpolation(step, data_interpolation):
    input_nodes = data_interpolation[::step]
    result = []
    for x in range(input_nodes[-1][0] + 1):
        height = lagrange(x, input_nodes)
        result.append((x, height))
    return result, input_nodes
