# Gêmeo Digital Epidemiológico para Doenças Agrícolas

Um sistema integrado de Inteligência Artificial Geoespacial (GeoIA) e modelagem matemática, projetado para simular a propagação espacial e temporal de patógenos agrícolas em cenários reais.

O projeto tem como estudo de caso a **Ferrugem Asiática da Soja** (*Phakopsora pachyrhizi*). O objetivo do sistema é transcender a detecção estática de doenças, criando um "Gêmeo Digital" da lavoura que ingere imagens de satélite, identifica focos iniciais de infecção via Machine Learning e simula a dispersão futura da doença utilizando tensores meteorológicos (como direção e velocidade do vento).

## O Problema e a Proposta de Valor

A abordagem tradicional de monitoramento agrícola depende da identificação visual de sintomas ou da classificação estática de imagens. Quando uma doença como a ferrugem asiática se torna detectável em larga escala, o dano econômico já está consolidado.

Este projeto propõe uma mudança de paradigma da **análise descritiva** para a **análise preditiva e prescritiva**. Através da combinação de sensoriamento remoto e dinâmica de fluidos/propagação, o sistema não apenas responde "onde a doença está hoje", mas projeta "como ela se espalhará nos próximos 14 dias", permitindo intervenções agronômicas cirúrgicas e otimização do uso de defensivos.

## Arquitetura do Sistema (Data Pipeline & Modular Core)

O software foi desenhado utilizando princípios de *Separation of Concerns* (SoC), garantindo que a ingestão de dados geoespaciais, a inferência do modelo de IA e o motor matemático de simulação operem de forma desacoplada e escalável.

O sistema é dividido em quatro camadas lógicas (Pipelines):

### 1. Camada de Ingestão e Processamento Geoespacial
Responsável por traduzir o mundo físico para o ambiente computacional.
* **Processamento de Imagens:** Ingestão de arquivos GeoTIFF (ex: Sentinel-2) para extração de bandas multiespectrais e cálculo de índices vegetativos (NDVI, NDRE).
* **Mapeamento de Restrições:** Geração de matrizes booleanas (Máscaras de Plantio) para garantir que a simulação ocorra estritamente sobre áreas de cultivo, respeitando barreiras físicas naturais (estradas, rios).

### 2. Camada de Inteligência Artificial (Visão Computacional)
Atua como o "Diagnóstico Inicial" do sistema.
* Utiliza modelos de Machine Learning (Baseline: Random Forest / Avançado: Redes Neurais Convolucionais para segmentação) para mapear anomalias espectrais.
* **Output:** Gera um mapa geo-referenciado de probabilidade de infecção, estabelecendo o "Paciente Zero" e as condições iniciais (sementes) para o motor de simulação.

### 3. Camada de Simulação Epidemiológica (O Motor Matemático)
O núcleo de alta performance do sistema, fundamentado em dinâmica SEIR (Suscetível, Exposto, Infeccioso, Recuperado) adaptada para matrizes espaciais.
* **Processamento Vetorizado:** Utiliza NumPy para computar transições de estado celular através de convoluções locais.
* **Tensores Meteorológicos:** A matriz de propagação não é isotrópica (perfeitamente circular). O motor aplica Kernels Direcionais baseados em dados de vento, gerando plumas de dispersão assimétricas que mimetizam a biologia real da dispersão de esporos.

### 4. Camada de Apresentação e Suporte à Decisão
Isola a renderização visual da lógica de negócios.
* Projeta as matrizes de simulação de volta para o sistema de coordenadas geográficas originais, gerando **Mapas de Risco Futuro** que podem ser consumidos por sistemas GIS corporativos ou visualizados localmente (via Matplotlib/GeoPandas).

## Stack Tecnológico

A infraestrutura foi selecionada visando manipulação eficiente de tensores e dados geoespaciais:

* **Linguagem:** Python 3.10+
* **Core Matemático:** NumPy (Processamento de tensores e máscaras de alta performance).
* **Geoespacial:** Rasterio e GeoPandas (Manipulação de CRS e arquivos GeoTIFF).
* **Machine Learning:** Scikit-Learn e PyTorch (Em desenvolvimento).
* **Renderização:** Matplotlib.
* **Qualidade de Software:** Pytest (Garantia de determinismo matemático das matrizes de transição).

## Instalação e Reprodutibilidade

O projeto utiliza gerenciamento estrito de dependências para garantir a reprodutibilidade dos ambientes de Ciência de Dados e Simulação.

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/simulador-epidemiologico.git
cd simulador-epidemiologico
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. Instale as dependências da aplicação:
```bash
pip install -r requirements.txt
```

4. Execute o motor de simulação base (Proof of Concept):
```bash
python main.py
```

## Estado Atual e Evolução

O projeto encontra-se na fase de **Consolidação do Motor Matemático**. A atual *Proof of Concept* (PoC) implementa a dinâmica espacial SEIR com processamento vetorizado puro, rodando sobre matrizes sintéticas para homologação da lógica de contágio e vizinhança.

As próximas etapas de engenharia focarão na implementação dos pipelines de dados detalhados na Arquitetura (Integração de GeoTIFF via Rasterio e acoplamento dos tensores de vento).