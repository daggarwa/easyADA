import appuifw,audio
import e32,sys,key_codes,string,math
import graphics
from graphics import *
from appuifw import *
from random import randint
import time
import sysinfo
global c,a1
global codes


def quicksort(list,p,r):
    if p<r:
	    q=partition(list,p,r)
	    d=appuifw.Text(u"Pivot element : "+str(list[q])+u"\nNow list is : \n"+str(list))
            appuifw.app.body=d
	    e32.ao_sleep(3)
	    quicksort(list,p,q-1)
	    quicksort(list,q+1,r)

def partition(list,p,r):
    x=list[r]
    i=p-1
    for j in range(p,r):
	    if list[j]<=x:
		    i=i+1
		    temp=list[i]
		    list[i]=list[j]
		    list[j]=temp
    temp=list[i+1]
    list[i+1]=list[r]
    list[r]=temp
    return i+1


def qsort():
    n=appuifw.query(u"Enter the no. of elements to be sorted : ","number")
    n=int(n)
    
    list=[]
    for i in range(n):
	a=appuifw.query(u"Enter element"+str(i+1)+":",'number')
	list.append(a)
	
    p=0
    r=n-1
    b=appuifw.Text(u"Initial list : \n"+str(list))
    appuifw.app.body=b
    
    e32.ao_sleep(3)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    quicksort(list,p,r)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    c=appuifw.Text(u"Sorted elements are : \n"+str(list))
    appuifw.app.body=c
    
    e32.ao_sleep(3)
    d=appuifw.Text(u"Memory usage : \n"+str(s1-s2))
    appuifw.app.body=d
    e32.ao_sleep(3)

    c=appuifw.Text(u"Time for execution : \n"+str(t2-t1-3)+u"sec")
    appuifw.app.body=c
    
    e32.ao_sleep(3)
	

about=appuifw.Text(u'''Quicksort is based on the Divide and Conquer technique.
It chooses a pivot element and places it at its correct position in such a way that the elements in the left subarray of pivot are all less than it and the elements in the right subarray of pivot are all greater than it.
Since the subarrays are sorted in place there is no need to combine them as in mergesort.
Complexity of quicksort in best as well as average case in O(nlgn) and in worst case is O(n^2)''')

def handle_tabq(index):
       
    if(index==0):
        app.body=about        
        e32.ao_sleep(30)
    if(index==1):
        qsort()
    
def rand_quicksort(list,p,r):
    if p<r:
        q=rand_partition(list,p,r)
        d=appuifw.Text(u"Pivot element : "+str(list[q])+u"\nNow list is: \n"+str(list))
	appuifw.app.body=d
	e32.ao_sleep(3)
        rand_quicksort(list,p,q-1)
        rand_quicksort(list,q+1,r)
    

def rand_partition(list,p,r):
    i=randint(p,r)
    temp=list[r]
    list[r]=list[i]
    list[i]=temp
    return partition(list,p,r)

def rqsort():
    n=appuifw.query(u"Enter the no. of elements to be sorted : ","number")
    n=int(n)
    list=[]
    for i in range(n):
        a=appuifw.query(u"Enter element "+str(i+1)+" : ",'number')
        list.append(a)
    p=0
    r=n-1
    b=appuifw.Text(u"Initial list : \n"+str(list))
    appuifw.app.body=b
    e32.ao_sleep(3)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    rand_quicksort(list,p,r)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    c=appuifw.Text(u"sorted elements are : \n"+str(list))
    appuifw.app.body=c
    e32.ao_sleep(3)
    c=appuifw.Text(u"Space usage is:"+str(s1-s2))
    appuifw.app.body=c
    e32.ao_sleep(3)
    c=appuifw.Text(u"Time for execution : \n"+str(t2-t1-3)+u"sec")
    appuifw.app.body=c
    e32.ao_sleep(3)

about1=appuifw.Text(u'''Randomized quicksort is based on the Divide and Conquer technique.
It chooses a pivot element randomly, places in its correct position and then proceeds in the same way as quicksort.
It's complexity is O(nlgn)in any case.''')
def handle_tabrq(index):
       
    if(index==0):
        app.body=about1
        e32.a0_sleep(30)
    if(index==1):
        rqsort()

def mergesort(list,low,high):
    if low<high:
        
        mid=(low+high)//2
        mergesort(list,low,mid)
        mergesort(list,mid+1,high)
        merge(list,low,mid,high)
def merge(list,low,mid,high):
    i=low
    j=mid+1
    b=[]
    while (i<=mid)and(j<=high):
        if list[i]<=list[j]:
            b.append(list[i])
            i+=1
        else:
            b.append(list[j])
            j=j+1
        
    while i<=mid:
        b.append(list[i])
        i+=1
    while j<=high:
        b.append(list[j])
        j+=1
    for k in range(0,high-low+1):
        list[low+k]=b[k]
    
    
def msort():
    n=appuifw.query(u"Enter the no. of elements to be sorted : ","number")
    n=int(n)
    list=[]
    for i in range(n):
        a=appuifw.query(u"Enter element "+str(i+1)+" : ",'number')
        list.append(a)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    low=0
    high=n-1
    b=appuifw.Text(u"Initial list : \n"+str(list))
    appuifw.app.body=b
    e32.ao_sleep(3)
    mergesort(list,low,high)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    c=appuifw.Text(u"Sorted list is : \n"+str(list))
    appuifw.app.body=c
    e32.ao_sleep(3)
    c=appuifw.Text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=c
    e32.ao_sleep(3)
    c=appuifw.Text(u"Time for execution : \n"+str(t2-t1-3)+u"sec")
    appuifw.app.body=c
    e32.ao_sleep(3)

about2=appuifw.Text(u'''Merge Sort is based on the Divide and Conquer technique.
It divides the list recursively and then combines the sublists to produce a sorted list.
It's complexity is O(nlgn) in any case.''')

def handle_tabms(index):
       
    if(index==0):
        app.body=about2
        e32.ao_sleep(30)
    if(index==1):
        msort()




