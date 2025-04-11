# Análise Preditiva de Turnover de Funcionários com RandomForest

Este projeto aplica um pipeline completo de Ciência de Dados para identificar fatores-chave que levam à saída de colaboradores em uma empresa de tecnologia fictícia e constrói um modelo preditivo como ferramenta de apoio à decisão para o RH.

## Introdução e Motivação

Este projeto representa uma atualização e aprofundamento de uma análise anterior sobre turnover de funcionários, realizada durante meus estudos em Ciência de Dados (atualmente no 3º semestre). O objetivo principal foi aplicar um pipeline completo de Data Science para identificar os principais fatores que levam à saída de colaboradores em uma empresa de tecnologia fictícia e construir um modelo preditivo como ferramenta de apoio à decisão para o RH.

A rotatividade de funcionários é um problema custoso e relevante, e este projeto busca demonstrar a aplicação de técnicas de análise exploratória, pré-processamento, modelagem (RandomForestClassifier), otimização de hiperparâmetros (GridSearchCV com Validação Cruzada) e interpretação de resultados (Feature Importance) para gerar insights acionáveis.

## Dataset

O conjunto de dados utilizado é fictício e representa informações de 1470 funcionários, fornecido pelo RH da empresa. Ele contém 19 variáveis preditoras, incluindo:

* Dados Demográficos (Idade, Gênero, Estado Civil)
* Dados Funcionais (Salário, Tempo de Empresa, Cargo, Chefe)
* Dados de Satisfação e Engajamento (E-Sat, Equilibrio de Vida, Frequência de Viagens)
* Dados Históricos (Qte Empresas Trabalhadas, Promoções)
* A variável alvo: `Funcionário_deixou_a_empresa` (Sim/Não).

## Metodologia e Pipeline

O projeto seguiu as seguintes etapas:

1. **Carregamento e Limpeza Inicial:** Leitura dos dados, verificação de tipos e valores nulos.
2. **Análise Exploratória de Dados (EDA):** Investigação visual e quantitativa da relação entre cada variável e o turnover, utilizando Plotly para gráficos interativos/estáticos. Cálculo de taxas de turnover por grupo e análise de distribuições. Geração de matriz de correlação.
3. **Pré-processamento:**
   * Mapeamento de variáveis binárias ('Sim'/'Não') e ordinais (níveis de satisfação, formação, etc.) para formato numérico.
   * Aplicação de One-Hot Encoding (com `pd.get_dummies`) na variável nominal 'Estado_Civil'.
4. **Divisão Treino/Teste:** Separação dos dados em 75% para treino e 25% para teste, utilizando estratificação (`stratify=y`) para manter a proporção da classe alvo em ambos os conjuntos.
5. **Modelagem e Otimização:**
   * Treinamento de um modelo base `RandomForestClassifier` com `class_weight='balanced'` para lidar inicialmente com o desbalanceamento.
   * Avaliação do modelo base (foco em Acurácia, Matriz de Confusão e Recall da classe minoritária).
   * Otimização de hiperparâmetros (`n_estimators`, `max_depth`, `min_samples_leaf`, `min_samples_split`) utilizando `GridSearchCV` com Validação Cruzada de 5 folds, otimizando para o **Recall** da classe positiva ('Sim, Deixou').
6. **Avaliação Final:** Avaliação do modelo otimizado no conjunto de teste final, analisando as métricas de classificação (Precision, Recall, F1-Score).
7. **Interpretação:** Extração e visualização da importância das features (`feature_importances_`) do modelo otimizado para entender quais fatores foram mais decisivos.

## Principais Achados e Recomendações

* **Fatores de Maior Impacto:** Salário, Idade, Tempo de Carreira/Empresa, Fazer Horas Extras e Distância do Trabalho foram os principais fatores identificados pelo modelo e/ou EDA.
* **Desempenho do Modelo:** O modelo otimizado alcançou um Recall de 24% para identificar funcionários que saíram (melhora significativa em relação aos 10% do modelo base), mas com uma Precision de 45%. Isso indica um trade-off e que o modelo é mais útil como ferramenta de apoio do que para automação completa.
* **Recomendações:** As ações sugeridas para a empresa incluem revisão salarial, gestão da carga de trabalho, foco no engajamento inicial, promoção do equilíbrio vida-trabalho e investigação do impacto da distância.


## Trabalhos Futuros

* Testar outros algoritmos de classificação (LightGBM, XGBoost, Regressão Logística).
* Aplicar técnicas de oversampling/undersampling (ex: SMOTE).
* Realizar engenharia de features mais avançada.
* Aprofundar a análise por segmentos (departamento, cargo).
* Melhorar e implantar o aplicativo Streamlit.

---

## Conclusão

Este projeto demonstrou a aplicação prática de um pipeline completo de Ciência de Dados, desde a coleta e limpeza de dados até a modelagem e interpretação de resultados. Ele ilustra como técnicas avançadas podem ser aplicadas para resolver problemas reais e fornecer insights valiosos para a tomada de decisão em Recursos Humanos.


---
## Contato

Estou em busca de uma oportunidade de estágio na área de Ciência de Dados ou Inteligência Artificial. Se você gostou do meu trabalho ou tem alguma dúvida, sinta-se à vontade para entrar em contato:

- **LinkedIn**: [Alisson Pereira](https://www.linkedin.com/in/alisson-pereira-ds/)
- **E-mail**: alissonpereira.contato@gmail.com
- **GitHub**: [alissonpereirads](https://github.com/alissonpereirads)

---

Feito com ❤️ por [Alisson Pereira] | Estudante de Ciência de Dados e IA

*Este projeto foi desenvolvido para fins educacionais e de portfólio, demonstrando a aplicação de técnicas de Ciência de Dados em um problema de negócio simulado.*
