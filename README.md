# Programando la abstracción cuántica con registros como unidad de información
## Resolutor SMT cuántico basado en abstracciones lógicas

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Qiskit Version](https://img.shields.io/badge/qiskit-2.x-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

### Descripción General

Hemos instanciado un resolutor *SMT* (problemas de teoría de satisfacibilidad módulo, por sus siglas en inglés) aplicando las abstracciones lógicas (**`PhaseAND`**, **`PhaseOR`** y sus negaciones) presentadas en el artículo. Para su implementación se utiliza Qiskit (v2.3.1), especificado en el documento **`requirements.txt`**. Este diseño demuestra el potencial y el tipo de operaciones complejas que se pueden crear de forma modular estructurando el código con estas abstracciones. 

## Fundamento Teórico y Funcionamiento

Este proyecto implementa una arquitectura cuántica escalable de múltiples registros para resolver problemas *SMT* utilizando el algoritmo de Grover. El diseño adopta un enfoque análogo al propuesto por Lin et al. (2023). En lugar de agrupar la evaluación de todas las condiciones en un único registro representativo, la evaluación se distribuye en registros independientes que actúan como unidades de información modulares.

La codificación se establece mediante la inicialización de una variable en cada registro, o bien mediante su sincronización cuando abarca múltiples registros. La evaluación de cada cláusula se efectúa sobre el qubit ancilla, componiendo así la fórmula completa. Estas cláusulas se establecen siguiendo la consideración de tratar a las variables empquetadas en los registros como enteros, recurriendo a la teoría de aritmética modular. Para establecer los predicados, se generan oráculos que establecen reglas aritméticas modulares para enteros según la estrategia propuesta por Sanchez-Rivero et al. (2025).  De este modo, la aplicación de operadores de alto nivel como **`PhaseAND`** y **`PhaseOR`** marca con una fase *π* los estados cuánticos que satisfagan la relación lógica (conjunción o disyunción, respectivamente).

El resolutor está implementado sobre el framework Qiskit (v2.3.1). Si bien Qiskit exige tradicionalmente un paradigma de programación de bajo nivel (puerta a puerta), este repositorio demuestra el potencial de la modularidad: los componentes del resolutor están encapsulados en módulos aislados que permiten operar con abstracciones lógicas mayores y los diferentes componentes del algoritmo. No obstante, se reconoce como limitación la construcción inicial obligatoria de estas estructuras a un bajo nivel. Esto hace que este tipo de lenguajes no sea el más adecuado para trabajar de forma nativa con estas abstracciones.

## Contenidos del Repositorio

El proyecto está organizado en diferentes módulos:

* **Directorio `src/`:** Contiene los componentes modulares del resolutor SMT empaquetada como una librería de Python. Incluye:
  * Las abstracciones lógicas de alto nivel (`PhaseAND`, `PhaseOR`, etc.).
  * Los operadores de amplificación de amplitud de Grover y preparación de estados.
  * Los constructores para oráculos de desigualdades e intervalos.
* **Directorio `notebooks/`:** Contiene el entorno interactivo (Jupyter Notebook) donde se instancian los circuitos, se configuran los parámetros del problema SMT y se analizan los resultados.
* **Archivo `pyproject.toml`:** Archivo de configuración de empaquetamiento, permitiendo importaciones globales y limpias desde cualquier parte del proyecto.
* **Archivo `requirements.txt`:** Dependencias externas que fijan las versiones.
* **Archivos de Infraestructura (`.gitignore` y `.gitattributes`):** Políticas de control internas.

## Instalación y Uso

Para garantizar la reproducibilidad de los experimentos, el código fuente está empaquetado para ejecutarse en un entorno virtual aislado.

Ejecute los siguientes comandos en la terminal de su sistema:

1. **Clonación del repositorio:**
   ```bash
   git clone [https://github.com/davidchs/programando-abstraccion-cuantica.git](https://github.com/davidchs/programando-abstraccion-cuantica.git)
   cd programando-abstraccion-cuantica
   ```

2. **Creación de un entrono virtual (Linux/macOS):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .\.venv\Scripts\Activate.ps1
    ```

3. **Instalación de dependencias y despliegue del paquete local:**
    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

Una vez configurado el entorno, todo el código base contenido en la carpeta `src/` estará disponible para ser invocado desde cualquier cuaderno en la carpeta `notebooks/`. Asegúrese de seleccionar el kernel `.venv` en su editor.

## Licencia

Este proyecto se distribuye de forma abierta bajo la licencia MIT.

## Referencias

> Qiskit Development Team. (2026). Qiskit: An open-source framework for quantum computing (Version 2.3.1). [https://github.com/Qiskit/qiskit](https://github.com/Qiskit/qiskit)

> Lin, S. W., Wang, T. F., Chen, Y. R., Hou, Z., Sanán, D., & Teo, Y. S. (2023). A parallel and distributed quantum SAT solver based on entanglement and quantum teleportation. arXiv preprint arXiv:2308.03344. [https://doi.org/10.48550/arXiv.2308.03344](https://doi.org/10.48550/arXiv.2308.03344)

> Sanchez-Rivero, J., Talaván, D., Garcia-Alonso, J., Ruiz-Cortés, A., & Murillo, J. M. (2025). Automatic generation of efficient oracles: The less-than case. Journal of Systems and Software, 219, 112203 [https://doi.org/10.1016/j.jss.2024.112203](https://doi.org/10.1016/j.jss.2024.112203)
