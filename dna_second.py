class DNASequence:
    def __init__(self, identifier, data, valid_chars):
        self.identifier = identifier
        if not set(data).issubset(valid_chars):
            raise ValueError('Invalid character')
        else:
            self.data = data
        self.valid_chars = {'A', 'T', 'C', 'G'}
    def __str__(self):
        return f'>{self.identifier}: {self.data}'
    def __len__(self):
        return len(self.data)
    def mutate(self, position, value):
        if value not in self.valid_chars:
            raise ValueError('Invalid character')
        self.data = self.data[:position] + value + self.data[position+1:]
    def find_motif(self, motif):
        positions = []
        for i in range(len(self.data) - len(motif) + 1):
            if self.data[i:i + len(motif)] == motif:
                positions.append(i)
        return positions
    def complement(self):
        return DNASequence(self.identifier,
                           ''.join([{'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[char] for char in self.data]),
                           self.valid_chars)
    def transcribe(self):
        return RNASequence(self.identifier,
                           self.data.replace('T', 'U'),
                           self.valid_chars)

class RNASequence(DNASequence):
    valid_chars = {'A', 'U', 'C', 'G'}
    def complement(self):
        return RNASequence(self.identifier,
                           ''.join([{'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}[char] for char in self.data]),
                           self.valid_chars)
    def translate(self):
        return ProteinSequence(self.identifier,
                               ''.join([{'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
                                        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
                                        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
                                        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
                                        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                                        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                                        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                                        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                                        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
                                        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                                        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                                        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                                        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                                        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                                        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                                        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}[self.data[i:i+3]]
                                       for i in range(0, len(self.data), 3)]),
                               self.valid_chars)

class ProteinSequence(RNASequence):
    valid_chars = {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', '*'}
