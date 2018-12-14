from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

source = "Virat_Kohli"
destination = "Muvva_Gopaludu"

temp_src=""

src = dict()
dest = dict()

"""
firs  i will insert both source and destination into dictionaries
as keys and their links as values. After that Now each value will be stored as keys and its links are stored 
as values keeping so on...

"""

src[source]=[]
dest[destination]=[]

"""

common src and common destination are for checking duplicates in the list.

"""


common_src = []
cmn_src_i = 0
common_src.insert(cmn_src_i,source)
cmn_src_i = cmn_src_i+1
common_dest = []
cmn_dest_j = 0
common_dest.insert(cmn_dest_j,destination)
cmn_dest_j = cmn_dest_j+1

src_index = 0
dest_index = 0
src_count = 0
dest_count = 0

t=0
i=0
j=0

"""
    path src and destination are for storing the path.

"""

pathsrc_a =[]
pathsrc_h=0
pathdest_b=[]
pathdest_n=0

midpoint =""
q=""
midcount =0

"""
    I used flag to execute at a time either source or destination artcile's traversing.

"""
while(j!=1):
    
    g=""
    if(t==0):
        if(src_count==0):
            g="https://en.wikipedia.org/wiki/"+source
            print("this is strtng 0th index of src  ",g),
            #src_count=src_count+1
        
        else:
            source_len = len(src[source])           
            print("this is source_len of 0th  ",source_len),
            temp_src = src[source][src_index]
            print("this is temp_src dhonis articles ",temp_src),
            src_index = src_index+1
            g="https://en.wikipedia.org/wiki/"+temp_src
            print("this values of 1st key of source  ",g),
            src[temp_src]=[] #source artcile's value(links) inserted as key to its dictionary same case for destination also
            
            
    
    
    else:
        if(dest_count==0):
            g="https://en.wikipedia.org/wiki/"+destination
            print("thisi is strtng destination  ",g),
            #dest_count=dest_count+1
        
        
        else:
        
            dest_len=len(dest[destination])
            print("this is len of dest 0th index ",dest_len),
            temp_dest=dest[destination][dest_index]
            print("this is temp_dest US articles ",temp_dest),
            dest_index = dest_index+1
            g="https://en.wikipedia.org/wiki/"+temp_dest
            dest[temp_dest]=[]
            
    url=g
    print("final url to process is##  ",url),
    html = urlopen(url)
    bs = BeautifulSoup(html, "lxml")
    links = bs.findAll("a" , href = re.compile("/wiki/[A-Za-z]"))  
    
    """
        removing all the unnecessary links like footer,catlinks etc.  
          
    """
    
    
    
    url2=g
    print("second final url to process is##  ",url2),
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    
    test2=""
    reflink=[]
    reflink_count=0
    
    for link in soup.find_all('a',{'class':"external text"}):
        test2=str(link.get('href'))
        reflink.insert(reflink_count,test2)
        reflink_count=reflink_count+1

    
    for link in soup.find_all('a',{'class':"mw-disambig"}):
        test2=str(link.get('href'))
        reflink.insert(reflink_count,test2)
        reflink_count=reflink_count+1
    
    
    
    
    
    
    for div in soup.findAll('div', {'class': 'reflist columns references-column-width'}):
        a = div.findAll('a')

    for link in a:
        test2=str(link.get('href'))
        reflink.insert(reflink_count,test2)
        reflink_count=reflink_count+1
        
    
    for div in soup.findAll('div', {'class':'navbox'}):
        a = div.findAll('a')

    for link in a:
        test2=str(link.get('href'))
        reflink.insert(reflink_count,test2)
        reflink_count=reflink_count+1
    
    
    
    
        
    for div in soup.findAll('div', {'class': 'refbegin columns references-column-width'}):
        a = div.findAll('a')

    for link in a:
        test2=str(link.get('href'))
        reflink.insert(reflink_count,test2)
        reflink_count=reflink_count+1

        
      
      
    for div in soup.findAll('div', {'id': 'coordinates'}):
        a = div.findAll('a')
        
    for link in a:
        test2=str(link.get('href'))
        reflink.insert(reflink_count,test2)
        reflink_count=reflink_count+1  
    
    
        
        
        

    for div in soup.findAll('div', {'id': 'footer'}):
        a = div.findAll('a')
        
    for link in a:
        test2=str(link.get('href'))
        reflink.insert(reflink_count,test2)
        reflink_count=reflink_count+1
        
        

    for div in soup.findAll('div', {'id': 'catlinks'}):
       a= div.findAll('a')
        
    for link in a:
        test2=str(link.get('href'))
        reflink.insert(reflink_count,test2)
        reflink_count=reflink_count+1

    
    
    
    
  
    
    test=""
    
    """
    from the obtained link getting only article name
    
    """
    for link in links:
        #print(link.get('href'))
        test=str(link.get('href'))
        if(test not in reflink):
        
        
            c=0
            ln=len(test)
            s=""
            m=""
            #print(ln)
            for i in range(0,ln):
                if(test[-(i+1)]=='/'):
                    break
                else:
                    #print(st[-(i+1)]),
                    if(test[-(i+1)]==':' or test[-(i+1)]=='#'):
                        c=1
                        break
                    else:
                        s=s+test[-(i+1)]
            #print(s),
            l1=len(s)
            if(c!=1):
                for i in range(0,l1):
                    m=m+s[-(i+1)]
                    
                    
            
            if(c!=1):
                if(m!="Terms_of_Use" and m!="Privacy_policy" and m!="How_to_contribute" and m!="Cookie_statement" and m!="Main_Page" and m!=source and m!=destination):
                    
                    #print("this is m@@@    ",m),
                    
                    
                    if(t==0):
                        if(m not in common_src and common_dest): #checking for duplicates
                            common_src.insert(cmn_src_i,m)
                            cmn_src_i = cmn_src_i+1
                            if(src_count==0):   
                                src[source].append(m)   #adding article name to the dictionary's respective key
                            
                            else:
                                
                                #print("this is temp_src  ",temp_src),
                                #print("######src is #####"),
                                #print(src),
                                src[temp_src].append(m)
                        
                    else:
                        if(m not in common_dest and common_src):
                            common_dest.insert(cmn_dest_j,m)
                            cmn_dest_j=cmn_dest_j+1
                            if(dest_count==0):
                                dest[destination].append(m)
                                
                            else:
                                dest[temp_dest].append(m)
                            
                    
    if(src_count==0 and t==0):
        src_count=1
    if(dest_count==0 and t==1):
        dest_count = 1
    if(t==0):
        t=1
    else:
        t=0
                      
    
   # print("######dest is ######"),
   # print(dest),
    #print("#########src is ########"),
    #print(src),
    
    """
        comparing src and destinatino links to get common articles
    
    """
    
    for i in src.keys():
    #print(len(source[i])),
        k=len(src[i])
        for d in range(0,k):
            #print(source[i][j]),
            for l in dest.keys():
                h=len(dest[l])
                for m in range(0,h):
                    if(src[i][d]==dest[l][m] and midcount!=1):
                        #print("common valuesand midpoints are ",src[i][d],"keys of source and dest are ",i,l),
                        q = src[i][d]
                        midpoint = src[i][d]
                        search_src = i
                        search_dest = l
                        pathdest_b.insert(pathdest_n,search_dest)
                        pathdest_n=pathdest_n+1
                        pathsrc_a.insert(pathsrc_h,search_src)
                        pathsrc_h=pathsrc_h+1
                        search_dest = l
                        midcount=1
                        j=1
    if(midcount==1):
        j=1



