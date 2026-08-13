# CENTELHA.md

# CardioSM - Analise para Submissao ao Programa Centelha

## Fontes consideradas

Este documento foi elaborado a partir das seguintes fontes:

- codigo atual do repositorio CardioSM;
- `README.md`;
- dissertação de mestrado `Recomendação de um modelo de aprendizado de máquina parapredição de risco cardiovascular com biomarcadores da síndrome.pdf`;
- `Edital.pdf` do Programa Centelha Alagoas 2026.

Quando uma conclusao for baseada diretamente nas fontes, isso sera indicado no texto. Quando for uma interpretacao estrategica para submissao, sera marcada como **inferencia**.

## 1. Resumo Executivo

O CardioSM e um MVP academico de software para estratificacao de risco cardiovascular com foco em biomarcadores da sindrome metabolica e no Escore de Risco Global de Framingham. O projeto atual possui uma interface em Streamlit, dois modos de uso - modo completo/laboratorial e modo de triagem rapida - e um motor de risco demonstrativo.

A dissertação que fundamenta o projeto teve como objetivo recomendar um modelo de aprendizado de maquina para estimar risco de eventos cardiovasculares em pacientes com sindrome metabolica, explorando marcadores da SM e do escore de Framingham. Nos cenarios avaliados, o modelo Random Forest aparece como o candidato mais consistente, com resultados promissores, embora a propria dissertação recomende validacoes adicionais e melhorias para identificacao de casos positivos.

Para o Programa Centelha, o CardioSM deve ser apresentado como uma proposta de transformacao de pesquisa aplicada em produto HealthTech. O edital do Programa Centelha Alagoas busca ideias inovadoras com potencial de se transformar em produtos, servicos ou processos inovadores e em negocios de base tecnologica. Nesse contexto, o CardioSM pode ser posicionado como uma plataforma digital de apoio a triagem, acompanhamento e priorizacao de risco cardiometabolico, voltada a profissionais, clinicas, programas preventivos e, futuramente, saude populacional.

O ponto forte da proposta e a combinacao entre base cientifica propria, relevancia clinica do problema, MVP funcional e possibilidade de evolucao para software comercial com IA. O ponto critico e que o produto ainda nao esta pronto para uso clinico real: o codigo atual nao acopla o modelo treinado, nao persiste dados, nao tem autenticacao, nao possui auditoria e usa regras demonstrativas.

## 2. Problema

Doencas cardiovasculares estao associadas a fatores de risco como hipertensao, diabetes, dislipidemia, obesidade abdominal, tabagismo e alteracoes metabolicas. A dissertação analisada afirma que a sindrome metabolica aumenta o risco de desenvolver doenca cardiovascular e que a identificacao precoce de pacientes em risco e crucial para intervencao mais adequada.

O problema pratico que o CardioSM busca resolver e a dificuldade de transformar dados clinicos e laboratoriais em uma estratificacao padronizada, rapida e rastreavel de risco cardiometabolico.

Problemas especificos observados:

- triagem de risco muitas vezes manual e dependente da experiencia individual do profissional;
- uso fragmentado de dados clinicos, antropometricos e laboratoriais;
- baixa padronizacao entre atendimentos, unidades e profissionais;
- dificuldade de priorizar pacientes que precisam de acompanhamento preventivo;
- pouca rastreabilidade sobre qual regra, escore ou modelo foi usado;
- ausencia, no MVP atual, de um produto digital completo que conecte a pesquisa de mestrado a uma operacao clinica segura.

**Inferencia:** o problema comercial mais promissor nao e "substituir o medico", mas reduzir friccao operacional em triagens e programas preventivos, oferecendo uma camada de apoio a decisao supervisionada.

## 3. Solucao

A solucao proposta e evoluir o CardioSM para uma plataforma HealthTech de apoio a estratificacao de risco cardiometabolico.

No MVP atual, o sistema ja demonstra:

- interface web responsiva em Streamlit;
- coleta de idade, sexo, pressao arterial sistolica e circunferencia abdominal;
- modo laboratorial com triglicerideos, glicemia de jejum, HDL, colesterol total, LDL, tabagismo, uso de anti-hipertensivo e diabetes;
- exibicao de classificacao de risco;
- recomendacao textual;
- aviso de que se trata de ferramenta educacional/prototipo.

A evolucao de produto deve transformar esse MVP em:

