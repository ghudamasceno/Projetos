# Analisador de Logs – Projeto #1

Este projeto faz parte do meu **plano de estudos de Segurança da Informação**.
O objetivo é criar um **script em Python** que analisa o arquivo `/var/log/auth.log` em sistemas Linux e gera alertas simples sobre tentativas de autenticação.

---

## Objetivo

* Ler o arquivo de autenticação do sistema (`/var/log/auth.log`).
* Identificar padrões comuns de segurança:

  * Tentativas de senha incorreta
  * Usuários inválidos
  * Login root bem-sucedido
* Gerar um relatório simples com as contagens.

---

## Tecnologias utilizadas

* **Python 3**
* **Linux (Ubuntu/Kali/Debian)**
* Módulo padrão `re` (expressões regulares)

---

## Estrutura do projeto

```
projeto-log-analyzer/
├── log_analyzer.py   # Script principal
└── README.md         # Documentação
```

---

## Como executar

1. Clone ou copie este repositório:

   ```bash
   git clone https://github.com/seu-usuario/projeto-log-analyzer.git
   cd projeto-log-analyzer
   ```

2. Dê permissão de execução ao script:

   ```bash
   chmod +x log_analyzer.py
   ```

3. Execute com privilégios de administrador (necessário para acessar `/var/log/auth.log`):

   ```bash
   sudo ./log_analyzer.py
   ```

---

## 📖 Exemplo de saída esperada

```bash
🔍 Resultados da análise de logs:

- Falhas de senha: 12
- Usuário inválido: 5
- Sucesso root: 1
```

---

