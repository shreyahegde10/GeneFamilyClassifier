### an example for extracting data using biomart ###########
from biomart import BiomartServer


server = BiomartServer("http://www.ensembl.org/biomart")
print("Connected to BioMart")

### Accessimg human genome dataset##############
dataset = server.datasets['hsapiens_gene_ensembl']

metadata_attributes = [
    'ensembl_gene_id',        # Ensembl Gene ID
    'ensembl_transcript_id',  # Transcript ID
    'external_gene_name',     # Gene Name
    'description',            # Gene Description
    'transcript_source'       # Source of transcript
]

print("Querying metadata...")
metadata_response = dataset.search({
    'attributes': metadata_attributes,
    'filters': {}
})

# ###################Parse data into a dictionary ####### ########
metadata = {}
for line in metadata_response.iter_lines(decode_unicode=True):
    fields = line.split("\t")
    if len(fields) < 5:
        continue
    ensembl_gene_id, transcript_id, gene_name, description, source = fields
    metadata[transcript_id] = {
        'gene_id': ensembl_gene_id,
        'gene_name': gene_name,
        'description': description,
        'source': source,
    }

print(f"Retrieved metadata for {len(metadata)} transcripts.")

sequence_attributes = [
    'ensembl_transcript_id',  # Transcript ID
    'cdna'                    # Coding DNA Sequence
]

print("Querying sequences...")
sequence_response = dataset.search({
    'attributes': sequence_attributes,
    'filters': {}
})


sequences = {}
for line in sequence_response.iter_lines(decode_unicode=True):
    fields = line.split("\t")
    if len(fields) < 2:
        continue
    transcript_id, cds_sequence = fields
    sequences[transcript_id] = cds_sequence

print(f"Retrieved sequences for {len(sequences)} transcripts.")


output_file = "human_cds_sequences.fasta"
with open(output_file, 'w') as fasta_file:
    for transcript_id, cds_sequence in sequences.items():
        if transcript_id in metadata:
            meta = metadata[transcript_id]
            header = (f">Gene:{meta['gene_name']} | Description:{meta['description']} | "
                      f"Source:{meta['source']} | Transcript:{transcript_id}")
            fasta_file.write(f"{header}\n{cds_sequence}\n")

print(f"FASTA file saved as {output_file}")
