import os
import time
import sys
from PyPDF2 import PdfMerger
from colorama import Fore, Style, init

init(autoreset=True)


def print_banner():

    print(Fore.RED + r"""

 _______  ______   _______    _______  _______  _______  _______  _______  _______ 
(  ____ )(  __  \ (  ____ \  (       )(  ____ \(  ____ )(  ____ \(  ____ \(  ____ )
| (    )|| (  \  )| (    \/  | () () || (    \/| (    )|| (    \/| (    \/| (    )|
| (____)|| |   ) || (__      | || || || (__    | (____)|| |      | (__    | (____)|
|  _____)| |   | ||  __)     | |(_)| ||  __)   |     __)| | ____ |  __)   |     __)
| (      | |   ) || (        | |   | || (      | (\ (   | | \_  )| (      | (\ (   
| )      | (__/  )| )        | )   ( || (____/\| ) \ \__| (___) || (____/\| ) \ \__
|/       (______/ |/         |/     \|(_______/|/   \__/(_______)(_______/|/   \__/                                                                                

""" + Style.RESET_ALL)

    print(Fore.RED + "Coded By : Subir Sutradhar | Version : 1.0\n" + Style.RESET_ALL)


def merging_animation():
    frames = ["[=     ]", "[==    ]", "[===   ]", "[====  ]", "[===== ]", "[======]"]
    for i in range(18):
        frame = frames[i % len(frames)]
        sys.stdout.write(Fore.RED + "\rMerging PDF files " + frame)
        sys.stdout.flush()
        time.sleep(0.12)
    print()


def merge_pdfs(sort_order='asc', output_filename='merged.pdf'):

    input_folder = "./input_pdfs"
    output_folder = "./output"

    if not os.path.exists(input_folder):
        print(Fore.RED + "[❌] input_pdfs folder missing!")
        return

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

    if not pdf_files:
        print(Fore.RED + "[x] No PDF files found in input_pdfs!")
        return

    if sort_order == "asc":
        pdf_files.sort()
    elif sort_order == "desc":
        pdf_files.sort(reverse=True)
    else:
        print(Fore.RED + "[x] Invalid sort order! Use asc or desc")
        return

    merger = PdfMerger()

    print(Fore.YELLOW + "\nStarting merge...\n")
    merging_animation()

    for pdf in pdf_files:
        merger.append(f"{input_folder}/{pdf}")

    merger.write(f"{output_folder}/{output_filename}")
    merger.close()

    print(Fore.GREEN + "\n[#] Merge Complete!")
    print(Fore.CYAN + f"[#] Saved as: {output_folder}/{output_filename}")
    print(Fore.MAGENTA + f"[#] Merged in this order:\n{pdf_files}\n")


if __name__ == "__main__":

    print_banner()

    print(Fore.CYAN + "Sorting order? asc / desc")
    order = input("> ").lower()

    print(Fore.CYAN + "\nEnter output file name (with .pdf):")
    filename = input("> ")

    merge_pdfs(order, filename)
