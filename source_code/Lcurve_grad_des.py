my_lambda=np.logspace(-4,0.5,20)
x=[]  #empty list for solution  norm
y=[]   #empty list for residual norm
for i in my_lambda:
    x_sol,itr=decon_reg(A,dnew,xo,i,500)
    x.append((np.linalg.norm(x_sol))**2)
    y.append((np.linalg.norm(dnew-np.dot(A,x_sol)))**2)
plt.figure(figsize=(8, 4))
plt.title('L curve')
plt.ylabel("residual norm")
plt.xlabel("solution norm ")
plt.grid(True) 
plt.plot(x,y,".-")
for i in range(len(x)):
    plt.text(x[i],y[i],""+str(np.round(my_lambda[i],2)),fontsize=6)
directory = './results/noisy_data'
figure_path = os.path.join(directory,'L_curve.png')
plt.savefig(figure_path)
plt.show()  
