my_lambda=np.logspace(-3,-0.8,20)
# empty list for solution and residual norm
x=[]
y=[]
for i in my_lambda:
    e=0.000001    #epsilon
    x_sol_reg_new,final_iter=decon_reg_new(A,dnew,xo,i,5000)
    x.append((np.linalg.norm(np.sqrt(x_sol_reg_new**2+e**2))-e))#norm ofsolution 
    y.append((np.linalg.norm(dnew-np.dot(A,x_sol_reg_new)))**2)#norm of residual 
plt.figure(figsize=(10, 5))
plt.plot(x,y,".-")
plt.title('L curve Re(x) norm')
plt.ylabel("residual norm")
plt.xlabel("solution norm ")
plt.grid(True)   
for i in range(len(x)):
    plt.text(x[i],y[i],""+str(np.round(my_lambda[i],6)),fontsize=8)
directory = './results/noisy_data'
figure_path = os.path.join(directory,'L_curve_Re(x).png')
plt.savefig(figure_path)
plt.show()     
