"""
License: Apache
Organization: UNIR
"""

import os
import sys
import argparse

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(words, remove_duplicates=False):
    if remove_duplicates:
        words = list(set(words))  # Eliminar duplicados

    sorted_words = sorted(words)
    return items

def remove_duplicates_from_list(items):
    return list(set(items))

def main():
    parser = argparse.ArgumentParser(description='Ordenar e imprimir una lista de palabras.')
    parser.add_argument('words', nargs='+', help='Palabras para ordenar e imprimir.')
    parser.add_argument('--remove-duplicates', action='store_true', help='Eliminar duplicados antes de imprimir.')
    args = parser.parse_args()

    words = args.words
    if args.remove_duplicates:
        words = list(set(words))  # Eliminar duplicados

    sorted_words = sort_list(words, remove_duplicates=args.remove_duplicates)
    print(sorted_words)

if __name__ == '__main__':
    main()
