
import numpy as np
from scipy import sparse
from sklearn.model_selection import train_test_split


rows = [0,1,2,8]
cols = [1,0,4,8]
vals = [1,2,1,4]

A = sparse.coo_matrix((vals, (rows, cols)))

print(A.todense())

B = A.tocsr()

C = sparse.csr_matrix(np.array([0,1,0,0,2,0,0,0,1]).reshape(1,9))
print(B.shape,C.shape)
D = sparse.vstack([B,C])
print(D.todense())


## read and write
file_name = "sparse_matrix.npz"
sparse.save_npz(file_name, D)
E = sparse.load_npz(file_name)


X = E
y = np.random.randint(0,2,E.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


