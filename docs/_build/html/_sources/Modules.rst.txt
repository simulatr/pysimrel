Modules
=====================================

Examples
----------------

>>> sobj = Simrel(n_pred = 10, n_relpred = '4, 5', pos_relcomp = '0, 1; 2, 3, 4', 
    gamma = 0.7, rsq = '0.7, 0.8', n_resp = 4, eta = 0.7, pos_resp = '0, 2; 1, 3')

>>> print(sobj.properties)
Numpy Arrays:
---------------------------------------------
eigen_x:                 Shape: (10,)        
eigen_y:                 Shape: (4,)         
rotation_x:              Shape: (10, 10)     
rotation_y:              Shape: (4, 4)       
sigma_latent:            Shape: (14, 14)     
sigma:                   Shape: (14, 14)     
rsq:                     Shape: (4, 4)       
rsq_w:                   Shape: (4, 4)       
minerror:                Shape: (4, 4)       
beta_z:                  Shape: (10, 4)      
beta:                    Shape: (10, 4)      
beta0:                   Shape: (4,)         
Dictionaries:
---------------------------------------------
relevant_predictors:     Keys: rel, irrel  

>>> print(sobj.covariances)
    Numpy Arrays:
    +-------------+-------------------+
    |             |                   |
    |    cov_ww   |       cov_wz      |
    |    cov_yy   |       cov_xy      |
    |    (4, 4)   |      (4, 10)      |
    |             |                   |
    +-------------+-------------------+
    |             |                   |
    |             |                   |
    |    cov_zw   |       cov_zz      |
    |    cov_xy   |       cov_xx      |
    |   (10, 4)   |      (10, 10)     |
    |             |                   |
    |             |                   |
    +-------------+-------------------+ 


.. automodule:: pysimrel
    :members:
    :undoc-members:
    :show-inheritance:


