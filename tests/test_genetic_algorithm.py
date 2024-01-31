import unittest
from dna.genetic_algorithm import *
from dna.RotTable import RotTable
import random

def mocked_random_choice(liste,k):
    return [liste[0],liste[1]]

class TestGeneticAlgorithm(unittest.TestCase):
    def test_populate(self):
        rot_table = RotTable()
        population_size1 = 10
        gen_alg1 = GeneticAlgorithm(population_size1, rot_table, None)
        self.assertEqual(len(gen_alg1.population), population_size1)
        for table in gen_alg1.population:
            self.assertIsNotNone(table)
            for row in table.getTable().values():
                self.assertIsNotNone(row)
        
        population_size2 = 50
        gen_alg2 = GeneticAlgorithm(population_size2, rot_table, None)
        self.assertEqual(len(gen_alg2.population), population_size2)
        for table in gen_alg2.population:
            self.assertIsNotNone(table)
            for row in table.getTable().values():
                self.assertIsNotNone(row)

# class TestGeneticAlgorithmFuncs(unittest.Test):
#     def test_symmetrize_table(self):
#         rot_table = RotTable()
#         non_symmetric_table = rot_table.getNonSymmetric()
#         for i, dinucleotide in enumerate(non_symmetric_table):
#             rot_table.setTwist(dinucleotide,i)
#             rot_table.setWedge(dinucleotide,i)
#             rot_table.setDirection(dinucleotide,i)
        
