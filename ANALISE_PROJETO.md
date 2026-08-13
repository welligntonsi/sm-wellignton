# Analise do Projeto CardioSM

## 1. Visao geral

O projeto e um prototipo educacional em Streamlit para estratificacao de risco cardiovascular. A aplicacao apresenta dois modos de uso:

- **Modo completo/laboratorial**: coleta dados clinicos e laboratoriais e chama `predict_complete_risk`.
- **Modo triagem rapida**: coleta apenas idade, sexo, pressao arterial sistolica e circunferencia abdominal e chama `predict_quick_screening`.

A arquitetura atual e pequena e centralizada. Existem apenas dois arquivos de codigo:

- `app.py`: ponto de entrada da aplicacao, responsavel por interface, coleta de dados, chamada do motor de risco e exibicao do resultado.
- `src/risk_engine.py`: motor de regras demonstrativas, responsavel por retornar a classificacao de risco, recomendacao e metricas exibidas.

O README descreve uma intencao de evolucao para modelos treinados com `joblib`, `pandas` e `scikit-learn`, mas o codigo atual ainda nao implementa carregamento de modelos, pipelines, DataFrames, predicao por modelo serializado ou testes automatizados.

## 2. Estrutura de arquivos

```text
CARDIOSM/
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
└── src/
    └── risk_engine.py
```

Arquivos ou diretorios mencionados no README, mas ausentes no projeto atual:

- `models/`
- `models/full_model.pkl`
- `models/quick_model.pkl`
- `models/.gitkeep`
- `tests/`
- `src/__init__.py`

## 3. Arquitetura do sistema

### Camada de interface

Arquivo: `app.py`

Responsabilidades:

- Configurar a pagina Streamlit com `st.set_page_config`.
- Inserir CSS customizado e cabecalho visual.
- Exibir o seletor de modo rapido/completo.
- Montar o formulario com `st.form`.
- Coletar entradas clinicas e laboratoriais.
- Converter o sexo selecionado na interface para o valor interno `masculino` ou `feminino`.
- Chamar a funcao correta do motor de risco.
- Renderizar o resultado, a recomendacao e os avisos de seguranca.

Observacao: `st.set_page_config` aparece duas vezes seguidas em `app.py`. Em Streamlit, essa chamada deve ser a primeira chamada Streamlit e normalmente deve ocorrer apenas uma vez. A duplicidade pode causar erro ou comportamento indesejado.

### Camada de regras de negocio e calculo

Arquivo: `src/risk_engine.py`

Responsabilidades:

- Definir a excecao `ValidationError`.
- Definir a estrutura dinamica `RiskResult`.
- Implementar a regra demonstrativa de triagem rapida em `predict_quick_screening`.
- Implementar a regra demonstrativa do modo completo em `predict_complete_risk`.

Nao ha separacao adicional entre regras de negocio, validacao clinica, calculo de escore e integracao com modelo treinado. Tudo isso, no estado atual, esta concentrado em `src/risk_engine.py`.

### Camada de dependencia/configuracao

Arquivo: `requirements.txt`

Dependencias declaradas:

- `streamlit>=1.36,<2`
- `pandas>=2.0,<3`
- `scikit-learn>=1.3,<2`
- `joblib>=1.3,<2`

No codigo atual, apenas `streamlit` e usado diretamente. `pandas`, `scikit-learn` e `joblib` aparecem como dependencias futuras para suporte aos modelos descritos no README, mas nao sao importados nem usados na implementacao atual.

## 4. Fluxo do sistema

1. O usuario executa `streamlit run app.py`.
2. `app.py` adiciona o diretorio raiz do projeto ao `sys.path`.
3. `app.py` importa `ValidationError`, `predict_complete_risk` e `predict_quick_screening` de `src.risk_engine`.
4. A interface Streamlit e configurada e o cabecalho visual e renderizado.
5. O usuario escolhe entre modo completo e modo triagem rapida.
6. O formulario coleta dados basicos:
   - idade
   - sexo
   - PAS
   - circunferencia abdominal
7. Se o modo completo estiver ativo, o formulario tambem coleta:
   - triglicerideos
   - glicemia de jejum
   - HDL
   - colesterol total
   - LDL
   - tabagismo
   - uso de anti-hipertensivo
   - diabetes
