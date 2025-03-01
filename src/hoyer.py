import numpy as np

def hoyer_squared_norm(x):
    """Compute the Hoyer squared norm: (||x||_1)^2 / ||x||_2^2."""
    S1 = np.linalg.norm(x, 1)  # L1 norm
    S2 = np.linalg.norm(x, 2)**2  # L2 norm squared
    return (S1**2) / (S2 + 1e-8)  # Avoid division by zero

def my_hoyer_squared_norm_derivative(x):
    m = len(x)
    v=np.zeros_like(x)
    v_l1=np.sum(np.abs(x))+1e-8
    v_l2=np.sum(x**2)+1e-8
    
    if v_l2 == 0:
        return np.zeros_like(x)  # Avoid division by zero
    
    for i in range(m):
        v[i]=np.sign(x[i])*(v_l1/v_l2**2)*(v_l2-(np.abs(x[i])*v_l1));
        
    return v


def SD_hoyer_squared(A, d, x0, alpha, lam, max_iter=1000, tol=1e-6):
    
    x = x0 
    for i in range(max_iter):
        temp=np.dot(A, x)
        r=temp-d
        grad=np.dot(A.T, r)
        reg=my_hoyer_squared_norm_derivative(x)
        x=x-alpha*(grad+lam*reg)
    
        res= np.dot(r, r)
        if res<tol:
            break
    x_sol=x;
    final_iter=i;

    return x_sol, final_iter

def SD_hoyer_squared_radon(forward_func, adjoint_func, d, dt, h, q, N, flow, fhigh, alpha, lam, max_iter=1000, tol=1e-6):
    
    x = adjoint_func(d, dt, h, q, N, flow, fhigh) 
    m,n=x.shape
    for i in range(max_iter):
        temp=forward_func(x, dt, h, q, N, flow, fhigh)#np.dot(A, x)
        r=temp-d
        grad=adjoint_func(r, dt, h, q, N, flow, fhigh) #np.dot(A.T, r)
        
        k=x.flatten()
        
        hoyer=my_hoyer_squared_norm_derivative(k)
        
        reg=np.reshape(hoyer, ((m,n)))
        
        x=x-alpha*(grad+lam*reg)
    
        res= np.sum(r.flatten()**2)
        if res<tol:
            break
    x_sol=x;
    final_iter=i;

    return x_sol, final_iter



