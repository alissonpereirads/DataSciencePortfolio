# Projeto de Machine Learning: Previsão de Custos de Plano de Saúde

![Streamlit App Screenshot][URL_DA_SUA_SCREENSHOT](https://raw.githubusercontent.com/alissonpereirads/DataSciencePortfolio/refs/heads/main/OtimizacaoPlanoSaude/calculdora_saude.jpg)
*Interface do Web App interativo desenvolvido com Streamlit para previsão de custos.*

## Visão Geral

Este projeto utiliza técnicas de Ciência de Dados e Machine Learning para analisar e prever os custos individuais de planos de saúde para colaboradores de uma empresa do ramo alimentício. O objetivo é identificar os principais fatores que influenciam esses custos e desenvolver um modelo preditivo robusto, culminando em um web app interativo para estimativas em tempo real.

## Contexto e Problema de Negócio

Uma grande empresa brasileira do ramo alimentício (> 20.000 colaboradores) observou um aumento significativo nos custos do plano de saúde ao longo dos anos. A gerência de Benefícios e Bem-Estar suspeitava que fatores como tabagismo e obesidade (IMC) poderiam ser os principais responsáveis, mas carecia de uma análise baseada em dados. Para investigar, foi realizada uma pesquisa com 1.338 colaboradores aleatórios, coletando dados demográficos, de hábitos e de saúde.

O desafio central é transformar esses dados brutos em insights acionáveis e em uma ferramenta preditiva para auxiliar a empresa a entender e, potencialmente, gerenciar melhor esses custos.

## Objetivos do Projeto

1. **Análise Exploratória de Dados (EDA):** Investigar profundamente os dados para identificar padrões, relações e os principais fatores que influenciam o `Custo_Saude`.
2. **Desenvolvimento de Modelo Preditivo:** Construir e avaliar diferentes modelos de Machine Learning (Regressão) para prever o custo individual do plano de saúde com base nas características do colaborador.
3. **Interpretação do Modelo:** Identificar quais fatores o modelo considera mais importantes para suas previsões.
4. **Deployment Interativo:** Criar um web application simples (usando Streamlit) que permita aos usuários inserir dados e obter uma estimativa de custo do plano de saúde baseada no modelo treinado.

## Fonte dos Dados

Os dados utilizados foram provenientes da pesquisa interna simulada, fornecida como um arquivo Excel (`base_plano_de_saude.xlsx`). As features incluem:

* `Idade`: Idade do colaborador (numérica).
* `Sexo`: Gênero do colaborador (categórica: Masculino/Feminino).
* `IMC`: Índice de Massa Corpórea (numérica).
* `Qte_Filhos`: Quantidade de filhos/dependentes (numérica).
* `Fumante`: Se o colaborador é fumante (categórica: Sim/Não).
* `Região`: Região do Brasil onde o colaborador reside/trabalha (categórica).
* `Custo_Saude`: Custo individual do plano de saúde (variável alvo, numérica).

## Metodologia e Pipeline

O projeto seguiu as etapas padrão de um pipeline de Ciência de Dados:

1. **Carregamento e Preparação Inicial:** Leitura dos dados, verificação inicial de tipos, valores ausentes e duplicados.
2. **Análise Exploratória de Dados (EDA):**
   * Utilização de uma abordagem narrativa ("storytelling") para guiar a exploração.
   * Análise da distribuição da variável alvo (`Custo_Saude`).
   * Investigação das relações bivariadas entre cada feature e a variável alvo, usando `Box Plots` e `Scatter Plots` (Plotly).
   * Análise de correlação entre variáveis numéricas (`Heatmap`).
   * Identificação de interações chave (principalmente com a variável `Fumante`).
3. **Pré-processamento:**
   * Separação dos dados em conjuntos de treino e teste (`train_test_split`).
   * Aplicação de `OneHotEncoder` para variáveis categóricas.
   * Aplicação de `StandardScaler` para variáveis numéricas.
   * Uso de `ColumnTransformer` para organizar o pré-processamento.
4. **Seleção e Treinamento de Modelos:**
   * Avaliação de múltiplos algoritmos de regressão (Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting).
   * Uso de `K-Fold Cross-Validation` (K=10) no conjunto de treino para avaliação robusta do desempenho.
   * Seleção do `Gradient Boosting Regressor` como modelo final com base nas métricas da validação cruzada (R², MAE, RMSE).
   * Treinamento do modelo final no conjunto completo de treino.
5. **Avaliação Final:**
   * Avaliação do modelo treinado no conjunto de teste (dados não vistos).
   * Cálculo das métricas finais (R², MAE, RMSE).
   * Análise visual dos resultados (Real vs. Predito, Análise de Resíduos).
6. **Interpretação:**
   * Análise da importância das features (`feature_importances_`) do modelo Gradient Boosting para entender os drivers da previsão.
7. **Deployment:**
   * Salvamento do modelo treinado e do pré-processador usando `joblib`.
   * Desenvolvimento de um web app interativo com `Streamlit` para realizar previsões com base em inputs do usuário.

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas Principais:**
  * Pandas: Manipulação e análise de dados.
  * NumPy: Computação numérica.
  * Scikit-learn: Pré-processamento, modelagem de Machine Learning, avaliação.
  * Plotly & Seaborn/Matplotlib: Visualização de dados.
  * Streamlit: Criação do web application interativo.
  * Joblib: Salvamento/carregamento de objetos Python (modelo e pré-processador).
* **Ambiente:** Jupyter Notebook (para desenvolvimento e análise) e VS Code (para o script Streamlit).

## Principais Resultados e Achados

* O modelo `Gradient Boosting Regressor` final alcançou um excelente desempenho no conjunto de teste:
  * **R²:** ~0.90 (explicando aproximadamente 90% da variância nos custos).
  * **MAE:** ~R$ 253.50 (erro médio absoluto das previsões).
  * **RMSE:** ~R$ 427.21
* A análise de importância das features confirmou os insights da EDA:
  * **Status de Fumante** é, de longe, o fator mais impactante nos custos.
  * **IMC** e **Idade** são os próximos fatores mais relevantes.
  * **Região** também demonstrou ter alguma influência.
* O modelo desenvolvido fornece uma ferramenta valiosa para a empresa estimar custos e entender os fatores de risco associados.

## Web Application (Streamlit)

Um aplicativo web interativo foi desenvolvido para permitir a previsão de custos de forma simples:

* **Funcionalidade:** O usuário insere os dados de um colaborador (idade, sexo, IMC, etc.) através de campos na interface.
* **Previsão:** Ao clicar no botão "Calcular Custo Estimado", o app utiliza o modelo treinado e o pré-processador salvos para gerar e exibir a estimativa de custo.

**Como Executar o App Localmente:**

1. Clone este repositório: `git clone [URL do repositório]`
2. Navegue até a pasta do projeto: `cd [Nome da pasta do projeto]`
3. Crie um ambiente virtual: `python -m venv .venv`
4. Ative o ambiente virtual:
   * Windows: `.\.venv\Scripts\activate`
   * macOS/Linux: `source .venv/bin/activate`
5. Instale as dependências: `pip install -r requirements.txt`
6. Execute o aplicativo Streamlit: `streamlit run app.py`
7. Acesse o app no seu navegador no endereço fornecido (geralmente `http://localhost:8501`).



## Autor

* **Alisson Pereira**
* **LinkedIn:** [Alisson Pereira](https://www.linkedin.com/in/alisson-pereira-ds/)
* **GitHub:** [alissonpereirads](https://github.com/alissonpereirads)

---

*Este projeto foi desenvolvido para fins educacionais e de portfólio, demonstrando a aplicação de técnicas de Ciência de Dados em um problema de negócio simulado.*
