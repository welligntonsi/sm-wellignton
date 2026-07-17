from __future__ import annotations

class ValidationError(Exception):
    """Exceção para dados clínicos inválidos ou fora dos limites."""
    pass

class RiskResult:
    def __init__(self, risk_label: str, recommendation: str, model_source: str, **kwargs):
        self.risk_label = risk_label
        self.recommendation = recommendation
        self.model_source = model_source
        # Atribui dinamicamente os valores adicionais (probability, framingham_probability, etc.)
        for key, value in kwargs.items():
            setattr(self, key, value)

def predict_quick_screening(data: dict) -> RiskResult:
    """Regra demonstrativa para a Triagem Rápida CV-3"""
    idade = data.get("idade", 45)
    pas = data.get("pas", 120)
    cintura = data.get("circunferencia_abdominal", 90)
    
    # Lógica mock/demonstrativa simples baseada nos fatores informados
    score_simulado = (idade * 0.4) + (pas * 0.2) + (cintura * 0.3)
    # Normaliza para uma escala aproximada de 100
    screening_index = min(max(score_simulado - 20, 0), 100)
    
    if screening_index < 40:
        label = "Baixo"
        rec = "Manter hábitos saudáveis e reavaliar anualmente na Atenção Primária."
    elif screening_index < 70:
        label = "Moderado"
        rec = "Acompanhamento clínico regular focado em modificação de estilo de vida."
    else:
        label = "Alto"
        rec = "Encaminhar para avaliação clínica detalhada e monitoramento rigoroso dos fatores de risco."
        
    return RiskResult(
        risk_label=label,
        recommendation=rec,
        model_source="Regras lógicas lineares de demonstração acadêmica (Triagem CV-3)",
        screening_index=screening_index
    )

def predict_complete_risk(data: dict) -> RiskResult:
    """Regra demonstrativa para o Modo Completo (Laboratorial)"""
    # Exemplo simulando os 10 anos de risco baseados em Framingham + Biomarcadores
    idade = data.get("idade", 45)
    diabetes = data.get("diabetes", False)
    tabagismo = data.get("tabagismo", False)
    
    prob_simulada = 5.0
    if idade > 55: prob_simulada += 8.5
    if diabetes: prob_simulada += 12.0
    if tabagismo: prob_simulada += 6.5
    
    prob_simulada = min(prob_simulada, 99.9)
    
    if prob_simulada < 10.0:
        label = "Baixo"
        rec = "Risco cardiovascular estimado baixo a longo prazo. Estimular prevenção primária."
    elif prob_simulada < 20.0:
        label = "Moderado"
        rec = "Risco moderado. Considerar metas terapêuticas lipídicas e controle estrito da PAS."
    else:
        label = "Alto"
        rec = "Risco cardiovascular elevado em 10 anos. Intervenção farmacológica conforme diretrizes."

    return RiskResult(
        risk_label=label,
        recommendation=rec,
        model_source="Equação Base D'Agostino (2008) Simulada + Regras Acadêmicas",
        probability=prob_simulada,
        framingham_probability=prob_simulada * 0.95  # apenas para diferenciar as métricas no mock
    )