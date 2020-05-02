import requests
c=0
inn=[]
with open('input/input.txt', mode='r',encoding='utf8') as f:
        inn=f.readlines()
f.close()
fo=open('output/shrunked.txt','w',encoding='utf8')
for i in inn:
    r =requests.get('https://oke.io/api/?api=a9bf4fa648573dc138b33263f1890914001a0ed8&url='+i+'&format=text')
    print(c," ",i,"\n")
    fo.write(r.text +"\n")
    c+=1
fo.close()
