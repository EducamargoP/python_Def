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

- `/exercicios`: arquivos com os desafios resolvidos  
- `/notas`: anotações e insights do processo de aprendizado  
- `README.md`: este documento que resume o projeto  

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

| Nº  | Exercício               | Foco Principal                              |
|-----|-------------------------|---------------------------------------------|
| 01  | `breakingRecords`       | Recordes em sequência                       |
| 02  | `soma_elementos_lista`  | Soma dos elementos em uma lista             |
| 03  | `maior_valor_lista`     | Encontrar o maior valor em uma lista        |
| 04  | `palindromo_check`      | Verificar se uma palavra é palíndromo       |
| 05  | `calcular_media`        | Média dos números em uma lista              |
| 06  | `fatorial`              | Cálculo de fatorial                         |
| 07  | `verificar_primo`       | Verificar se um número é primo              |
| 08  | `contador_letras`       | Contar letras em uma string                 |
| 09  | `frequencia_elementos`  | Frequência de elementos em lista            |
| 10  | `gerar_tabuada`         | Tabuada com função e retorno de resultados  |
| 11  | `adivinhe`              | Jogo interativo com while e input           |
| 12  | `data_por_extenso`      | Conversão de data para formato textual      |
| 13  | `soma_pares`            | Soma de números pares                       |
| 14  | `dobro_valor`           | Retorna o dobro de um número inteiro        |

🚧 Este projeto está sempre em construção — cada função nova é mais um passo rumo à maestria em Python. 🧠✨