def l_c_s():
    l1=[]
    l2=[]
    l3=[]
    m=appuifw.query(u"Enter Length of sequence 1 : ","number")

    for i in range(1,m+1,1):
            v=appuifw.query(u"Element "+str(i)+u"of seq 1 : ","text")
            v=str(v)
            l1.append(v)

    n=appuifw.query(u"Enter Length of sequence 2 : ","number")
    for i in range(1,n+1,1):
            v=appuifw.query(u"Element "+str(i)+u"of seq 2 : ","text")
            v=str(v)
            l2.append(v)
    a=appuifw.Text(u"Sequence 1 is:"+str(l1)+u"\n\nSequence 2 is:"+str(l2))
    app.body=a
    e32.ao_sleep(4)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()

    c=[[0] * (n+1) for i in range(m+1)]
    b=[[0] * (n+1) for i in range(m+1)]
    def lcs(l1,l2):
            for i in range(1,m+1,1):
                    c[i][0]=0
            for j in range(0,n+1,1):
                    c[0][j]=0
            for i in range(1,m+1,1):
                    for j in range(1,n+1,1):
                            if l1[i-1]==l2[j-1]:
                                    c[i][j]=c[i-1][j-1]+1
                                    b[i][j]='#'
                            elif c[i-1][j]>=c[i][j-1]:
                                    c[i][j]=c[i-1][j]	
                                    b[i][j]='$'
                            else:
                                    c[i][j]=c[i][j-1]
                                    b[i][j]='@'
            return b,c
    b,c=lcs(l1,l2)
   
    def printlcs(b,l1,i,j):
            if i==0 or j==0:
                    return
            if b[i][j]=='#':
                    printlcs(b,l1,i-1,j-1)
                    w=str(l1[i-1])
                    l3.append(w)
                    
            elif b[i][j]=='$':
                    printlcs(b,l1,i-1,j)
            else:
                    printlcs(b,l1,i,j-1)

	
    				
    x=printlcs(b,l1,m,n)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    
    a=appuifw.Text(u"Lcs is: "+str(l3))
    app.body=a
    e32.ao_sleep(4)
    c=appuifw.Text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=c
    e32.ao_sleep(3)

    c=appuifw.Text(u"Time for execution : \n"+str(t2-t1)+u"sec")
    appuifw.app.body=c
    e32.ao_sleep(3)


about3=appuifw.Text(u'''The longest common subsequence (LCS) problem is to find the longest subsequence common to all sequences in a set of sequences (often just two).
It can be solved using dynamic programming.
For the case of two sequences of n and m elements, the running time of the dynamic programming approach is O(n × m)''')


def handle_tablcs(index):
       
    if(index==0):
        app.body=about3
        e32.ao_sleep(30)
    if(index==1):
        l_c_s()
        
def naiveu():
    t=[]
    p=[]
    
    n=appuifw.query(u"Enter length of text : ","number")
        
    for i in range(n):
        v=appuifw.query(u"Element : "+str(i+1),"text")
        v=str(v)
        t.append(v)
       
    m=appuifw.query(u"Enter length of pattern : ","number")
    for i in range(m):
        v=appuifw.query(u"Element : "+str(i+1),"text")
        v=str(v)
        p.append(v)
    app.body=appuifw.Text(u"Entered text is:"+str(t)+u"\nEntered pattern is:"+str(p))
    e32.ao_sleep(3)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    

    def naive(t,p,m,n):
        tag=0
        for s in range(0,n-m+1,1):
            for i in range(1,m+1,1):
                flag=1
                if p[i-1]!=t[s+i-1]:
                    flag=0
                    break
            if flag==1:
                                   
                b=appuifw.Text(u"Pattern  occurs at shift:"+str(s))
                appuifw.app.body=b
                e32.ao_sleep(3)
                tag=1
        if tag==0:
            c=appuifw.Text(u"Pattern not found !!!")
            appuifw.app.body=c
            

    naive(t,p,m,n)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    c=appuifw.Text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=c
    e32.ao_sleep(3)

    
    c=appuifw.Text(u"Time for execution is:\n"+str(t2-t1-3)+u"sec")
    appuifw.app.body=c
    e32.ao_sleep(3)

def naives():
    
    def handle_redraw(rect):
        ca.blit(c)
    ca=appuifw.Canvas(event_callback=None,redraw_callback=handle_redraw)
    appuifw.app.body=ca
    c=Image.new((320,240))
    c.clear(0xffff00)
    c.text((100,60),u"a")
    c.text((110,60),u"b")
    c.text((120,60),u"c")
    c.text((130,60),u"d")
    c.text((140,60),u"e")
    c.text((150,60),u"f")

    c.text((100,80),u"d")
    c.text((110,80),u"e")
    
    for i in range(0,40,10):
          
        c.text((100+i,80),u"d",0xff0000)
        ca.blit(c)
        c.text((110+i,80),u"e",0xff0000)
        ca.blit(c)
        c.text((100,110),u"Shift="+str(i/10),0xf00fff)
        ca.blit(c)
        
        e32.ao_sleep(1)
        c.text((100,110),u"Shift="+str(i/10),0xffff00)
        ca.blit(c)
                
        c.text((100+i,80),u"d",0xffff00)
        ca.blit(c)
              
        
        c.text((110+i,80),u"e",0xffff00)
        ca.blit(c)
        
    e32.ao_sleep(1)
    c.text((130,80),u"d",0xfefefe)
    ca.blit(c)
    c.text((130,80),u"d",0x000000)
    ca.blit(c)
    c.text((140,80),u"e",0xfefefe)
    ca.blit(c)
    c.text((140,80),u"e",0x000000)
    ca.blit(c)
    c.text((100,130),u"Pattern found at shift=3",0xff0000)
    e32.ao_sleep(1)
    i1=graphics.screenshot()
    i1.save("e:\\5.jpg")
    e32.ao_sleep(20)
    
