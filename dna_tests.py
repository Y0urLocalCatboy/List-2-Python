import unittest
from dna import DNASequence, RNASequence, ProteinSequence

class TestSequence(unittest.TestCase):
    """
    Unit test class for testing DNA, RNA, and Protein sequence classes.
    Methods:

        setUp(): Initializes sequence instances for DNA, RNA, and Protein.
        test_dna_str(): Tests string function of DNA sequence.
        test_rna_str(): Tests string function of RNA sequence.
        test_protein_str(): Tests string function of Protein sequence.
        test_dna_len(): Tests length function for DNA sequence.
        test_rna_len(): Tests length function for RNA sequence.
        test_protein_len(): Tests length function for Protein sequence.
        test_dna_mutate(): Tests mutation function for DNA sequence.
        test_rna_mutate(): Tests mutation function for RNA sequence.
        test_protein_mutate(): Tests mutation function for Protein sequence.
        test_dna_find_motif(): Tests finding motif function in DNA sequence.
        test_rna_find_motif(): Tests finding motif function in RNA sequence.
        test_protein_find_motif(): Tests finding motif function in Protein sequence.
        test_dna_complement(): Tests generation of complement function for DNA sequence.
        test_rna_complement(): Tests generation of complement function for RNA sequence.
        test_rna_translate(): Tests RNA sequence translation function to protein sequence.
    """

    def setUp(self):
        """
        Sets up instances for DNA, RNA, and Protein sequences with specified sequences
        and allowed characters for each test.
        """
        self.dna = DNASequence('seq1', 'ATCG', {'A', 'T', 'C', 'G'})
        self.rna = RNASequence('seq2', 'AUCGAUC', {'A', 'U', 'C', 'G'})
        self.protein = ProteinSequence(
            'seq3', 'M', {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
                          'Q', 'R', 'S', 'T', 'V', 'W', 'Y', '*'}
        )

    def test_dna_str(self):
        """Tests DNA sequence string representation."""
        self.assertEqual(str(self.dna), '>seq1: ATCG')

    def test_rna_str(self):
        """Tests RNA sequence string representation."""
        self.assertEqual(str(self.rna), '>seq2: AUCGAUC')

    def test_protein_str(self):
        """Tests Protein sequence string representation."""
        self.protein = ProteinSequence(
            'seq3', 'MN', {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*'}
        )
        self.assertEqual(str(self.protein), '>seq3: MN')

    def test_dna_len(self):
        """Tests length calculation for DNA sequence."""
        self.assertEqual(len(self.dna), 4)

    def test_rna_len(self):
        """Tests length calculation for RNA sequence."""
        self.assertEqual(len(self.rna), 7)

    def test_protein_len(self):
        """Tests length calculation for Protein sequence."""
        self.protein = ProteinSequence('seq3', 'MN', {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                                                      'X', 'Y', 'Z', '*'})
        self.assertEqual(len(self.protein), 2)

    def test_dna_mutate(self):
        """Tests mutation functionality for DNA sequence."""
        self.dna.mutate(0, 'T')
        self.assertEqual(str(self.dna), '>seq1: TTCG')

    def test_rna_mutate(self):
        """Tests mutation functionality for RNA sequence."""
        self.rna.mutate(0, 'U')
        self.assertEqual(str(self.rna), '>seq2: UUCGAUC')

    def test_protein_mutate(self):
        """Tests mutation functionality for Protein sequence."""
        self.protein = ProteinSequence('seq3', 'NM', {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                                      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                                                      'U', 'V', 'W', 'X', 'Y', 'Z', '*'})
        self.protein.mutate(0, 'M')
        self.assertEqual(str(self.protein), '>seq3: MM')

    def test_dna_find_motif(self):
        """Tests finding motif positions in DNA sequence."""
        self.dna = DNASequence('seq1', 'ATCGATCG', {'A', 'T', 'C', 'G'})
        self.assertEqual(self.dna.find_motif('AT'), [0, 4])

    def test_rna_find_motif(self):
        """Tests finding motif positions in RNA sequence."""
        self.rna = RNASequence('seq2', 'AUCGAUC', {'A', 'U', 'C', 'G'})
        self.assertEqual(self.rna.find_motif('AU'), [0, 4])

    def test_protein_find_motif(self):
        """Tests finding motif positions in Protein sequence."""
        self.protein = ProteinSequence('seq3', 'MNOMN', {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                                                         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                                         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*'})
        self.assertEqual(self.protein.find_motif('MN'), [0, 3])

    def test_dna_complement(self):
        """Tests generation of complement for DNA sequence."""
        self.assertEqual(str(self.dna.complement()), '>seq1: TAGC')

    def test_rna_complement(self):
        """Tests generation of complement for RNA sequence."""
        self.assertEqual(str(self.rna.complement()), '>seq2: UAGCUAG')

    def test_rna_translate(self):
        """Tests RNA sequence translation to Protein sequence."""
        self.rna = RNASequence('seq2', 'UUUUUU', {'A', 'U', 'C', 'G'})
        self.assertEqual(str(self.rna.translate()), '>seq2: FF')

if __name__ == "__main__":
    unittest.main()
