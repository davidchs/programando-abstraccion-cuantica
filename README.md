# Programando la abstracción cuántica con regsitros como unidad de información
## Resolutor SMT cuántico basado en abstracciones

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Qiskit Version](https://img.shields.io/badge/qiskit-2.x-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

### Descripción General

Este repositorio contiene la implementación y el entorno de experimentación de un solver cuántico para el problema de Satisfacibilidad Booleana (SAT). El código explora arquitecturas de circuitos cuánticos optimizados, abstracciones lógicas (oráculos y difusores) y algoritmos de amplificación de amplitud (Grover) para la evaluación eficiente de cláusulas proposicionales complejas.

## Fundamento Teórico y Funcionamiento

Este proyecto implementa una arquitectura cuántica escalable de múltiples registros para resolver problemas de Satisfacibilidad Módulo Teorías (SMT) utilizando el algoritmo de Grover. El diseño adopta un enfoque análogo al propuesto por Lin et al. (2023). En lugar de agrupar la evaluación de todas las condiciones en un único registro representativo, la evaluación se distribuye en registros independientes que actúan como unidades de información modulares.

La codificación se establece mediante la inicialización de una variable en cada registro, o bien mediante su sincronización cuando abarca múltiples registros. La evaluación de cada cláusula se efectúa sobre el qubit ancilla, componiendo así la fórmula completa. De este modo, la aplicación de operadores de alto nivel como `PhaseAND` y `PhaseOR` marca con una fase de π los estados cuánticos que satisfacen la relación lógica (conjunción o disyunción).

El resolutor está implementado sobre el framework Qiskit (v2.3.1). Si bien Qiskit exige tradicionalmente un paradigma de programación de bajo nivel (puerta a puerta), este repositorio demuestra el potencial de la modularidad: los componentes del resolutor están encapsulados en módulos aislados que permiten operar con abstracciones lógicas mayores (`PhaseAND`, `PhaseOR`, `PhaseNAND`, `PhaseNOR`). No obstante, se reconoce como limitación metodológica que la construcción inicial obligatoria de estas estructuras desde un nivel tan bajo hace que este tipo de lenguajes presente desafíos de escalabilidad para sistemas masivos.

## Instalación y Uso

Para garantizar la reproducibilidad de los experimentos, el código fuente está empaquetado para ejecutarse en un entorno virtual aislado en modo editable.

1. **Clonación del repositorio:**
   ```bash
   git clone [https://github.com/davidchs/programando-abstraccion-cuantica.git](https://github.com/davidchs/programando-abstraccion-cuantica.git)
   cd quantum-smt-solver
   ```

2. **Creación de un entrono virtual (Linux/MacOS):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .\.venv\Scripts\Activate.ps1
    ```

3. **Instalación de dependencias y despliegue del paquete local:**
    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

## Licencia

Este proyecto se distribuye de forma abierta bajo la licencia MIT.

## Refrencias

Lin, S. W., Wang, T. F., Chen, Y. R., Hou, Z., Sanán, D., & Teo, Y. S. (2023). A parallel and distributed quantum SAT solver based on entanglement and quantum teleportation. arXiv preprint arXiv:2308.03344. [https://doi.org/10.48550/arXiv.2308.03344](https://doi.org/10.48550/arXiv.2308.03344)

Qiskit Development Team. (2026). Qiskit: An open-source framework for quantum computing (Version 2.3.1). [https://github.com/Qiskit/qiskit](https://github.com/Qiskit/qiskit)