about5=appuifw.Text(u'''Naive string matching finds the occurrence of a given pattern by shifting the pattern against the text.
It's preprocessing time is zero.
It's matching time is O((n-m+1)m) where m=length of pattern and n=length of text.''')
def handle_tabn(index):
       
    if(index==0):
        appuifw.app.body=about5
        e32.ao_sleep(30)
    if(index==1):
        naives()
        
    if(index==2):
        naiveu()
 
  				
def rabinkarp():
    t=[]
    p=[]
    p.append(0)
    t.append(0)
    n=appuifw.query(u"Enter length of text :","number")
    for i in range(n):
            v=appuifw.query(u"Enter element of text "+str(i+1),"number")
            t.append(v)
    m=appuifw.query(u"Enter length of pattern :",u"number")
    for i in range(m):
            v=appuifw.query(u"Enter element of pattern"+str(i+1),"number")
            p.append(v)
    q=appuifw.query(u"Enter modulus ","number")
    d=appuifw.query(u"Enter value of radix","number")
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    def rabin(t,p,d,q):
            h=(d**(m-1))%(q)
            pp=0
            tt=[]
            tag=0
            f=0
            for i in range(1,m+1,1):
                    pp=(d*pp+p[i])%(q)
                    f=(d*f+t[i])%(q)
            tt.append(f)
            for s in range(0,n-m+1,1):
                    flag=0

                    if pp==tt[s]:			
			
                            for i in range(1,m+1,1):
                                    if p[i]!=t[s+i]:
                                            flag=1
                                            break
                            if flag==0:
                                    a=appuifw.Text(u"Pattern found at shift "+str(s))
				
                                    appuifw.app.body=a
                                    tag=1
                                    e32.ao_sleep(3)

                    if s<n-m:
                            tt.append((d*(tt[s]-t[s+1]*h)+t[s+m+1])%(q))
            if tag==0:
                    a=appuifw.Text(u"Pattern not found")
                    appuifw.app.body=a
                    e32.ao_sleep(3)
                    
                    
    rabin(t,p,d,q)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    b=appuifw.Text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=b
    e32.ao_sleep(4)
    b=appuifw.Text(u"Time for execution : "+str(t2-t1-3)+u"sec.")
    appuifw.app.body=b
    e32.ao_sleep(4)

about7=appuifw.Text(u'''In this algorithm each character is a decimal digit and we compute values using any modulo(generally prime no.).
We look for windows whose computed value using any modulo equals the value of pattern using that modulo.
Rabin Karp uses O(m) preprocessing time and it's worst case running time is O((n-m+1)m).''')


def handle_tabrk(index):
       
    if(index==0):
        appuifw.app.body=about7
        e32.ao_sleep(30)
    if(index==1):
        rabinkarp()


def m_c_m():
    import sys
    L=[]
    l=[]
    
    n=appuifw.query(u"Enter no. of matrices to be multiplied : ","number")
    n=int(n)
    for i in range(n+1):
      v=appuifw.query(u"Enter element"+str(i+1) +u"of dimension vector : ","number")
      L.append(v)

    a=appuifw.Text(u"The dimension vector is "+str(L))
    appuifw.app.body=a
    e32.ao_sleep(3)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()

    m = [[0] * (n+1) for i in range(n+1)]
    s = [[0] * (n+1) for i in range(n+1)]
    q=0
    def mcm():
            for i in range(1,n+1,1):
                    m[i][i]=0
            for l in range (2,n+1,1):
                    for i in range(1,n-l+1+1,1):	
                            j=i+l-1
                            m[i][j]=sys.maxint
                            for k in range(i,j-1+1,1):
                                    q=m[i][k]+m[k+1][j]+L[i-1]*L[k]*L[j]
                                    if q<m[i][j]:
                                            m[i][j]=q
                                            s[i][j]=k

            return m,s 
    m,s=mcm()
   
    def pop(s,i,j):
            if i==j:
                    x="A"+str(i)
                    l.append(x)
            else:	
		
                    y="("
                    l.append(y)
                    pop(s,i,s[i][j])
                    pop(s,s[i][j]+1,j)
                    z=")"
                    l.append(z)
                    
                    
    
    pop(s,1,n)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    appuifw.app.body=appuifw.Text(u"paranthesization:"+str(l))
    e32.ao_sleep(5)
    c=appuifw.Text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=c
    e32.ao_sleep(3)
    c=appuifw.Text(u"Time for execution : \n"+str(t2-t1)+u"sec")
    appuifw.app.body=c
    e32.ao_sleep(3)


about4=appuifw.Text(u'''Matrix chain multiplication is an optimization problem that can be solved using dynamic programming.
Given a sequence of matrices, we want to find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.
It requires O(n^3) time for computation.''')

def handle_tabmcm(index):
       
    if(index==0):
        app.body=about4
        e32.ao_sleep(30)
    if(index==1):
        m_c_m()
                


def knapsack():
    wt=[]
    val=[]
    profit=[]
    sel=[]
    num=[]
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    
    sz=appuifw.query(u"Enter size of bag : ","number")
    n=appuifw.query(u"Enter no. of items : ","number")
    sz=int(sz)
    n=int(n)

    for i in range(n):
        
        a,b=appuifw.multi_query(u"Enter weight of : "u"item"+str(i+1),u"Enter profit of: "+u"item"+str(i+1))
        a=float(a)
        wt.append(a)
        b=float(b)
        profit.append(b)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    
    for i in range(n):
        c=profit[i]/wt[i]
        c=float(c)
        val.append(c)
        num.append(i+1)

    for i in range(n-1):
        for j in range(i+1,n):
            if val[i]<val[j]:
                temp=wt[i]
                wt[i]=wt[j]
                wt[j]=temp
              
                temp=profit[i]
                profit[i]=profit[j]
                profit[j]=temp
           
                temp=num[i]
                num[i]=num[j]
                num[j]=temp

                
                temp=val[i]
                val[i]=val[j]
                val[j]=temp


    i=0
    while sz>=0:
        sz=sz-wt[i]
        sel.append(1)
        i+=1

    
    if sz<0:
        i-=1
        sz=sz+wt[i]
        sel[i]=sz/wt[i]
        x=appuifw.Text(u"sel"+str(sel))
        appuifw.app.body=x
        e32.ao_sleep(4)

    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    y=appuifw.Text(u"Knapsack contains the following items: ")
    appuifw.app.body=y
    e32.ao_sleep(4)
    for j in range(i+1):
        z1=(str(num[j]))
        z2=(str(wt[j]))
        z3=(str(profit[j]))
        z4=(str(sel[j]))
         
        l1.append(z1)
        l2.append(z2)
        l3.append(z3)
        l4.append(z4)

    
    a=appuifw.Text(u"Item number"+str(l1)+u"\nweight"+str(l2)+u"\nprofit"+str(l3)+u"\nselected"+str(l4)+u" units\n")
    appuifw.app.body=a
    e32.ao_sleep(6)
    b=appuifw.Text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=b
    e32.ao_sleep(3)

    b=appuifw.Text(u"Time for execution :\n"+str(t2-t1-4)+u" sec.")
    appuifw.app.body=b
    e32.ao_sleep(3)

