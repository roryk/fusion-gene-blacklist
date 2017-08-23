This repository has a list of gene:gene pairs which overlap in the genome.
These overlapping genes are more likely to be called as false positives by
fusion gene callers so fusions overlapping these pairs should be treated
skeptically.

1. Download GTF. It must have gene_id and gene_name entries. Ensembl would be a good place to grab a good GTF.
2. Dissect out just the gene entries.

```
grep -v transcript_id Homo_sapiens.GRCh38.89.gtf > Homo_sapiens.GRCh38.89-genesonly.gtf
```

3. Run bedtools intersect to get all overlapping entries:

```bash
bedtools intersect -wao -a Homo_sapiens.GRCh38.89-genesonly.gtf -b Homo_sapiens.GRCh38.89-genesonly.gtf > intersect.tsv
```

4. Run fusion_blacklist.py:

```bash
python scripts/fusion-blacklist.py intersect.tsv | sort | uniq > GRCh38.89-blacklist.csv
```

This will make a CSV file of all gene_idA:gene_idB and gene_nameA:gene_nameB fusions which could be
caused by two genes with overlapping annotations.
