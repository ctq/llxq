import numpy as np
import pandas as pd
import sys


df = pd.read_excel('/Users/kelvin/Documents/hj0518.xlsx',sheet_name='一年级字库')
#print(sheet)
df = df.dropna(subset=['一年级','词性','场景','要求'])
class Record:
    def __init__(self, word, nian_ji, ci_xing, chang_jing, yao_qiu):
        self.word = word
        self.nian_ji = nian_ji
        self.ci_xing = ci_xing
        self.chang_jing = chang_jing
        self.yao_qiu = yao_qiu
    def __str__(self):
     return self.word
records = []
for index,row in df.iterrows():
    records.append(Record(row['一年级'], '一年级', row['词性'], row['场景'], row['要求']))
    #print(row['一年级'])
rows = []
columns = ['一年级名词','一年级动词']
chang_jing_group = df.groupby(['场景'])
chang_jing_list = df.场景.unique()
chang_jing_count = len(chang_jing_list)
print('场景数：' + str(chang_jing_count))

ci_xing_group = df.groupby(['词性'])
ci_xing_list = df.词性.unique()
ci_xing_count = len(ci_xing_list)
print('词性数:' + str(ci_xing_count))


df3 = pd.DataFrame(index=chang_jing_list, columns=ci_xing_list)
data = np.array([np.arange(chang_jing_count)]*ci_xing_count).T
#print(df3)


for (method,group) in chang_jing_group:
    rows.append(method)
    print('场景：' + method)
    #print(group)
    df2 = pd.DataFrame(group)
    for (method2, group2) in df2.groupby(['词性']):
        print('  词性：' + method2)
        words = ""
        word_count = 0
        for word in (group2['一年级']):
            word_count += 1
            if(word_count % 16 == 0):
                words += word + '\n'
            else:
                words += word + ' '
        df3.loc[method,method2] = words
        print('    词汇：' + words)
    print("\n")
print(df3)
df3.to_excel("/Users/kelvin/Documents/result.xlsx")
    #df = pd.DataFrame(np.random.randint(1, 2), 'myRow', )
    #print(list(zip(group['场景'],group['一年级'] ,group['词性'])))
    #df2 = pd.DataFrame(group)

#print(rows)
#df2 = pd.DataFrame({
#    "场景":records
#})
#print(df)
#for myRecord in records:
#    print(myRecord.word)
sys.exit()


for (method, group) in (df.groupby(['场景'])):
    print(method)
    currentChangJing = ''
    

    for word in group['一年级']:
        currentChangJing += word + ' '
        
        #print(":" + temp)
  #  print(currentChangJing)
    print("\n")
    

#print(df)


#outsheet = pd.read_excel('/Users/kelvin/Documents/hj0518.xlsx',sheet_name='结果')
#sheet.at['关系', '一年级'] = '一年级关系'
#print(sheet.at['关系', '一年级'])
#print(outsheet)
#outsheet.to_excel('/Users/kelvin/Documents/zk0518.xlsx')
sys.exit()

#for index, row in sheet.iterrows(): 
#    print(row['一年级'] + row['词性'] + row['场景'] + row['要求'])
    #print(output.xs(row['词性'], level=0, drop_level=False))
    #df.xs('volume', level=1, drop_level=False)
sys.exit()
#print(output[['名词','一年级']])
count = 0
#f = open("/Users/kelvin/Documents/hj.txt", "a")


for word in sheet:
    if(count < 8):
        count += 1
        
 #       f.write(word + ' ')
    else:
        count = 0
#f.write('\n')
#f.close()
sys.exit()
numbers = [0, 1, 2]
colors = ['green', 'purple']
df = pd.MultiIndex.from_product([numbers, colors],
                           names=['number', 'color'])
print(df)
sys.exit()
df=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})
columns=[('c','a'),('c','b')]

index = pd.MultiIndex.from_product([['stock1','stock2','stock3'],['prices1','volume1'],['price2','volume2']])
df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10,11,12], index)
print(df)
#print(df.xs('volume', level=1, drop_level=False))
sys.exit()