about6=appuifw.Text(u'''Fractional knapsack is based on Greedy Strategy.
The items are selected for putting in the knap such that the profit is maximised with the constraint that the total weight of all the items input is less than or equal to the size of the bag.
It's complexity is O(nlgn).''')



def handle_tabknap(index):
       
    if(index==0):
        app.body=about6
        e32.ao_sleep(30)

    if(index==1):
        knapsack()
def huff():
    
    codes={}
    l1=[]
    l2=[]

    def frequency (str1) :
        freqs = {}
        for ch in str1 :
            freqs[ch] = freqs.get(ch,0) + 1
        return freqs

    def sortFreq (freqs) :
        letters = freqs.keys()
        tuples = []
        for let in letters :
            tuples.append((freqs[let],let))
        tuples.sort()
        return tuples

    def buildTree(tuples) :
        while len(tuples) > 1 :
            leastTwo = tuple(tuples[0:2])                
            theRest  = tuples[2:]                        
            combFreq = leastTwo[0][0] + leastTwo[1][0]   
            tuples   = theRest + [(combFreq,leastTwo)]   
            tuples.sort()                                
        return tuples[0]           

    def trimTree (tree) :
        p = tree[1]                                   
        if type(p) == type("") : return p             
        else : return (trimTree(p[0]), trimTree(p[1]))

    def assignCodes (node, pat='') :
        #global codes
        if type(node) == type("") :
            codes[node] = pat
        else  :                               
            assignCodes(node[0], pat+"0")
            assignCodes(node[1], pat+"1")    

    def encode (str1) :
        #global codes
        output = ""
        for ch in str1 : output += codes[ch]
        return output


    def main () :
        debug = None
        str1 =appuifw.query(u"Enter a string","text")
        str1=str(str1)
        freqs = frequency(str1)
    
        tuples = sortFreq(freqs)

        tree = buildTree(tuples)
    

        tree = trimTree(tree)
    

        assignCodes(tree)
        small = encode(str1)
        for i in freqs.keys():
            a1= str((i))
            a2=str((codes[i]))

            l1.append(a1)
            l2.append(a2)
        a=appuifw.Text(u"Code for letter"+str(l1)+u"\nis\n"+str(l2))
        appuifw.app.body=a
        e32.ao_sleep(6)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    main()
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    a=appuifw.text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=a
    e32.ao_sleep(3)
    a=appuifw.text(u"Time for execution is:"+str(t2-t1)+u"sec")
    appuifw.app.body=a
    e32.ao_sleep(3)
about10=appuifw.Text(u'''It is a Data Compression technique based on Greedy strategy.
It is a variable length prefix code which assigns smaller code to a letter having more frequency and vice verse.
It's complexity is O(nlogn) for a string of length n''')
        
def handle_tabhuff(index):
       
    if(index==0):
        app.body=about10
        e32.ao_sleep(30)
    if(index==1):
        huff()

def act():
    f=[]
    s=[]
    index=[]
    n=appuifw.query(u"Enter no of activities","number")
    for i in range(n):
        u,v=appuifw.multi_query(u"Enter start time of activity"+str(i+1),u"Enter finish time of activity"+str(i+1))
        u=int(u)
        v=int(v)
        s.append(u)
        f.append(v)
        index.append(i+1)
    a=appuifw.Text(u"Activities:"+str(index)+"\n"+u"Start times:"+str(s)+"\n"+u"finish times:"+str(f))
    appuifw.app.body=a
    e32.ao_sleep(3)
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    for i in range(n-1):
        for j in range(i+1,n,1):
            if f[i]>f[j] :
                temp=f[i]
                f[i]=f[j]
                f[j]=temp
            
                temp=s[i]
                s[i]=s[j]
                s[j]=temp

                temp=index[i]
                index[i]=index[j]
                index[j]=temp

    a=appuifw.Text(u"After Sorting:\n"+u"Activities:"+str(index)+"\n"+u"Start times:"+str(s)+"\n"+u"finish times:"+str(f))
    appuifw.app.body=a
    e32.ao_sleep(3)
    def act_sel(f,s):
        a=[]
        a.append(index[0])
        i=0
        for m in range(1,n,1):
            if s[m]>=f[i]:
                p=index[m]
                a.append(p)
                i=m
        return a

    b=act_sel(f,s)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    a=appuifw.Text(u"Maximum size subset of mutually compatible activies are\n"+str(b))
    appuifw.app.body=a
    e32.ao_sleep(2)
    b=appuifw.text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=b
    e32.ao_sleep(3)
    b=appuifw.text(u"Time for execution is:"+str(t2-t1-3)+u"sec")
    appuifw.app.body=b
    e32.ao_sleep(3)        
about11=appuifw.Text(u'''An activity-selection is the problem of scheduling a resource among several competing activity.
Given a set S of n activities with and start time, Si and fi, finish time of an ith activity. Find the maximum size set of mutually compatible activities.
Compatible Activities:Activities i and j are compatible if the half-open internal [si, fi) and [sj, fj) do not overlap, that is, i and j are compatible if si ≥ fj  and sj ≥ fi
It's complexity is O(nlogn) for sorting and theta(n)for n activities ''')
        
