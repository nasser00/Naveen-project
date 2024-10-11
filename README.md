
# Regularized Linear Inversion Techniques

this projects uses different deconvolution methods to  recover the reflectivity series from sesmic data .

Different algorithm inclues :

1)gradient 

2)conjucate gradient

3)Hybrid 𝓁1∕𝓁2 norm

4)huber norm

5)cauchy norm 

6)IRLS

7)FISTA

8)Blind deconvolution 

we tested each algorithm  on  both synthetically  generated sesimic data and real data .you  can get the code for each algorithms  in the source code directory .Each algorithm works on a single trace.


## Results
Results are store at results folder within the source_code  directory
`source_code/results`
## data
data generated is saved in data  folder within the source_code  directory 
 `source_code/data`
## Demo
To deploy this project run demo file and make sure that you are in source_code directory

https://github.com/nasser00/Naveen-project/blob/main/tutorial/demo.ipynb


## dependencies 
matplotlib      ==          3.7.1

numpy           ==          1.25.0

scipy           ==          1.10.1