- motor de risco versionado;
- integracao real com modelo de aprendizado de maquina validado;
- cadastro e historico de pacientes;
- relatorios clinicos;
- painel de acompanhamento por profissional ou unidade;
- trilha de auditoria;
- controle de acesso;
- conformidade com LGPD;
- protocolo de validacao com profissionais de saude.

**Inferencia:** para a submissao ao Centelha, a solucao deve ser descrita como um produto digital em desenvolvimento, com prova de conceito ja implementada, e nao como produto clinico finalizado.

## 4. Diferenciais tecnologicos

Os diferenciais tecnologicos do CardioSM estao na combinacao entre pesquisa aplicada, modelagem preditiva e produto digital focado em sindrome metabolica.

Diferenciais baseados nas fontes:

- a dissertação comparou regressao logistica, arvore de decisao, Random Forest, Gradient Boosting, SVM e KNN;
- o Random Forest foi identificado como modelo de destaque em diferentes cenarios;
- a pesquisa explorou combinacoes de marcadores da sindrome metabolica e do escore de Framingham;
- a dissertação observou desempenho consideravel em combinacoes mais simples de variaveis, o que sugere possibilidade de triagem menos invasiva;
- o README ja antecipa arquitetura futura com modelos serializados em `joblib` e uso de `pandas.DataFrame`;
- o MVP ja possui dois fluxos de uso: completo e triagem rapida.

Diferenciais por inferencia:

- possibilidade de criar um motor de risco explicavel e versionado;
- possibilidade de oferecer modo de baixa complexidade para triagem inicial;
- potencial de adaptar o produto a contextos de atencao primaria, campanhas e programas preventivos;
- potencial de gerar dados longitudinais para melhoria continua do modelo.

## 5. Inovacao

Segundo o edital, propostas devem apresentar produtos, servicos ou processos inovadores com potencial de se transformar em negocio e incorporar novas tecnologias. O CardioSM se alinha a esse criterio quando apresentado como transformacao de uma pesquisa de aprendizado de maquina em plataforma digital aplicavel a saude preventiva.

Inovacao tecnologica:

- uso de aprendizado de maquina para predicao/estratificacao de risco cardiometabolico;
- combinacao de biomarcadores da sindrome metabolica com escore de Framingham;
- arquitetura futura com modelo preditivo serializado e pipeline de inferencia;
- possibilidade de explicabilidade por fatores de risco.

Inovacao de processo:

- padronizacao de triagem cardiometabolica;
- reducao do tempo para consolidar dados clinicos e laboratoriais;
- apoio a priorizacao de pacientes em programas preventivos;
- criacao de historico longitudinal.

Inovacao de negocio:

- transformacao de conhecimento academico em produto HealthTech;
- modelo SaaS para clinicas e programas de saude;
- possibilidade de parcerias com hospitais, laboratorios e instituicoes de pesquisa.

**Inferencia:** a inovacao deve ser defendida menos como "novo algoritmo isolado" e mais como "produto de apoio a decisao clinica que operacionaliza pesquisa propria em ML para risco cardiometabolico".

## 6. Base cientifica utilizada

A base cientifica principal e a dissertação de mestrado desenvolvida na UFAL, cujo tema e a recomendacao de um modelo de aprendizado de maquina para predicao de risco cardiovascular com biomarcadores da sindrome metabolica e escore de Framingham.

Pontos cientificos extraidos da dissertação:

- objetivo: recomendar um modelo de Machine Learning para estimar riscos de eventos cardiovasculares em pacientes com sindrome metabolica;
- algoritmos avaliados: regressao logistica, arvore de decisao, Random Forest, Gradient Boosting, SVM e KNN;
- bases utilizadas: NHANES, conjunto combinado de doencas cardiacas do repositorio UCI e dados da plataforma Kaggle relacionados a Framingham;
- achado do primeiro cenario: diferenca percentual de 81,74% nas medias de risco cardiovascular entre populacoes com e sem sindrome metabolica;
- achado recorrente: Random Forest se destacou em diversos cenarios;
- no conjunto combinado de doencas cardiacas, o Random Forest apresentou acuracia de 0,95 com todos os marcadores, 0,80 com tres marcadores da SM e 0,84 com cinco marcadores SM + FRS;
- no modelo com marcadores SM + FRS, a curva ROC apresentou area de 0,87 e acuracia geral de 0,78 em uma avaliacao descrita;
- no cenario com dataset Framingham, o Random Forest obteve acuracia aproximada de 0,835;
- a dissertação ressalta que a taxa de acerto para classe positiva foi baixa em determinado cenario, indicando necessidade de melhorias e ajustes;
- as limitacoes incluem ausencia de todas as variaveis necessarias em cada base de dados e substituicao da circunferencia da cintura por IMC no dataset de Framingham;
- as recomendacoes futuras incluem equipe multidisciplinar, parcerias com hospitais e laboratorios, consentimento dos participantes e desenvolvimento de escore de facil uso e acessivel.

