# Author: Enes Kemal Ergin
# Date: 06/10/2017

# This is the my understanding and implementation of MinHashing Algorithm
# Sources that I've used to learn:
# 1. http://mccormickml.com/2015/06/12/minhash-tutorial-with-python-code/
# 2. http://maciejkula.github.io/2015/02/01/minhash/
# 3. https://robertheaton.com/2014/05/02/jaccard-similarity-and-minhash-for-winners/
# 4. http://www.bogotobogo.com/Algorithms/minHash_Jaccard_Similarity_Locality_sensitive_hashing_LSH.php

# Will work on more


def jaccard_similarity(set1, set2):
    """Function to calculate the Jaccard Similarity score"""
    inter_len = len(set1.intersection(set2))
    return inter_len / float(len(set1) + len(set2) - inter_len)

def minHash():
    pass
