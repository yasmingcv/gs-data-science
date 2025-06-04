# 🔥 Wildfire Analysis

Este projeto faz parte da disciplina de **Data Science** do curso de **Engenharia de Software** da **FIAP**, desenvolvido no contexto da **Global Solution**. O objetivo principal é realizar uma análise exploratória e visual de dados sobre incêndios florestais nos Estados Unidos, identificando padrões temporais, espaciais e causais.

---

## 📊 Tecnologias e Bibliotecas Utilizadas

- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## 📁 Estrutura do Projeto

- `wildfire_analysis.py`: Script principal contendo todo o pipeline de análise de dados.
- `wildfires.csv`: Arquivo com os dados brutos. O arquivo pode ser baixado [aqui](https://www.kaggle.com/datasets/behroozsohrabi/us-wildfire-records-6th-edition?select=data.csv).
- Gráficos gerados em `.png`:
  - `grafico_incendios_por_ano.png`
  - `grafico_mapa_calor.png`
  - `grafico_top_10_causas.png`
  - `grafico_tamanho_por_classificacao_causa.png`
  - `grafico_incendios_por_mes.png`

---

## ⚙️ Como Executar

1. Clone o repositório:

       git clone https://github.com/yasmingcv/gs-data-science

2. Navegue até a pasta do projeto:

       cd wildfire-analysis

3. Certifique-se de que o arquivo `wildfires.csv` está no mesmo diretório do script.

4. Instale as dependências (de preferência em um ambiente virtual):

       pip install pandas numpy matplotlib seaborn

5. Execute o script:

       python wildfire_analysis.py

---

## 🧠 O que o Projeto Faz

O script realiza as seguintes etapas:

1. **Carregamento dos dados**: Lê o dataset bruto de incêndios florestais.
2. **Limpeza dos dados**: Remove duplicatas, converte datas e trata valores nulos e outliers.
3. **Amostragem**: Seleciona uma amostra aleatória com base em uma SEED definida.
4. **Análise descritiva**: Gera estatísticas e frequências relevantes.
5. **Visualizações**:
   - Linha do tempo de incêndios por ano.
   - Mapa de calor da localização dos incêndios.
   - Gráfico das 10 causas gerais mais frequentes.
   - Boxplot do tamanho dos incêndios por classificação (humana vs natural).
   - Incêndios por mês do ano.

---

## 📈 Exemplos de Insights Gerados

- Quais estados possuem maior ocorrência de incêndios.
- Padrões sazonais (quais meses concentram mais ocorrências).
- Relação entre causa e intensidade do incêndio.
- Áreas geográficas com maior densidade de focos de incêndio.

---

## 📌 Observações

- Os gráficos gerados são salvos automaticamente na pasta do projeto.
- A SEED utilizada é `42`, mas pode ser modificada no código.
- A amostra analisada é de 500.000 registros para otimizar performance.

---

## 👥 Integrantes

- David Murillo de Oliveira Soares (RM 559078)
- Lucas Serrano Rocco (RM 555170)
- Yasmin Gonçalves Coelho (RM 559147)

---

## 🧾 Licença

Este projeto é apenas para fins educacionais.
# gs-data-science
# gs-data-science
