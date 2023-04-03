---
layout: post
title: "QUANTUM CIRCUIT MAPPING WITH MACHINE LEARNING"
description: "This project aims to map logical qubits created onto actual processor qubits using machine learning algorithms and also demonstrate other quantum computing algorithms."
categories: compsoc
thumbnail: "placeholder-image.jpg"
year: 2023
gmeet: ""
---

### Mentor
- Anirudh Prabharkaran

### Members
- Calvin Dominic Fernandes
- Chinmaya Sahu
- Varun Iyer

## Acknowledgements
We would like to extend our heartfelt gratitude to Anirudh Prabhakaran, our mentor, for his invaluable guidance and support throughout our IEEE year-long project on quantum circuit mapping and other quantum computing algorithms. His deep understanding of the subject matter, his dedication to helping us succeed, and his willingness to go above and beyond to ensure that we were on the right track have been instrumental in our project's success.
We would also like to extend our thanks to Anirudh T. His work in his DAAD internship gave us the idea for this project. Without his resources, references, and guidance, it wouldn't have been possible for us to do this project.

## Aim
This project aims to find a quantum circuit mapping from the qubits of a theorized quantum circuit to the qubits of an actual quantum processor using a machine learning algorithm. The project also aims to showcase some quantum computing algorithms such as Grover's Search Algorithm, Quantum Teleportation, and the No Cloning Theorem.

## Introduction
Quantum computing is a rapidly advancing field that has the potential to revolutionize computing as we know it. As more and more organizations and researchers explore the possibilities of quantum computing, it is becoming increasingly important to develop effective ways of mapping quantum circuits onto actual quantum processors. In this project, we focused on developing a machine learning algorithm using a deep learning approach to map the qubits of a quantum circuit to an actual quantum processor's qubits.

Our project aims to address the challenges associated with quantum circuit mapping by developing an algorithm that could optimize the mapping process and produce high-quality results. To do this, we leveraged our expertise in both quantum computing and machine learning to create an algorithm that was both accurate and efficient.

In addition to our work on quantum circuit mapping, we also explored some of the foundational concepts of quantum computing, such as the No-Cloning Theorem, Quantum Teleportation, and Grover's Search Algorithm. Through these demonstrations, we gained a deeper understanding of quantum computing and its potential applications.

Overall, our project represents an important step forward in the development of quantum computing technology. By developing a machine learning algorithm to optimize the mapping of quantum circuits to actual quantum processors, we have made a small contribution towards making quantum computing a more practical and accessible technology.

## No Cloning Theorem

### Theorem

The No Cloning theorem is a fundamental concept in quantum mechanics that states that it is impossible to create an identical copy of an unknown quantum state. This theorem has significant implications for quantum computing and communication, as it restricts the ability to copy and transmit quantum information.

### Problems

One of the primary problems that the No Cloning theorem poses is that it makes it impossible to create exact copies of quantum data, which is essential for many applications of quantum computing, including quantum cryptography and quantum error correction. Without the ability to create copies of quantum data, these applications become much more difficult to implement, as errors and losses in the transmission of data cannot be corrected by simply creating new copies.

### Consequences

A consequence of the No Cloning theorem is that it imposes limitations on the security of quantum cryptography protocols. In particular, it makes it impossible for an eavesdropper to copy the quantum states that are being transmitted without being detected. This means that quantum cryptography protocols can be used to establish secure communication channels that are resistant to eavesdropping, but they cannot be used to guarantee absolute secrecy, as it is impossible to prevent an attacker from intercepting and measuring the quantum states that are being transmitted. As a result, quantum cryptography protocols need to be carefully designed to take into account the limitations imposed by the No Cloning theorem and to ensure that they are secure against the most common types of attacks.

## Quantum Teleportation

### What?

Quantum teleportation is a quantum communication technique that allows for the transfer of quantum information from one qubit to another, without physically transporting the qubit itself. The process of quantum teleportation involves creating an entangled pair of qubits, one of which is given to the sender and the other to the receiver. The sender then measures the entangled pair and the qubit to be teleported, generating two classical bits of information that are sent to the receiver. The receiver then performs certain quantum operations on their half of the entangled pair based on the information received, which causes their qubit to become a perfect copy of the original qubit.

### Why?

The need for quantum teleportation arises from the fact that quantum information is extremely fragile and can be easily disturbed or destroyed during transmission. Quantum teleportation enables the transfer of quantum information across large distances without the need for physical transport of the qubits themselves, thus overcoming the limitations of conventional communication methods. Additionally, quantum teleportation has potential applications in quantum cryptography, quantum computing, and quantum networking, among others.

### How?

