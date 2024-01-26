# Agora project


First lets change name to the orthologues

```
cd /home/PERSONALE/alessand.formaggion2/Results_Jan31_bivalve_only/Orthogroups
c=1; for b in `awk -F ":" '{print$2}' Orthogroups_selected.txt`; do zero=""; for a in `seq 1 $(( 15 - $(echo $c | wc -c) ))`; do zero=$zero"0"; done; echo -e $b'\t'${b:0:4}$zero$c; c=$(( c+1 )); done > change_name.list
```
Modifying the file for AGORA input
```
cat ../Orthogroups/change_name.list | while read -r a; do uno=`echo $a | awk '{print$1}'`; due=`echo $a | awk '{print$2}'`; sed -i "s/$uno/$due/g" Gene_list_BP/genes.${due:0:4}.list; sed -i "s/$uno/$due/g" trees_reconciliated_2.nhx; done
```

Modifying the file for Generax input
```
cd /home/PERSONALE/alessand.formaggion2/Results_Jan31_bivalve_only/01_generax
cat /home/PERSONALE/alessand.formaggion2/Results_Jan31_bivalve_only/Orthogroups/change_name.list | while read -r a; do uno=`echo $a | awk '{print$1}'`; due=`echo $a | awk '{print$2}'`; ortho=`grep -w $uno /home/PERSONALE/alessand.formaggion2/Results_Jan31_bivalve_only/Orthogroups/Orthogroups_selected.txt | awk -F ":" '{print$1}'` ;sed -i "s/$uno/$due/g" 01_alignments/${ortho}_tree*.fna; done

```
```
for a in  `cat species_list.txt`;
 do grep -h -A1 ">"$a Selected_orthogroup/Orthogroup_Sequences/*.fa |  awk -F "_" '{if (substr($1,0,1) == ">") {print$1i++} else {print$1}}' > Selected_orthogroup/Orthogroup_Sequences/${a}.fasta
```