8. Ao clicar em "Calcular estratificacao", `app.py` monta um dicionario `data`.
9. Se o modo rapido estiver ativo, chama `predict_quick_screening(data)`.
10. Se o modo completo estiver ativo, chama `predict_complete_risk(data)`.
11. O motor de risco retorna um objeto `RiskResult`.
12. `app.py` escolhe o estilo visual conforme `risk_label`: `Baixo`, `Moderado` ou `Alto`.
13. O resultado e exibido com indice/probabilidade, recomendacao e fonte do calculo.

## 5. Calculo do risco

### Triagem rapida

Funcao: `predict_quick_screening(data)`

Arquivo: `src/risk_engine.py`

Entradas efetivamente usadas:

- `idade`
- `pas`
- `circunferencia_abdominal`

Apesar de o modo rapido tambem coletar `sexo`, o sexo nao e usado no calculo atual.

Formula atual:

```text
score_simulado = idade * 0.4 + pas * 0.2 + circunferencia_abdominal * 0.3
screening_index = limitar(score_simulado - 20, minimo=0, maximo=100)
```

Classificacao:

- `< 40`: Baixo
- `>= 40` e `< 70`: Moderado
- `>= 70`: Alto

Conclusao: a triagem rapida e uma regra linear demonstrativa. Nao ha modelo estatistico treinado nem validacao clinica implementada.

### Modo completo/laboratorial

Funcao: `predict_complete_risk(data)`

Arquivo: `src/risk_engine.py`

Entradas efetivamente usadas:

- `idade`
- `diabetes`
- `tabagismo`

Entradas coletadas pela interface, mas nao usadas no calculo atual:

- `sexo`
- `pas`
- `circunferencia_abdominal`
- `triglicerideos`
- `glicemia_jejum`
- `hdl`
- `colesterol_total`
- `ldl`
- `anti_hipertensivo`

Regra atual:

```text
prob_simulada = 5.0
se idade > 55: soma 8.5
se diabetes: soma 12.0
se tabagismo: soma 6.5
prob_simulada = limitar(prob_simulada, maximo=99.9)
framingham_probability = prob_simulada * 0.95
```

Classificacao:

- `< 10%`: Baixo
- `>= 10%` e `< 20%`: Moderado
- `>= 20%`: Alto

Conclusao: o modo completo nao implementa de fato a equacao de Framingham/D'Agostino descrita no README. Ele apenas simula uma probabilidade com tres fatores.

## 6. Dependencias ausentes ou inconsistentes

### Ausencias no ambiente verificado

Neste ambiente, os comandos `python` e `py` nao estao disponiveis no PATH. Isso impede executar diretamente os comandos sugeridos pelo README, criar ambiente virtual via `py -m venv` ou validar as dependencias instaladas.

Comandos testados:

- `python --version`: nao encontrado.
- `py --version`: nao encontrado.

### Dependencias declaradas, mas nao usadas

As dependencias abaixo estao em `requirements.txt`, porem nao sao usadas pelo codigo atual:

- `pandas`
- `scikit-learn`
- `joblib`

Elas seriam coerentes com a arquitetura descrita no README para modelos treinados, mas essa arquitetura ainda nao existe no codigo.

### Dependencias funcionais minimas

Para o estado atual do codigo, a dependencia realmente necessaria para rodar a interface e:

- `streamlit`

Para a evolucao descrita no README, tambem seriam necessarias:

- `pandas`
- `scikit-learn`
- `joblib`
- artefatos de modelo em `models/`

## 7. Possiveis problemas para execucao

1. **Python indisponivel no PATH**

   O ambiente analisado nao reconhece `python` nem `py`. Sem corrigir isso, nao sera possivel executar `pip install`, `streamlit run app.py` ou os testes mencionados.

2. **Chamada duplicada de `st.set_page_config`**

   `app.py` chama `st.set_page_config` duas vezes. Streamlit pode reclamar se a configuracao da pagina for chamada mais de uma vez.

3. **README descreve recursos inexistentes**

   O README afirma que o codigo procura `models/full_model.pkl` e `models/quick_model.pkl`, mas nao ha codigo de carregamento desses arquivos.

4. **Diretorio `models/` ausente**

   Mesmo que o carregamento fosse implementado, o diretorio e os arquivos de modelo nao existem no repositorio atual.

