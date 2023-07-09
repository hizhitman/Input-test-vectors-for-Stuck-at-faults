# Input-test-vectors-for-Stuck-at-faults

Requirements:

- Python 3.8  
- Libraries or Modules needed: networkx, time, itertools, memory_profiler(%pip install in jupyter note) 
- Input text files:
  - "Circuit File.txt" containing the circuit netlist
  - "Fault.txt" containing the faulty node and type of fault
- Make sure you have the libraries imported and the Text files in the same directory as the Python application used.
- Just run the code titled "main.py" to create a file named "Sample output.txt" in the same directory 
- You also need to have downloaded QUCS 19 and import the given .sch file to check the simulations
- QUCS simulation schematics have been attached as well


Proof of correctness:\
Other sample inputs and outputs are included as well under the title: SAMPLE_FAULTN

Project Description:
- We have a purely combinational circuit, made of just AND, OR, NOT and XOR gates, with 4 inputs A, B, C and D.
The circuit netlist is provided and we can construct the circuit from it using file reading techniques and other manipulations. The stuck at fault node and type of fault is provided and we are expected to print the list of possible input test vectors to an output file. 

- Solution in a nutshell:
  A Directed Acyclic Graph is created by using the ‘networkx’ library from Python, to model the circuit. We also create 16 test cases to test all different variations of the inputs.
  
  We need to separately write cases for each of the 4 gates and create a solved graph, with updated values at the nodes. We do this twice: 
  1. To calculate the node values when there is no stuck at fault
  2. To calculate the node values when there is a stuck at fault
  While solving in the second iteration, we take only those input values such that the value at the Faulty node is complementary to the given fault type. We neglect the values of the nodes that precede the faulty node and solve the rest of the circuit. We compare the values of all 8 nodes,  in the 12 combinations such that the value at net_f is ‘1’.
  Among these 12 combinations, we compare the Z values in Iteration 1 and 2, and if they are different then that test vector is correct. If not, it won’t help us in detecting the stuck at fault at the given node


Algorithm explanation:

- The process of logic simulation involves evaluating the state of each net in the combinational circuit. Clearly we need a starting point, and here we assume that the primary inputs have been assigned values, and we need to evaluate the remaining net values. 
- We take inputs from the file titled "Circuit File.txt"- containing the circuit netlist, “Fault.txt” containing the fault node and the fault type, and store the necessary information
- We create a set to hold all the input nodes (all but Z in this case)
- We create a dictionary to hold all the input output pairs
- We traverse  through the data obtained from the files and generate the DAG, The input set(3), the dictionary(4)
- Note that the ~ NOT gate is handled differently from the other 3 gates owing to the difference in circuit format
- We set the gatetypes of the A,B,C,D nodes to Primary input type and for the other nodes except the first 4, We set the gate types to the corresponding Output nodes. The value of all the nodes is initialized to 0. We can also topologically sort the graph to establish an hierarchy in the nets
For ex: A,B,C,D - primary inputs, net_e, net_f: primary net, net_g:secondary net
- We create a list with all 16 possible permutations for the input nodes, using itertools module. 
- We also create functions for implementing all the 4 gates and reference them later as and when needed
- STEP 1: NORMAL EVALUATION: Once the Nodes are established for the graph, we update the values of every node by a method called “Topological Evaluation”. We take a different input list from the permutation,  and update every node depending on its 1. Predecessors and 2. GateType. The final nodes that we have will be the state  of  the nodes after complete evaluation
- STEP 2:  FAULTY EVALUATION:  We are analyzing SA0 at net_f. From our understanding of Stuck at faults we know that we need to find the input vectors such that the value of net_f in the NORMAL EVALUATION is complementary to the fault,  i.e., net_f has to be ‘1’. And there should be a change in Z output value as it is the only detectable node. So  we make a note of the input test cases for which net_f takes a value of 1 and store them in a unique list called ‘l4’.  We use these test cases alone for further FAULTY EVAL.
- case 1: When fault is in the PRIMARY INPUT or in the Primary nest: (given example of net_f): Here we use a separate codeblock[solve_with_faults_primary] to disregard the inputs C and D and set net_f  to ‘0’ . We calculate  net_g, Z and backtrack  to get net_e, A and B. 
 - case 2: When fault is in the SECONDARY INPUT: (net_g, SA0): Here we use a separate codeblock [solve_with_faults_secondary] to disregard the predecessors of net_g which is net_f  and set net_g to ‘0’/. We calculate Z and backtrack  to get net_e, A and B. 
- The outputs from the NORMAL and FAULTY evaluation will have the same first 4 terms, (same A,B,C,D). We check all of these pairs and output only those that have different Z (last elements) 
- We print all the possible input test vectors in the file names “Example Output.txt”
