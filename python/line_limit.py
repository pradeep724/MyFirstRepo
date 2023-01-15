import os
import math

import pandas as pd

line=''
df = pd.read_csv('line_limit.csv')

for i,code in df.iterrows():
    line += (code['servername']) + ' ' + (code['octopusname']) + ' ' + (code['octopusdc']) + (' ' + code['octopusvendor']) + ' ' + (code['octopusenv']) + ' ' + (code['octopuspurpose']) + ' ' + (code['octopusrole']) + ' ' + (code['master'])
    line+='\n'

linx=[ln for ln in line.splitlines(0) if 'linux' in ln.lower()]
win=[ln for ln in line.splitlines(0) if 'windows' in ln.lower()]

line_limit=20
lp_l=[linx,win]
index=0
data=''

for prj in lp_l:
    prj_len = (len(prj))
    count=(math.ceil(prj_len/line_limit))
    print(count)
    index=0
    for cn in range(count):
        ind=(cn+1)
        val=ind%line_limit
        if data == '':
            data += 'Heading'
            data += '\n'
        if count != 1:
            fl = index
            ll = line_limit * ind
            data += ('\n'.join(prj[fl:ll]))
            print(data)
            data=''
            count=count-1
            index=ll
        elif count==1:
            data += '\n'.join((prj[index:]))
            print(data)
            data=''







    # exit()
    # for lsn in prj:
    #     print(len(data))
    #     if len(data) == 0:
    #         data.append('Heading')
    #     data.append(lsn)
    #     if len(data) == line_limit:
    #         print('\n'.join(data))
    #         data=[]
    #     elif lsn == prj[-1]:
    #         print('\n'.join(data))
    #         data=[]

        