"""
License: Apache
Organization: UNIR
"""

import os
import sys
import argparse

from googletrans import Translator
import argparse


DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

# Ordena la lista según la opción proporcionada


def sort_list(items, ascending=False):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))


def translate_to_english(text):
        translator = Translator()
        translation = translator.translate(text, src='es', dest='en')
    return translation.text

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print(translate_to_english("Se debe indicar el fichero como primer argumento"))
        print(translate_to_english("El segundo argumento indica si se quieren eliminar duplicados"))
        print(translate_to_english("El tercer argumento indica si el orden debe ser ascendente"))
        sys.exit(1)

    print(translate_to_english(f"Se leerán las palabras del fichero {filename}"))
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(translate_to_english(f"El fichero {filename} no existe"))
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]


    sorted_words = sort_list(words, remove_duplicates=args.remove_duplicates)
    print(sorted_words)

if __name__ == '__main__':
    main()
