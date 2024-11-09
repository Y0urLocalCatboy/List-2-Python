class DNASequence:
    """
    A class representing a DNA sequence, providing methods for mutation, motif finding,
    generating a complementary sequence, and transcription to RNA.

    Attributes:
        identifier (str): A unique identifier for the DNA sequence.
        data (str): The DNA sequence data.
        valid_chars (set): The set of valid characters for the DNA sequence (e.g., {'A', 'T', 'C', 'G'}).

    Methods:
        __str__(): Returns a formatted string representation of the DNA sequence.
        __len__(): Returns the length of the DNA sequence.
        mutate(position, value): Mutates a nucleotide at the specified position with the provided value.
        find_motif(motif): Finds and returns the start positions of a specified motif within the DNA sequence.
        complement(): Generates and returns a complementary DNA sequence.
        transcribe(): Transcribes the DNA sequence into RNA and returns an RNASequence object.
    """

    def __init__(self, identifier, data, valid_chars):
        """
        Initializes a DNASequence object with an identifier, data, and valid characters.

        Parameters:
            identifier (str): A unique identifier for the DNA sequence.
            data (str): The DNA sequence.
            valid_chars (set): Set of valid characters for the DNA sequence (e.g., {'A', 'T', 'C', 'G'}).

        Raises:
            ValueError: If data contains characters not in valid_chars.
        """
        self.identifier = identifier
        self.data = data
        self.valid_chars = valid_chars
        if not set(data).issubset(valid_chars):
            raise ValueError('Invalid character: ' + str(set(data) - valid_chars))

    def __str__(self):
        """Returns a formatted string representation of the DNA sequence."""
        return f'>{self.identifier}: {self.data}'

    def __len__(self):
        """Returns the length of the DNA sequence."""
        return len(self.data)

    def mutate(self, position, value):
        """
        Mutates a nucleotide at the specified position with the provided value.

        Parameters:
            position (int): The index position to mutate in the DNA sequence.
            value (str): The new nucleotide character to replace at the given position.

        Raises:
            ValueError: If value is not in valid_chars.
        """
        if value not in self.valid_chars:
            raise ValueError('Invalid character')
        self.data = self.data[:position] + value + self.data[position + 1:]

    def find_motif(self, motif):
        """
        Finds and returns the start positions of a specified motif within the DNA sequence.

        Parameters:
            motif (str): The motif to search for in the DNA sequence.

        Returns:
            list: List of starting positions where the motif is found.
        """
        positions = []
        for i in range(len(self.data) - len(motif) + 1):
            if self.data[i:i + len(motif)] == motif:
                positions.append(i)
        return positions

    def complement(self):
        """
        Generates and returns a complementary DNA sequence.

        Returns:
            DNASequence: A new DNASequence object that is the complement of the current sequence.
        """
        return DNASequence(self.identifier,
                           ''.join([{'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[char] for char in self.data]),
                           self.valid_chars)

    def transcribe(self):
        """
        Transcribes the DNA sequence into RNA by replacing thymine ('T') with uracil ('U').

        Returns:
            RNASequence: An RNASequence object that represents the transcribed RNA sequence.
        """
        return RNASequence(self.identifier,
                           self.data.replace('T', 'U'),
                           self.valid_chars)


class RNASequence(DNASequence):
    """
    A subclass of DNASequence representing an RNA sequence, with methods for generating
    a complementary RNA sequence and translating the RNA into a protein sequence.

    Attributes:
        valid_chars (set): Set of valid characters for RNA (e.g., {'A', 'U', 'C', 'G'}).

    Methods:
        complement(): Returns the complement of the RNA sequence.
        translate(): Translates the RNA sequence into a protein sequence.
    """
    valid_chars = {'A', 'U', 'C', 'G'}

    def complement(self):
        """
        Generates and returns a complementary RNA sequence.

        Returns:
            RNASequence: A new RNASequence object that is the complement of the current sequence.
        """
        return RNASequence(self.identifier,
                           ''.join([{'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}[char] for char in self.data]),
                           self.valid_chars)

    def translate(self):
        """
        Translates the RNA sequence into a protein sequence by mapping codons to amino acids.

        Returns:
            ProteinSequence: A ProteinSequence object representing the translated protein sequence.
        """
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
                                         'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}[self.data[i:i + 3]]
                                        for i in range(0, len(self.data), 3)]),
                               ProteinSequence.valid_chars)


class ProteinSequence(RNASequence):
    """
    A class representing a protein sequence, generated from RNA translation.

    Attributes:
        valid_chars (set): Set of valid characters for amino acids.
    """
    valid_chars = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*'}
