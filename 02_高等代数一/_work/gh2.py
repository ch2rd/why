import json,urllib.request,urllib.parse
u="https://api.github.com/repos/lib-pku/libpku/contents/"+urllib.parse.quote("专业课/高等代数")
r=urllib.request.Request(u,headers={'User-Agent':'dsh','Accept':'application/vnd.github+json'})
d=json.load(urllib.request.urlopen(r,timeout=40))
lines=[]
for it in d:
    lines.append(f"{it['type']}\t{it.get('size','')}\t{it['name']}\t{it.get('download_url','')}")
open(r'D:\大一上学习\大一上期中复习试卷\02_高等代数一\_work\ghlist.txt','w',encoding='utf-8').write("\n".join(lines))
print("ok",len(lines))
