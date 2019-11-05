import pytest
import numpy as np
from pysimrel.utilities import *

@pytest.fixture
def cov_mat():
    n_pred = 10
    n_resp = 4
    lmd = get_eigen(0.8, n_pred)
    kappa = get_eigen(1.2, n_resp)
    pos_relcomp = [list(range(4)), list(range(5, 7))]
    rsq = [0.7, 0.8]
    rs = np.random.RandomState(123)
    alpha_ = [rs.uniform(-1, 1, len(x)) for x in pos_relcomp]
    covs = get_cov(pos_relcomp, rsq, kappa, lmd)
    return n_pred, n_resp, lmd, kappa, pos_relcomp, rsq, covs
    
def test_cov_mat_shape(cov_mat):
    p, m, l, k, relpos, rsq, covs = cov_mat
    

# def test_rotmat_properties(rotation_matrix):
#    p, relpred, relcomp, rel_irrel, rot_mat = rotation_matrix
#    AtA = np.dot(rot_mat.T, rot_mat)
#    AAt = np.dot(rot_mat, rot_mat.T)
#    eye = np.eye(rot_mat.shape[0])
#    # Test if Square
#    assert rot_mat.shape[0] == rot_mat.shape[1]
#    # Test if Orthogonal
#    assert np.allclose(AtA, eye, atol=1e-15, rtol=1e-15)
#    assert np.allclose(AAt, eye, atol=1e-15, rtol=1e-15)

# def test_rotmat_values(rotation_matrix):
#     p, relpred, relcomp, rel_irrel, rot_mat = rotation_matrix
#     rel = [x for y in rel_irrel['rel'] for x  in y]
#     irrel = list(rel_irrel['irrel'])
#     assert np.all(rot_mat[irrel][:,rel] == 0)
#     assert np.all(rot_mat[rel][:,irrel] == 0)