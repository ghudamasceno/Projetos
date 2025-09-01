#!/usr/bin/env python3
import re

# Arquivo de log a ser analisado
LOG_FILE = "/var/log/auth.log"

# Padrões de interesse (regex)
patterns = {
    "Falhas de senha": r"Failed password",
    "Usuário inválido": r"Invalid user",
    "Sucesso root": r"Accepted password for root"
}

def analyze_log():
    results = {key: 0 for key in patterns}  # inicializa contadores

    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                for key, pattern in patterns.items():
                    if re.search(pattern, line):
                        results[key] += 1

        # Exibe resultados
        print("\n🔍 Resultados da análise de logs:\n")
        for key, count in results.items():
            print(f"- {key}: {count}")

    except PermissionError:
        print("❌ Permissão negada! Rode o script com sudo.")
    except FileNotFoundError:
        print(f"❌ Arquivo {LOG_FILE} não encontrado!")
    except Exception as e:
        print(f"⚠️ Erro inesperado: {e}")

if __name__ == "__main__":
    analyze_log()