Conclusao cientifica aplicavel ao produto:

O CardioSM tem uma base cientifica coerente para evoluir, mas ainda precisa de validacao clinica, calibracao, avaliacao de vies, melhoria de desempenho em casos positivos e governanca de dados antes de uso assistencial.

## 7. Estado atual do MVP

O repositorio atual contem:

- `app.py`: interface Streamlit, formulario e exibicao de resultados;
- `src/risk_engine.py`: motor de regras demonstrativas;
- `requirements.txt`: dependencias declaradas;
- `README.md`: descricao do MVP, execucao e intencao de conectar modelos treinados;
- documentos de analise e roadmap criados no processo de preparacao.

Estado funcional:

- o app roda localmente em Streamlit;
- o ambiente virtual foi criado anteriormente e dependencias foram instaladas;
- o app possui dois modos de uso;
- a interface coleta os campos previstos;
- o resultado e apresentado com classificacao, metrica e recomendacao.

Limitacoes do MVP atual:

- nao ha modelo de ML treinado acoplado ao codigo;
- nao existe pasta `models/` com `full_model.pkl` ou `quick_model.pkl`;
- o motor atual usa regras demonstrativas;
- parte dos campos coletados no modo completo nao influencia o calculo atual;
- nao ha persistencia de pacientes ou avaliacoes;
- nao ha login, autorizacao, auditoria ou criptografia aplicada no produto;
- nao ha testes automatizados;
- nao ha conformidade LGPD implementada;
- nao ha validacao clinica operacional do software.

**Inferencia:** o MVP atual e adequado como demonstrador para banca, pitch ou prova de conceito tecnica, mas nao deve ser apresentado como dispositivo medico ou ferramenta clinica pronta.

## 8. Evolucao necessaria para produto comercial

Para virar produto comercial, o CardioSM precisa evoluir em quatro frentes: tecnologia, clinica, seguranca/regulatorio e negocio.

Evolucao tecnologica:

- acoplar modelo treinado e versionado;
- criar pipeline de pre-processamento identico ao usado no treinamento;
- implementar testes unitarios e de integracao;
- separar frontend, backend, motor de risco e persistencia;
- criar banco de dados;
- gerar relatorios;
- criar logs tecnicos e clinicos;
- implementar monitoramento de desempenho do modelo.

Evolucao clinica:

- validar o modelo com dados reais e governados;
- envolver equipe multidisciplinar, como recomendado pela dissertação;
- definir protocolo de uso;
- avaliar sensibilidade, especificidade, calibracao, AUC, precisao, recall e F1-score;
- avaliar desempenho por subgrupos;
- melhorar identificacao de casos positivos;
- documentar limitacoes e indicacoes de uso.

Evolucao de seguranca e LGPD:

- implementar autenticacao e perfis de acesso;
- registrar consentimento quando aplicavel;
- criar politica de privacidade;
- minimizar dados coletados;
- criptografar dados em transito e repouso;
- auditar acessos;
- pseudonimizar ou anonimizar dados para pesquisa;
- elaborar RIPD, se aplicavel.

Evolucao comercial:

- definir primeiro nicho de cliente;
- validar disposicao de pagamento;
- desenhar modelo SaaS;
- construir proposta de valor para clinicas e programas preventivos;
- executar piloto supervisionado;
- produzir materiais de venda e pitch.

Ligacao com o edital:

O edital indica que a Fase 2 avalia potencial de mercado, modelo de negocio, cronograma, orcamento, dominio tecnologico e capacidade de execucao. Portanto, a evolucao deve ser organizada em entregaveis de ate 12 meses, compatíveis com o prazo de execucao previsto.

## 9. Publico-alvo

Publico-alvo primario:

- clinicas de cardiologia;
- clinicas de endocrinologia;
- profissionais de saude que acompanham pacientes com fatores cardiometabolicos;
- programas de medicina preventiva;
- servicos de atencao primaria privada.

Publico-alvo secundario:

