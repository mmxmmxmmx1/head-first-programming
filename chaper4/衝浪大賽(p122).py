high_score = 0
resuals_f = open('C:\\Users\HP\Desktop\\resuals.txt','r')
for line in resuals_f :
    (name,score)=line.split()    
    if float(score) > high_score:
       high_score=float(score)
resuals_f.close()
print("the highest score was: ")
print(high_score)
