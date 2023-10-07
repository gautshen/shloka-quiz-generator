#!/usr/bin/python3
import os
import sys
import devtrans
import random
from pylatex import Document, Section, Subsection, Tabular, Command
from pylatex import TextColor, MultiColumn, Tabular, LargeText, MediumText
from pylatex import LineBreak, NewPage, Hyperref, Package
from pylatex.utils import italic, bold, NoEscape, escape_latex

MAXSHLOKA = 100
MAXQUESTIONS=5


def add_table_word(table, word):
    table.add_hline()
    table.add_row((MultiColumn(4, align='|c|', data=""), ))    
    table.add_row((MultiColumn(4, align='|c|', data=LargeText(bold(word))),))
    table.add_row((MultiColumn(4, align='|c|', data=""), ))    
    table.add_hline()

def append_table_options(table, word_options, correct_option, correct_color, other_color):
    color_option = []
    for i in range(0, 4):
        if i == correct_option:
            color_option.append(correct_color)
        else:
            color_option.append(other_color)

    table.add_row((MultiColumn(2, align='|c|', data=""), MultiColumn(2, align='|c|', data=""), ))
    table.add_row((MultiColumn(2, align='|c|', data=TextColor(color_option[0], word_options[0])), MultiColumn(2, align='|c|', data=TextColor(color_option[1], word_options[1])), ))
    table.add_row((MultiColumn(2, align='|c|', data=""), MultiColumn(2, align='|c|', data=""), ))
    table.add_hline()
    table.add_row((MultiColumn(2, align='|c|', data=""), MultiColumn(2, align='|c|', data=""), ))
    table.add_row((MultiColumn(2, align='|c|', data=TextColor(color_option[2], word_options[2])), MultiColumn(2, align='|c|', data=TextColor(color_option[3], word_options[3])), ))
    table.add_row((MultiColumn(2, align='|c|', data=""), MultiColumn(2, align='|c|', data=""), ))
    table.add_hline()
    
def append_table_shloka(table, shloka_arr, correct_paada):
    color_option = []
    for i in range(0, 4):
        if i == correct_paada:
            color_option.append("blue")
        else:
            color_option.append("black")
    table.add_row((MultiColumn(4, align='|c|', data=""), ))
    for i in range(0, 4):
        table.add_row((MultiColumn(4, align='|c|', data=TextColor(color_option[i], shloka_arr[i])), ))
    table.add_row((MultiColumn(4, align='|c|', data=""), ))
    
    table.add_hline()
    

def add_word_page(doc, word):
    doc.append(NewPage())
    table1 = Tabular('|c|c|c|c|')
    add_table_word(table1, word)
    doc.append(table1)

def add_word_options_page(doc, word, options_array, correct_option):
    doc.append(NewPage())
    table1 = Tabular('|c|c|c|c|')
    add_table_word(table1, word)
    append_table_options(table1, options_array, correct_option, "black", "black")
    doc.append(table1)

def add_final_page(doc, word, options_array, shloka_arr, correct_option, correct_paada):
    doc.append(NewPage())
    table1 = Tabular('|c|c|c|c|')
    add_table_word(table1, word)
    append_table_options(table1, options_array, correct_option, "blue", "black")    
    append_table_shloka(table1, shloka_arr, correct_paada)

    doc.append(table1)

def add_pages(doc, word, options_array, shloka_arr, correct_option, correct_paada):
    add_word_page(doc, word)    
    add_word_options_page(doc, word, options_array, correct_option)
    add_final_page(doc, word, options_array, shloka_arr, correct_option, correct_paada)


def generate_quiz(doc, lines):
    shlokanum_options = []
    while len(shlokanum_options) < 4:
        shlokanum = random.randint(0, MAXSHLOKA-1)
        if shlokanum not in shlokanum_options:
            shlokanum_options.append(shlokanum)

    shloka_options_arr = []
    for snum in shlokanum_options:
        shloka_options_arr.append(lines[snum].split(',')[0])
    print(shloka_options_arr)

    correct_option = random.randint(0, 3)
    shlokanum = shlokanum_options[correct_option]
    shloka = lines[shlokanum]
    print(shloka)
    print("[Option %d, SHLOKA %02d] " %(correct_option, shlokanum) + shloka.strip())

    paadas = shloka.split(',')
    print(paadas)
    numpaadas = len(paadas)
    paada_num = random.randint(1, 3)
    print(paada_num)
    paada = paadas[paada_num]
    print("[PAADA  %02d] " %(paada_num), paada.strip())

    words = paada.split()
    num_words = len(words)
    word_num = random.randint(0, num_words - 1)
    print(word_num)
    word = words[word_num]

    print("[SHABDA ] ", word.strip())

    for i in range(0, 4):
        print("[Shloka %d] Option %d: " %(shlokanum_options[i], i) + shloka_options_arr[i])

    print("")
    print("Correct Answer: Option %d: " %(correct_option) + shloka_options_arr[correct_option])
    print("")
    print("Full Shloka:")
    for paada in paadas:
        paada.strip()
        print(paada)

    add_pages(doc, word, shloka_options_arr, paadas, correct_option, paada_num)
    
    

if __name__ == '__main__':    
    filename=sys.argv[1]

    if len(sys.argv) > 2:
        MAXQUESTIONS = int(sys.argv[2])

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    geometry_options = {"tmargin": "1cm", "lmargin": "1cm", "margin": "1cm"}
    doc = Document(geometry_options=geometry_options, documentclass="beamer")
    doc.packages.append(Package('hyperref'))
    
    with doc.create(Section('Titlepage')):
        doc.preamble.append(Command('title', 'Shloka Quiz'))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(r'\maketitle'))

    for i in range(MAXQUESTIONS):
        generate_quiz(doc, lines)
    doc.generate_pdf('Shloka-Quiz', clean_tex=True, clean=True)
