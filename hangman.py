import qiskit
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import execute
import random

word_list = ['apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig']

word = random.choice(word_list)

qr = QuantumRegister(len(word))
cr = ClassicalRegister(len(word))
qc = QuantumCircuit(qr, cr)

for i in range(len(word)):
    qc.h(qr[i])

for i in range(len(word)):
    if i % 2 == 0:
        qc.x(qr[i])

qc.measure(qr, cr)

backend = qiskit.BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1)
result = job.result()
counts = result.get_counts()

# 예측 결과 출력
guess = ''
for i in range(len(word)):
    if list(counts.keys())[0][i] == '1':
        guess += word[i]
    else:
        guess += '_'

print("Guess the word:", guess)
