import numpy as np
from qiskit import QuantumCircuit

def PhaseAND(main_circuit: QuantumCircuit, q_regs: list, qubits: int):
  """
  Performs boolean combination of clauses in conjunctive normal form to apply
  π-phase shift

  Args:
        main_circuit (QuantumCircuit): The Qiskit QuantumCircuit object to which
                                       the PhaseAND is applied.
        qubits (int): The total number of qubits in the each register, with the
                      ancilla.
        q_regs (list): A list of QuantumRegister objects representing the
                       clauses.

    Returns:
        QuantumCircuit: The modified Qiskit QuantumCircuit object after
                        appending the PhaseAND operation.
  """
  circuit = QuantumCircuit(*q_regs, name="PhaseAND")

  controls = [q_regs[j][qubits-1] for j in range(len(q_regs)-1)]
  target = q_regs[len(q_regs)-1][qubits-1]

  # Apply MCZ operation
  circuit.h(target)
  circuit.mcx(controls, target)
  circuit.h(target)

  # COnvert to gate and append to main_circuit
  phase_and_gate = circuit.to_gate()
  gate_qubits = [qubit for reg in q_regs for qubit in reg]
  main_circuit.append(phase_and_gate, gate_qubits)

  return main_circuit

def PhaseNAND(main_circuit: QuantumCircuit, q_regs: list, qubits: int):
  """
  Performs a negated boolean combination of clauses in conjunctive normal form to
  apply π-phase shift

  Args:
        main_circuit (QuantumCircuit): The Qiskit QuantumCircuit object to which
                                       the PhaseNAND is applied.
        qubits (int): The total number of qubits in the each register, with the
                      ancilla.
        q_regs (list): A list of QuantumRegister objects representing the
                       clauses.

    Returns:
        QuantumCircuit: The modified Qiskit QuantumCircuit object after
                        appending the PhaseAND operation.
  """
  circuit = QuantumCircuit(*q_regs, name="PhaseAND")

  controls = [q_regs[j][qubits-1] for j in range(len(q_regs)-1)]
  target = q_regs[len(q_regs)-1][qubits-1]

  PhaseAND(circuit, q_regs, qubits)
  # Invert whole subspace up to global phase
  circuit.rz(2*np.pi, target)

  # Convert to gate and append to main_circuit
  phase_and_gate = circuit.to_gate()
  gate_qubits = [qubit for reg in q_regs for qubit in reg]
  main_circuit.append(phase_and_gate, gate_qubits)

  return main_circuit

def PhaseNOR(main_circuit: QuantumCircuit, q_regs: list, qubits: int):
  """
  Performs a negated boolean combination of clauses in disjunctive normal form to 
  apply π-phase shift.

  Args:
        main_circuit (QuantumCircuit): The Qiskit QuantumCircuit object to which
                                       the PhaseNOR is applied.
        qubits (int): The total number of qubits in the each register, with the
                      ancilla.
        q_regs (list): A list of QuantumRegister objects representing the
                       clauses.

    Returns:
        QuantumCircuit: The modified Qiskit QuantumCircuit object after
                        appending the PhaseNOR operation.
  """
  circuit = QuantumCircuit(*q_regs, name='PhaseNOR')

  controls = [q_regs[j][qubits-1] for j in range(len(q_regs)-1)]
  target = q_regs[len(q_regs)-1][qubits-1]

  # Following that NOR is equivalent to AND in negate inputs:
  # Apply X gates over the controls and target
  for control in controls:
    circuit.x(control)
  circuit.x(target)

  # Apply MCZ operation
  #circuit.h(target)
  #circuit.mcx(controls, target)
  #circuit.h(target)
  PhaseAND(circuit, q_regs, qubits)

  # Undo the X gates
  for control in controls:
    circuit.x(control)
  circuit.x(target)

  phase_nor_gate = circuit.to_gate()
  gate_qubits = [qubit for reg in q_regs for qubit in reg]
  main_circuit.append(phase_nor_gate, gate_qubits)

  return main_circuit

def PhaseOR(main_circuit: QuantumCircuit, q_regs: list, qubits: int):
  """
  Performs boolean combination of clauses in disjunctive normal form to
  apply π-phase shift.

  Args:
        main_circuit (QuantumCircuit): The Qiskit QuantumCircuit object to which
                                       the PhaseNOR is applied.
        qubits (int): The total number of qubits in the each register, with the
                      ancilla.
        q_regs (list): A list of QuantumRegister objects representing the
                       clauses.

    Returns:
        QuantumCircuit: The modified Qiskit QuantumCircuit object after
                        appending the PhaseNOR operation.
  """
  circuit = QuantumCircuit(*q_regs, name='PhaseNOR')

  controls = [q_regs[j][qubits-1] for j in range(len(q_regs)-1)]
  target = q_regs[len(q_regs)-1][qubits-1]

  PhaseNOR(circuit, q_regs, qubits)
  # Invert whole subspace up to global phase
  circuit.rz(2*np.pi, target)

  phase_nor_gate = circuit.to_gate()
  gate_qubits = [qubit for reg in q_regs for qubit in reg]
  main_circuit.append(phase_nor_gate, gate_qubits)

  return main_circuit
