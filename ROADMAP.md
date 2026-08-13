# Roadmap de Evolucao do CardioSM para Produto HealthTech

## 1. Visao de produto

O CardioSM deve evoluir de um MVP academico demonstrativo para uma plataforma HealthTech de apoio a estratificacao de risco cardiometabolico, voltada inicialmente para triagem, acompanhamento e suporte a decisao clinica em contextos supervisionados.

O produto nao deve ser posicionado como substituto do profissional de saude. A proposta mais segura e viavel e atuar como ferramenta de apoio, priorizacao, acompanhamento longitudinal e organizacao de informacoes clinicas, sempre com rastreabilidade, explicabilidade e governanca.

## 2. Principios de evolucao

- Separar claramente demonstracao academica, uso assistencial supervisionado e produto validado.
- Tratar dados de saude como dados pessoais sensiveis desde o primeiro desenho arquitetural.
- Validar clinicamente qualquer modelo antes de uso em producao.
- Manter explicabilidade minima para profissionais de saude e pacientes.
- Registrar versoes de modelos, regras, parametros e recomendacoes.
- Construir primeiro uma base segura e auditavel antes de escalar automacoes com IA.

## 3. Funcionalidades

### Fase 1: Produto minimo seguro

- Cadastro de pacientes com identificacao minima necessaria.
- Registro de avaliacoes cardiometabolicas.
- Historico de avaliacoes por paciente.
- Comparacao longitudinal de indicadores.
- Exportacao de relatorio em PDF.
- Classificacao de risco com aviso explicito de ferramenta de apoio.
- Painel para profissional de saude.
- Registro da fonte do calculo usado em cada avaliacao.
- Controle de versao do algoritmo aplicado.

### Fase 2: Operacao clinica supervisionada

- Perfis de usuario: administrador, medico, enfermeiro, pesquisador e auditor.
- Cadastro de unidades, equipes e permissoes por organizacao.
- Dashboard populacional por grupo de risco.
- Filtros por idade, sexo, unidade, periodo e fatores de risco.
- Alertas de acompanhamento para pacientes de maior risco.
- Agendamento ou encaminhamento integrado ao fluxo da clinica.
- Registro de condutas, observacoes e plano de acompanhamento.
- Trilhas de auditoria para acessos, alteracoes e calculos.

### Fase 3: Plataforma HealthTech

- Portal do paciente com visualizacao simplificada e educativa.
- Integracao com prontuarios eletronicos via APIs.
- Importacao de exames laboratoriais.
- Integracao com dispositivos e wearables, quando clinicamente justificavel.
- Modulo de pesquisa com dados anonimizados ou pseudonimizados.
- Gestao de consentimento.
- Relatorios gerenciais para operadoras, clinicas e programas de saude populacional.
- APIs para integracao com parceiros.

## 4. Arquitetura recomendada

### Arquitetura inicial

- Frontend: Streamlit pode continuar para prototipagem e demonstracoes.
- Backend: FastAPI para regras, autenticacao, auditoria, modelos e APIs.
- Banco de dados: PostgreSQL.
- Cache e filas: Redis e worker assíncrono quando houver tarefas de relatorio, IA ou integracoes.
- Armazenamento de arquivos: storage privado para PDFs, documentos e artefatos de modelo.
- Deploy: container Docker com ambientes separados de desenvolvimento, homologacao e producao.

### Arquitetura alvo

```text
Frontend Web / Portal Clinico
        |
API Gateway / Backend FastAPI
        |
Servicos de dominio
        |-- Pacientes
        |-- Avaliacoes
        |-- Risco cardiometabolico
        |-- Relatorios
        |-- Consentimento
        |-- Auditoria
        |-- Integracoes
        |-- IA e modelos
        |
PostgreSQL + Storage privado + Redis + Observabilidade
```

### Separacao de responsabilidades

- Interface: coleta, visualizacao e fluxo de uso.
- Backend: autenticacao, autorizacao, validacao, persistencia e orquestracao.
- Motor de risco: regras e modelos versionados.
- Camada de IA: inferencia, explicabilidade, monitoramento e avaliacao.
- Auditoria: registro imutavel de eventos relevantes.
- Integracoes: conectores externos isolados do nucleo clinico.

