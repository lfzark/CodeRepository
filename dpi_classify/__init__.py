import hashlib
import random
def getMd5(filevalue):
    #return  md5.new(file1.read()).hexdigest()
    x = hashlib.md5()
    x.update(filevalue)
    return x.hexdigest()
    
def getHash(srcID,srcPort,destID='',destPort=''):
    return getMd5(str(srcID)+str(srcPort)+str(destID)+str(destPort))

def judge(c):
    if c=='?':
        return '0'
    else:
        return '1'
    
   
def calbitmask(pattern_list):
         bmlist=[]
         for pattern in pattern_list:
#               for i in range(len(pattern)):             
#               #pattern = pattern.replace('?','0')
              result = [ judge(s) for s in pattern]
              bmlist.append( ''.join(result))
         return bmlist
def makeEncodedSignatureDB(m,pattern):
    i = 0
    r = []
    for c in pattern:
        #s=  str(m[i][ord(c)])
        if c!='?':
            #print c
            #print m[i][ord(c)] 
            r.append(m[i][ord(c)]) 
        i+=1
        #print bin (m[i][ord(c)]) 
    return reduce(lambda x,y:x^y,r)

def check_signature(payload,bitmask_list,m):
    result=[]
    r=[]
    for bitmask in bitmask_list:
        i=0
        result=[]
        for c in bitmask:
            if c == '1':
                #print 'payload:',payload[i]
                t = m[i][ord(payload[i])]
                result.append(t)
            i+=1        
        #print result
        r.append(reduce(lambda x,y:x^y,result))
        #print r
       
    return r
pattern_list = ['goo?????i?g']

 
row = 256
maxlen=11
cols = maxlen
m = [[0] * row] *  cols
rlength = row*  cols
rlist =  random.sample(range(rlength*2),rlength)


for i in range(cols):
    for j in range(row):
        #print 'ramdon',rlist[i*cols+j]
        m[i][j]=rlist[i*cols+j]
        #print 'ramdon...',m[i][j]
print 'pattern_list:',pattern_list
print 'hash:',getHash("127.0.0.1", 80)
r = makeEncodedSignatureDB(m,'goo?????i?g')
#print r
stree={}
stree[r]=getHash("127.0.0.1", 80)

print 'encoded signature:',bin(r)
#print int('1101',2)
bitmask_list = calbitmask(pattern_list)
print 'bitmask:',bitmask_list

result_list  = check_signature('goodmorning',bitmask_list,m)

print '='*20+'RUN'+'='*20
print 'payload:','goodmornig'
for result_ in result_list:
    #print 'result_:',bin(result_)
    if stree.has_key(result_):
        print 'GOT' ,stree[result_] ,'[+1]'
print '='*20+'DONE'+'='*20
result_list  = check_signature('goodafternoon',bitmask_list,m)

print 
print 

print '='*20+'RUN'+'='*20
print 'payload:','goodafternoon'
count = 0
for result_ in result_list:
    #print 'result_:',bin(result_)
    if stree.has_key(result_):
        print 'GOT' ,stree[result_] ,'[+1]'
        count += 1
if count == 0:
    print 'Not Found'
print '='*20+'DONE'+'='*20