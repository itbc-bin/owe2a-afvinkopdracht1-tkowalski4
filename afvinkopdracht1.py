def dna_error(r):
    print("deze sequentie is geen dna")

def enzyme_error(o):
    print("Het bestand met enzymen kan niet gevonden worden")
    raise SystemExit

def file_yerror(e):
    print("De bestandsnaam is fout, dit bestand kan namelijk niet gevonden worden")
    raise SystemExit


def knipt(seqs,index,zoekwoord):
    try:
        enzymen = open("enzymens.txt")
    except Exception as o:
        enzyme_error(o)
    enzym_list = []
    i=0
    for regel in enzymen:
        enzym, seq = regel.split()
        seq = seq.replace("^","")
        for seq_index in range(0, len(seqs[index])):
            if seqs[index][seq_index:len(seq)+seq_index] == seq:
                if enzym not in enzym_list:
                    enzym_list.append(enzym)
    print("Deze restrictie enzymen knippen in de sequentie die bij het zoekwoord",zoekwoord,"hoort:")
    while i < len(enzym_list):
        print(enzym_list[i])
        i += 1


def is_dna(seqs,index):
    aantalg = int(seqs[index].count("G"))
    aantalc = int(seqs[index].count("C"))
    aantala = int(seqs[index].count("A"))
    aantalt = int(seqs[index].count("T"))
    totaal = aantalg + aantalc + aantala + aantalt
    #print(totaal)
    #print(len(seqs[index]))
    isDNA= False
    try:
        if totaal == len(seqs[index]):
    except Exception as r:
        dna_error(r)
    isDNA = True
    return isDNA


def lees_inhoud(bestands_naam):
    try:
        bestand = open(bestands_naam, "r")
    except Exception as e:
        file_error(e)
    
    headers = []
    seqs = []
    seq=""
    for line in bestand:
        if line.startswith(">"):
            line = line.replace("\n","")
            headers.append(line)
            if seqs != "":
                seqs.append(seq)
                seq = ""

        else:
            line = line.replace("\n","")
            seq += line
            seqs.append(seq)
    seqs.remove('')
    return headers, seqs


def main():
    bestand = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fasta"
    zoekwoord = input("Geef een zoekwoord op: ")

    headers, seqs = lees_inhoud(bestand)

    lijstZoekwoord = [i for i, s in enumerate(headers) if zoekwoord in s]
    i=0
    index = 0
    print("Het aantal keer dat het zoekwoord voorkomt in de headers is:",len(lijstZoekwoord))
    print("In deze headers staat het zoekwoord:",lijstZoekwoord)


    for item in lijstZoekwoord:
        print(60*"-")
        index = int(lijstZoekwoord[i])
        isDNA = is_dna(seqs, index)
        print("Dit is de header die bij de sequentie hoort:")
        print(headers[index])
        knipt(seqs,index,zoekwoord)
        if isDNA == True:
            print("Het is een DNA sequentie.")
        else:
            print("Het is geen DNA sequentie of er zitten andere tekens dan alleen ATCG in.")
            i+=1

main()
