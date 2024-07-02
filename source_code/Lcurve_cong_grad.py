my_lambda=np.logspace(-3,0.5,10)
x=[]
y=[]
for i in my_lambda:
    x_sol_cg_noise_reg,itr=conjugate_gradient_reg(A,dnew,xo,i,500,tol=0.000001)
    x.append((np.linalg.norm(x_sol_cg_noise_reg))**2)
    y.append((np.linalg.norm(dnew-np.dot(A,x_sol_cg_noise_reg)))**2)
plt.figure(figsize=(14, 8))
plt.plot(x,y,".-")
plt.title('L curve')
plt.ylabel("residual norm")
plt.xlabel("solution norm ")
plt.grid(True)   
for i in range(len(x)):
    plt.text(x[i],y[i],""+str(np.round(my_lambda[i],6)),fontsize=8)
