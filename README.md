# CardioSM - protótipo de estratificação cardiovascular

Aplicação Streamlit mobile-first para demonstração acadêmica da dissertação. Há dois fluxos:

- **Modo completo (laboratorial):** calcula o Escore de Risco Global (ERG) de Framingham de 10 anos e encaminha os biomarcadores ao modelo completo.
- **Modo Triagem Rápida:** **Triagem CV-3**, com idade/sexo, PAS e circunferência abdominal. É propositalmente separado do modelo laboratorial e não deve ser interpretado como risco de evento em 10 anos antes da validação.

## Requisitos clínicos e segurança

Este repositório é um **MVP educacional**, não um dispositivo médico. Sem arquivos de modelo, o app usa regras de demonstração identificadas na tela. Não use o resultado para diagnóstico, prescrição ou decisão de urgência. A validação deve incluir protocolo aprovado, governança/LGPD, avaliação de viés por subgrupo, calibração, validação externa e supervisão clínica.

O ERG implementado usa a equação de D'Agostino et al. (2008), adequada a adultos de 30 a 74 anos. Para calcular a equação são necessários dois campos adicionais além da lista inicial: uso de anti-hipertensivo e diabetes diagnosticado.

## Como executar no Visual Studio Code

1. Abra esta pasta no Visual Studio Code.
2. No terminal integrado, crie e ative um ambiente virtual:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as bibliotecas e execute:

   ```powershell
   pip install -r requirements.txt
   streamlit run app.py
   ```

O terminal mostrará o endereço local. Abra-o no navegador. Para testar no celular da mesma rede, use o endereço de rede informado pelo Streamlit; não exponha dados reais de pacientes nesse modo.

## Como conectar seus modelos treinados

O código procura, nesta ordem, por `models/full_model.pkl` e `models/quick_model.pkl`. Os artefatos devem ser serializados com `joblib`, suportar `predict_proba` (preferido) ou `predict`, e receber um `pandas.DataFrame` com estas colunas:

| Modelo | Colunas |
| --- | --- |
| Completo | `idade`, `sexo_masculino`, `tabagismo`, `pas`, `anti_hipertensivo`, `diabetes`, `circunferencia_abdominal`, `triglicerideos`, `hdl`, `glicemia_jejum`, `colesterol_total`, `ldl`, `framingham_10a` |
| Triagem CV-3 | `idade`, `sexo_masculino`, `pas`, `circunferencia_abdominal` |

Treine e serialize também o pré-processamento no mesmo `Pipeline` do scikit-learn, para impedir divergência entre treinamento e produção. A dissertação aponta Random Forest como melhor candidato nos cenários analisados; portanto, ele é um excelente primeiro baseline. Compare-o com regressão logística calibrada e gradient boosting/XGBoost, escolhendo pelo desempenho de validação externa, calibração e sensibilidade clínica - não somente acurácia.

## Testes

```powershell
python -m unittest discover -s tests -v
```

## Deploy para a banca

### Streamlit Community Cloud (mais simples)

1. Crie um repositório privado ou público no GitHub e envie estes arquivos (não envie modelos ou dados identificáveis sem autorização).
2. Acesse [share.streamlit.io](https://share.streamlit.io/), conecte o GitHub, selecione o repositório, a branch e `app.py`.
3. Clique em **Deploy**. O serviço instala `requirements.txt` e fornece um link responsivo para a banca.

### Hugging Face Spaces

Crie um Space do tipo **Streamlit**, envie os arquivos e mantenha `app.py` e `requirements.txt` na raiz. É uma boa alternativa para demonstração pública.

### Render

Crie um **Web Service** Python, use `pip install -r requirements.txt` como build command e `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT` como start command. É útil se precisar de controles adicionais, mas o plano gratuito pode hibernar.

Antes de disponibilizar, substitua as regras demonstrativas pelos modelos validados, documente sua versão/métricas/limitações e configure uma política de privacidade. O app não persiste dados de pacientes.
