# Wordlist.py — Gerador de Wordlists para Estudo

## 📌 Visão geral

Este projeto contém o script **Wordlist.py**, escrito em **Python 3**, desenvolvido **exclusivamente para fins educacionais e de estudo em cursos** relacionados a:

* Segurança da informação
* Testes de força bruta controlados
* Entendimento de padrões comuns de criação de senhas
* Programação em Python aplicada à automação

O script implementa, de forma didática, diversas técnicas clássicas utilizadas na geração de wordlists, permitindo ao estudante compreender **como combinações de palavras, números, símbolos e variações de escrita aumentam drasticamente o espaço de busca de senhas**.

> ⚠️ **Aviso importante**: este código é apenas para estudo em ambientes autorizados. Não utilize para atacar sistemas, contas ou serviços sem permissão explícita.

---

## 🎯 Objetivo educacional

O objetivo principal do **Wordlist.py** é demonstrar:

* Como funcionam substituições do tipo *leet speak*
* Geração combinatória com `itertools`
* Manipulação de strings
* Controle de duplicatas
* Impacto exponencial de combinações simples

O script não foi otimizado para grandes volumes de dados nem para uso em produção. Ele prioriza **clareza e aprendizado**, não performance.

---

## 🧠 Como o script funciona

A partir de uma lista de palavras-base (fornecida via arquivo), o script gera variações aplicando múltiplas camadas de transformação.

### 1️⃣ Entrada

* Um arquivo de texto contendo **uma palavra por linha**
* Cada palavra representa uma base para geração de variações

Exemplo:

```
admin
senha
user
```

---

### 2️⃣ Substituições Leet (leet speak)

Alguns caracteres são substituídos por equivalentes visuais comuns:

| Letra | Variações |
| ----- | --------- |
| a     | a, @, 4   |
| e     | e, 3      |
| i     | i, 1      |
| o     | o, 0      |
| s     | s, $, 5   |
| l     | l, 1      |

Exemplo:

```
admin → adm1n, @dm1n, adm!n (dependendo das combinações)
```

---

### 3️⃣ Variações de maiúsculas e minúsculas

Cada palavra (já com leet aplicado) passa por todas as combinações possíveis de:

* Letras minúsculas
* Letras maiúsculas

Exemplo:

```
admin → admin, Admin, aDmin, ADMIN, etc.
```

---

### 4️⃣ Sufixos numéricos

São adicionados ao final da palavra:

* Nenhum número
* Números de 0 a 9999
* Anos de 1970 até o ano atual
* Sequências comuns como:

  * 123
  * 1234
  * 123456
  * 0123456789

Isso reflete padrões reais observados em senhas fracas.

---

### 5️⃣ Sufixos com símbolos

São utilizados símbolos comuns:

```
!, @, #, $, %
```

Aplicados como:

* Símbolo único
* Repetição (!!, ###, $$$)
* Combinações de dois símbolos

---

### 6️⃣ Combinação símbolos + números

O script também gera combinações do tipo:

```
admin!123
senha@2023
user##99
```

Essa etapa aumenta significativamente o número final de variações.

---

### 7️⃣ Controle de duplicatas

Para evitar repetição:

* Todas as senhas geradas são armazenadas em um `set`
* Apenas valores únicos são impressos

Isso garante consistência na wordlist final.

---

## ▶️ Uso

### Requisitos

* Python 3.x

### Tornar executável (opcional)

```
chmod +x Wordlist.py
```

### Execução

```
python3 Wordlist.py palavras.txt > wordlist.txt
```

Onde:

* `palavras.txt` → arquivo de entrada
* `wordlist.txt` → wordlist gerada

---

## 📤 Saída

* A saída é impressa diretamente no **stdout**
* Cada linha contém **uma senha gerada**
* Ideal para redirecionamento para arquivo

---

## ⚠️ Limitações conhecidas

* Crescimento exponencial muito rápido
* Alto consumo de CPU/RAM com palavras longas
* Não há limite configurável de geração
* Não possui argumentos avançados (flags)

Essas limitações são **intencionais**, pois o foco é o aprendizado e não eficiência extrema.

---

## 💡 Sugestões de melhorias (exercícios)

* Adicionar argumentos CLI (`argparse`)
* Permitir ativar/desativar módulos (leet, números, símbolos)
* Definir limites máximos de geração
* Suporte a prefixos
* Escrita direta em arquivo com controle de buffer
* Uso de multiprocessing para estudo de paralelismo

---

## 🧪 Boas práticas e ética

* Utilize apenas em **laboratórios**, **CTFs** ou ambientes autorizados
* Não use em sistemas reais sem permissão
* Wordlists podem conter dados sensíveis — cuide do armazenamento

---

## 📚 Nota final

Este projeto é um **estudo prático de Python aplicado à segurança**, criado para compreender como pequenas variações humanas na criação de senhas podem ser exploradas — e, mais importante, **como evitá-las**.

Conhecer o problema é o primeiro passo para resolvê-lo.
