from qiskit import QuantumCircuit

# Oracles constructed following the scheme from:
# > Sanchez-Rivero, J., Talaván, D., Garcia-Alonso, J., Ruiz-Cortés, A., & Murillo, J. M. (2025).
# > Automatic generation of efficient oracles: The less-than case. Journal of Systems and Software, 219, 112203. 
# > [https://doi.org/10.1016/j.jss.2024.112203]

def oracle_less(number: int, qubits: int):
    """
    Constructs an oracle that stores information in an ancilla about whether or 
    not a value is less than a certain number. It is hermitian, so the adjoint 
    is effectively the same operator.

    Args:
        number (int): The integer value (the specific target state) to be
                      marked.
        qubits (int): The total number of qubits in the oracle register, without
                      considering the ancilla.

    Returns:
        Gate: The Qiskit QuantumCircuit of the oracle "less than" converted to a
              Gate object for it to be appended.
    """
    circuit = QuantumCircuit(qubits+1, name=f'Oracle\n x<{number}')

    # Convert the target integer 'number' into its binary representation.
    number_bin = format(number, f'0{qubits}b')
    # Apply gates based on the bits of the target 'number'
    for idx, bit in enumerate(number_bin):
        if bit == '1':
            circuit.x(idx)
            circuit.mcx(list(range(idx+1)), qubits)
            circuit.x(idx)
        elif bit == '0':
            circuit.x(idx)

    for idx, bit in enumerate(number_bin):
        if bit == '0':
            circuit.x(idx)

    return circuit.to_gate()

def oracle_greatereq(number: int, qubits: int):
  """
  Constructs an oracle that stores information in an ancilla about whether or 
  not a value is greater (or equal) than a certain number. It is hermitian, so 
  the adjoint is effectively the same operator.

  Args:
      number (int): The integer value (the specific target state) to be marked.
      qubits (int): The total number of qubits in the oracle register, without
                    considering the ancilla.

  Returns:
      Gate: The Qiskit QuantumCircuit of the oracle "greater (or equal) than" 
            converted to a Gate object for it to be appended.
  """
  circuit = QuantumCircuit(qubits+1, name=f'Oracle\n x>={number}')

  # Reusing the less-than oracle
  gate_qubits = list(range(qubits + 1))
  circuit.append(oracle_less(number, qubits), gate_qubits)
  # Invert the ancilla value to effectively mark the states
  # for the greater-than instance
  circuit.x(qubits)

  return circuit.to_gate()

def oracle_eq(number: int, qubits: int):
  """
  Constructs an oracle that stores information in an ancilla about whether or 
  not a value is equal than a certain number. It is hermitian, so the adjoint 
  is effectively the same operator.

  Args:
      number (int): The integer value (the specific target state) to be marked.
      qubits (int): The total number of qubits in the oracle register, without
                    considering the ancilla.

  Returns:
      Gate: The Qiskit QuantumCircuit of the oracle "equal to" converted to a 
            Gate object for it to be appended.
  """
  circuit = QuantumCircuit(qubits+1, name=f'Oracle\n x={number}')

  # Convert the target integer 'number' into its binary representation.
  number_bin = format(number, f'0{qubits}b')

  # Apply gates based on the bits of the target 'number'
  for idx, bit in enumerate(number_bin):
    if bit == '0':
      circuit.x(idx)

  circuit.mcx(list(range(qubits)), qubits)

  for idx, bit in enumerate(number_bin):
    if bit == '0':
      circuit.x(idx)

  return circuit.to_gate()

def oracle_interval(lower_number: int, higher_number: int, qubits: int):
  """
  Constructs an oracle that stores information in an ancilla about whether or 
  not a value is inside the range [lower_number, higher_number). It is hermitian,
  so the adjoint is effectively the same operator.

  Args:
      lower_number (int): The lower integer value included in the interval.
      higher_number (int): The higher boundary of the interval.
      qubits (int): The total number of qubits in the oracle register, without
                    considering the ancilla.

  Returns:
      Gate: The Qiskit QuantumCircuit of the oracle "greater (or equal) than 
            lower_number and less than higher_number"
            converted to a Gate object for it to be appended.
  """
  circuit = QuantumCircuit(qubits+1,
                           name=f'Oracle\n x∈[{lower_number},{higher_number})')

  # Reusing the less-than oracle and greater (or equal) than oracle
  gate_qubits = list(range(qubits + 1))
  circuit.append(oracle_less(higher_number, qubits), gate_qubits)
  circuit.append(oracle_greatereq(lower_number, qubits), gate_qubits)

  # Invert the ancilla value to effectively mark the states
  # for the interval instance
  circuit.x(qubits)

  return circuit.to_gate()
