import json,urllib.request,urllib.parse,os
def api(p):
    u="https://api.github.com/repos/lib-pku/libpku/contents/"+urllib.parse.quote(p)
    r=urllib.request.Request(u,headers={'User-Agent':'dsh','Accept':'application/vnd.github+json'})
    return json.load(urllib.request.urlopen(r,timeout=40))
try:
    for p in ["专业课/高等代数"]:
        d=api(p)
        for it in d:
            print(it['type'], it.get('size'), it['name'])
except Exception as e:
    print("ERR",type(e).__name__,e)