- operadoras de saude;
- saude ocupacional;
- programas de check-up;
- instituicoes de ensino e pesquisa;
- hospitais e laboratorios em projetos de validacao.

**Inferencia:** o melhor publico inicial e B2B, especialmente clinicas e programas preventivos, porque o software exige supervisao profissional e ainda nao deve ser ofertado diretamente ao paciente como ferramenta autonoma.

## 10. Mercado

O mercado abordado e o de saude digital aplicada a prevencao cardiometabolica e apoio a decisao clinica.

Com base no edital, a proposta deve demonstrar oportunidade de mercado e potencial de escala. Com base no projeto, os segmentos mais coerentes sao:

- HealthTech;
- software de apoio a decisao clinica;
- prevencao cardiovascular;
- acompanhamento de sindrome metabolica;
- analytics em saude;
- triagem em programas preventivos.

Oportunidades de mercado:

- clinicas precisam padronizar avaliacoes e gerar historico;
- programas de prevencao precisam priorizar pacientes;
- operadoras buscam reduzir risco e custo evitavel;
- instituicoes academicas precisam transformar pesquisa em aplicacoes;
- laboratorios e prontuarios podem se beneficiar de uma camada de interpretacao de risco.

Limitacao importante:

Os documentos analisados nao trazem dimensionamento financeiro do mercado, TAM/SAM/SOM, ticket medio, numero de clinicas-alvo ou estudo de concorrencia. Esses dados devem ser levantados antes da Fase 2 do Centelha.

## 11. Modelo de negocio

Modelos possiveis:

- SaaS B2B para clinicas;
- assinatura por profissional;
- assinatura por unidade;
- cobranca por volume de avaliacoes;
- licenciamento institucional;
- modulo premium de relatorios;
- modulo de integracao com prontuario ou laboratorio;
- projetos de validacao e pesquisa com instituicoes parceiras.

Modelo recomendado para inicio:

**Inferencia:** iniciar como SaaS B2B para clinicas e programas preventivos, com mensalidade por unidade ou profissional, e piloto supervisionado gratuito ou subsidiado para gerar evidencia de valor.

Proposta de valor comercial:

- reduzir tempo de triagem;
- padronizar avaliacao;
- gerar relatorios;
- acompanhar evolucao;
- priorizar pacientes;
- apoiar decisao clinica supervisionada;
- criar base estruturada para pesquisa e melhoria do modelo.

Ligacao com o edital:

O edital solicita descricao de modelo de negocio e estrategia de monetizacao na Fase 2. A proposta deve apresentar preco inicial, segmento-alvo, canais de venda, custo de implantacao, custo mensal de infraestrutura e estrategia de sustentabilidade financeira.

## 12. Concorrentes

Os documentos analisados nao listam concorrentes diretos. Assim, a analise abaixo e uma **inferencia por categoria**, nao uma afirmacao de concorrentes nominalmente validados.

Categorias concorrentes ou substitutas:

- calculadoras clinicas tradicionais de risco cardiovascular;
- uso manual do Escore de Framingham ou outros escores;
- planilhas internas de clinicas;
- prontuarios eletronicos com campos de avaliacao clinica;
- plataformas de telemedicina e check-up com modulos de risco;
- sistemas de BI em saude;
- softwares academicos ou modelos de ML ainda nao transformados em produto.

Como o CardioSM pode se diferenciar:

- foco especifico em sindrome metabolica e risco cardiometabolico;
- origem em pesquisa propria de mestrado;
- combinacao de marcadores SM + Framingham;
- caminho para modelo ML validado;
- simplicidade de triagem;
- possibilidade de historico longitudinal e painel populacional.

Ponto de atencao:

Antes da submissao final, recomenda-se pesquisa de concorrentes reais no Brasil, incluindo calculadoras, prontuarios, health analytics e soluções de medicina preventiva.

## 13. Barreiras de entrada

Barreiras tecnicas:

- necessidade de modelo validado;
- necessidade de dados clinicos de qualidade;
- integracao com fluxo real de profissionais;
- interoperabilidade com prontuarios e laboratorios.

Barreiras cientificas:

- obter amostras representativas;
- melhorar predicao de casos positivos;
- validar em populacao brasileira/local;
- calibrar o modelo e monitorar drift.

Barreiras regulatorias e juridicas:

- LGPD por tratar dados sensiveis de saude;
- eventual enquadramento como software medico, a depender das alegacoes e funcionalidades;
- necessidade de termos, consentimento, governanca e auditoria;
- necessidade de documentacao de risco e validacao.