#         rot_table = symmetrizeTable(rot_table)
                
    def test_evaluate(self): 
        rot_table = RotTable()
        traj = Traj3D()
        a = GeneticAlgorithm(1,rot_table,0.1)
        a.population = [rot_table]
        seq = "AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAAGGTTAAGTCAGTTGGGGACTGCTTAACCGGGTAACTGGCTTGGTGGAGCACAGATACCAAATACTGTCCTTCTAGTGTAGCCGCAGTTAGGCCACCACTTCAAGAACTCTTAATATCTCAATCCACCTTGTCCAGTTACCAGTGGCTGCTGCCAGTGGCGCTTTGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAGCCGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCGTCGATTTTTATGATGCTCGTCAGGGGGGCGGAGCCTATGGAAAAACGCCAACGGCGCAGCCTTTTCCTGGTTCTCGTTTTTTGCTCACATGTTTCTTTTGGCGTTATCCCCTGATTCTGTGGATAACCGCATCTCCGCTTTTGAGTGAGCAGACACCGCTCGCCGCAGCCGAACGACCGAGTGTAGCGAGTCAGTGAGCGAGGAAGCGGAAGAGCGCCGGAACGTGCATTTTCTCCTTACGCATCTGTGCGGCATTTCACATCGGACATGGTGCGCTTTCCATACAATTCGTACTGATGCCGCATAGTTAAGCCAGTATACACTCCGCTATCGCTACGTGACTGGTTCAGGGCTTCGCCCCGAAACCCCCTGACGCGCCCTGAGGGGCTTGTCTGCTCCCGGCATCCGCTCACAGACAAGCTGTTACCGTCTCCGGGAGCTGTATGTGTCAGAGGTTTTCACCGTCATCCCCGAAGCGTGCGAGGCAGCTGCGGTAAAGCTCGTCGGCGTGGTCGTGAAGTGATTCACAAATATCGGCCTGTTCATCTGCGTCCAGTTCGTTGAGTTTCTCCAGCAGCGTTAATGTCTGGCTTCTGATAAAACGGGCCATGTTAAGGGCGGTTTTTTCCTGTTTAGTCACTGATGCCTCCGTGTAAGGGGGATTTCTGTTTTATGGGGTAATGATACCGATGAAACGCGAGAGGATGCTCACCATACGGGTTACTGATGATGAACATGCCCGGTTACTGGAACGCTGTGAGGGTAAACAGCTGGCGGTATGGATGCGGCGGGTCTGCCTGGGTGAGCCGGTTGCACGCTCCGGGAAGCTGCCGACACTGGCACCGCCGTTACTGCGTCAGCTGGCCGCCATCGGGAATAACCTGAATCAGACAGCGAGGAAGGTGAACAGCGGGCAGTGGTCTTCCGGTGATCGGGTTCAGGTGTTGGCTGCGCTGATGGCCATCGGGGAGGAGCTGCGTCGGCTGCGTCTGGCCGTCAGGGAACAGGGCGCGCGGGATGATTGTTAAATTTCATGCCAGGGGAAAAGGCGGTGGCAGTGGTCCGGTTGATTACCTGCTGGGAAGGGAGCGAAACCGGGAAGGGGCAACGGTGCTTCAGGGTAATCCGGAAGAAGTCCGGGAACTCATCGATGCCACGCCATTTGCGAAGAAATACACGTCAGGTGTTCTGTCGTTCGCGGAGAAGGAGCTGCCGCCGGGAGGACGTGAAAAGGTGATGGCGAGCTTTGAGCGTGTACTGATGCCCGGTCTCGAAAAGAATCAGTACAGCATCCTGTGGGTGGAGCACCAGGACAAGGGACGGCTTGAGCTGAATTTTGTCATTCCGAACATGGAGCTACAGACCGGAAAACGCCTCCAGCCGTACTACGACCGGGCAGACAGGCCGAGAATTGATGCCTGGCAGACGCTGGTGAATCACCATTACGGGCTGCATGACCCCAACGCCCCGGAGAACCGCCGGATACTGACTCTCCCTGATAACCTGCCGGAAACGAAACAGGCGCTTGCAGAGAGCGTCACACGCGGGATAGACGCTCTTTATCATGTCGGGGAGATAAAAGGTCGTCAGGATGTGATTCAGGCGCTCACAGAGGCAGGGCTTGAAGTGGTCAGGGTGATGCGAAGCAGTATCAGCATTGCAGACCCGAACGGTGGGAAGAATATCAGGCTGAAAGGAGCATTTTATGAGCAATCTTTTACAGACGGGCGCGGAGTTCGAGAAAAAGCTGAAAGAGAGAGCCGAATCTACAGAGACAATGCTGAACGACGAGTTCAGCAAGCTCGAAAAATCTGTAAGCAAGGCTGTGACATCAAACGAGACGAAAATCAAAGACGCTATAGCCCTGTTCACAGCTTCGACAGAGGAATCACTGAAAAAACACCGGGAAGGGGTGAAAGAGGCGATGATGCAGCACAGGAAGGACGTGTTAAAGCTGGCAGGGAATACGGGCATGATGTTACTGGGGATGGTCCTTTTCCTGTTTACCGTGAGTGGCGGGACGCTCTGGTATCTTGGCGGGATGATACAGGCGAACCTGGAAGAAATCAGGATACAGGAAGAAACATTGCAGAAACTGAACGCGAAGACATGGGGCGTGGAGTTTGTGCAGGACGGGAGAAGGAAATTTCTGGTTATCCCTCAGGGGAAATCGGCAACGGTGATTCCCTATCAGGGGAAGGACTGGGTACAACTGACGGAGTGACACAGAGTGACGGAGCTGGAAAGACATTTGCTGAACGCCTTAGAGCAACTGCAACAGGACTATATGCAGCGGCTGAACGAATGGGAGAGCGCCTTCGTGGAATTGCAGAAAATGTTTTCGCTTACGCAACGGGACAACGCGATGCTGAACGAGCGGGTCATGCAGTTGAGTCAGCAGGTGCAGCACTTGAGCGAGCAGACAGAACGCTTGAGCCAGTTATACAGCGAGAACAGGAGATAAGGGATGAACGGCTGATACAGGAACGCGAACATGAGTTATCCCTGGAGCGTGAGCGCCAGCTGGAAATACAGGAACGGACACAGGATGGCCCTTCGCTGGGATGGTAATCAGAGACAGGCTAAAATGTTGTCAGCGCGTTTCCGGTGCATTTTTTGGGATAATGGTTGGTTCGGGGGCACCGGGAACGCGCTTCAGTCAGACCTTGCTGAAAACACAGGAACGCGTTAAAACGCATACGGGCGCGATTCTGGTGTGTCTTTTGTTGCTGTGTTTTGCCTCTATTGCCAGATCGCGCTCATTCCCCTGAACTTCTGTTTTCCCGCTCCGGTCCCCGTCTTCTTCGCTTCCGAAAGCATGAAAAAAATCCGTTTCAGCTGTCTCTGGCTGGCAATTCCTGCGTGATTCACATGGCTGCATAGCTATGCATGTGGTTAAAATTTACCGGGTGCGATCGCGGCAGTTTTTCGGGTGGTTTGTTGCCATTTTTACCTGTCTGCTGCCGTGATCGCGCCGAACGCGTTTCAGCGGTGCGTACAATAAGGGATTATGGTAAATTATCTTGTTCCTTAGAGAATGATTTGAGGTGGTATCCTGCACTTATTTAAATATGCTTGCTTGGGAAATTCCAGGTTGCAGTATGGTTGAGTTGTAATTTTCCTATGATAGGAAAAATGTTATATTATTAATTTATTTGTGAGGCTTCATAAAGAATGAAAATTTCTGATATTGAAAAAAACATATATAAAGGACTAGCTGAATTTATTTCACAAAAAATCAGAGATGAACATGATATATGCCTTGGACAGTTTGAATCAGAGGAATTACTTGATGAGATTCTTAAAAGAGTAATCCCAGTCATATATAATGTGGCTATTGATGATGCTATAAAATCAGTAAGGAATGTTGGGGATAGATTAGAGGAGGAATTAGATATGAGGAAGGTAGTGTGACTAATTTTAAATCAGACTTAAATCTAATAAGAAAAGAATGGTATAATGCATTTTATTCAGGTAATACTGAAATGCTAGATTACTTGGAAGCTGATTGGTTTATTTCAACAAATGGTCAAAAAGTTATCTATAAAAAACATCAGTTACGAAAGATTGATATGCGTCCAGCGAGGATTTTACCTAGCATAGAAAGATATGAATATGAGGTCGTAATGCGTGAGTTTAAAGGCATTGCTTGTGTTTCAGGGAAAGCTGAAATAAAGCAAAATGATGGAAATATATTAATGGCTTTTATTGAGAATTGGATAAAGGTTAATGGTGGATGGAAAATGCAGTTTATATCGTATGAAAAAATCTAAGGGGAAGCCCCCTTAGATTAATGGTTATATATGTTCAAGTTTTATTTTTTTATAGCGATAAGTTCTGCTTTGAGCTTTAAGCATGTTTTCTGCAAACTGAATATCAAAACTATTTATAGCATTAGTTATTATAGTTTTTATTTTTTCTTTATCAGATAATGAATCACCATGCTCTATAGGTTCCCGCATATATGGATTGTTTTTTAATTCATCAAATAATGTTTTAAATAGTTCTAATCGACGAGGTCTTATAACTGTAAAAGATATATGAAGAGAGTGTTTGCTCTGAGTCGTAACATTGTGCCAGTATCCAGCAGGAAGATATATGGCCTGACCTGGGGTTATATCAAACTCATAATCTGGGGAGGTATTAGGTGGTAGATAATCGAAGCTTCTTTCATCTTCGAGAGGGTATGAATAGGTAGGGTTGTAAACTTTCCATTTTTTTATTCCCTCAATTTGAACAGCTATTACATCATGATTGTCAAAATGAAGCCCAAAGCTTGGTGTTGCTGTAAATGCAGCATATAGATTAGCACTACATGTACATTCTAACTCTTTAGATAACCATAGTCTGCTTTCATCTACAGATTCAAAGAATGACTGGCATCGATCTACTATAAGGGTTGCGCCATCACGTAAGCATTTATATAGCTGATGGCGATTTATATGTGGTGTTCTATCGCCTGTTTGGCTATATGTGTATCTTATAAATCCTTTATACCCCCTAATTTCGGGAAAGTTGTCATTTGCCATTCTAACTCTAGGATAGTGCAATATATCTTTTTCAAGCAATTTATTAAGATCATTCCAGTTGATTAAGTTTTTATAATTAACATCCGTGAATACAAACGGATATTTCTGGAAATTATATTTCTTAAATTTTTCTATGATTTCCTTTTTTATAAGATTATTCATTTTTAAACCTCATGTTTTGTGATATCTATAATCTGTGCTTTAGGTATATTATTTATAAGTTGTTCATCATGAGATATAACAATGATATGCTTTTCCTTGTTTTCCTCTTTTATATAATCACTGATTATTTTTATACCAAGTGAATCAAACCCTTTTGTCGGTTCATCGAAAATAATCAAGTCTACGTTTTTTCCAGATGTAAGAGATACTCCTAATTTTTGTTTTTGTCCACCAGATAAATTATGTCCGTAACCTTTGATCTCATAATCTAGTGGTTTGTCGAACTTAAATCTGTGTAGCAGCTTTTTAATTGTATTTAAATTATTAATGCCGGAATAATGTAATATATTTTCCTCTATAGTTCCAGGCATGAGATCTAGATCTTGAGGAACGTATAAGACATTAACAAAAGGAGAATTTGCTTTTTCTTGTTGTATCCCATTGATTTTTATTGTGTTTTCTTCTGTTGTTATATTGCCAGAGAGAATTTTTGCAATAGTTGTTTTTCCCGAACCATTCTCACCGGTTATAAAGGTAACAACGCCTTTTGTTAATATTAATTTATGGTTGAATGATTTGTTGTATATTTCAATATTGCAAATATTGTCTTTTACATGAAGATATTGCTTGTCTGTGTAATTTGTTTTTTTTATGTCGTTTATTTCGGCACAGTATAAATCAATTTCTGTTCTTGCCATTTTTATTTGTCTAAATAGATAACCAATGCGATTTAATGGGAGAAAAACTTGGAATAAAAAAGTGGCAAGCATAATAATACTACCACGGCTTGCTCTACCATGAAGAAACATCCAGTATGCTGATAGGATAATCAGACTACTAAAAATGACTGAAAGAAAAGCGGAGCTGATACCAAACAGGAAAAATTCATTATTTACTTTTCTTTGTTTTTCTGAATGTGTATTTACAGCTTGAATTACTCGTTTACGACTTTTATCCGTGGTATGGAAAGCTTTATCCATAGGATACATGTGCATCATATCAAACATTCTTCCAGATGCGAATTTGGAGCTAAGTGCAACTGATTTCATCATTGGAAATCTACGTTGTGTCATTTTTATGACAAATATTATATAGATTGCCATTATTATTATAAACTCAATGGCTATTAATGTATTAACACTTATACAAATTGTTATGATTATTCCAATCATTTGTATTAATAATGGTACTACATCAGAACATATTGTATAAAATAATGATGATGCAGAAGAAAGCATGCTTTCTATAACCTTATTTAGTTCTCCTTTATTTTTCTTTAAAAAATGCTCTTGGTGAGAATTTTGTATATTATCAATAACTTGCTCTCTAAGCTTTACAGATAATTCTATATTTGTTTTTTGAGTCAAGTATTCCGATATGCTATATCCAGCAGGCATAAGGAATCTAATTGATAAGAAACATGCTATAAATATTAATAATGAGTTTATTTCTCCTATTGAATCTTTATTGTCAATAACTGTTTTTATTAAATATCCGAATAGAACGAAAAGAAAACTACTTATAGTTGATAATAATATAATAAAAAACAAATTACATTTATTAAATGTGATGATGTACTTTTCAATAAAATTCAATTTATAATCCTTAAAGCCCGTATATTACGGGCTTTATGTTATCTAGAATTACATGAGCACCCAGCGCCACATCCTTTACCGCTGCAACCACAAACAGAACCATTATCATTCCAAACATCTTTTCGCATTATTATTTTTACAAATTCTGCGGCTGGAAGGTGAGTGATACTCTTTACTTTTTCGATGTAAGAATCACTGGATATGGATTCTTTTGGAATTCTTATAGTATTAATGTTCTTTATGCTGTATCTTACAGCATAATCACCATACCACTTTGCGACAGTTTCATGACCTAGGTAAAAAGCGATTTTTTCAATTTGATTTTTATATTCGTTAAAACGATATTCTTGGAATGTTATACCATGCTCATTAACATGCCTTATCTCATTTTTTAGCATGTCATTTGTATTTGGATAATGGTGGAGGTAAGCACCAAGATATTTTTCACAAAAGCTGGTATAAGCATCTGTAAATTGAATAAACGTATGCCACATTTCATCTATAATTTGTAATTGCTCGTGAACTTTTATATTGTAGCATTCCGTTAGGCATGTTGAGGCTAGCCAGATGAATTTCTTTGTTTCATTAAAGATATCATCAGCTTCTTCTGGTGTTACATTCCATTCTTTACGAAATTTTAGAAGAACATCATCATTGTGATAACTCATGATATCTTCTAATGAGCTAACATTATGAACTTTTGCATAAGAACTGCTGTTCATCTTATGTTGTAGCATAACACCCCCAATTATATATTTGAATGTAGATGAGAATAGTTATCATTTGTTATGGTATTGTTAAATTTGTGCTTGTGTCAATATGCCTAATTCTATAAATGAGATAGTAATCAAGTTTTTTAATGGTTATAGGATCCATTAGTAATACAAGGTTTTTGCAGCCAGTTTTTACGGGTAGGGGCTGCAAGGAAAACAAAATTTTCCCACTCTAAGAGAAGAGAATTGAGTTGGTTGAATGAGTGGATGCATCTAGGGCCGCTAATTCACCGAGTGTAAAGGCTGTACGAAATGTGTTGCAGTCCGATAATAGCCCCCTCCATTGACGTTTTACACATGTGTTGTAGGTTCCAGGAGTGGGCGGATCTCAAAAAGATC"
        a.evaluate(seq,traj)
        for score in a.scores:
            assert(int(score)==5404)
    
    def test_selection(self):
        traj = Traj3D()
        rot_table = RotTable() #Value around 5400
        seq = "AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAAGGTTAAGTCAGTTGGGGACTGCTTAACCGGGTAACTGGCTTGGTGGAGCACAGATACCAAATACTGTCCTTCTAGTGTAGCCGCAGTTAGGCCACCACTTCAAGAACTCTTAATATCTCAATCCACCTTGTCCAGTTACCAGTGGCTGCTGCCAGTGGCGCTTTGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAGCCGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCGTCGATTTTTATGATGCTCGTCAGGGGGGCGGAGCCTATGGAAAAACGCCAACGGCGCAGCCTTTTCCTGGTTCTCGTTTTTTGCTCACATGTTTCTTTTGGCGTTATCCCCTGATTCTGTGGATAACCGCATCTCCGCTTTTGAGTGAGCAGACACCGCTCGCCGCAGCCGAACGACCGAGTGTAGCGAGTCAGTGAGCGAGGAAGCGGAAGAGCGCCGGAACGTGCATTTTCTCCTTACGCATCTGTGCGGCATTTCACATCGGACATGGTGCGCTTTCCATACAATTCGTACTGATGCCGCATAGTTAAGCCAGTATACACTCCGCTATCGCTACGTGACTGGTTCAGGGCTTCGCCCCGAAACCCCCTGACGCGCCCTGAGGGGCTTGTCTGCTCCCGGCATCCGCTCACAGACAAGCTGTTACCGTCTCCGGGAGCTGTATGTGTCAGAGGTTTTCACCGTCATCCCCGAAGCGTGCGAGGCAGCTGCGGTAAAGCTCGTCGGCGTGGTCGTGAAGTGATTCACAAATATCGGCCTGTTCATCTGCGTCCAGTTCGTTGAGTTTCTCCAGCAGCGTTAATGTCTGGCTTCTGATAAAACGGGCCATGTTAAGGGCGGTTTTTTCCTGTTTAGTCACTGATGCCTCCGTGTAAGGGGGATTTCTGTTTTATGGGGTAATGATACCGATGAAACGCGAGAGGATGCTCACCATACGGGTTACTGATGATGAACATGCCCGGTTACTGGAACGCTGTGAGGGTAAACAGCTGGCGGTATGGATGCGGCGGGTCTGCCTGGGTGAGCCGGTTGCACGCTCCGGGAAGCTGCCGACACTGGCACCGCCGTTACTGCGTCAGCTGGCCGCCATCGGGAATAACCTGAATCAGACAGCGAGGAAGGTGAACAGCGGGCAGTGGTCTTCCGGTGATCGGGTTCAGGTGTTGGCTGCGCTGATGGCCATCGGGGAGGAGCTGCGTCGGCTGCGTCTGGCCGTCAGGGAACAGGGCGCGCGGGATGATTGTTAAATTTCATGCCAGGGGAAAAGGCGGTGGCAGTGGTCCGGTTGATTACCTGCTGGGAAGGGAGCGAAACCGGGAAGGGGCAACGGTGCTTCAGGGTAATCCGGAAGAAGTCCGGGAACTCATCGATGCCACGCCATTTGCGAAGAAATACACGTCAGGTGTTCTGTCGTTCGCGGAGAAGGAGCTGCCGCCGGGAGGACGTGAAAAGGTGATGGCGAGCTTTGAGCGTGTACTGATGCCCGGTCTCGAAAAGAATCAGTACAGCATCCTGTGGGTGGAGCACCAGGACAAGGGACGGCTTGAGCTGAATTTTGTCATTCCGAACATGGAGCTACAGACCGGAAAACGCCTCCAGCCGTACTACGACCGGGCAGACAGGCCGAGAATTGATGCCTGGCAGACGCTGGTGAATCACCATTACGGGCTGCATGACCCCAACGCCCCGGAGAACCGCCGGATACTGACTCTCCCTGATAACCTGCCGGAAACGAAACAGGCGCTTGCAGAGAGCGTCACACGCGGGATAGACGCTCTTTATCATGTCGGGGAGATAAAAGGTCGTCAGGATGTGATTCAGGCGCTCACAGAGGCAGGGCTTGAAGTGGTCAGGGTGATGCGAAGCAGTATCAGCATTGCAGACCCGAACGGTGGGAAGAATATCAGGCTGAAAGGAGCATTTTATGAGCAATCTTTTACAGACGGGCGCGGAGTTCGAGAAAAAGCTGAAAGAGAGAGCCGAATCTACAGAGACAATGCTGAACGACGAGTTCAGCAAGCTCGAAAAATCTGTAAGCAAGGCTGTGACATCAAACGAGACGAAAATCAAAGACGCTATAGCCCTGTTCACAGCTTCGACAGAGGAATCACTGAAAAAACACCGGGAAGGGGTGAAAGAGGCGATGATGCAGCACAGGAAGGACGTGTTAAAGCTGGCAGGGAATACGGGCATGATGTTACTGGGGATGGTCCTTTTCCTGTTTACCGTGAGTGGCGGGACGCTCTGGTATCTTGGCGGGATGATACAGGCGAACCTGGAAGAAATCAGGATACAGGAAGAAACATTGCAGAAACTGAACGCGAAGACATGGGGCGTGGAGTTTGTGCAGGACGGGAGAAGGAAATTTCTGGTTATCCCTCAGGGGAAATCGGCAACGGTGATTCCCTATCAGGGGAAGGACTGGGTACAACTGACGGAGTGACACAGAGTGACGGAGCTGGAAAGACATTTGCTGAACGCCTTAGAGCAACTGCAACAGGACTATATGCAGCGGCTGAACGAATGGGAGAGCGCCTTCGTGGAATTGCAGAAAATGTTTTCGCTTACGCAACGGGACAACGCGATGCTGAACGAGCGGGTCATGCAGTTGAGTCAGCAGGTGCAGCACTTGAGCGAGCAGACAGAACGCTTGAGCCAGTTATACAGCGAGAACAGGAGATAAGGGATGAACGGCTGATACAGGAACGCGAACATGAGTTATCCCTGGAGCGTGAGCGCCAGCTGGAAATACAGGAACGGACACAGGATGGCCCTTCGCTGGGATGGTAATCAGAGACAGGCTAAAATGTTGTCAGCGCGTTTCCGGTGCATTTTTTGGGATAATGGTTGGTTCGGGGGCACCGGGAACGCGCTTCAGTCAGACCTTGCTGAAAACACAGGAACGCGTTAAAACGCATACGGGCGCGATTCTGGTGTGTCTTTTGTTGCTGTGTTTTGCCTCTATTGCCAGATCGCGCTCATTCCCCTGAACTTCTGTTTTCCCGCTCCGGTCCCCGTCTTCTTCGCTTCCGAAAGCATGAAAAAAATCCGTTTCAGCTGTCTCTGGCTGGCAATTCCTGCGTGATTCACATGGCTGCATAGCTATGCATGTGGTTAAAATTTACCGGGTGCGATCGCGGCAGTTTTTCGGGTGGTTTGTTGCCATTTTTACCTGTCTGCTGCCGTGATCGCGCCGAACGCGTTTCAGCGGTGCGTACAATAAGGGATTATGGTAAATTATCTTGTTCCTTAGAGAATGATTTGAGGTGGTATCCTGCACTTATTTAAATATGCTTGCTTGGGAAATTCCAGGTTGCAGTATGGTTGAGTTGTAATTTTCCTATGATAGGAAAAATGTTATATTATTAATTTATTTGTGAGGCTTCATAAAGAATGAAAATTTCTGATATTGAAAAAAACATATATAAAGGACTAGCTGAATTTATTTCACAAAAAATCAGAGATGAACATGATATATGCCTTGGACAGTTTGAATCAGAGGAATTACTTGATGAGATTCTTAAAAGAGTAATCCCAGTCATATATAATGTGGCTATTGATGATGCTATAAAATCAGTAAGGAATGTTGGGGATAGATTAGAGGAGGAATTAGATATGAGGAAGGTAGTGTGACTAATTTTAAATCAGACTTAAATCTAATAAGAAAAGAATGGTATAATGCATTTTATTCAGGTAATACTGAAATGCTAGATTACTTGGAAGCTGATTGGTTTATTTCAACAAATGGTCAAAAAGTTATCTATAAAAAACATCAGTTACGAAAGATTGATATGCGTCCAGCGAGGATTTTACCTAGCATAGAAAGATATGAATATGAGGTCGTAATGCGTGAGTTTAAAGGCATTGCTTGTGTTTCAGGGAAAGCTGAAATAAAGCAAAATGATGGAAATATATTAATGGCTTTTATTGAGAATTGGATAAAGGTTAATGGTGGATGGAAAATGCAGTTTATATCGTATGAAAAAATCTAAGGGGAAGCCCCCTTAGATTAATGGTTATATATGTTCAAGTTTTATTTTTTTATAGCGATAAGTTCTGCTTTGAGCTTTAAGCATGTTTTCTGCAAACTGAATATCAAAACTATTTATAGCATTAGTTATTATAGTTTTTATTTTTTCTTTATCAGATAATGAATCACCATGCTCTATAGGTTCCCGCATATATGGATTGTTTTTTAATTCATCAAATAATGTTTTAAATAGTTCTAATCGACGAGGTCTTATAACTGTAAAAGATATATGAAGAGAGTGTTTGCTCTGAGTCGTAACATTGTGCCAGTATCCAGCAGGAAGATATATGGCCTGACCTGGGGTTATATCAAACTCATAATCTGGGGAGGTATTAGGTGGTAGATAATCGAAGCTTCTTTCATCTTCGAGAGGGTATGAATAGGTAGGGTTGTAAACTTTCCATTTTTTTATTCCCTCAATTTGAACAGCTATTACATCATGATTGTCAAAATGAAGCCCAAAGCTTGGTGTTGCTGTAAATGCAGCATATAGATTAGCACTACATGTACATTCTAACTCTTTAGATAACCATAGTCTGCTTTCATCTACAGATTCAAAGAATGACTGGCATCGATCTACTATAAGGGTTGCGCCATCACGTAAGCATTTATATAGCTGATGGCGATTTATATGTGGTGTTCTATCGCCTGTTTGGCTATATGTGTATCTTATAAATCCTTTATACCCCCTAATTTCGGGAAAGTTGTCATTTGCCATTCTAACTCTAGGATAGTGCAATATATCTTTTTCAAGCAATTTATTAAGATCATTCCAGTTGATTAAGTTTTTATAATTAACATCCGTGAATACAAACGGATATTTCTGGAAATTATATTTCTTAAATTTTTCTATGATTTCCTTTTTTATAAGATTATTCATTTTTAAACCTCATGTTTTGTGATATCTATAATCTGTGCTTTAGGTATATTATTTATAAGTTGTTCATCATGAGATATAACAATGATATGCTTTTCCTTGTTTTCCTCTTTTATATAATCACTGATTATTTTTATACCAAGTGAATCAAACCCTTTTGTCGGTTCATCGAAAATAATCAAGTCTACGTTTTTTCCAGATGTAAGAGATACTCCTAATTTTTGTTTTTGTCCACCAGATAAATTATGTCCGTAACCTTTGATCTCATAATCTAGTGGTTTGTCGAACTTAAATCTGTGTAGCAGCTTTTTAATTGTATTTAAATTATTAATGCCGGAATAATGTAATATATTTTCCTCTATAGTTCCAGGCATGAGATCTAGATCTTGAGGAACGTATAAGACATTAACAAAAGGAGAATTTGCTTTTTCTTGTTGTATCCCATTGATTTTTATTGTGTTTTCTTCTGTTGTTATATTGCCAGAGAGAATTTTTGCAATAGTTGTTTTTCCCGAACCATTCTCACCGGTTATAAAGGTAACAACGCCTTTTGTTAATATTAATTTATGGTTGAATGATTTGTTGTATATTTCAATATTGCAAATATTGTCTTTTACATGAAGATATTGCTTGTCTGTGTAATTTGTTTTTTTTATGTCGTTTATTTCGGCACAGTATAAATCAATTTCTGTTCTTGCCATTTTTATTTGTCTAAATAGATAACCAATGCGATTTAATGGGAGAAAAACTTGGAATAAAAAAGTGGCAAGCATAATAATACTACCACGGCTTGCTCTACCATGAAGAAACATCCAGTATGCTGATAGGATAATCAGACTACTAAAAATGACTGAAAGAAAAGCGGAGCTGATACCAAACAGGAAAAATTCATTATTTACTTTTCTTTGTTTTTCTGAATGTGTATTTACAGCTTGAATTACTCGTTTACGACTTTTATCCGTGGTATGGAAAGCTTTATCCATAGGATACATGTGCATCATATCAAACATTCTTCCAGATGCGAATTTGGAGCTAAGTGCAACTGATTTCATCATTGGAAATCTACGTTGTGTCATTTTTATGACAAATATTATATAGATTGCCATTATTATTATAAACTCAATGGCTATTAATGTATTAACACTTATACAAATTGTTATGATTATTCCAATCATTTGTATTAATAATGGTACTACATCAGAACATATTGTATAAAATAATGATGATGCAGAAGAAAGCATGCTTTCTATAACCTTATTTAGTTCTCCTTTATTTTTCTTTAAAAAATGCTCTTGGTGAGAATTTTGTATATTATCAATAACTTGCTCTCTAAGCTTTACAGATAATTCTATATTTGTTTTTTGAGTCAAGTATTCCGATATGCTATATCCAGCAGGCATAAGGAATCTAATTGATAAGAAACATGCTATAAATATTAATAATGAGTTTATTTCTCCTATTGAATCTTTATTGTCAATAACTGTTTTTATTAAATATCCGAATAGAACGAAAAGAAAACTACTTATAGTTGATAATAATATAATAAAAAACAAATTACATTTATTAAATGTGATGATGTACTTTTCAATAAAATTCAATTTATAATCCTTAAAGCCCGTATATTACGGGCTTTATGTTATCTAGAATTACATGAGCACCCAGCGCCACATCCTTTACCGCTGCAACCACAAACAGAACCATTATCATTCCAAACATCTTTTCGCATTATTATTTTTACAAATTCTGCGGCTGGAAGGTGAGTGATACTCTTTACTTTTTCGATGTAAGAATCACTGGATATGGATTCTTTTGGAATTCTTATAGTATTAATGTTCTTTATGCTGTATCTTACAGCATAATCACCATACCACTTTGCGACAGTTTCATGACCTAGGTAAAAAGCGATTTTTTCAATTTGATTTTTATATTCGTTAAAACGATATTCTTGGAATGTTATACCATGCTCATTAACATGCCTTATCTCATTTTTTAGCATGTCATTTGTATTTGGATAATGGTGGAGGTAAGCACCAAGATATTTTTCACAAAAGCTGGTATAAGCATCTGTAAATTGAATAAACGTATGCCACATTTCATCTATAATTTGTAATTGCTCGTGAACTTTTATATTGTAGCATTCCGTTAGGCATGTTGAGGCTAGCCAGATGAATTTCTTTGTTTCATTAAAGATATCATCAGCTTCTTCTGGTGTTACATTCCATTCTTTACGAAATTTTAGAAGAACATCATCATTGTGATAACTCATGATATCTTCTAATGAGCTAACATTATGAACTTTTGCATAAGAACTGCTGTTCATCTTATGTTGTAGCATAACACCCCCAATTATATATTTGAATGTAGATGAGAATAGTTATCATTTGTTATGGTATTGTTAAATTTGTGCTTGTGTCAATATGCCTAATTCTATAAATGAGATAGTAATCAAGTTTTTTAATGGTTATAGGATCCATTAGTAATACAAGGTTTTTGCAGCCAGTTTTTACGGGTAGGGGCTGCAAGGAAAACAAAATTTTCCCACTCTAAGAGAAGAGAATTGAGTTGGTTGAATGAGTGGATGCATCTAGGGCCGCTAATTCACCGAGTGTAAAGGCTGTACGAAATGTGTTGCAGTCCGATAATAGCCCCCTCCATTGACGTTTTACACATGTGTTGTAGGTTCCAGGAGTGGGCGGATCTCAAAAAGATC"
        a = GeneticAlgorithm(2,rot_table,0.1)
        rot_table2 = RotTable()
        rot_table2.setTwist("AA",rot_table.getTwist("AA")+1) #Value around 2200 score
        a.population = [rot_table,rot_table2]
        a.selection(seq,traj)
        assert(len(a.population)==1)
        for table in a.population:
            assert(table == rot_table2)
    
    def test_get_results(self):
        traj = Traj3D()
        rot_table = RotTable() #Value around 5400
        seq = "AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAAGGTTAAGTCAGTTGGGGACTGCTTAACCGGGTAACTGGCTTGGTGGAGCACAGATACCAAATACTGTCCTTCTAGTGTAGCCGCAGTTAGGCCACCACTTCAAGAACTCTTAATATCTCAATCCACCTTGTCCAGTTACCAGTGGCTGCTGCCAGTGGCGCTTTGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAGCCGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCGTCGATTTTTATGATGCTCGTCAGGGGGGCGGAGCCTATGGAAAAACGCCAACGGCGCAGCCTTTTCCTGGTTCTCGTTTTTTGCTCACATGTTTCTTTTGGCGTTATCCCCTGATTCTGTGGATAACCGCATCTCCGCTTTTGAGTGAGCAGACACCGCTCGCCGCAGCCGAACGACCGAGTGTAGCGAGTCAGTGAGCGAGGAAGCGGAAGAGCGCCGGAACGTGCATTTTCTCCTTACGCATCTGTGCGGCATTTCACATCGGACATGGTGCGCTTTCCATACAATTCGTACTGATGCCGCATAGTTAAGCCAGTATACACTCCGCTATCGCTACGTGACTGGTTCAGGGCTTCGCCCCGAAACCCCCTGACGCGCCCTGAGGGGCTTGTCTGCTCCCGGCATCCGCTCACAGACAAGCTGTTACCGTCTCCGGGAGCTGTATGTGTCAGAGGTTTTCACCGTCATCCCCGAAGCGTGCGAGGCAGCTGCGGTAAAGCTCGTCGGCGTGGTCGTGAAGTGATTCACAAATATCGGCCTGTTCATCTGCGTCCAGTTCGTTGAGTTTCTCCAGCAGCGTTAATGTCTGGCTTCTGATAAAACGGGCCATGTTAAGGGCGGTTTTTTCCTGTTTAGTCACTGATGCCTCCGTGTAAGGGGGATTTCTGTTTTATGGGGTAATGATACCGATGAAACGCGAGAGGATGCTCACCATACGGGTTACTGATGATGAACATGCCCGGTTACTGGAACGCTGTGAGGGTAAACAGCTGGCGGTATGGATGCGGCGGGTCTGCCTGGGTGAGCCGGTTGCACGCTCCGGGAAGCTGCCGACACTGGCACCGCCGTTACTGCGTCAGCTGGCCGCCATCGGGAATAACCTGAATCAGACAGCGAGGAAGGTGAACAGCGGGCAGTGGTCTTCCGGTGATCGGGTTCAGGTGTTGGCTGCGCTGATGGCCATCGGGGAGGAGCTGCGTCGGCTGCGTCTGGCCGTCAGGGAACAGGGCGCGCGGGATGATTGTTAAATTTCATGCCAGGGGAAAAGGCGGTGGCAGTGGTCCGGTTGATTACCTGCTGGGAAGGGAGCGAAACCGGGAAGGGGCAACGGTGCTTCAGGGTAATCCGGAAGAAGTCCGGGAACTCATCGATGCCACGCCATTTGCGAAGAAATACACGTCAGGTGTTCTGTCGTTCGCGGAGAAGGAGCTGCCGCCGGGAGGACGTGAAAAGGTGATGGCGAGCTTTGAGCGTGTACTGATGCCCGGTCTCGAAAAGAATCAGTACAGCATCCTGTGGGTGGAGCACCAGGACAAGGGACGGCTTGAGCTGAATTTTGTCATTCCGAACATGGAGCTACAGACCGGAAAACGCCTCCAGCCGTACTACGACCGGGCAGACAGGCCGAGAATTGATGCCTGGCAGACGCTGGTGAATCACCATTACGGGCTGCATGACCCCAACGCCCCGGAGAACCGCCGGATACTGACTCTCCCTGATAACCTGCCGGAAACGAAACAGGCGCTTGCAGAGAGCGTCACACGCGGGATAGACGCTCTTTATCATGTCGGGGAGATAAAAGGTCGTCAGGATGTGATTCAGGCGCTCACAGAGGCAGGGCTTGAAGTGGTCAGGGTGATGCGAAGCAGTATCAGCATTGCAGACCCGAACGGTGGGAAGAATATCAGGCTGAAAGGAGCATTTTATGAGCAATCTTTTACAGACGGGCGCGGAGTTCGAGAAAAAGCTGAAAGAGAGAGCCGAATCTACAGAGACAATGCTGAACGACGAGTTCAGCAAGCTCGAAAAATCTGTAAGCAAGGCTGTGACATCAAACGAGACGAAAATCAAAGACGCTATAGCCCTGTTCACAGCTTCGACAGAGGAATCACTGAAAAAACACCGGGAAGGGGTGAAAGAGGCGATGATGCAGCACAGGAAGGACGTGTTAAAGCTGGCAGGGAATACGGGCATGATGTTACTGGGGATGGTCCTTTTCCTGTTTACCGTGAGTGGCGGGACGCTCTGGTATCTTGGCGGGATGATACAGGCGAACCTGGAAGAAATCAGGATACAGGAAGAAACATTGCAGAAACTGAACGCGAAGACATGGGGCGTGGAGTTTGTGCAGGACGGGAGAAGGAAATTTCTGGTTATCCCTCAGGGGAAATCGGCAACGGTGATTCCCTATCAGGGGAAGGACTGGGTACAACTGACGGAGTGACACAGAGTGACGGAGCTGGAAAGACATTTGCTGAACGCCTTAGAGCAACTGCAACAGGACTATATGCAGCGGCTGAACGAATGGGAGAGCGCCTTCGTGGAATTGCAGAAAATGTTTTCGCTTACGCAACGGGACAACGCGATGCTGAACGAGCGGGTCATGCAGTTGAGTCAGCAGGTGCAGCACTTGAGCGAGCAGACAGAACGCTTGAGCCAGTTATACAGCGAGAACAGGAGATAAGGGATGAACGGCTGATACAGGAACGCGAACATGAGTTATCCCTGGAGCGTGAGCGCCAGCTGGAAATACAGGAACGGACACAGGATGGCCCTTCGCTGGGATGGTAATCAGAGACAGGCTAAAATGTTGTCAGCGCGTTTCCGGTGCATTTTTTGGGATAATGGTTGGTTCGGGGGCACCGGGAACGCGCTTCAGTCAGACCTTGCTGAAAACACAGGAACGCGTTAAAACGCATACGGGCGCGATTCTGGTGTGTCTTTTGTTGCTGTGTTTTGCCTCTATTGCCAGATCGCGCTCATTCCCCTGAACTTCTGTTTTCCCGCTCCGGTCCCCGTCTTCTTCGCTTCCGAAAGCATGAAAAAAATCCGTTTCAGCTGTCTCTGGCTGGCAATTCCTGCGTGATTCACATGGCTGCATAGCTATGCATGTGGTTAAAATTTACCGGGTGCGATCGCGGCAGTTTTTCGGGTGGTTTGTTGCCATTTTTACCTGTCTGCTGCCGTGATCGCGCCGAACGCGTTTCAGCGGTGCGTACAATAAGGGATTATGGTAAATTATCTTGTTCCTTAGAGAATGATTTGAGGTGGTATCCTGCACTTATTTAAATATGCTTGCTTGGGAAATTCCAGGTTGCAGTATGGTTGAGTTGTAATTTTCCTATGATAGGAAAAATGTTATATTATTAATTTATTTGTGAGGCTTCATAAAGAATGAAAATTTCTGATATTGAAAAAAACATATATAAAGGACTAGCTGAATTTATTTCACAAAAAATCAGAGATGAACATGATATATGCCTTGGACAGTTTGAATCAGAGGAATTACTTGATGAGATTCTTAAAAGAGTAATCCCAGTCATATATAATGTGGCTATTGATGATGCTATAAAATCAGTAAGGAATGTTGGGGATAGATTAGAGGAGGAATTAGATATGAGGAAGGTAGTGTGACTAATTTTAAATCAGACTTAAATCTAATAAGAAAAGAATGGTATAATGCATTTTATTCAGGTAATACTGAAATGCTAGATTACTTGGAAGCTGATTGGTTTATTTCAACAAATGGTCAAAAAGTTATCTATAAAAAACATCAGTTACGAAAGATTGATATGCGTCCAGCGAGGATTTTACCTAGCATAGAAAGATATGAATATGAGGTCGTAATGCGTGAGTTTAAAGGCATTGCTTGTGTTTCAGGGAAAGCTGAAATAAAGCAAAATGATGGAAATATATTAATGGCTTTTATTGAGAATTGGATAAAGGTTAATGGTGGATGGAAAATGCAGTTTATATCGTATGAAAAAATCTAAGGGGAAGCCCCCTTAGATTAATGGTTATATATGTTCAAGTTTTATTTTTTTATAGCGATAAGTTCTGCTTTGAGCTTTAAGCATGTTTTCTGCAAACTGAATATCAAAACTATTTATAGCATTAGTTATTATAGTTTTTATTTTTTCTTTATCAGATAATGAATCACCATGCTCTATAGGTTCCCGCATATATGGATTGTTTTTTAATTCATCAAATAATGTTTTAAATAGTTCTAATCGACGAGGTCTTATAACTGTAAAAGATATATGAAGAGAGTGTTTGCTCTGAGTCGTAACATTGTGCCAGTATCCAGCAGGAAGATATATGGCCTGACCTGGGGTTATATCAAACTCATAATCTGGGGAGGTATTAGGTGGTAGATAATCGAAGCTTCTTTCATCTTCGAGAGGGTATGAATAGGTAGGGTTGTAAACTTTCCATTTTTTTATTCCCTCAATTTGAACAGCTATTACATCATGATTGTCAAAATGAAGCCCAAAGCTTGGTGTTGCTGTAAATGCAGCATATAGATTAGCACTACATGTACATTCTAACTCTTTAGATAACCATAGTCTGCTTTCATCTACAGATTCAAAGAATGACTGGCATCGATCTACTATAAGGGTTGCGCCATCACGTAAGCATTTATATAGCTGATGGCGATTTATATGTGGTGTTCTATCGCCTGTTTGGCTATATGTGTATCTTATAAATCCTTTATACCCCCTAATTTCGGGAAAGTTGTCATTTGCCATTCTAACTCTAGGATAGTGCAATATATCTTTTTCAAGCAATTTATTAAGATCATTCCAGTTGATTAAGTTTTTATAATTAACATCCGTGAATACAAACGGATATTTCTGGAAATTATATTTCTTAAATTTTTCTATGATTTCCTTTTTTATAAGATTATTCATTTTTAAACCTCATGTTTTGTGATATCTATAATCTGTGCTTTAGGTATATTATTTATAAGTTGTTCATCATGAGATATAACAATGATATGCTTTTCCTTGTTTTCCTCTTTTATATAATCACTGATTATTTTTATACCAAGTGAATCAAACCCTTTTGTCGGTTCATCGAAAATAATCAAGTCTACGTTTTTTCCAGATGTAAGAGATACTCCTAATTTTTGTTTTTGTCCACCAGATAAATTATGTCCGTAACCTTTGATCTCATAATCTAGTGGTTTGTCGAACTTAAATCTGTGTAGCAGCTTTTTAATTGTATTTAAATTATTAATGCCGGAATAATGTAATATATTTTCCTCTATAGTTCCAGGCATGAGATCTAGATCTTGAGGAACGTATAAGACATTAACAAAAGGAGAATTTGCTTTTTCTTGTTGTATCCCATTGATTTTTATTGTGTTTTCTTCTGTTGTTATATTGCCAGAGAGAATTTTTGCAATAGTTGTTTTTCCCGAACCATTCTCACCGGTTATAAAGGTAACAACGCCTTTTGTTAATATTAATTTATGGTTGAATGATTTGTTGTATATTTCAATATTGCAAATATTGTCTTTTACATGAAGATATTGCTTGTCTGTGTAATTTGTTTTTTTTATGTCGTTTATTTCGGCACAGTATAAATCAATTTCTGTTCTTGCCATTTTTATTTGTCTAAATAGATAACCAATGCGATTTAATGGGAGAAAAACTTGGAATAAAAAAGTGGCAAGCATAATAATACTACCACGGCTTGCTCTACCATGAAGAAACATCCAGTATGCTGATAGGATAATCAGACTACTAAAAATGACTGAAAGAAAAGCGGAGCTGATACCAAACAGGAAAAATTCATTATTTACTTTTCTTTGTTTTTCTGAATGTGTATTTACAGCTTGAATTACTCGTTTACGACTTTTATCCGTGGTATGGAAAGCTTTATCCATAGGATACATGTGCATCATATCAAACATTCTTCCAGATGCGAATTTGGAGCTAAGTGCAACTGATTTCATCATTGGAAATCTACGTTGTGTCATTTTTATGACAAATATTATATAGATTGCCATTATTATTATAAACTCAATGGCTATTAATGTATTAACACTTATACAAATTGTTATGATTATTCCAATCATTTGTATTAATAATGGTACTACATCAGAACATATTGTATAAAATAATGATGATGCAGAAGAAAGCATGCTTTCTATAACCTTATTTAGTTCTCCTTTATTTTTCTTTAAAAAATGCTCTTGGTGAGAATTTTGTATATTATCAATAACTTGCTCTCTAAGCTTTACAGATAATTCTATATTTGTTTTTTGAGTCAAGTATTCCGATATGCTATATCCAGCAGGCATAAGGAATCTAATTGATAAGAAACATGCTATAAATATTAATAATGAGTTTATTTCTCCTATTGAATCTTTATTGTCAATAACTGTTTTTATTAAATATCCGAATAGAACGAAAAGAAAACTACTTATAGTTGATAATAATATAATAAAAAACAAATTACATTTATTAAATGTGATGATGTACTTTTCAATAAAATTCAATTTATAATCCTTAAAGCCCGTATATTACGGGCTTTATGTTATCTAGAATTACATGAGCACCCAGCGCCACATCCTTTACCGCTGCAACCACAAACAGAACCATTATCATTCCAAACATCTTTTCGCATTATTATTTTTACAAATTCTGCGGCTGGAAGGTGAGTGATACTCTTTACTTTTTCGATGTAAGAATCACTGGATATGGATTCTTTTGGAATTCTTATAGTATTAATGTTCTTTATGCTGTATCTTACAGCATAATCACCATACCACTTTGCGACAGTTTCATGACCTAGGTAAAAAGCGATTTTTTCAATTTGATTTTTATATTCGTTAAAACGATATTCTTGGAATGTTATACCATGCTCATTAACATGCCTTATCTCATTTTTTAGCATGTCATTTGTATTTGGATAATGGTGGAGGTAAGCACCAAGATATTTTTCACAAAAGCTGGTATAAGCATCTGTAAATTGAATAAACGTATGCCACATTTCATCTATAATTTGTAATTGCTCGTGAACTTTTATATTGTAGCATTCCGTTAGGCATGTTGAGGCTAGCCAGATGAATTTCTTTGTTTCATTAAAGATATCATCAGCTTCTTCTGGTGTTACATTCCATTCTTTACGAAATTTTAGAAGAACATCATCATTGTGATAACTCATGATATCTTCTAATGAGCTAACATTATGAACTTTTGCATAAGAACTGCTGTTCATCTTATGTTGTAGCATAACACCCCCAATTATATATTTGAATGTAGATGAGAATAGTTATCATTTGTTATGGTATTGTTAAATTTGTGCTTGTGTCAATATGCCTAATTCTATAAATGAGATAGTAATCAAGTTTTTTAATGGTTATAGGATCCATTAGTAATACAAGGTTTTTGCAGCCAGTTTTTACGGGTAGGGGCTGCAAGGAAAACAAAATTTTCCCACTCTAAGAGAAGAGAATTGAGTTGGTTGAATGAGTGGATGCATCTAGGGCCGCTAATTCACCGAGTGTAAAGGCTGTACGAAATGTGTTGCAGTCCGATAATAGCCCCCTCCATTGACGTTTTACACATGTGTTGTAGGTTCCAGGAGTGGGCGGATCTCAAAAAGATC"
        #Sequence coresponding to plasmid_8k.fasta
        a = GeneticAlgorithm(2,rot_table,0.1)
        rot_table2 = RotTable()
        rot_table2.setTwist("AA",rot_table.getTwist("AA")+1) #Value around 2200 score
        a.population = [rot_table,rot_table2]
        table,score = a.get_results(seq,traj)
        assert(table == rot_table2)


if __name__ == '__main__':
    unittest.main()
