

for i in 1 2 3 4; do paste site-${i}_fragment-hits.openeye.smi site-${i}_fragment-hits.ids > site-${i}_fragment-hits.openeye.csv ; done

  585  cut -f 1 -d , site-1_fragment-hits.csv  > site-1_fragment-hits.ids
  586  cut -f 1 -d , site-2_fragment-hits.csv  > site-2_fragment-hits.ids
  587  cut -f 1 -d , site-3_fragment-hits.csv  > site-3_fragment-hits.ids
  588  cut -f 1 -d , site-4_fragment-hits.csv  > site-4_fragment-hits.ids

  575  convert.py site-1_fragment-hits.smi site-1_fragment-hits.openeye.smi
  576  convert.py site-2_fragment-hits.smi site-2_fragment-hits.openeye.smi
  577  convert.py site-3_fragment-hits.smi site-3_fragment-hits.openeye.smi
  578  convert.py site-4_fragment-hits.smi site-4_fragment-hits.openeye.smi

  571  cut -f 2 -d , site-1_fragment-hits.csv > site-1_fragment-hits.smi
  572  cut -f 2 -d , site-2_fragment-hits.csv > site-2_fragment-hits.smi
  573  cut -f 2 -d , site-3_fragment-hits.csv > site-3_fragment-hits.smi
  574  cut -f 2 -d , site-4_fragment-hits.csv > site-4_fragment-hits.smi


for i in 1 2 3 4; do paste -d , site-${i}_fragment-hits.openeye.smi site-${i}_fragment-hits.ids > site-${i}_fragment-hits.openeye.csv ; done

