def decon_reg_new(A,b,xo,my_lambda,Max_iter):
    i=0
    while i<Max_iter: 
        e=0.000001
        temp=(np.dot(A,xo)-b)
        r=np.dot(A.T,temp) +(my_lambda/2)*(np.divide(xo,(np.sqrt((xo)**2+e**2))))
        beta=0.1;#np.dot(r.T,r)/np.dot(r.T,np.dot(A.T,b))
        y=xo
        xo=xo-beta*r
        xnew=xo
        if np.linalg.norm(xnew-y)<0.0001:
            break
        else:
            i=i+1
            
    x_sol=xnew;
    final_iter=i;

    return x_sol,final_iter
# x_sol_reg_new,final_iter=decon_reg_new(A,dnew,xo,0,500)
# plt.plot(x_sol_reg_new)
