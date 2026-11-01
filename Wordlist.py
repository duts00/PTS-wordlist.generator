#!/usr/bin/env python3
"""
Wordlist.py - Gerador de wordlists para estudo de seguranca da informacao.

Uso autorizado apenas: laboratorios, CTFs e testes com permissao explicita.

Exemplos:
    python3 Wordlist.py palavras.txt
    python3 Wordlist.py palavras.txt -o wordlist.txt
    python3 Wordlist.py palavras.txt --leet --numbers --max 100000
    python3 Wordlist.py palavras.txt --no-symbols --case capitalize
"""

import sys
import argparse
import itertools
import datetime

YEAR = datetime.datetime.now().year

# Mapa de substituicoes leet (um caractere -> varios equivalentes visuais)
LEET = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    'l': ['l', '1'],
}

SYMBOLS = ['!', '@', '#', '$', '%']


def leet_all(word):
    """Gera todas as variacoes leet de uma palavra."""
    pools = [LEET.get(c, [c]) for c in word.lower()]
    for combo in itertools.product(*pools):
        yield ''.join(combo)


def case_variants(word, mode):
    """Gera variacoes de maiusculas/minusculas conforme o modo escolhido.

    - 'realistic' (padrao): apenas os padroes que humanos usam de verdade
      (minuscula, Primeira maiuscula, TUDO MAIUSCULO). Poucas variacoes.
    - 'all': todas as 2^n combinacoes (explode rapido; use com cuidado).
    - 'none': mantem a palavra como esta.
    """
    if mode == 'none':
        yield word
    elif mode == 'all':
        pools = [[c.lower(), c.upper()] for c in word]
        for combo in itertools.product(*pools):
            yield ''.join(combo)
    else:  # realistic
        variantes = {word.lower(), word.capitalize(), word.upper()}
        for v in variantes:
            yield v


def number_suffixes():
    """Sufixos numericos comuns em senhas fracas."""
    yield ''
    for i in range(0, 10000):
        yield str(i)
    for y in range(1970, YEAR + 1):
        yield str(y)
    for seq in ('123', '1234', '123456', '0123456789'):
        yield seq


def symbol_suffixes():
    """Sufixos de simbolos: unico, repetido e pares."""
    yield ''
    for s in SYMBOLS:
        yield s
        yield s * 2
        yield s * 3
    for combo in itertools.product(SYMBOLS, repeat=2):
        yield ''.join(combo)


def build_suffixes(use_numbers, use_symbols):
    """Monta o conjunto de sufixos conforme os modulos ativos."""
    yield ''  # sempre inclui "sem sufixo"
    if use_numbers:
        for n in number_suffixes():
            if n:
                yield n
    if use_symbols:
        for s in symbol_suffixes():
            if s:
                yield s
    if use_numbers and use_symbols:
        for s in symbol_suffixes():
            if not s:
                continue
            for n in number_suffixes():
                if n:
                    yield s + n


def generate(word, args):
    """Gera as variacoes de uma palavra-base, respeitando os modulos escolhidos."""
    seen = set()
    leet_source = leet_all(word) if args.leet else [word.lower()]
    for base in leet_source:
        for cased in case_variants(base, args.case):
            for suf in build_suffixes(args.numbers, args.symbols):
                pwd = cased + suf
                if pwd not in seen:
                    seen.add(pwd)
                    yield pwd


def parse_args():
    parser = argparse.ArgumentParser(
        description="Gerador de wordlists para estudo de seguranca (uso autorizado apenas).",
        epilog="Exemplo: python3 Wordlist.py palavras.txt --leet --numbers -o saida.txt",
    )
    parser.add_argument("entrada", help="Arquivo de palavras-base (uma por linha)")
    parser.add_argument("-o", "--output", help="Arquivo de saida (padrao: stdout)")
    parser.add_argument("--max", type=int, default=0,
                        help="Numero maximo de senhas a gerar (0 = sem limite)")

    # Modulos: ligados por padrao; use --no-xxx para desligar
    parser.add_argument("--leet", dest="leet", action="store_true", default=True,
                        help="Ativa substituicoes leet (padrao: ativo)")
    parser.add_argument("--no-leet", dest="leet", action="store_false",
                        help="Desativa substituicoes leet")
    parser.add_argument("--numbers", dest="numbers", action="store_true", default=True,
                        help="Ativa sufixos numericos (padrao: ativo)")
    parser.add_argument("--no-numbers", dest="numbers", action="store_false",
                        help="Desativa sufixos numericos")
    parser.add_argument("--symbols", dest="symbols", action="store_true", default=True,
                        help="Ativa sufixos de simbolos (padrao: ativo)")
    parser.add_argument("--no-symbols", dest="symbols", action="store_false",
                        help="Desativa sufixos de simbolos")
    parser.add_argument("--case", choices=["realistic", "all", "none"],
                        default="realistic",
                        help="Modo de capitalizacao (padrao: realistic)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Le as palavras-base, com tratamento de erro amigavel
    try:
        with open(args.entrada, encoding="utf-8") as f:
            bases = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        sys.exit(f"[erro] Arquivo nao encontrado: {args.entrada}")

    if not bases:
        sys.exit("[erro] O arquivo de entrada esta vazio.")

    # Define para onde escrever (arquivo ou stdout)
    out = open(args.output, "w", encoding="utf-8") if args.output else sys.stdout

    total = 0
    try:
        for base in bases:
            for pwd in generate(base, args):
                out.write(pwd + "\n")
                total += 1
                if args.max and total >= args.max:
                    raise StopIteration
    except StopIteration:
        pass
    finally:
        if args.output:
            out.close()

    # Resumo vai para stderr, para nao sujar a wordlist no stdout
    print(f"[ok] {total} senhas geradas a partir de {len(bases)} palavra(s)-base.",
          file=sys.stderr)


if __name__ == "__main__":
    main()
