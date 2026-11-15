import re,os,glob
r=r'D:\大一上学习\大一上期中复习试卷\02_高等代数一\外校真题\raw'
o=r'D:\大一上学习\大一上期中复习试卷\02_高等代数一\_work\txt2'
for f in glob.glob(os.path.join(r,'*.doc')):
    data=open(f,'rb').read()
    # UTF-16LE 中文/ASCII 连续片段
    out=[]
    for m in re.finditer(rb'(?:[\x20-\x7e]\x00|[\x00-\xff][\x4e-\x9f]){6,}', data):
        try:
            s=m.group().decode('utf-16-le','ignore')
        except Exception:
            continue
        s=s.strip()
        if len(s)>=6 and re.search(r'[\u4e00-\u9fff]', s):
            out.append(s)
    name=os.path.splitext(os.path.basename(f))[0]
    p=os.path.join(o,name+'.raw.txt')
    open(p,'w',encoding='utf-8').write('\n'.join(out))
    print(name, len(out), 'fragments ->', os.path.getsize(p))
