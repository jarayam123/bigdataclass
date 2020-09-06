"""Toy join function to showcase spark functions."""

def join_dataframes(left, right, columns_left, columns_right):
    where = []
    for column in range(len(columns_left)):
        lc = left[columns_left[column]]
        rc = right[columns_right[column]]
        where.append(lc==rc)

    return left.join(right, where)