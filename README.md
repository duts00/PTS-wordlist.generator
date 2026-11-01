# Wordlist.py — Gerador de Wordlists para Estudo

Script em Python 3 para geração de wordlists, desenvolvido exclusivamente para fins educacionais e de estudo em segurança da informação. O objetivo é demonstrar, de forma didática, como combinações de palavras, números, símbolos e variações de escrita ampliam de maneira exponencial o espaço de busca de senhas — e, a partir disso, compreender como construir senhas resistentes.

---

## Aviso Legal

Este código destina-se apenas a estudo em ambientes autorizados (laboratórios, CTFs e testes com permissão explícita). O uso de wordlists contra sistemas, contas ou serviços de terceiros sem autorização formal por escrito constitui crime (no Brasil, Lei 12.737/2012 e Marco Civil da Internet). O autor não se responsabiliza por uso indevido.

---

## Visão Geral

O `Wordlist.py` implementa técnicas clássicas de geração de wordlists com finalidade didática. A partir de uma lista de palavras-base, o script aplica camadas sucessivas de transformação (substituições leet, variações de capitalização, sufixos numéricos e de símbolos) e demonstra o impacto combinatório dessas variações.

O script prioriza clareza e aprendizado, não desempenho: não foi otimizado para grandes volumes nem para uso em produção.

Conceitos exercitados:

- Substituições do tipo *leet speak*
- Geração combinatória com `itertools`
- Manipulação de strings
- Controle de duplicatas com `set`
- Impacto exponencial de combinações simples

---

## Como Funciona

A partir de uma lista de palavras-base fornecida por arquivo, o script gera variações aplicando as etapas a seguir.

### 1. Entrada

Um arquivo de texto com uma palavra por linha; cada palavra é a base para a geração de variações.

```
admin
senha
user
```

### 2. Substituições Leet

Alguns caracteres são substituídos por equivalentes visuais comuns:

| Letra | Variações |
|-------|-----------|
| a | a, @, 4 |
| e | e, 3 |
| i | i, 1 |
| o | o, 0 |
| s | s, $, 5 |
| l | l, 1 |

Exemplo: `admin` gera variações como `adm1n`, `@dm1n`, `4dm1n`, conforme as combinações.

### 3. Variações de Capitalização

Cada palavra (já com leet aplicado) passa por combinações de letras maiúsculas e minúsculas.

Exemplo: `admin`, `Admin`, `aDmin`, `ADMIN`, entre outras.

### 4. Sufixos Numéricos

São adicionados ao final da palavra, refletindo padrões reais de senhas fracas:

- Nenhum número
- Números de 0 a 9999
- Anos de 1970 até o ano atual
- Sequências comuns: `123`, `1234`, `123456`, `0123456789`

### 5. Sufixos com Símbolos

Símbolos comuns (`!`, `@`, `#`, `$`, `%`) aplicados como símbolo único, repetição (`!!`, `###`, `$$$`) e combinações de dois símbolos.

### 6. Combinação de Símbolos e Números

Gera variações como `admin!123`, `senha@2023`, `user##99`. Esta etapa aumenta de forma significativa o total de combinações.

### 7. Controle de Duplicatas

As variações são armazenadas em um `set`, garantindo que apenas valores únicos sejam impressos na saída.

---

## Uso

### Requisitos

- Python 3.x

### Execução

```bash
python3 Wordlist.py palavras.txt > wordlist.txt
```

Onde:

- `palavras.txt` — arquivo de entrada (uma palavra-base por linha)
- `wordlist.txt` — wordlist gerada

### Tornar executável (opcional)

```bash
chmod +x Wordlist.py
```

---

## Saída

- A saída é impressa diretamente no `stdout`, uma senha por linha.
- O formato é ideal para redirecionamento para arquivo, como no exemplo de uso acima.

---

## Limitações Conhecidas

As limitações abaixo são intencionais — o foco é o aprendizado, não a eficiência.

- Crescimento exponencial muito rápido do número de combinações
- Alto consumo de CPU e memória com palavras longas
- Sem limite configurável de geração
- Sem argumentos de linha de comando avançados

---

## Sugestões de Melhoria (exercícios)

- Adicionar argumentos de CLI com `argparse`
- Permitir ativar/desativar módulos (leet, números, símbolos)
- Definir limite máximo de geração
- Suporte a prefixos, além de sufixos
- Escrita direta em arquivo com controle de buffer
- Uso de `multiprocessing` para estudo de paralelismo

---

## Boas Práticas e Ética

- Utilizar apenas em laboratórios, CTFs ou ambientes autorizados.
- Nunca usar em sistemas reais sem permissão formal.
- Wordlists podem conter dados sensíveis — armazená-las com cuidado.

---

## Nota Final

Este é um estudo prático de Python aplicado à segurança, criado para compreender como pequenas variações humanas na criação de senhas podem ser exploradas — e, principalmente, como evitá-las. Conhecer o problema é o primeiro passo para resolvê-lo.

---

Desenvolvido por duts00 — projeto de estudo em segurança da informação
