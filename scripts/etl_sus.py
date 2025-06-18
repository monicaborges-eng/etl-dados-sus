import pandas as pd
import os

# URL de dados do SUS (CNES - estabelecimentos)
url = "https://dados.gov.br/dataset/ce273ba6-eeb0-4b11-970c-01f9a9ff95b0/resource/f18b3b0c-d19c-4460-bc62-e68239aa43c3/download/stab202403.csv"

# 1. Extração
print("🔽 Baixando dados...")
df_raw = pd.read_csv(url, sep=';', encoding='latin1', low_memory=False)
os.makedirs("data", exist_ok=True)
df_raw.to_csv("data/estabelecimentos_raw.csv", index=False)
print("✅ Dados brutos salvos.")

# 2. Transformação
print("🧹 Filtrando dados de saúde ocupacional...")
df_filtrado = df_raw[df_raw["NOMEFANTASIA"].str.contains("trabalho", case=False, na=False)]
df_filtrado.to_csv("data/estabelecimentos_tratado.csv", index=False)
print("✅ Dados tratados salvos.")
