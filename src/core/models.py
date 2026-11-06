from dataclasses import dataclass

@dataclass(frozen=True)
class DiseaseModel:
    """
    Encapsula as propriedades biológicas da doença simulada.
    Utiliza dataclass frozen para garantir a imutabilidade durante a simulação.
    
    Attributes:
        incubation_period (int): Tempo (em ciclos/dias) que a doença leva do estado Exposto para Infeccioso.
        infectious_period (int): Tempo (em ciclos/dias) que a planta permanece infecciosa antes de se recuperar/morrer.
        base_transmission_rate (float): Probabilidade base (0.0 a 1.0) da doença ser transmitida para um vizinho.
    """
    incubation_period: int
    infectious_period: int
    base_transmission_rate: float