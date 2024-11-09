import unittest
from dna import DNASequence, RNASequence, ProteinSequence

class TestSequence(unittest.TestCase):
    def test_setUp(self):
        self.dna = DNASequence('seq1', 'ATCG', {'A', 'T', 'C', 'G'})
        self.rna = RNASequence('seq2', 'AUCGAUC', {'A', 'U', 'C', 'G'})
        self.protein = ProteinSequence('seq3', 'M', {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', '*'})
    def test_dna_str(self):
        self.dna = DNASequence('seq1', 'ATCG', {'A', 'T', 'C', 'G'})
        self.assertEqual(str(self.dna), '>seq1: ATCG')
    def test_rna_str(self):
        self.rna = RNASequence('seq2', 'AUCGAUC', {'A', 'U', 'C', 'G'})
        self.assertEqual(str(self.rna), '>seq2: AUCGAUC')
    def test_protein_str(self):
        self.protein = ProteinSequence('seq3', 'MN', {'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*'})
        self.assertEqual(str(self.protein), '>seq3: MN')
    def test_dna_len(self):
        self.dna = DNASequence('seq1', 'ATCG', {'A', 'T', 'C', 'G'})
        self.assertEqual(len(self.dna), 4)
    def test_rna_len(self):
        self.rna = RNASequence('seq2', 'AUCGAUC', {'A', 'U', 'C', 'G'})
        self.assertEqual(len(self.rna), 7)
    def test_protein_len(self):
        self.protein = ProteinSequence('seq3', 'MN', {'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*'})
        self.assertEqual(len(self.protein), 2)
    def test_dna_mutate(self):
        self.dna = DNASequence('seq1', 'ATCG', {'A', 'T', 'C', 'G'})
        self.dna.mutate(0, 'T')
        self.assertEqual(str(self.dna), '>seq1: TTCG')
    def test_rna_mutate(self):
        self.rna = RNASequence('seq2', 'AUCGAUC', {'A', 'U', 'C', 'G'})
        self.rna.mutate(0, 'U')
        self.assertEqual(str(self.rna), '>seq2: UUCGAUC')
    def test_protein_mutate(self):
        self.protein = ProteinSequence('seq3', 'NM', {'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*'})
        self.protein.mutate(0, 'M')
        self.assertEqual(str(self.protein), '>seq3: MM')
    def test_dna_find_motif(self):
        self.dna = DNASequence('seq1', 'ATCGATCG', {'A', 'T', 'C', 'G'})
        self.assertEqual(self.dna.find_motif('AT'), [0, 4])
    def test_rna_find_motif(self):
        self.rna = RNASequence('seq2', 'AUCGAUC', {'A', 'U', 'C', 'G'})
        self.assertEqual(self.rna.find_motif('AU'), [0, 4])
    def test_protein_find_motif(self):
        self.protein = ProteinSequence('seq3', 'MNOMN', {'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*'})
        self.assertEqual(self.protein.find_motif('MN'), [0, 3])
    def test_dna_complement(self):
        self.dna = DNASequence('seq1', 'ATCG', {'A', 'T', 'C', 'G'})
        self.assertEqual(str(self.dna.complement()), '>seq1: TAGC')
    def test_rna_complement(self):
        self.rna = RNASequence('seq2', 'AUCGAUC', {'A', 'U', 'C', 'G'})
        self.assertEqual(str(self.rna.complement()), '>seq2: UAGCUAG')
    def test_rna_translate(self):
        self.rna = RNASequence('seq2', 'UUUUUU', {'A', 'U', 'C', 'G'})
        self.assertEqual(str(self.rna.translate()), '>seq2: FF')

if __name__ == "__main__":
    unittest.main()