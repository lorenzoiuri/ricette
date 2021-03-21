#!/usr/bin/python3

import sys, os

def print_usage():
    print("*** Usage ***")
    print(str(sys.argv[0]) + " input_file.txt > output_file.tex")
    
def valid_file(arg):
    return (os.path.exists(arg) and os.path.isfile(arg))

def make_latex(title, persone, preparazione, cottura, costo, ing_list, steps_list):
    
    # number of steps for a Large font size
    max_steps = 5
    max_ingr = 8
    
    print("\chapter{"+ title +"}")
    print("\infotable{" + persone + "}{" + preparazione + " minuti}{"+ cottura + " minuti}{" + costo + "}")
    
    if len(steps_list) > max_steps or len(ing_list) > max_ingr:
        print("\large")
    else:
        print("\Large")
    
    print("\section*{Ingredienti}")
    
    print("\\begin{ingredients}")
    for item in ing_list:
        print("\item " + item)
    print("\end{ingredients}")
    
    print("\section*{Preparazione}")
    print("\\vspace{16pt}")
    
    print("\\begin{enumerate}")
    for item in steps_list:
        print("\item " + item)  
    print("\end{enumerate}")
    print("\\normalsize")
    
def main(arg):
    if not valid_file(arg):
        print("Error: Input file is not valid")
        exit()
    f = open(arg, "r")
    lines_ = f.readlines()
    
    # removing empty lines and trailing newline
    lines = []
    for line in lines_:
        if (line == '\n'): continue
        lines.append(line.strip())
    
    # recipe title
    title = lines[0]
    #print(title)
    
    # dettagli
    persone = lines[1].split()[2]
    preparazione = lines[2].split()[2]
    cottura = lines[3].split()[2]
    costo = lines[4].split()[2]
    
    # ingredienti
        
    i = 6
    ing_list = []
    while(lines[i][0] == "-"):
        ing_list.append(lines[i][1:].lstrip())
        i+=1
    
    # preparazione
    i+=1
    steps_list = []
    while( (i < len(lines) and (lines[i][0] == "-") ) ):
        steps_list.append(lines[i][1:].lstrip())
        i+=1
        
    make_latex(title, persone, preparazione, cottura, costo, ing_list, steps_list)
    
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        exit()
    main(sys.argv[1])