Barreiras comerciais:

- confianca de profissionais de saude;
- ciclo de venda em saude;
- comparacao com processos manuais gratuitos;
- necessidade de mostrar retorno operacional.

Barreiras positivas para defesa competitiva:

- base cientifica propria;
- know-how do dominio clinico-computacional;
- dados e validacoes futuras;
- parcerias com clinicas, hospitais e laboratorios;
- reputacao academica e tecnica da equipe.

## 14. Riscos

Riscos tecnicos:

- o MVP ainda nao usa o modelo de ML da dissertação;
- regras atuais sao demonstrativas;
- ausencia de testes automatizados;
- ausencia de banco, login e auditoria;
- risco de divergencia entre treinamento e producao se o pipeline nao for preservado.

Riscos cientificos:

- bases usadas na dissertação possuem limitacoes de variaveis;
- necessidade de validar em dados reais e locais;
- desempenho inferior em casos positivos em alguns cenarios;
- risco de vies entre subgrupos;
- risco de baixa generalizacao.

Riscos clinicos:

- usuario interpretar como diagnostico automatico;
- recomendacao inadequada sem supervisao profissional;
- uso fora do publico ou contexto validado;
- impacto indevido em condutas clinicas sem validacao.

Riscos LGPD e seguranca:

- tratamento de dados pessoais sensiveis;
- vazamento ou acesso indevido;
- uso de dados para IA sem base legal adequada;
- ausencia atual de controles de acesso.

Riscos regulatorios:

- possivel necessidade de enquadramento regulatorio conforme uso pretendido;
- necessidade de documentar ciclo de vida do software;
- necessidade de acompanhamento juridico/regulatorio.

Riscos comerciais:

- dificuldade de conversao de pilotos em receita;
- resistencia de profissionais;
- competicao com ferramentas ja incorporadas a prontuarios;
- falta de dimensionamento de mercado validado;
- dependencia de parcerias para dados e validacao.

Mitigacoes recomendadas:

- manter posicionamento como apoio a decisao supervisionada;
- implementar validacao clinica;
- criar governanca LGPD;
- iniciar por piloto controlado;
- documentar desempenho, limitacoes e versoes;
- realizar pesquisa de mercado antes da Fase 2.

## 15. Proximos passos

Proximos passos para submissao ao Centelha:

1. Definir titulo oficial e manter o mesmo nome durante a submissao, conforme alerta do edital.
2. Preparar resumo publicavel com problema, solucao, inovacao e impacto.
3. Transformar este documento em respostas objetivas para a Fase 1: problema, mercado, solucao, diferencial e impacto.
4. Preparar pitch de ate 3 minutos, embora o edital indique video como opcional na Fase 1 e obrigatorio na Fase 2.
5. Levantar dados de mercado e concorrentes reais antes da Fase 2.
6. Definir publico inicial de piloto: clinica, laboratorio, unidade academica ou programa preventivo.
7. Formalizar cronograma de 12 meses, alinhado ao prazo de execucao do edital.
8. Planejar uso dos recursos: desenvolvimento, validacao, LGPD, consultoria regulatoria, UX, infraestrutura, propriedade intelectual e marketing inicial.
9. Definir equipe executora com dominio tecnologico, clinico e mercadologico.
10. Elaborar plano de validacao com profissionais de saude e, se houver coleta de dados reais, com consentimento e governanca.
11. Revisar o README e a narrativa publica para deixar claro que o MVP atual e demonstrativo.
12. Evoluir o motor de risco para usar modelo treinado, versionado e testado.
13. Criar prototipo comercial com login, persistencia, historico, relatorio e auditoria.
14. Avaliar juridicamente LGPD e possivel enquadramento regulatorio.
15. Preparar plano de sustentabilidade financeira, como solicitado na Fase 2 do edital.

## Conclusao

O CardioSM tem aderencia ao Programa Centelha por combinar base cientifica, software funcional, problema relevante de saude e potencial de negocio de base tecnologica. A proposta e mais forte quando apresentada como evolucao de uma pesquisa de mestrado para uma plataforma HealthTech de apoio a decisao supervisionada.

A submissao deve ser honesta quanto ao estagio atual: o MVP demonstra o fluxo e a proposta de valor, mas ainda nao entrega um produto clinico validado. O financiamento deve ser justificado como etapa para transformar a prova de conceito em produto comercial seguro, auditavel, validado e aderente a LGPD.
