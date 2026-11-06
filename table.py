def row_sums(matrix):
    result = []
    for row in matrix:
        result.append(sum(row))
    return result


def column_sums(matrix):
    if not matrix:
        return []
    columns = len(matrix[0])
    result = [0] * columns
    for row in matrix:
        for index, value in enumerate(row):
            result[index] += value
    return result