## 5. Seguranca

### Controles essenciais

- Autenticacao obrigatoria.
- Autorizacao por perfil e organizacao.
- MFA para administradores e profissionais.
- Criptografia em transito com HTTPS/TLS.
- Criptografia em repouso para banco e arquivos.
- Segredos fora do repositorio.
- Logs sem dados sensiveis desnecessarios.
- Auditoria de acesso a dados de pacientes.
- Backup automatizado e testado.
- Politica de retencao e descarte de dados.

### Controles avancados

- RBAC ou ABAC para permissoes granulares.
- Rate limiting nas APIs.
- Protecao contra brute force.
- Monitoramento de eventos suspeitos.
- Revisao periodica de permissoes.
- Pentest antes de pilotos em ambiente real.
- SAST/DAST no pipeline.
- Assinatura e versionamento de artefatos de modelo.

## 6. LGPD e governanca de dados

Dados de saude sao dados pessoais sensiveis pela LGPD. O produto deve nascer com governanca juridica e tecnica.

### Requisitos basicos

- Definir controlador, operador e encarregado/DPO.
- Mapear bases legais para cada finalidade.
- Coletar apenas dados necessarios.
- Criar politica de privacidade clara.
- Implementar termos de uso adequados ao contexto clinico.
- Registrar consentimento quando aplicavel.
- Permitir atendimento a direitos do titular.
- Manter inventario de dados tratados.
- Documentar compartilhamentos com terceiros.
- Estabelecer contratos com operadores e subprocessadores.

### Privacidade por desenho

- Minimizar campos identificaveis.
- Separar dados identificadores de dados clinicos quando possivel.
- Usar pseudonimizacao para pesquisa, analise e treinamento.
- Usar anonimizacao quando a finalidade nao exigir reidentificacao.
- Restringir exportacoes.
- Auditar acessos a prontuarios e avaliacoes.

### Documentos recomendados

- RIPD: Relatorio de Impacto a Protecao de Dados.
- Politica de privacidade.
- Politica de seguranca da informacao.
- Politica de retencao e descarte.
- Registro de operacoes de tratamento.
- Plano de resposta a incidentes.
- Modelo de consentimento, quando aplicavel.

## 7. IA e modelos preditivos

### Curto prazo

- Manter regras demonstrativas separadas dos modelos reais.
- Implementar motor de risco versionado.
- Registrar entradas, saidas, versao do algoritmo e contexto de uso.
- Criar testes unitarios para calculos.
- Implementar validacao clinica das faixas e campos.

### Medio prazo

- Treinar modelos com pipeline reprodutivel.
- Usar dados curados, com aprovacao etica e base legal adequada.
- Comparar modelos simples e explicaveis com modelos mais complexos.
- Medir calibracao, sensibilidade, especificidade, AUC, recall por subgrupo e valor preditivo.
- Implementar explicabilidade por fator de risco.
- Validar desempenho por sexo, idade, unidade, etnia/cor quando disponivel e juridicamente apropriado.

### Longo prazo

- Monitoramento de drift de dados e performance.
- Recalibracao periodica.
- Registro de modelo com versoes aprovadas.
- Workflow de aprovacao clinica antes de publicar um modelo.
- IA generativa apenas para apoio textual, nunca para decisao autonoma.
- Guardrails para impedir recomendacoes clinicas indevidas.

### Principio clinico

Qualquer IA deve ser apresentada como apoio a decisao. A decisao final deve permanecer com profissional habilitado, especialmente em diagnostico, prescricao, urgencia e condutas terapeuticas.

## 8. Escalabilidade

### Escala tecnica

- Containerizar aplicacao.
- Separar frontend, backend e banco.
- Usar banco gerenciado com backups.
- Adicionar cache para dashboards e consultas frequentes.
- Processar PDFs, relatorios e integracoes em filas.
- Implementar observabilidade com metricas, logs e tracing.
- Configurar CI/CD com testes automatizados.
- Criar ambientes separados: dev, staging e producao.

### Escala operacional