To perform quantum teleportation, a sender and a receiver must share an entangled pair of qubits. The sender then performs a Bell state measurement on their half of the entangled pair and the qubit to be teleported, generating two classical bits of information that are sent to the receiver. Based on the information received, the receiver performs certain quantum operations on their half of the entangled pair, which causes their qubit to become a perfect copy of the original qubit. The entangled pair is then destroyed, leaving the original qubit in an unknown state. Quantum teleportation relies on the principles of entanglement and quantum measurement to transfer quantum information across large distances without the need for physical transport of the qubits themselves.

## Grover's Search Algorithm

### What?

Grover's search algorithm is a quantum computing algorithm that can be used to search an unsorted database in a faster and more efficient way than classical algorithms. The algorithm is based on the principles of quantum superposition and interference and is designed to find the location of a marked item in an unsorted database with a complexity of O(√N), where N is the number of items in the database. This represents a quadratic speedup over classical algorithms, which require O(N) operations.

### Why?

The need for Grover's search algorithm arises from the fact that classical algorithms become increasingly inefficient as the size of the database grows. Grover's algorithm provides a faster and more efficient way to search large databases and can be used to solve a variety of problems, such as finding the optimal solution to an optimization problem or searching for a specific element in a large dataset. The algorithm has potential applications in fields such as cryptography, data analysis, and machine learning.

### Where?

Grover's search algorithm has potential applications in cryptography, data analysis, and machine learning. In cryptography, the algorithm can be used to break certain types of cryptographic codes by searching for a specific key in a large key space. In data analysis, the algorithm can be used to search large datasets and find specific patterns or correlations, which is useful in fields such as bioinformatics, finance, and marketing. In machine learning, the algorithm can be used to search for the optimal solution to an optimization problem or to perform database searches more efficiently. Overall, Grover's search algorithm provides a significant speedup over classical algorithms for searching unsorted databases and has the potential to revolutionize fields that rely on large amounts of data analysis and processing.

### How?

Grover's search algorithm can be implemented using a quantum computer and requires the use of several quantum gates, including the Hadamard gate, the Oracle gate, and the Grover diffusion operator. The algorithm begins by creating a superposition of all possible states in the database, which is then used to apply the Oracle gate to mark the location of the desired item. The algorithm then uses the Grover diffusion operator to amplify the amplitude of the marked item, while reducing the amplitude of the other states. This process is repeated multiple times until the marked item is found with a high probability.


## Quantum Circuit Mapping

### Abstract

The quantum circuit mapping problem is a critical issue in the field of quantum computing, where a quantum circuit's qubits must be mapped onto the physical qubits of a quantum processor. The problem arises due to the limited connectivity between physical qubits in a quantum processor, which makes it difficult to execute quantum circuits accurately. The solution to this problem lies in developing efficient mapping algorithms that can map a quantum circuit's qubits onto the physical qubits of a quantum processor while minimizing errors and maintaining the circuit's functionality. This problem has important implications for the scalability and reliability of quantum computing systems and has significant practical applications in fields such as quantum simulation, quantum cryptography, and quantum machine learning.

### Introduction

Quantum computing has the potential to revolutionize many fields, from cryptography to drug discovery, but it also presents significant challenges. One of the biggest challenges is the quantum circuit mapping problem, which involves mapping a quantum circuit's logical qubits to the physical qubits of a quantum processor. The problem arises because the connectivity between physical qubits is limited, and a quantum circuit may require specific qubit interactions that are not available on the processor. Solving this problem is critical for the scalability and reliability of quantum computing systems, as errors in mapping can lead to incorrect results and significant computational overhead.

To address the quantum circuit mapping problem, researchers have developed a range of mapping algorithms that aim to minimize errors and maintain the circuit's functionality. These algorithms use a combination of classical and quantum techniques to optimize the mapping process, taking into account factors such as the available connectivity of the physical qubits and the complexity of the quantum circuit. As quantum computing technology continues to advance, the quantum circuit mapping problem is likely to become even more significant, highlighting the need for continued research in this area.

### Methodology

To address the quantum circuit mapping problem, we have developed a machine learning algorithm using a deep learning approach. The algorithm takes in various parameters of the quantum circuit, such as the number of CNOT gates, SWAP gates, and other gate types, as well as the connectivity of the physical qubits. It then uses a deep neural network architecture, comprising fully connected layers with slots at the end, to optimize the mapping of logical qubits to physical qubits. The slots at the end of the network allow for a flexible number of physical qubits to be used for the mapping, allowing the algorithm to adapt to different quantum processors.

### Implementation

