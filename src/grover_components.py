from qiskit import QuantumCircuit

def diffuser(main_circuit: QuantumCircuit, q_regs: list, qubits: int):
        """
        Applies the Grover diffusion operator to the given quantum circuit.
        This operator amplifies the amplitudes of the marked states and
        reduces the amplitudes of the unmarked states, effectively rotating
        the state vector towards the marked states.

        Args:
            main_circuit (QuantumCircuit): The Qiskit QuantumCircuit object to
                                           which the diffuser is appended.
            q_regs (list): A list of QuantumRegister objects representing the
                           clauses.
            qubits (int): The total number of qubits in the oracle register,
                          without considering the ancilla.

        Returns:
            QuantumCircuit: The main Qiskit QuantumCircuit object with the
                            diffusion operation appended.
        """
        circuit = QuantumCircuit(*q_regs, name='Grover\n Diffuser')

        # Undo the entanglement (GHZ_Init^dagger)
        for i in range(qubits):
        # Apply CNOTs in reverse and then Hadamards
          for j in range(1, len(q_regs)):
              circuit.cx(q_regs[0][i], q_regs[j][i])
          circuit.h(q_regs[0][i])
          # Precondition for controlled operation with the |0...0> state
          circuit.x(q_regs[0][i])

        controls = [q_regs[0][i] for i in range(qubits-1)]
        target = q_regs[0][qubits-1]

        # Apply a multi-controlled Z
        circuit.h(target)
        circuit.mcx(controls, target)
        circuit.h(target)

        # Redo the entanglement
        for i in range(qubits):
          circuit.x(q_regs[0][i])
          circuit.h(q_regs[0][i])
          for j in range(1, len(q_regs)):
              circuit.cx(q_regs[0][i], q_regs[j][i])

        # Convert diffuser circuit to gate
        diffuser_gate = circuit.to_gate()
        gate_qubits = [q_regs[j][i] for j in range(len(q_regs))
                       for i in range(qubits+1)]

        # Append the gate to the main circuit
        main_circuit.append(diffuser_gate, gate_qubits)

        return main_circuit

def ghz_init(main_circuit: QuantumCircuit, q_regs: list, qubits: int):
  """
  Encapsulates the preparation of a GHZ-like entangled state across the qubits
  of all provided registers.

  Args:
      main_circuit (QuantumCircuit): The Qiskit QuantumCircuit object to which
                                     the GHZ-like state preparation is applied.
      q_regs (list): A list of QuantumRegister objects.
      qubits (int): The total number of qubits in each register, including the
                    ancilla qubit.

  Returns:
      QuantumCircuit: The modified Qiskit QuantumCircuit object after the
                      GHZ-like state preparation.
  """
  circuit = QuantumCircuit(*q_regs, name="GHZ_Init")
  # GHZ-like states between registers
  for i in range(qubits-1):
      # Apply Hadamard to the i-th qubit on first register
      circuit.h(q_regs[0][i])

      # Apply CX from the i-th qubit on first register to the i-th qubit of
      # the rest of the registers
      for j in range(1, len(q_regs)):
          circuit.cx(q_regs[0][i], q_regs[j][i])

  # Convert GHZ_Init to gate
  ghz_init_gate = circuit.to_gate()

  # Apply GHZ_Init to all qubits of the circuit
  gate_qubits = [qubit for reg in q_regs for qubit in reg]
  main_circuit.append(ghz_init_gate, gate_qubits)

  return main_circuit