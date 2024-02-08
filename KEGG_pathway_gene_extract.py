from bioservices import KEGG
import pandas as pd

# Create a KEGG object
k = KEGG()

# Replace "mmu03320" with the desired KEGG pathway ID
pathway_id = "mmu03320"

# Get the pathway information
pathway_info = k.get(pathway_id)

# Parse the pathway information for gene IDs
genes = k.parse(pathway_info)

# Extract gene IDs and gene names
genes_data = []
for gene_id, gene_info in genes['GENE'].items():
    gene_name = gene_info.split(';')[0]  # This splits the description and takes the gene name
    genes_data.append({'GeneID': gene_id, 'GeneName': gene_name})

# Convert to DataFrame
genes_df = pd.DataFrame(genes_data)

# Save the DataFrame to a CSV file
csv_file_path = f'KEGG_{pathway_id}_ppar_genes.csv'
genes_df.to_csv(csv_file_path, index=False)
