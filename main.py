# DNA and RNA mappings for the alphabet (made by-paramsoni)
dna_map = {
    'a': 'ATG', 'b': 'CGT', 'c': 'GCA', 'd': 'TAC', 'e': 'GTT',
    'f': 'ACT', 'g': 'CAG', 'h': 'GAT', 'i': 'TGA', 'j': 'CAT',
    'k': 'AGC', 'l': 'TGC', 'm': 'GCG', 'n': 'TAG', 'o': 'GGA',
    'p': 'GAC', 'q': 'TTC', 'r': 'CCA', 's': 'CTG', 't': 'GCT',
    'u': 'AGT', 'v': 'TAA', 'w': 'GTC', 'x': 'CGC', 'y': 'TAT',
    'z': 'GTA', ' ': '---'  # Using '---' for spaces in sentences
}

# RNA mapping is the same except 'T' is replaced by 'U'
rna_map = {k: v.replace('T', 'U') for k, v in dna_map.items()}

# Function to convert text to DNA
def text_to_dna(text):
    dna_sequence = ''.join([dna_map[char] for char in text.lower() if char in dna_map])
    return dna_sequence

# Function to convert DNA back to text
def dna_to_text(dna_sequence):
    reverse_map = {v: k for k, v in dna_map.items()}
    decrypted_text = ''
    for i in range(0, len(dna_sequence), 3):
        triplet = dna_sequence[i:i+3]
        decrypted_text += reverse_map.get(triplet, '?')  # '?' for unknown characters
    return decrypted_text

# Function to convert text to RNA
def text_to_rna(text):
    rna_sequence = ''.join([rna_map[char] for char in text.lower() if char in rna_map])
    return rna_sequence

# Function to convert RNA back to text
def rna_to_text(rna_sequence):
    reverse_rna_map = {v: k for k, v in rna_map.items()}
    decrypted_text = ''
    for i in range(0, len(rna_sequence), 3):
        triplet = rna_sequence[i:i+3]
        decrypted_text += reverse_rna_map.get(triplet, '?')
    return decrypted_text

# Example usage
user_input = input("Enter a sentence: ")

# Convert text to DNA and RNA
dna_encoded = text_to_dna(user_input)
rna_encoded = text_to_rna(user_input)

print("\nDNA Encoded Sequence:", dna_encoded)
print("\nRNA Encoded Sequence:", rna_encoded)

# Decode back from DNA and RNA to original text
decoded_text_dna = dna_to_text(dna_encoded)
decoded_text_rna = rna_to_text(rna_encoded)

print("\nDecoded from DNA:", decoded_text_dna)
print("\nDecoded from RNA:", decoded_text_rna)
