from __future__ import annotations

import streamlit as st

from src.risk_engine import ValidationError, predict_complete_risk, predict_quick_screening

st.set_page_config(page_title="CardioSM | Estratificação de Risco", page_icon="♥", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
  .block-container {max-width: 1120px; padding-top: 1.4rem; padding-bottom: 2rem;}
  .hero {padding: 1.3rem 1.45rem; border-radius: 18px; color: #fff; background: linear-gradient(115deg,#0b5269,#126d78); margin-bottom: 1rem;}
  .hero h1 {font-size: clamp(1.5rem, 4vw, 2.25rem); margin: 0 0 .3rem;}.hero p{margin:0; opacity:.95}
  .notice {border-left: 4px solid #e6a700; background:#fff8df; padding:.8rem 1rem; border-radius:8px; color:#584300; margin:.6rem 0 1rem;}
  .result {padding:1rem 1.2rem;border-radius:14px;margin:.8rem 0;}.low{background:#e8f6ee;border-left:6px solid #12834e}.moderate{background:#fff5d7;border-left:6px solid #d58b00}.high{background:#fde8e8;border-left:6px solid #c62d2d}
  @media (max-width: 640px) {.block-container {padding-left: .8rem; padding-right: .8rem;}.hero {padding:1rem}.stButton>button {min-height: 48px; font-size: 1rem; width:100%;}}
</style>
<div class="hero"><h1>CardioSM</h1><p>Estratificação de risco cardiovascular com biomarcadores da síndrome metabólica.</p></div>
""", unsafe_allow_html=True)

quick = st.toggle("Ativar Modo Triagem Rápida (Apenas 3 marcadores)", value=False, help="Idade/sexo, pressão arterial sistólica e circunferência abdominal.")
if quick:
    st.markdown('<div class="notice"><strong>Aviso:</strong> Este é um score de triagem inicial rápida para atenção primária. Não substitui o diagnóstico laboratorial completo.</div>', unsafe_allow_html=True)
    st.caption("Modelo: Triagem CV-3 (nome provisório). O índice exibido só terá validade clínica após treinamento e validação externa.")
else:
    st.caption("Modo laboratorial: ERG de Framingham + biomarcadores da síndrome metabólica.")

with st.form("risk_form", clear_on_submit=False):
    st.subheader("Dados do paciente")
    col1, col2, col3 = st.columns(3)
    with col1:
        idade = st.number_input("Idade (anos)", min_value=18, max_value=120, value=45, step=1)
    with col2:
        sexo_ui = st.selectbox("Sexo", ["Feminino", "Masculino"])
    with col3:
        pas = st.number_input("Pressão arterial sistólica - PAS (mmHg)", min_value=70, max_value=250, value=120, step=1)
    cintura = st.number_input("Circunferência abdominal (cm)", min_value=40.0, max_value=200.0, value=90.0, step=0.5)

    data = {"idade": idade, "sexo": "masculino" if sexo_ui == "Masculino" else "feminino", "pas": pas, "circunferencia_abdominal": cintura}
    if not quick:
        st.subheader("Dados laboratoriais e clínicos")
        a, b, c = st.columns(3)
        with a:
            data["triglicerideos"] = st.number_input("Triglicerídeos (mg/dL)", 1.0, 1000.0, 150.0, 1.0)
            data["glicemia_jejum"] = st.number_input("Glicemia de jejum (mg/dL)", 1.0, 1000.0, 95.0, 1.0)
        with b:
            data["hdl"] = st.number_input("Colesterol HDL (mg/dL)", 10.0, 150.0, 50.0, 1.0)
            data["colesterol_total"] = st.number_input("Colesterol total (mg/dL)", 70.0, 500.0, 190.0, 1.0)
        with c:
            data["ldl"] = st.number_input("Colesterol LDL (mg/dL)", 1.0, 1000.0, 110.0, 1.0)
            data["tabagismo"] = st.toggle("Tabagismo atual", value=False)
        x, y = st.columns(2)
        with x:
            data["anti_hipertensivo"] = st.toggle("Usa medicação anti-hipertensiva", value=False)
        with y:
            data["diabetes"] = st.toggle("Diabetes diagnosticado", value=False)
    submitted = st.form_submit_button("Calcular estratificação", type="primary")

if submitted:
    try:
        result = predict_quick_screening(data) if quick else predict_complete_risk(data)
        style = {"Baixo": "low", "Moderado": "moderate", "Alto": "high"}[result.risk_label]
        main_value = f"{result.screening_index:.1f}/100" if quick else f"{result.probability:.1f}%"
        metric_name = "Índice de triagem" if quick else "Risco estimado pelo modelo"
        framingham = "" if quick else f"<p><strong>ERG de Framingham (10 anos):</strong> {result.framingham_probability:.1f}%</p>"
        st.markdown(f'<div class="result {style}"><h2>{result.risk_label} risco</h2><p><strong>{metric_name}:</strong> {main_value}</p>{framingham}<p><strong>Recomendação:</strong> {result.recommendation}</p></div>', unsafe_allow_html=True)
        st.caption(f"Fonte do cálculo: {result.model_source}.")
        st.warning("Ferramenta educacional/protótipo. Não usar isoladamente para diagnóstico, prescrição ou decisão de urgência. Em sintomas agudos, siga o fluxo de emergência local.")
    except ValidationError as exc:
        st.error(str(exc))
