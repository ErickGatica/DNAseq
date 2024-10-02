import unittest
from src.dna_seq import DNASeq

class TestDNASeq(unittest.TestCase):
    def test_valid_dna_sequence(self):
        """Tests creating a DNASeq object with a valid DNA sequence."""
        dna_seq = DNASeq("ATCG")
        self.assertEqual(dna_seq.seq, "atcg")

    def test_invalid_dna_sequence(self):
        """Tests creating a DNASeq object with an invalid DNA sequence."""
        with self.assertRaises(ValueError):
            DNASeq("XXX")

    def test_dna_sequence_case_insensitivity(self):
        """Tests that the DNA sequence is converted to lowercase."""
        dna_seq = DNASeq("ATCG")
        self.assertEqual(dna_seq.seq, "atcg")

    def test_dna_sequence_empty_string(self):
        """Tests creating a DNASeq object with an empty string."""
        dna_seq = DNASeq("")
        self.assertEqual(dna_seq.seq, "")

    def test_dna_sequence_whitespace(self):
        """Tests creating a DNASeq object with whitespace."""
        with self.assertRaises(ValueError):
            DNASeq(" ATCG ")


# Run the test with the following command:
if __name__ == '__main__':
    unittest.main()