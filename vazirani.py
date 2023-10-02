from qiskit import *
import numpy as np

def deueth_joza(n):
    qc = QuantumCircuit(n, n)
    a = np.random.randint(1, 2**n)
    oracleType=[np.random.randint(2) for i in range(n-1)]
    qc.x(n-1)
    qc.barrier()
    print(oracleType)
    for index,i in enumerate(oracleType):
        if i == 1:       #If the oracleType is "0", the oracle returns oracleValue for all input. 
            qc.cx(n-1,index)
    qc.barrier()
    for i in range(n):
        qc.h(i)
    qc.barrier()
    for i in range(n-1):
        qc.measure(i, i)
    return qc



qc = deueth_joza(8)

qc.draw(output='mpl')
count = execute(qc, Aer.get_backend('qasm_simulator'),shots=1).result().get_counts()

print(count)