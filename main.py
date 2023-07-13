import networkx as nx
import time
from memory_profiler import *
from itertools import permutations

def main():
    g = nx.DiGraph() 
    with open("Circuit File.txt") as fo : #To collect data from the circuit netlist given
        lines = fo.readlines()

    inputs = set() #A set to hold all the input nodes (all but Z in this case)
    ip = []
    outputs = {} #dictionary to hold all the input output pairs

    with open("Fault.txt") as ff : #Reading the type of fault from the file given
        fault = ff.readlines()
    node_fault=fault[0].split()[2] #Storing the fault node
    type_fault=fault[1].split()[2][2] #Storing the fault type
 

    for indline in lines :#Generating a DAG, Input set, Output Dictionary
        line = indline.split()
        if len(line) == 4 and line[2]=='~': #Handling the not gate separately due to different input style
            i=line[-1]
            o=line[0]
            inputs.add(i)
            outputs[o] = line[2]
            g.add_edge(i,o)
        else: #Handling all other gates except the NOT gate
            i1= line[2]
            i2= line[4]
            o= line[0]
            inputs.add(i1)
            inputs.add(i2)
            outputs[o] = line[3]
            g.add_edge(i1,o)
            g.add_edge(i2,o)

    for inp in inputs :
        if inp in outputs.keys() :
            continue
        else :
            ip.append(inp) #ip is a list that holds just the primary inputs (A,B,C,D)

    for inp in ip : #We set the gatetypes of the A,B,C,D nodes to Primaryinput type
        g.nodes[inp]["gateType"] = "PrimaryInput"
    for out in outputs:#For the other nodes except the first 4, We set the gatetypes to the corresponding Output nodes
        g.nodes[out]["gateType"] = outputs[out]
    n1 = list(nx.topological_sort(g)) #n1 contains all the nodes in the order in which they appear in the graph
  
    a=[]
    for node in n1:
        a.extend(list(g.predecessors(node)))
   

        

    for node in n1:
        g.nodes[node]['value'] = 0 #We initialise all nodes with a value of 0
    f=g.copy() #We create a deep copy of this graph for the second DAG evaluation



    l1= ["A","B","C","D"]  #l1 holds the primary inputs
    l2= list(set(permutations([0,0,0,0,1,1,1,1], 4))) #We are testing all 16 possible inputs, and hence we create a permutation such that all 16 are created
    l3=[]

    #Below we have defined the logical Operations encountered and the outputs for alll cases
    def AND(a, b):
        return a*b
    def OR(a,b) :
        if a+b == 0 :
            return 0
        else :
            return 1
    def XOR(a,b) :
        if (a==1 and b==0) or (a==0 and b==1):
            return 1
        else :
            return 0
    def NOT(a):
        if a == 1:
            return 0
        else :
            return 1

    #This update code is for the first DAG evaluation. This takes a node and checks the predecessor and gatetype to change the value in the node in graph g
    def update(node):
        ip = list(g.predecessors(node))
        ips = []
        for i in ip:
            ips.append(g.nodes[i]['value'])
        if g.nodes[node]['gateType'] == "&":
            g.nodes[node]['value'] =  AND(ips[0], ips[1]) 
        if g.nodes[node]['gateType'] == "|" :
            g.nodes[node]['value'] =  OR(ips[0], ips[1])  
        if g.nodes[node]['gateType'] == "^":
            g.nodes[node]['value'] =  XOR(ips[0], ips[1]) 
        if g.nodes[node]['gateType'] == "~":
            g.nodes[node]['value'] =  NOT(ips[0]) 
    
    #This update code is for the second DAG evaluation. This takes a node and checks the predecessor and gatetype to change the value in the node in graph f
    def fault_update(node):
        ip = list(f.predecessors(node))

        ips = []
        for i in ip:
            ips.append(f.nodes[i]['value'])
        if f.nodes[node]['gateType'] == "&":
            f.nodes[node]['value'] =  AND(ips[0], ips[1]) 
        if f.nodes[node]['gateType'] == "|" :
            f.nodes[node]['value'] =  OR(ips[0], ips[1])  
        if f.nodes[node]['gateType'] == "^":
            f.nodes[node]['value'] =  XOR(ips[0], ips[1]) 
        if f.nodes[node]['gateType'] == "~":
            f.nodes[node]['value'] =  NOT(ips[0])

    #This DAG function sends the node to DAG evaluation, provided it is not a Primary input
    def DAG():
        for node in n1 :
            if g.nodes[node]['gateType'] == "PrimaryInput" :
                continue
            else :
                update(node)
    #This DAG function checks if the node is not the predecessor of the fault node, and that it is not primary, and sends the node to DAG evaluation
    def fault_DAG():
        for node in n1 :
            if node not in uu:
           
                
                if f.nodes[node]['gateType'] == "PrimaryInput":
                    continue
                elif node==node_fault:
                    f.nodes[node]['value'] = int(type_fault)
                else:
                    
                    fault_update(node)


    #Actual solver main code for the first evaluation
    def solveDAG(g, l1, l2, n1):

        yyy=[]
        while len(l2) !=0 :

            l21 = l2[0]    
            for ele in l1:
                g.nodes[ele]['value'] = int(l21[l1.index(ele)]) #We get different values of A,B,C,D from l2 and change it in the graph g
            DAG() #We change the values of other output nodes 
            
            u=l2.pop(0) #We move to the next set of input values
            #for node in n1:
            #    print(g.nodes[node]['value'],end='')
           # print(',')
            
            
            if g.nodes[node_fault]['value']==1^int(type_fault): #l3 will have all A,B,C,D values such that the value at the node is opposite to the stuck at given
                for node in n1:
                    l3.append(u) #This list is created to store values for the next round of faulty evaluation
        global l4; #We save l4 as the set of values in l3 to ensure uniqueness


        l4=list(set(l3))
        l5=list(l4)
        

        #The below code is to make sure that the order of elements returned by this evaluation and the faulty evaluation are in the same order as ;4

        while len(l5) !=0 :
            s=''
            l23 = l5[0]    
            for ele in l1:
                g.nodes[ele]['value'] = int(l23[l1.index(ele)])
            DAG()
            u=l5.pop(0)


            if g.nodes[node_fault]['value']==1^int(type_fault):
                for node in n1:
                    s+=str((g.nodes[node]['value']))

            yyy.append(s)
   
        return yyy


    pred=(list(g.predecessors(node_fault))) #This saves the predecessors values


    l=[] 
    for i in n1:
        if i not in pred:
            l.append(i) 
    #Actual solver for primary faults
    def solve_with_faults_primary(f, l1, l2, n1,uu):
        yyy=[]
        while len(l2) !=0 :
            s=''
            l21 = l2[0]    
            for ele in l1:        
                if ele!=node_fault and ele not in pred:
                    f.nodes[ele]['value'] = int(l21[l1.index(ele)])
                elif ele==node_fault and ele not in pred :
                    f.nodes[ele]['value'] = int(type_fault)
            fault_DAG() #We use a different solver with a different update function

            rr=l2.pop(0)

            for node in n1:
                if node in l:

                    s+=str(f.nodes[node]['value'])
                else:
                    s+=str(rr[uu[node]]) #Here when the node is C or D, we instruct the function to take the original value itsself without taking the eval one
            yyy.append(s)
        return(yyy)

    #Actual solver for secondary or more faults
    def solve_with_faults_secondary(f, l1, l2, n1,uu):
        yyy=[]
        yp=0
        while len(l2) !=0 :

            s=''
            l21 = l2[0]    

            for ele in l1:        
                f.nodes[ele]['value'] = int(l21[l1.index(ele)])

            fault_DAG()
            rr=l2.pop(0)

            for node in n1:
                if node not in uu:

                    s+=str(f.nodes[node]['value'])
                else:
                    s+=var1[yp][uu[node]] #Here when the node is one of the predecessors, we instruct the function to take the original value itsself without taking the eval one

            yyy.append(s)
            yp+=1
        return(yyy)

    begin = time.time()
    var1=solveDAG(g, l1, l2, n1)
  
 
    for pre in pred: #fanout condition with predecessors coinciding
        
        if a.count(pre)==1: #ensures no fanout
            f.remove_node(pre) #This removes the nodes of the predecessors as well
    gh=f.nodes

    F=0 #Flag 
    if node_fault in l1 or pred[0] in l1: #if the fault node is at Primary level, or at one of the inputs A,B,C,D
        uu={}

        for i in pred:
            uu[i]=(l1.index(i))
        var2=solve_with_faults_primary(f, l1, l4, n1,uu)

    elif node_fault not in l1 or pred[0] not in l1:#if the fault node is at Secondary level
        uu={}
      

        for im in pred:
            if im not in gh:
                uu[im]=(list(inputs).index(im))

        var2=solve_with_faults_secondary(f, l1, l4,n1,uu)
  
    fobj=open("Sample Output.txt",'a+') #Writing to the output file

    for i in range(len(var1)):
        if var1[i][-1]!=var2[i][-1]: #if the Z value differs, we include it as a valid test input vector
            a_s=var2[i][:4]
            a_l=[]
            F=1
            for ii in a_s:
                a_l.append(int(ii))
                
            #print("[A, B, C, D] =",a_l,", Z = ",int(var2[i][-1]))
            fobj.write("[A, B, C, D] ="+str(a_l)+", Z = "+(var2[i][-1])+"\n")
   
    if F==0:
        fobj.write("NO INPUT TEST VECTOR CAN HELP US IDENTIFY THIS STUCK-AT-FAULT")
    #print(nx.draw(g,pos=nx.spring_layout(g),with_labels=True,node_color='y',font_color='r',arrowsize=5))
    end = time.time()
    fobj.close()
    print("Time taken is "+str(end-begin))
    
main()