5. **Diretorio `tests/` ausente**

   O README recomenda `python -m unittest discover -s tests -v`, mas nao existe pasta `tests`.

6. **`src` sem `__init__.py`**

   Em versoes modernas do Python, o import `from src.risk_engine import ...` pode funcionar por namespace package, especialmente porque `app.py` insere a raiz no `sys.path`. Ainda assim, adicionar `src/__init__.py` deixaria o pacote mais explicito e compativel.

7. **`ValidationError` nao e usado pelo motor**

   A interface captura `ValidationError`, mas as funcoes de risco nao levantam essa excecao. Atualmente, as validacoes dependem quase totalmente dos limites dos componentes Streamlit.

8. **Campos clinicos coletados mas ignorados**

   O modo completo coleta varios biomarcadores, mas o calculo usa apenas idade, diabetes e tabagismo. Isso pode causar falsa percepcao de que todos os fatores influenciam o resultado.

9. **Sexo coletado mas ignorado**

   O sexo e coletado nos dois modos, mas nao influencia nenhuma das regras atuais.

10. **Texto clinico pode sugerir mais robustez que a implementacao**

    A interface e o README mencionam Framingham, biomarcadores e estratificacao cardiovascular, mas o calculo atual e explicitamente mock/demonstrativo.

11. **Possivel problema de codificacao em alguns terminais**

    Arquivos contem acentos e simbolos. Em alguns terminais PowerShell, a exibicao pode aparecer com caracteres corrompidos se a pagina de codigo nao estiver em UTF-8. No navegador, o Streamlit tende a renderizar corretamente se os arquivos estiverem salvos em UTF-8.

## 8. Responsabilidade por area

| Area | Arquivo | Elementos principais |
| --- | --- | --- |
| Interface | `app.py` | `st.set_page_config`, CSS, `st.toggle`, `st.form`, `st.number_input`, `st.selectbox`, `st.form_submit_button`, `st.markdown` |
| Coleta de dados | `app.py` | Montagem do dicionario `data` com campos clinicos e laboratoriais |
| Orquestracao do fluxo | `app.py` | Escolha entre `predict_quick_screening` e `predict_complete_risk` |
| Regras de negocio | `src/risk_engine.py` | Classificacao `Baixo`, `Moderado`, `Alto`; recomendacoes textuais |
| Calculo de risco | `src/risk_engine.py` | Formula linear da triagem e probabilidade simulada do modo completo |
| Dependencias | `requirements.txt` | Streamlit, pandas, scikit-learn, joblib |
| Documentacao | `README.md` | Como executar, intencao clinica, deploy e descricao futura dos modelos |

## 9. Lacunas entre documentacao e implementacao

| Tema | README | Codigo atual |
| --- | --- | --- |
| Framingham/D'Agostino | Diz que o ERG e implementado | Usa uma probabilidade simulada |
| Modelos `.pkl` | Diz que o codigo procura modelos em `models/` | Nao ha carregamento de modelos |
| `pandas.DataFrame` | Diz que modelos recebem DataFrame | Nao ha uso de pandas |
| `joblib` | Diz que modelos sao serializados com joblib | Nao ha import de joblib |
| `scikit-learn` | Descreve pipelines/modelos | Nao ha uso de scikit-learn |
| Testes | Instrui rodar unittest em `tests` | Pasta `tests` nao existe |
| Biomarcadores | Diz que entram no modelo completo | Sao coletados, mas ignorados no calculo |

## 10. Conclusao

O CardioSM, no estado atual, e um MVP Streamlit funcional em conceito, mas ainda baseado em regras demonstrativas. A interface esta implementada em `app.py`, enquanto as regras e calculos estao em `src/risk_engine.py`.

O principal risco tecnico e a divergencia entre o README/interface e o motor real: a documentacao descreve Framingham, biomarcadores e modelos treinados, mas o codigo executa apenas regras simples. Para uma demonstracao academica, isso pode ser aceitavel se ficar claramente rotulado como mock. Para uso clinico, validacao, deploy formal ou apresentacao como modelo preditivo, seria necessario implementar o calculo real, integrar modelos treinados, adicionar validacoes, criar testes e revisar a comunicacao de risco.

Tambem ha impedimentos praticos para execucao neste ambiente: `python` e `py` nao estao disponiveis no PATH, portanto nao foi possivel instalar dependencias, rodar o Streamlit ou executar testes automatizados.
