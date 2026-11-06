from enum import Enum

class DiseaseState(Enum):
    """
    Representa os estados epidemiológicos possíveis de uma célula no grid
    baseado no modelo SEIR (Susceptible, Exposed, Infectious, Recovered).
    Os valores numéricos garantem compatibilidade com as operações matriciais do NumPy.
    """
    SUSCEPTIBLE = 0
    EXPOSED = 1
    INFECTIOUS = 2
    RECOVERED = 3