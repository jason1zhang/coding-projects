import numpy as np 
import pandas as pd

"""
    This Utils.py serves as a place for commonly used tools.
"""

def groupCountValueChange(data, indices, attr, threshold):
    """
        Split the data (DataFrame) into groups based on the indices,
        then calculate the value differences of specified attribute between adjacent rows,
        and count the number of the differences that is greater than specified threshold, for each group.
    """
    group_counts = {}

    for i in range(len(indices) - 1):
        start_idx = indices[i]
        end_idx = indices[i + 1]

        group = data.iloc[start_idx: (end_idx + 1)]

        count = (group[attr] - group[attr].shift(1)).abs().gt(threshold).sum()

        group_counts[start_idx] = count

    results = pd.DataFrame(list(group_counts.items()), columns=['GroupStartIdx', 'count'])

    return results


"""
    test cases
""" 
data = {
    'attr1': [50, 23, 12, 11, 50, 9, 8, 50],
    'attr2': [1, 5, 1, 2, 11, 2, 91, 25]
}

df = pd.DataFrame(data)

indices = df[df['attr1'] == 50].index

attr = 'attr2'
threshold = 5

print(groupCountValueChange(df, indices, attr, threshold))


