# Mini simulador de armazenamento de dados

# ---- / / ---- / / ---- / / ---- / / ---

# 1. Estrutura dos dados:
meu_aprendizado = {
    "Linguagem Principal": "Python",
    "Banco de dados": "SQL",
    "Foco Atual": "Estruturas de Dados e Lógica",
}

# 2. Exiição das informações:
def exibir_status_estudos(dados):
  # Um print vazio cria uma linha em branco
  print()
  print ( "=" * 50 )
  print ("    STATUS DE APRENDIZADO - DNC ANDRADE   ")
  print()
  print (" ---- / / --- / / ---- / / ---- / / ----")
  print()

  for chave, valor in dados.items():
       print (f" 📌 { chave.ljust(20)}: {valor}")
       print()

# 3. Execução da função:
exibir_status_estudos(meu_aprendizado)
