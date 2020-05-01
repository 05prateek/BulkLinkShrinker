import requests
c=0
inn=[]
with open('input/input.txt', mode='r',encoding='utf8') as f:
        inn=f.readlines()
f.close()
fo=open('output/shrunked.txt','w',encoding='utf8')
for i in inn:
    r =requests.get('https://shrinkme.io/api?api=322fa5ea4e09eee44e178a3ea9e518d588d3d16a&url='+i+'&format=text')
    print(c," ",i,"\n")
    fo.write(r.text +"\n")
    c+=1
fo.close()
