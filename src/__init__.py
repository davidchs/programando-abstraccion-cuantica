"""
Quantum SMT Solver Core API.
Expone las funciones de inicialización, oráculos y abstracciones lógicas.
"""

# Importaciones relativas desde los submódulos internos
from .oracle_builder import oracle_less, oracle_eq, oracle_greatereq, oracle_interval
from .abstractions import PhaseAND, PhaseNAND, PhaseOR, PhaseNOR
from .grover_components import diffuser, ghz_init

# Definición estricta de la API pública
__all__ = [
    "oracle_less",
    "oracle_eq",
    "oracle_greatereq",
    "oracle_interval",
    "PhaseAND",
    "PhaseNAND",
    "PhaseOR",
    "PhaseNOR",
    "diffuser",
    "ghz_init",
]