def handle_tabact(index):
       
    if(index==0):
        app.body=about11
        e32.ao_sleep(30)
    if(index==1):
        act()


def knuth():
        
        t=[]
        p=[]
        t.append(0)
        p.append(0)

        n=appuifw.query(u"Enter length of text :","number")

        for i in range(1,n+1,1):
                v=appuifw.query(u"Enter element of text "+str(i),"text")
                v=str(v)
                t.append(v)
        m=appuifw.query(u"Enter length of pattern :",u"number")
        for i in range(1,m+1,1):
                v=appuifw.query(u"Enter element of pattern"+str(i),"text")
                v=str(v)
                p.append(v)
        a=appuifw.Text(u"The text is "+str(t[1:])+u"\nThe pattern is "+str(p[1:]))
        appuifw.app.body=a
        e32.ao_sleep(4)
    
        pi=[]
        for i in range(m+1):
                pi.append(0)
        def prefix(t,p):
	
                k=0
                for q in range(2,m+1,1):
                        while k>0 and p[k+1]!=p[q]:
                                        k=pi[k]
                        if p[k+1]==p[q]:
                                        k=k+1
                        pi[q]=k
                a=appuifw.Text(u"The function pi is "+str(pi))
                appuifw.app.body=a
                e32.ao_sleep(3)
	
                tag=0
	
                q=0
	
                for i in range(1,n+1,1):

                        while q>0 and p[q+1]!=t[i]:
                                q=pi[q]
                        if p[q+1]==t[i]:
                                q=q+1
                        if q==m:
                                a=appuifw.Text(u"Pattern found at shift "+str(i-m))
                                appuifw.app.body=a
                                e32.ao_sleep(3)
                                tag=1
                                q=pi[q]	
                if tag==0:                                        
                        a=appuifw.Text(u"Pattern not found")
                        appuifw.app.body=a
                        e32.ao_sleep(3)
								

        t1=time.clock()
        t1=int(t1)
        s1=sysinfo.free_ram()
        prefix(t,p)
	t2=time.clock()
	t2=float(t2)
	s2=sysinfo.free_ram()
	a=appuifw.Text(u"Space usage:"+str(s1-s2))
        appuifw.app.body=a
        e32.ao_sleep(3)
	a=appuifw.Text(u"Time for execution is:"+str(t2-t1-3)+u"sec")
        appuifw.app.body=a
        e32.ao_sleep(3)

about9=appuifw.Text(u'''The prefix function pi for a pattern encapsulates knowledge about how a pattern matches against shifts of itself.
This information can be used to avoid testing useless shifts.
It's preprocessing time is O(m) and matching time is O(n).''')

def handle_tabkmp(index):
       
    if(index==0):
        app.body=about9
        e32.ao_sleep(30)
    if(index==1):
        knuth()

        
