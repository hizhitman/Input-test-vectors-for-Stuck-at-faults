# Input-test-vectors-for-Stuck-at-faults

Requirements:

Python 3.8
Libraries or Modules needed:networkx, time, itertoolss(%pip install in jupyter note)
Input text files:
"Circuit File.txt" containing the circuit netlist
"Fault.txt" containing the faulty node and type of fault
Make sure you have the libraries imported and the Text files in the same directory as the Python application used.

Just run the code titled "main.py" to create a file named "Sample output.txt" in the same directory.

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

