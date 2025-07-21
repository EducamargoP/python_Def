# 🐍 Python_Def — Minha Jornada com Funções em Python

Bem-vindo ao meu repositório! Aqui estou registrando minha evolução no mundo da programação usando Python, com foco especial em **funções**. 💡

## 🚀 Sobre o Projeto

Este repositório é parte da minha jornada de aprendizado, onde estou praticando e entendendo como funções funcionam em Python. Estou explorando:

- Criação e uso de funções personalizadas
- Passagem de parâmetros e retorno de valores
- Casos práticos com lógica de programação
- Exercícios vindos de cursos e plataformas online

## 🎯 Objetivo

Compartilhar meu progresso enquanto aprendo Python com foco em funções — mesmo nos momentos difíceis, estou curtindo demais esse processo! 🧠✨

## 🛠️ Ferramentas de Aprendizado

Estou utilizando:

- 📚 [Udemy](https://www.udemy.com/) — cursos com teoria e exercícios
- 🧩 [HackerRank](https://www.hackerrank.com/) — desafios práticos
- 🤖 Inteligência Artificial — para tirar dúvidas e revisar soluções
- 🐙 GitHub — para registrar e compartilhar minha jornada

## 📂 Estrutura do Repositório


## 🧪 Exemplos de Exercícios

Um dos exercícios que trabalhei foi o clássico `breakingRecords`, onde praticamos a lógica para contar recordes máximos e mínimos de pontuação em uma temporada esportiva.

```python
def breakingRecords(scores):
    max_record = min_record = scores[0]
    max_breaks = min_breaks = 0
    for score in scores[1:]:
        if score > max_record:
            max_record = score
            max_breaks += 1
        elif score < min_record:
            min_record = score
            min_breaks += 1
    return [max_breaks, min_breaks]
## 📝 Lista de Exercícios com Funções em Python

| Nº | Título do Exercício            | Foco Principal                         | Status         |
|----|-------------------------------|----------------------------------------|----------------|
| 01 | `breakingRecords`             | Análise de recordes máximos e mínimos | ✅ Concluído   |
| 02 | `soma_elementos_lista`        | Somar elementos em uma lista           | ⏳ Em andamento |
| 03 | `maior_valor_lista`           | Encontrar o maior valor                | ⏳ Em andamento |
| 04 | `palindromo_check`            | Verificar se uma palavra é palíndromo | ❌ A iniciar    |
| 05 | `calcular_media`              | Média de números da lista              | ❌ A iniciar    |
| 06 | `fatorial`                    | Cálculo de fatorial                    | ❌ A iniciar    |
| 07 | `verificar_primo`             | Teste de número primo                  | ❌ A iniciar    |
| 08 | `contador_letras`             | Contar letras em uma string            | ❌ A iniciar    |
| 09 | `frequencia_elementos`        | Frequência de elementos em lista       | ❌ A iniciar    |
| 10 | `gerar_tabuada`               | Tabuada com função                     | ❌ A iniciar    |