def dfss():
        
    c=appuifw.Canvas()
    app.body=c
    c.clear(0xbbbbbb)
    c.text((10,150),u"CONSIDER A SAMPLE GRAPH",0x008000,font=(u'b1c65d',23,appuifw.STYLE_BOLD))

    c.text((10,50),u"               A",0x008000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((14,63),u"           /     \\",0x004000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((14,83),u"          B-D-C",0x008000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((20,101),u"         \  |  /",0x004000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((27,120),u"           E",0x008000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))

    
    e32.ao_sleep(4)

        
    d=appuifw.Canvas()
    app.body=d
    d.clear(0xffff00)
    d.text((140,60),u"A",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    for i in range(0,62,1):
        d.point((140-i,60+i),0x000000,width=4)
        e32.ao_sleep(0.020)
    d.text((65,132),u"B",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    d.text((142,130),u"D",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    for i in range(0,60,1):
        
        d.point((80+i,121),0x000000,width=4)
        e32.ao_sleep(0.020)

    d.text((142,212),u"E",font=(u'b1c65d',20,appuifw.STYLE_BOLD))

    for i in range(0,60,1):
        
        d.point((145,132+i),0x000000,width=4)
        e32.ao_sleep(0.020)
    d.text((220,130),u"C",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    for i in range(0,70,1):
        d.point((145+i,192-i),0x000000,width=4)
        e32.ao_sleep(0.020)
    e32.ao_sleep(20)

def iterative_dfs(d,start,path=[]):
     q=[start]
     while q:
         v=q.pop(0)
         if v not in path:
             path=path+[v]
             q=d[v]+q
             
     return path


def dfsu():
    
    dn={}
    l=[]
    n=[]
    ln=[]
    d1={}
    d2={}
    def graph():
    
        v=appuifw.query(u"Enter no of vertices:","number")
        r=6.28/v
    
        for i in range(v):
            v1=appuifw.query(u"Enter vertices:","number")
            l.append(v1)
        
        for i in range(v):
            a=appuifw.query(u"Enter no of neighbours of vertice"+str(i+1)+":","number")
            a=int(a)
            n.append(a)
        for i in range(v):
            ln.append(['0']*n[i])
        for i in range(v):
            for j in range(n[i]):
                b=appuifw.query(u"Enter neighbours of vertice"+str(i+1)+":","number")
                ln[i][j]=b
        for i in range(v):
            dn[l[i]]=(ln[i])
         
        def handle_redraw(a1):
            a1.blit(a)

        
        a1=appuifw.Canvas(event_callback=None,redraw_callback=handle_redraw)    
        appuifw.app.body=a1
        a=Image.new((176,208))
    
    
        def cir(x=80,y=70,radius=50, outline=0xfefefe,fill=0xfefefe ,width=1):
            a.ellipse((x-radius, y-radius, x+radius, y+radius), outline,fill,width)
            a1.blit(a)
            e32.ao_sleep(2)
        cir()
        for i in range(v):
            a.point((80-50*math.sin(r),70+50*math.cos(r)),0x000000,width=4)
            a1.blit(a)
            d1[l[i]]=80-50*math.sin(r)
            d2[l[i]]=70+50*math.cos(r)
            a.text((d1[l[i]]-15,d2[l[i]]),u""+str(l[i]))
            a1.blit(a)
            e32.ao_sleep(3)
            r=r+6.28/v
        
        j=0
        for k in l:
            for i in range(n[j]):
                 a.line((d1[k],d2[k],d1[dn[k][i]],d2[dn[k][i]]),0xff0000)
                 a1.blit(a)
                 e32.ao_sleep(2)
            j=j+1
        
        c=appuifw.query(u"Enter starting vertex:","number")
        t1=time.clock()
        l1=iterative_dfs(dn,c)
        t2=time.clock()
        a.text((30,10),u"DFS of graph is:"+str(l1),0x000000)
        a1.blit(a)
        
        for i in range (v):
            a.text((d1[l1[i]]-15,d2[l1[i]]),u""+str(l1[i]),0xffff00)
            a1.blit(a)
            e32.ao_sleep(2)
            a.text((d1[l1[i]]-15,d2[l1[i]]),u""+str(l1[i]),0x00000)
            a1.blit(a)
            e32.ao_sleep(1)
        
        e32.ao_sleep(2)    
        b=appuifw.text(u"Time for execution is:"+str(t2-t1)+u"sec")
        appuifw.app.body=b
   
           
    graph()
    e32.ao_sleep(5)
    

    

about8=appuifw.Text(u'''Depth-first search (DFS) is an algorithm  for traversing or searching a tree, tree structure, or graph.
One starts at the root (selecting some node as the root in the graph ) and explores as far as possible along each branch before backtracking.
Complexity of DFS is O(v+e)where v is no of vertices and e edges.''')

def handle_tabdfs(index):
       
    if(index==0):
        app.body=about8
        e32.ao_sleep(30)
    if(index==1):
        dfss()
    if(index==2):
        dfsu()


def bfss():
    c=appuifw.Canvas()
    app.body=c
    c.clear(0xbbbbbb)
    c.text((10,150),u"CONSIDER A SAMPLE GRAPH",0x008000,font=(u'b1c65d',23,appuifw.STYLE_BOLD))

    c.text((10,50),u"               A",0x008000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((14,63),u"           /     \\",0x004000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((14,83),u"          B-D-C",0x008000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((20,101),u"         \  |  /",0x004000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((27,120),u"           E",0x008000,font=(u'b1c65d',20,appuifw.STYLE_BOLD))

    e32.ao_sleep(4)
    c=appuifw.Canvas()
    app.body=c
    c.clear(0xffff00)
    c.text((140,30),u"A",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    for i in range(0,62,1):
        c.point((144-i,30+i),0x000000,width=4)
        e32.ao_sleep(0.020)
    c.text((70,125),u"B",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    c.text((214,125),u"C",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    for i in range(0,64,1):
        c.point((144+i,30+i),0x000000,width=4)
        e32.ao_sleep(0.020)
    c.text((142,125),u"D",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    for i in range(0,53,1):
        c.point((208-i,124),0x000000,width=4)
        e32.ao_sleep(0.020)
    c.text((142,195),u"E",font=(u'b1c65d',20,appuifw.STYLE_BOLD))
    for i in range(0,60,1):
        c.point((208-i,124+i),0x000000,width=4)
        e32.ao_sleep(0.020)    
    
def iterative_bfs(graph, start, path=[]):
    q=[start]
    while q:
        v=q.pop(0)
        if not v in path:
            path=path+[v]
            q=q+graph[v]
    return path
    
def bfsu():
    dn={}
    l=[]
    n=[]
    ln=[]
    d1={}
    d2={}
    def graph():
    
        v=appuifw.query(u"Enter no of vertices:","number")
        r=6.28/v
    
        for i in range(v):
            v1=appuifw.query(u"Enter vertices:","number")
            l.append(v1)
        
        for i in range(v):
            a=appuifw.query(u"Enter no of neighbours of vertex"+str(i+1)+":","number")
            a=int(a)
            n.append(a)
        for i in range(v):
            ln.append(['0']*n[i])
        for i in range(v):
            for j in range(n[i]):
                b=appuifw.query(u"Enter neighbours of vertex"+str(i+1)+":","number")
                ln[i][j]=b
        for i in range(v):
            dn[l[i]]=(ln[i])
         
        def handle_redraw(a1):
            a1.blit(a)

        
        a1=appuifw.Canvas(event_callback=None,redraw_callback=handle_redraw)    
        appuifw.app.body=a1
        a=Image.new((176,208))
    
    
        def cir(x=80,y=70,radius=50, outline=0xfefefe,fill=0xfefefe ,width=1):
            a.ellipse((x-radius, y-radius, x+radius, y+radius), outline,fill,width)
            a1.blit(a)
            e32.ao_sleep(2)
        cir()
        for i in range(v):
            a.point((80-50*math.sin(r),70+50*math.cos(r)),0x000000,width=4)
            a1.blit(a)
            d1[l[i]]=80-50*math.sin(r)
            d2[l[i]]=70+50*math.cos(r)
            a.text((d1[l[i]]-15,d2[l[i]]),u""+str(l[i]))
            a1.blit(a)
            e32.ao_sleep(3)
            r=r+6.28/v
        
        j=0
        for k in l:
            for i in range(n[j]):
                 a.line((d1[k],d2[k],d1[dn[k][i]],d2[dn[k][i]]),0xff0000)
                 a1.blit(a)
                 e32.ao_sleep(2)
            j=j+1
        c=appuifw.query(u"Enter starting vertex:","number")
        l1=iterative_bfs(dn,c)
        a.text((30,20),u"BFS of graph is:"+str(l1),0x000000)
        a1.blit(a)
        
        for i in range (v):
            a.text((d1[l1[i]]-15,d2[l1[i]]),u""+str(l1[i]),0xff00ff)
            a1.blit(a)
            e32.ao_sleep(1)
            a.text((d1[l1[i]]-15,d2[l1[i]]),u""+str(l1[i]),0x00000)
            a1.blit(a)
            e32.ao_sleep(1)
            
       
    graph()
    e32.ao_sleep(5)

about13=appuifw.Text(u'''In graph theory, breadth-first search (BFS) is a graph search algorithm that begins at the root node and explores all the neighboring nodes.
Then for each of those nearest nodes, it explores their unexplored neighbor nodes, and so on, until it finds the goal.
It's complexity is O(v+e)''')
def handle_tabbfs(index):
       
    if(index==0):
        app.body=about13
        e32.ao_sleep(30)
    if(index==1):
        bfss()
    if(index==2):
        bfsu()

def warshall():
    l=[]
    b=[]
    a=[]
    n=appuifw.query(u"Enter no of vertices:","number")

    for i in range(n):
        l.append([0]*n)
        a.append([0]*n)
        b.append([0]*n)
    for i in range(n):
        for j in range(n):
            if i==j:
                l[i][j]=0
            
            else:
                ch=appuifw.query(u"Is there an edge between vertex "+str(i+1)+u"and "+str(j+1)+u"\nEnter y or n:","text")
                ch=str(ch)
                if ch=='y':
                    x=appuifw.query(u"Enter weight ","number")
                    l[i][j]=x
                else:
                    l[i][j]=sys.maxint
                
    a=copy.deepcopy(l)
    tag=0
    def wars(a,tag):
        tag=tag+1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    b1=a[i][j]
                    b2=a[i][k]+a[k][j]
                    if b1<b2:
                        min=b1
                    else :
                        min=b2
                        b[i][j]=min

        if tag!=n+1:
            wars(b,tag)
        else:
            s=appuifw.Text(u"The shortest path matrix is:\n"+str(b))
            appuifw.app.body=s
            e32.ao_sleep(3)
      
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    wars(a,tag)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    a=appuifw.text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=a
    e32.ao_sleep(3)
    a=appuifw.text(u"Time for execution is:"+str(t2-t1)+u"sec")
    appuifw.app.body=a
    e32.ao_sleep(3)

about12=appuifw.Text(u'''Floyd-Warshall is a graph analysis algorithm  for finding shortest paths in a weighted graph (with positive or negative edge weights).
A single execution of the algorithm will find the lengths (summed weights) of the shortest paths between all pairs of vertices though it does not return details of the paths themselves.
The algorithm is an example of dynamic programming.It's complexity is O(v^3)''')

def handle_tabwars(index):
       
    if(index==0):
        app.body=about12
        e32.ao_sleep(30)
    if(index==1):
        warshall()


  
def dijkstra():
    
    v=[]
    n=[]
    l=[]
    g={}

   
    x=appuifw.query(u"Enter no of vertices:","number")
    for i in range(int(x)):
        y=appuifw.query(u"Enter vertice"+str(i+1)+":","number")
        v.append(y)
    z=appuifw.Text(u"Enter no of neighbours of each vertex:")
    appuifw.app.body=z
    for i in range(int(x)):
        a=appuifw.query(u"Enter no of neighbours of vertex"+str(i+1)+":","number")
        a=int(a)
        n.append(a)
    for i in range(int(x)):
        l.append([('0','0')]*n[i])

    for i in range(int(x)):
        for j in range(0,n[i],1):
            b=appuifw.query(u"Enter neighbours of vertex"+str(i+1)+":","number")
            w=appuifw.query(u"Enter wt of neighbour  of vertex"+str(i+1)+":","number")
            l[i][j]=(b,w)

    for k in v:
        for i in range(int(x)):
            g[v[i]]=dict(l[i])
    x=appuifw.Text(u"graph is "+str(g))
    appuifw.app.body=x
    e32.ao_sleep(3)

    d={}
    pi={}

    def init(g,s):
        for node in g.keys():
            d[node]=sys.maxint
            pi[node]=None


        d[s]=0
    def relax(u,v,w):
        if d[v]>d[u]+g[u][v]:
            d[v]=d[u]+g[u][v]
            pi[v]=u
        

    s=appuifw.query(u"Enter source ","number")    
    def dij(g,s):
       init(g,s)
   
       q=d.copy()
       for i in range(len(q)):
           q=d.copy()
           it=[(v,k) for k,v in d.items()]
           it.sort()
           x1=it.pop(i)
           del q[x1[1]]
           
       
           for j in range(len(g[x1[1]])): 
               nei=g[x1[1]]
               w=appuifw.Text(u"Neighbour of selected source "+str(nei))
               appuifw.app.body=w
               e32.ao_sleep(2)
               for k,v in nei.items():
                             
                   relax(x1[1],k,v)
       
       v=appuifw.Text(u"Shortest path from source to all other vertices in the graph\n"+str(d))
       appuifw.app.body=v
       e32.ao_sleep(5)
        
    t1=time.clock()
    t1=int(t1)
    s1=sysinfo.free_ram()
    dij(g,s)
    t2=time.clock()
    t2=float(t2)
    s2=sysinfo.free_ram()
    q=appuifw.Text(u"Space usage:"+str(s1-s2))
    appuifw.app.body=q
    e32.ao_sleep(3)
           
    q=appuifw.Text(u"Time for execution is:"+str(t2-t1)+u"sec")
    appuifw.app.body=q
    e32.ao_sleep(3)
           


about13=appuifw.Text(u'''Dijkstra's algorithm finds out single source shortest path.
It does not work for graphs having negative weight edges.''')


def handle_tabdij(index):
       
    if(index==0):
        app.body=about13
        e32.ao_sleep(30)
    if(index==1):
        dijkstra()
    

def menu1():
    appuifw.app.title=u'easyADA : Divide and Conquer'
    appuifw.app.set_tabs([],None)
    appuifw.app.menu=[(u"Previous menu",menu1),(u"Main Menu",menu)]
    var0=appuifw.selection_list([u'Merge Sort',u'Quick Sort',u'Randomized Quick Sort',u'Back'],1)
    if var0==0:
        appuifw.app.set_tabs([u"About mergesort", u"User Input"], handle_tabms)
        appuifw.app.body=about2
        e32.ao_sleep(10)
        
    if var0==1:
        appuifw.app.set_tabs([u"About quicksort", u"User Input"], handle_tabq)
        appuifw.app.body=about
        e32.ao_sleep(10)

    elif var0==2:
        appuifw.app.set_tabs([u"About randomquicksort", u"User Input"], handle_tabrq)
        appuifw.app.body=about1
        e32.ao_sleep(10)
    elif var0==3:
        menu()


def menu2():
    appuifw.app.title=u'easyADA : Dynamic Programming'
    appuifw.app.set_tabs([],None)
    appuifw.app.menu=[(u"Previous menu",menu2),(u"Main Menu",menu)]
    
    var1=appuifw.selection_list([u'Longest Common Sequence',u'Matrix Chain Multiplication',u'Back'],1)
    if var1==0:
        appuifw.app.set_tabs([u"About lcs", u"User Input"], handle_tablcs)
        appuifw.app.body=about3
        e32.ao_sleep(10)

    if var1==1:
        appuifw.app.set_tabs([u"About mcm", u"User Input"], handle_tabmcm)
        appuifw.app.body=about4
        e32.ao_sleep(10)
    if var1==2:
        menu()

def menu3():
    appuifw.app.title=u'easyADA : Greedy Strategy'
    appuifw.app.set_tabs([],None)
    appuifw.app.menu=[(u"Previous menu",menu3),(u"Main Menu",menu)]
    var2=appuifw.selection_list([u'Huffman Code',u'Fractional Knapsack',u'Activity Selection',u'Back'],1)
    if var2==0:
        appuifw.app.set_tabs([u"About Huffman", u"User Input"], handle_tabhuff)
        appuifw.app.body=about10
        e32.ao_sleep(10)
    
    if var2==1:
        appuifw.app.set_tabs([u"About knapsack", u"User Input"], handle_tabknap)
        appuifw.app.body=about6
        e32.ao_sleep(10)

    if var2==2:
        appuifw.app.set_tabs([u"About activity selection", u"User Input"], handle_tabact)
        appuifw.app.body=about11
        e32.ao_sleep(10)
    if var2==3:
        menu()

def menu4():
    appuifw.app.title=u'easyADA : String Matching'
    appuifw.app.set_tabs([],None)
    appuifw.app.menu=[(u"Previous menu",menu4),(u"Main Menu",menu)]
    var3=appuifw.selection_list([u'Naive',u'Rabin Karp',u'KMP',u'Back'],1)
    if var3==0:
        appuifw.app.set_tabs([u"About Naive", u"Sample",u"User input"], handle_tabn)
        appuifw.app.body=about5
        e32.ao_sleep(10)
         
    if var3==1:
        appuifw.app.set_tabs([u"About Rabin Karp",u"User input"], handle_tabrk)
        appuifw.app.body=about7
        e32.ao_sleep(10)
    if var3==2:
        appuifw.app.set_tabs([u"About KMP",u"User input"], handle_tabkmp)
        appuifw.app.body=about9
        e32.ao_sleep(10)
    if var3==3:
        menu()
        
def menu5a():
    appuifw.app.title=u'easyADA:Search Algorithms'
    appuifw.app.set_tabs([],None)
    appuifw.app.menu=[(u"Previous menu",menu5a),(u"Main Menu",menu)]

    var40=appuifw.selection_list([u'Breadth First Search',u'Depth First Search',u'Back'],1)
    if var40==0:
        appuifw.app.set_tabs([u"About BFS",u"Sample input",u"User input"], handle_tabbfs)
        appuifw.app.body=about13
        e32.ao_sleep(10)
                
    elif var40==1:
        appuifw.app.set_tabs([u"About DFS",u"Sample input",u"User input"], handle_tabdfs)
        appuifw.app.body=about8
        e32.ao_sleep(10)
    elif var40==2:
        menu5()

def menu5c():
    appuifw.app.title=u'easyADA:Shortest Path'
    appuifw.app.set_tabs([],None)
    appuifw.app.menu=[(u"Previous menu",menu5c),(u"Main Menu",menu)]
    var42=appuifw.selection_list([u'Dijkstra',u'Floyd-Warshall',u'Back'],1)
    if var42==0:
        appuifw.app.set_tabs([u"About Dijkstra",u"User input"], handle_tabdij)
        appuifw.app.body=about13
        e32.ao_sleep(10)
    elif var42==1:
        appuifw.app.set_tabs([u"About Warshall",u"User input"], handle_tabwars)
        appuifw.app.body=about12
        e32.ao_sleep(10)
    elif var42==2:
        menu5()

    
    
def menu5():
    appuifw.app.title=u'easyADA : Graphs'
    appuifw.app.set_tabs([],None)
    appuifw.app.menu=[(u"Previous menu",menu5),(u"Main Menu",menu)]
    var4=appuifw.selection_list([u'Search Algorithms',u'Shortest Path',u'Back'],1)
    if var4==0:
        menu5a()
        
    if var4==1:
        menu5c()
    if var4==2:
        menu()
        
    
   
    
        
audio.say("Welcome to easyADA")
appuifw.note(u"Welcome to easyADA ","conf")

e32.ao_sleep(0.5)
def menu():
    def quit():
        
        app_lock.signal()
    app_lock=e32.Ao_lock()
    
    def m():
        
        appuifw.app.title=u"easyADA"
        appuifw.app.set_tabs([],None)
        
        var=appuifw.selection_list([u'Divide and Conquer',u'Dynamic Programming',u'Greedy Strategy',u'String Matching',u'Graphs'],1)
        if var==0:
            menu1()
        
        elif var==1:
            menu2()
        
        elif var==2:
            menu3()
        
        elif var==3:
            menu4()
            
        elif var==4:
            menu5()

        k=appuifw.Canvas()
        k.text((20,20),u"EXITING...",0x000000)
        appuifw.app.body=k
        k.bind(key_codes.EKeyRightSoftkey,quit)
    m()
    
    appuifw.exit_key_handler=quit
    app_lock.wait()

        
    
menu()

                
