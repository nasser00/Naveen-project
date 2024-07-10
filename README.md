
# Irterative deconvolution methods

this projects uses different deconvolution methods to  recover the reflectivity series from sesmic data .

Different algorithm inclues :

1)gradient 

2)conjucate gradient

3)Re(x) norm

4)huber norm

5)cauchy norm 

6)IRLS

we tested each algorithm  on synthetically  generated sesimic data.you  can get the code for each algorithms  in the source code directory .Each algorithm woorks on a single trace 


## Results
Results are store at results folder within the source_code  directory
'source_code/results'
## data
data generated is saved in data  folder within the source_code  directory 
source_code/data
## Demo
To deploy this project run demo file and make sure that you are in source directory

https://github.com/nasser00/Naveen-project/blob/main/tutorial/demo.ipynb


## dependencies 
matplotlib      ==          3.7.1

numpy           ==          1.25.0

scipy           ==          1.10.1