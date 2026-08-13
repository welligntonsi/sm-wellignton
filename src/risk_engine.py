from __future__ import annotations

from dataclasses import dataclass


QUICK_SCORE_WEIGHTS = {
    "idade": 0.4,
    "pas": 0.2,
    "circunferencia_abdominal": 0.3,
}
QUICK_SCORE_OFFSET = 20
QUICK_LOW_THRESHOLD = 40
QUICK_HIGH_THRESHOLD = 70

COMPLETE_BASE_PROBABILITY = 5.0
COMPLETE_AGE_THRESHOLD = 55
COMPLETE_AGE_INCREMENT = 8.5
COMPLETE_DIABETES_INCREMENT = 12.0
COMPLETE_SMOKING_INCREMENT = 6.5
COMPLETE_LOW_THRESHOLD = 10.0
COMPLETE_HIGH_THRESHOLD = 20.0
MAX_PROBABILITY = 99.9
FRAMINGHAM_DISPLAY_FACTOR = 0.95


class ValidationError(Exception):
    """Exceção para dados clínicos inválidos ou fora dos limites."""


@dataclass
class RiskResult:
    risk_label: str
    recommendation: str
    model_source: str
    probability: float | None = None
    framingham_probability: float | None = None
    screening_index: float | None = None


def _clamp(value: float, min_value: float, max_value: float) -> float:
    return min(max(value, min_value), max_value)


def _quick_recommendation(screening_index: float) -> tuple[str, str]:
    if screening_index < QUICK_LOW_THRESHOLD:
        return "Baixo", "Manter hábitos saudáveis e reavaliar anualmente na Atenção Primária."
    if screening_index < QUICK_HIGH_THRESHOLD:
        return "Moderado", "Acompanhamento clínico regular focado em modificação de estilo de vida."
    return "Alto", "Encaminhar para avaliação clínica detalhada e monitoramento rigoroso dos fatores de risco."


def _complete_recommendation(probability: float) -> tuple[str, str]:
    if probability < COMPLETE_LOW_THRESHOLD:
        return "Baixo", "Risco cardiovascular estimado baixo a longo prazo. Estimular prevenção primária."
    if probability < COMPLETE_HIGH_THRESHOLD:
        return "Moderado", "Risco moderado. Considerar metas terapêuticas lipídicas e controle estrito da PAS."
    return "Alto", "Risco cardiovascular elevado em 10 anos. Intervenção farmacológica conforme diretrizes."


def predict_quick_screening(data: dict) -> RiskResult:
    """Regra demonstrativa para a Triagem Rápida CV-3."""
    idade = data.get("idade", 45)
    pas = data.get("pas", 120)
    cintura = data.get("circunferencia_abdominal", 90)

    # Regra linear de demonstração: preserva o mock atual ate existir modelo validado.
    score_simulado = (
        idade * QUICK_SCORE_WEIGHTS["idade"]
        + pas * QUICK_SCORE_WEIGHTS["pas"]
        + cintura * QUICK_SCORE_WEIGHTS["circunferencia_abdominal"]
    )
    screening_index = _clamp(score_simulado - QUICK_SCORE_OFFSET, 0, 100)
    label, recommendation = _quick_recommendation(screening_index)

    return RiskResult(
        risk_label=label,
        recommendation=recommendation,
        model_source="Regras lógicas lineares de demonstração acadêmica (Triagem CV-3)",
        screening_index=screening_index,
    )


def predict_complete_risk(data: dict) -> RiskResult:
    """Regra demonstrativa para o Modo Completo (Laboratorial)."""
    idade = data.get("idade", 45)
    diabetes = data.get("diabetes", False)
    tabagismo = data.get("tabagismo", False)

    # Esta probabilidade simulada ainda nao substitui a equacao clinica validada.
    probability = COMPLETE_BASE_PROBABILITY
    if idade > COMPLETE_AGE_THRESHOLD:
        probability += COMPLETE_AGE_INCREMENT
    if diabetes:
        probability += COMPLETE_DIABETES_INCREMENT
    if tabagismo:
        probability += COMPLETE_SMOKING_INCREMENT

    probability = min(probability, MAX_PROBABILITY)
    label, recommendation = _complete_recommendation(probability)

    return RiskResult(
        risk_label=label,
        recommendation=recommendation,
        model_source="Equação Base D'Agostino (2008) Simulada + Regras Acadêmicas",
        probability=probability,
        framingham_probability=probability * FRAMINGHAM_DISPLAY_FACTOR,
    )
