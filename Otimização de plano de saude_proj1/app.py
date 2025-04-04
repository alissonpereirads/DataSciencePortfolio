# app.py - Aplicativo Streamlit para Previsão de Custo de Saúde

import streamlit as st
import pandas as pd
import joblib
import numpy as np  # Necessário se o pré-processador/modelo o utilizarem implicitamente

# --- Carregar Modelo e Pré-processador ---
# É crucial que os arquivos .joblib estejam na mesma pasta que este script app.py
model_filename = "modelo_custo_saude.joblib"
preprocessor_filename = "preprocessor_custo_saude.joblib"

try:
    model = joblib.load(model_filename)
    preprocessor = joblib.load(preprocessor_filename)
    print(
        "Modelo e pré-processador carregados com sucesso."
    )  # Mensagem para o console onde Streamlit roda
except FileNotFoundError:
    st.error(
        f"Erro: Arquivos '{model_filename}' ou '{preprocessor_filename}' não encontrados."
    )
    st.stop()  # Interrompe a execução se os arquivos não forem encontrados
except Exception as e:
    st.error(f"Erro ao carregar modelo ou pré-processador: {e}")
    st.stop()


# --- Interface do Usuário ---
st.set_page_config(page_title="Previsor de Custos de Saúde", layout="centered")
st.title("Calculadora de Custo Estimado do Plano de Saúde 🩺")
st.markdown(
    "Insira as informações do colaborador para estimar o custo anual do plano de saúde."
)

# Criar colunas para melhor layout (opcional)
col1, col2 = st.columns(2)

with col1:
    idade = st.number_input("Idade", min_value=18, max_value=100, value=30, step=1)
    imc = st.number_input(
        "IMC (Índice de Massa Corpórea)",
        min_value=10.0,
        max_value=60.0,
        value=25.0,
        step=0.1,
        format="%.1f",
    )
    sexo = st.selectbox(
        "Sexo", options=["Masculino", "Feminino"]
    )  # Ordem/nomes devem bater com o treino

with col2:
    qte_filhos = st.number_input(
        "Quantidade de Filhos", min_value=0, max_value=10, value=0, step=1
    )
    fumante = st.selectbox(
        "Fumante?", options=["Não", "Sim"]
    )  # Ordem/nomes devem bater com o treino
    # As regiões devem ser exatamente as mesmas que estavam nos dados de treino
    regiao = st.selectbox(
        "Região", options=["Sudeste", "Centro", "Norte", "Sul"]
    )  # Ajuste as opções se necessário

# Botão para fazer a predição
if st.button("Calcular Custo Estimado", type="primary"):

    # --- Preparar Dados para Predição ---
    # 1. Criar DataFrame com os inputs do usuário
    #    As chaves (nomes das colunas) DEVEM ser idênticas às usadas no TREINO do pré-processador
    input_data = pd.DataFrame(
        {
            "Idade": [idade],
            "Sexo": [sexo],
            "IMC": [imc],
            "Qte_Filhos": [qte_filhos],
            "Fumante": [fumante],
            "Região": [regiao],
        }
    )

    st.markdown("---")  # Linha divisória
    st.subheader("Dados Inseridos:")
    st.dataframe(input_data, use_container_width=True)

    try:
        # 2. Aplicar o pré-processador aos dados de input
        input_processed = preprocessor.transform(input_data)
        print("Dados de input processados:", input_processed)  # Log no console

        # 3. Fazer a predição com o modelo carregado
        prediction = model.predict(input_processed)
        print("Predição bruta:", prediction)  # Log no console

        # Extrair o valor da predição (geralmente vem num array)
        predicted_cost = prediction[0]

        # --- Exibir Resultado ---
        st.subheader("Resultado da Estimativa:")
        # Usando st.metric para um visual legal
        st.metric(
            label="Custo Anual Estimado",
            value=f"R$ {predicted_cost:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", "."),
        )
        # Formatação acima tenta colocar em padrão brasileiro R$ XX.XXX,XX

        # Adicionar um pequeno disclaimer
        st.caption(
            "Nota: Esta é uma estimativa baseada em um modelo de Machine Learning e dados históricos. Custos reais podem variar."
        )

    except Exception as e:
        st.error(f"Erro durante o pré-processamento ou predição: {e}")
        # Imprimir detalhes do erro no console também pode ajudar a depurar
        print(f"Erro detalhado: {e}")