m=0
src_goal = source
dest_goal = destination

"""
building path from source to common article which is nothing but midpoint
"""

while(m!=1):
        if(search_src == src_goal):
            m=1
        else:
            z=0
            for i in src.keys():
                l=len(src[i])
                for j in range(0,l):
                    if(src[i][j] == search_src and z!=1):
                        #print("search source and key in loop is ",search_src,i),
                        search_src = i
                        pathsrc_a.insert(pathsrc_h,search_src)
                        pathsrc_h=pathsrc_h+1
                        z=1



pathsrc_a.reverse()
pathsrc_a.insert(pathsrc_h,midpoint)
pathsrc_h=pathsrc_h+1

for i in range(0,len(pathsrc_a)):
    print(pathsrc_a[i],'-->')

print(),
m=0

m = 0

"""
    storing path from destination to common article..

"""
while(m!=1):
        if(search_dest == dest_goal):
            m=1
        else:
            z=0
            for i in dest.keys():
                l=len(dest[i])
                for j in range(0,l):
                    if(dest[i][j] == search_dest and z!=1):
                       # print("search destinations  and key in loop is ",search_dest,i),
                        search_dest = i
                        pathdest_b.insert(pathdest_n,search_dest)
                        pathdest_n=pathdest_n+1
                        z=1
                        


#print("tis is dest")
#pathdest_b.reverse()
for i in range(0,len(pathdest_b)):
    print('<--',pathdest_b[i])                        

print("###### Smile plzzzzz####"),
            
        
        
        
        
        
          
