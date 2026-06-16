import numpy as np


# 示例共现矩阵
""" 我  喜欢  自然  语言  处理 。
	我  爱  深度  学习  。
	我  喜欢  机器  学习  。 """


M = np.array([[0, 2, 1, 1, 0],
              [2, 0, 0, 1, 1],
              [1, 0, 0, 2, 1],
              [1, 1, 2, 0, 0],
              [0, 1, 1, 0, 0]])

def pmi(M,positive=True):
    """
    Compute the Pointwise Mutual Information (PMI) matrix from a co-occurrence matrix M.

    Parameters:
    M (numpy.ndarray): Co-occurrence matrix where M[i, j] is the count of co-occurrences between items i and j.
    positive (bool): If True, return only positive PMI values; otherwise, return all PMI values.

    Returns:
    numpy.ndarray: PMI matrix of the same shape as M.
    """
    col_totals = M.sum(axis=0)      # 按列求和
    row_totals = M.sum(axis=1)      # 按行求和

    total = M.sum()                 # 总频次
    expected = np.outer(row_totals, col_totals) / total  # 计算期望频次

    M = M / expected  # 计算 PMI

    with np.errstate (divide='ignore', invalid='ignore'): # 处理除以零的情况
        M = np.log(M)  # 取对数
    M[~np.isfinite(M)] = 0.0  # 将无穷大和 NaN 替换为 0
    if positive:
        M = np.maximum(M, 0)  # 只保留正的 PMI 值
    return M

M_pmi = pmi(M)
np.set_printoptions(precision=2)
print(M_pmi)
