<p align="center">
  <img src="assets/fiap-logo.png" alt="FIAP" width="220">
</p>

## Integrantes:

Michelle Guedes Cavalari RM 564557

Graduação em Inteligência Artificial – FIAP  

Fase 5 – Assistente Cardiológico Inteligente e Conversacional
# CardioIA ❤️

Assistente Cardiológico Inteligente e Conversacional desenvolvido como parte da Fase 5 do projeto acadêmico de Inteligência Artificial.

O CardioIA utiliza processamento de linguagem natural para fornecer orientações iniciais sobre sintomas cardiovasculares, como:

- Dor no peito
- Palpitação
- Falta de ar

O sistema também identifica sinais de alerta e orienta o usuário a buscar atendimento médico quando necessário.

> ⚠️ O CardioIA não realiza diagnósticos e não substitui avaliação ou atendimento realizado por profissionais de saúde.

---

## Tecnologias utilizadas

- Python
- Flask
- IBM watsonx Assistant
- HTML
- CSS
- JavaScript
- IBM Watson Assistant API

---

## Arquitetura

Fluxo simplificado:

Usuário  
↓  
Interface Web HTML/CSS/JavaScript  
↓  
Backend Flask  
↓  
API IBM watsonx Assistant  
↓  
Processamento da mensagem e fluxo conversacional  
↓  
Resposta exibida ao usuário

---

## Funcionalidades

O assistente possui fluxos conversacionais para:

### Dor no peito
Avalia intensidade e presença de sinais de alerta.

### Palpitação
Verifica sintomas associados como dor no peito, falta de ar, tontura e desmaio.

### Falta de ar
Avalia intensidade e possíveis sinais de emergência.

### Fallback
Caso a mensagem do usuário não seja compreendida, o sistema orienta como reformular a pergunta.

---

## Segurança

O sistema possui mensagens de orientação para situações potencialmente graves.

Em situações de emergência, o usuário é orientado a procurar atendimento médico imediato ou entrar em contato com o SAMU pelo número 192.

As credenciais da IBM são armazenadas em variáveis de ambiente e não são disponibilizadas no repositório.

---

## Estrutura do projeto

```text
cardioia-fase5/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css