scores = {}
resuals_f = open ("C:\\Users\HP\Desktop\\resuals.txt")
for line in resuals_f :
    (name,score)=line.split()
    scores[score]=name
resuals_f.close()

print("The top scores were: ")
for each_score in scores.keys() :
    print("Surfer " + scores[each_score] + ' scored ' + each_score)