- Onboarding de clinicas e unidades.
- Gestao multi-tenant.
- Permissoes por organizacao.
- Suporte e monitoramento.
- Treinamento de usuarios.
- Base de conhecimento e materiais clinicos revisados.
- Processo de reporte de incidentes.

### Escala regulatoria

- Avaliar enquadramento como Software as a Medical Device.
- Mapear exigencias aplicaveis da Anvisa.
- Documentar ciclo de vida de software.
- Manter rastreabilidade de requisitos, testes e versoes.
- Formalizar validacao clinica e tecnica.

## 9. Monetizacao

### Modelos possiveis

- SaaS B2B para clinicas e consultorios.
- Licenca por profissional ativo.
- Licenca por unidade de saude.
- Plano por volume de avaliacoes.
- Contrato com operadoras ou programas de saude populacional.
- Modulo premium de relatorios e analytics.
- Modulo de integracao com prontuario/laboratorio.
- Projetos de pesquisa com dados anonimizados, respeitando LGPD e com governanca apropriada.

### Segmentos iniciais

- Clinicas de cardiologia.
- Clinicas de endocrinologia.
- Programas de saude ocupacional.
- Atencao primaria privada.
- Operadoras com programas de prevencao.
- Projetos academicos e centros de pesquisa.

### Cuidados comerciais

- Evitar promessas de diagnostico automatico.
- Vender reducao de friccao operacional, padronizacao de triagem e acompanhamento.
- Demonstrar valor com indicadores: tempo de avaliacao, pacientes estratificados, adesao ao acompanhamento e identificacao precoce de risco.
- Construir evidencia antes de afirmar impacto em desfechos clinicos.

## 10. Roadmap por fases

### 0 a 30 dias: fundacao

- Corrigir divergencia entre README, interface e motor real.
- Definir posicionamento: educacional, apoio clinico ou pesquisa.
- Criar testes unitarios para regras atuais.
- Criar estrutura de pacote mais explicita.
- Documentar limitacoes clinicas.
- Definir modelo de dados inicial.

### 30 a 90 dias: MVP seguro

- Criar backend com API.
- Persistir pacientes e avaliacoes.
- Implementar login e perfis.
- Criar auditoria basica.
- Gerar relatorio PDF.
- Criar historico por paciente.
- Criar pipeline de deploy.
- Elaborar documentos iniciais de LGPD.

### 3 a 6 meses: piloto supervisionado

- Executar piloto com profissionais de saude.
- Implementar dashboards por unidade.
- Refinar usabilidade com feedback real.
- Criar gestao de consentimento.
- Implementar logs e observabilidade.
- Validar regras com especialistas.
- Iniciar dataset governado para treinamento futuro.

### 6 a 12 meses: produto comercial inicial

- Implementar multi-tenant.
- Integrar com laboratorios ou prontuarios selecionados.
- Criar cobranca e planos.
- Fortalecer seguranca.
- Executar pentest.
- Formalizar suporte e onboarding.
- Preparar documentacao regulatoria.

### 12+ meses: IA validada e escala

- Treinar e validar modelos preditivos.
- Implementar registry de modelos.
- Monitorar drift e performance.
- Expandir integracoes.
- Estruturar parcerias com operadoras e redes de clinicas.
- Avaliar certificacoes, requisitos Anvisa e estrategia regulatoria completa.

## 11. Riscos principais

- Confundir prototipo demonstrativo com ferramenta clinica validada.
- Usar dados sensiveis sem governanca LGPD adequada.
- Falta de validacao externa do modelo.
- Vies de performance entre subgrupos.
- Recomendacoes clinicas excessivamente automaticas.
- Segurança insuficiente para dados de saude.
- Dependencia de integracoes complexas antes de validar valor.
- Monetizacao antes de evidencia minima de impacto operacional.

## 12. Proxima decisao recomendada

A decisao mais importante antes de programar e escolher o primeiro posicionamento comercial:

- **Ferramenta para pesquisa academica supervisionada**
- **SaaS operacional para clinicas**
- **Plataforma de saude populacional para operadoras**

Essa escolha define arquitetura, profundidade regulatoria, modelo de dados, experiencia de usuario, precificacao e nivel de validacao clinica necessario.