We implemented the model in TensorFlow using its high-level machine learning API, Keras. Keras provides a simple and intuitive interface for building complex models, making it easier to define the architecture of the network and train it efficiently. Additionally, TensorFlow supports distributed training, which allows the model to be trained on multiple GPUs or nodes, further increasing its efficiency.

In PyTorch, we defined the model using its dynamic computational graph feature, which allows the architecture of the network to be defined on the fly. This provides greater flexibility and control over the model architecture, allowing us to make changes and modifications easily during development. PyTorch also provides a powerful automatic differentiation feature, which simplifies the computation of gradients and makes it easier to optimize the model during training.

Despite the differences in the implementation of the model in TensorFlow and PyTorch, the core algorithm remains the same. We used the same deep learning architecture for both implementations, with minor modifications to tailor the models to the specific requirements of the frameworks. Overall, having implementations in both TensorFlow and PyTorch provides greater flexibility and allows the algorithm to be used in a wider range of applications, depending on the preferences and requirements of the user.

### Results

Our quantum circuit mapping model using deep learning algorithms has shown promising results in accurately mapping the qubits of a quantum circuit to a physical quantum processor. The model was trained on a large dataset of quantum circuits and their corresponding mappings and was able to learn the complex relationships between various parameters, such as the number of CNOT gates, SWAP gates, and other quantum gates, to accurately predict the mapping of the circuit to the physical qubits of the quantum processor.

The model was tested on a separate set of circuits, and was able to achieve a high accuracy rate, indicating its effectiveness in solving the quantum circuit mapping problem. Additionally, the model's predictions were compared to those of existing quantum circuit mapping algorithms and were found to be more accurate and efficient in many cases.

Overall, the results of our quantum circuit mapping model using deep learning algorithms show great promise in addressing the challenges of mapping quantum circuits to physical qubits, which is a critical problem in the development of large-scale quantum computing systems. The accuracy and efficiency of the model suggest that it may be a valuable tool for researchers and developers working on quantum computing applications, and may help to accelerate the development of quantum computing technologies.


## Conclusion

In conclusion, our year-long IEEE project on quantum circuit mapping and other quantum computing algorithms has demonstrated the potential of quantum computing and the challenges that researchers and developers face in harnessing this technology. Through our exploration of Quantum Teleportation, the No Cloning Theorem, and Grover's Search Algorithm, we have gained insights into the unique properties of quantum systems and the potential for quantum computing to revolutionize industries ranging from cryptography to drug discovery.

In particular, our work on quantum circuit mapping has addressed a critical challenge in the development of large-scale quantum computing systems. Our deep learning model, implemented in both TensorFlow and PyTorch, has shown promising results in accurately mapping quantum circuits to physical qubits in quantum processors, which is a critical step towards helping various companies build quantum processor systems by utilizing our quantum mapping algorithm.

Overall, our project has provided a valuable opportunity to explore cutting-edge technologies and concepts in the field of quantum computing. We hope that our work will inspire others to continue pushing the boundaries of this exciting field and to develop new algorithms and applications that will unlock the full potential of quantum computing in the years to come.

 

## References

1. T. G. Wong, _Introduction to classical and quantum computing_. Omaha, NE: Rooted Grove, 2022.
2. M. A. Nielsen and I. L. Chuang, _Quantum Computation and Quantum Information_. Cambridge: Cambridge University Press, 2022.
3. Giovanni Acampora, Roberto Schiattarella, Alfredo Troiano, A dataset for quantum circuit mapping, Data in Brief, Volume 39, 2021, 107526, ISSN 2352-3409, [https://doi.org/10.1016/j.dib.2021.107526](https://www.sciencedirect.com/science/article/pii/S2352340921008027)
4. Acampora, G., Schiattarella, R. Deep neural networks for quantum circuit mapping. _Neural Comput & Applic_ **33**, 13723–13743 (2021). [https://doi.org/10.1007/s00521-021-06009-3](https://link.springer.com/article/10.1007/s00521-021-06009-3)
5. "Qiskit Textbook," _Qiskit Textbook_. [Online]. Available: https://qiskit.org/learn/. [Accessed: 26-Mar-2023].
6. “Quantum Circuit Simulator,” _Quirk: Quantum Circuit Simulator_. [Online]. Available: https://algassert.com/quirk. [Accessed: 26-Mar-2023].
7. “Qiskit,” _YouTube_. [Online]. Available: https://www.youtube.com/@qiskit. [Accessed: 26-Mar-2023].
8. “IBM quantum composer,” _IBM Quantum_. [Online]. Available: https://quantum-computing.ibm.com/composer/docs/iqx/. [Accessed: 26-Mar-2023].