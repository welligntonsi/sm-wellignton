from __future__ import annotations

import os
import sys
from typing import Any

import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from src.risk_engine import ValidationError, predict_complete_risk, predict_quick_screening


PAGE_TITLE = "CardioSM | Estratificação de Risco"
PAGE_ICON = "♥"
RISK_STYLE_BY_LABEL = {"Baixo": "low", "Moderado": "moderate", "Alto": "high"}
SAFETY_WARNING = (
    "Ferramenta educacional/protótipo. Não usar isoladamente para diagnóstico, "
    "prescrição ou decisão de urgência. Em sintomas agudos, siga o fluxo de emergência local."
)


def configure_page() -> None:
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def render_header() -> None:
    st.markdown(
        """
<style>
  .block-container {max-width: 1120px; padding-top: 1.4rem; padding-bottom: 2rem;}
  .hero {padding: 1.3rem 1.45rem; border-radius: 18px; color: #fff; background: linear-gradient(115deg,#0b5269,#126d78); margin-bottom: 1rem;}
  .hero h1 {font-size: clamp(1.5rem, 4vw, 2.25rem); margin: 0 0 .3rem;}.hero p{margin:0; opacity:.95}
  .notice {border-left: 4px solid #e6a700; background:#fff8df; padding:.8rem 1rem; border-radius:8px; color:#584300; margin:.6rem 0 1rem;}
  .result {padding:1rem 1.2rem;border-radius:14px;margin:.8rem 0;}.low{background:#e8f6ee;border-left:6px solid #12834e}.moderate{background:#fff5d7;border-left:6px solid #d58b00}.high{background:#fde8e8;border-left:6px solid #c62d2d}
  @media (max-width: 640px) {.block-container {padding-left: .8rem; padding-right: .8rem;}.hero {padding:1rem}.stButton>button {min-height: 48px; font-size: 1rem; width:100%;}}
</style>
<div class="hero"><h1>CardioSM</h1><p>Estratificação de risco cardiovascular com biomarcadores da síndrome metabólica.</p></div>
""",
        unsafe_allow_html=True,
    )


def render_mode_notice(quick_mode: bool) -> None:
    if quick_mode:
        st.markdown(
            (
                '<div class="notice"><strong>Aviso:</strong> Este é um score de triagem '
                "inicial rápida para atenção primária. Não substitui o diagnóstico "
                "laboratorial completo.</div>"
            ),
            unsafe_allow_html=True,
        )
        st.caption(
            "Modelo: Triagem CV-3 (nome provisório). O índice exibido só terá validade "
            "clínica após treinamento e validação externa."
        )
        return

    st.caption("Modo laboratorial: ERG de Framingham + biomarcadores da síndrome metabólica.")


def collect_patient_data() -> dict[str, Any]:
    st.subheader("Dados do paciente")
    col1, col2, col3 = st.columns(3)

    with col1:
        idade = st.number_input("Idade (anos)", min_value=18, max_value=120, value=45, step=1)
    with col2:
        sexo_ui = st.selectbox("Sexo", ["Feminino", "Masculino"])
    with col3:
        pas = st.number_input(
            "Pressão arterial sistólica - PAS (mmHg)",
            min_value=70,
            max_value=250,
            value=120,
            step=1,
        )

    cintura = st.number_input(
        "Circunferência abdominal (cm)",
        min_value=40.0,
        max_value=200.0,
        value=90.0,
        step=0.5,
    )

    return {
        "idade": idade,
        "sexo": "masculino" if sexo_ui == "Masculino" else "feminino",
        "pas": pas,
        "circunferencia_abdominal": cintura,
    }


def collect_laboratory_data(data: dict[str, Any]) -> None:
    st.subheader("Dados laboratoriais e clínicos")
    col1, col2, col3 = st.columns(3)

    with col1:
        data["triglicerideos"] = st.number_input("Triglicerídeos (mg/dL)", 1.0, 1000.0, 150.0, 1.0)
        data["glicemia_jejum"] = st.number_input("Glicemia de jejum (mg/dL)", 1.0, 1000.0, 95.0, 1.0)
    with col2:
        data["hdl"] = st.number_input("Colesterol HDL (mg/dL)", 10.0, 150.0, 50.0, 1.0)
        data["colesterol_total"] = st.number_input("Colesterol total (mg/dL)", 70.0, 500.0, 190.0, 1.0)
    with col3:
        data["ldl"] = st.number_input("Colesterol LDL (mg/dL)", 1.0, 1000.0, 110.0, 1.0)
        data["tabagismo"] = st.toggle("Tabagismo atual", value=False)

    col4, col5 = st.columns(2)
    with col4:
        data["anti_hipertensivo"] = st.toggle("Usa medicação anti-hipertensiva", value=False)
    with col5:
        data["diabetes"] = st.toggle("Diabetes diagnosticado", value=False)


def render_result(data: dict[str, Any], quick_mode: bool) -> None:
    result = predict_quick_screening(data) if quick_mode else predict_complete_risk(data)
    style = RISK_STYLE_BY_LABEL[result.risk_label]
    main_value = f"{result.screening_index:.1f}/100" if quick_mode else f"{result.probability:.1f}%"
    metric_name = "Índice de triagem" if quick_mode else "Risco estimado pelo modelo"
    framingham = (
        ""
        if quick_mode
        else f"<p><strong>ERG de Framingham (10 anos):</strong> {result.framingham_probability:.1f}%</p>"
    )

    st.markdown(
        (
            f'<div class="result {style}"><h2>{result.risk_label} risco</h2>'
            f"<p><strong>{metric_name}:</strong> {main_value}</p>"
            f"{framingham}"
            f"<p><strong>Recomendação:</strong> {result.recommendation}</p></div>"
        ),
        unsafe_allow_html=True,
    )
    st.caption(f"Fonte do cálculo: {result.model_source}.")
    st.warning(SAFETY_WARNING)


def main() -> None:
    configure_page()
    render_header()

    quick_mode = st.toggle(
        "Ativar Modo Triagem Rápida (Apenas 3 marcadores)",
        value=False,
        help="Idade/sexo, pressão arterial sistólica e circunferência abdominal.",
    )
    render_mode_notice(quick_mode)

    with st.form("risk_form", clear_on_submit=False):
        data = collect_patient_data()
        if not quick_mode:
            collect_laboratory_data(data)
        submitted = st.form_submit_button("Calcular estratificação", type="primary")

    if submitted:
        try:
            render_result(data, quick_mode)
        except ValidationError as exc:
            st.error(str(exc))


if __name__ == "__main__":
    main()
