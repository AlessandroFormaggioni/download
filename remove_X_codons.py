from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#Launch this script in /home/STUDENTI/oscar.wallnoefer/01_squamata/01_oxphos_nucleari/02_protein_profiles/OXPHOS_nuclear

#gene_list is a file with the list of genes
with open("gene_list") as f:
    content = f.read().splitlines()

for gene in content:

    b=[a for a in SeqIO.parse("nt_mod/"+gene+".fasta","fasta")]
    aa_list=[]
    nt_list=[]


    for nt in b:
        #some seq have 
        if len(nt.seq)%3 != 0:
            diff=len(nt.seq)%3
            nt.seq=nt.seq[:-diff]
        nt.seq=
        aa=nt.seq.translate()
        while aa.find("*") != -1:
            pos=aa.find("*")
            nt.seq=nt.seq[0:pos*3]+ nt.seq[(pos+1)*3:]
            aa=nt.seq.translate()    
        while aa.find("X") != -1:
            pos=aa.find("X")
            nt.seq=nt.seq[0:pos*3]+ nt.seq[(pos+1)*3:]
            aa=nt.seq.translate()
        aa_list.append(SeqRecord(aa, id=nt.id, description="", name=""))
        nt_list.append(SeqRecord(nt.seq, id=nt.id, description="", name="" ))
    SeqIO.write(aa_list,"aa/"+gene+".fasta","fasta")
    SeqIO.write(nt_list,"nt/"+gene+".fasta","fasta")