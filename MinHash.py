# Author: Enes Kemal Ergin
# Date: 03/11/2017

# This is the my understanding and implementation of MinHashing Algorithm
# Sources that I've used to learn:
# 1. http://mccormickml.com/2015/06/12/minhash-tutorial-with-python-code/
# 2. http://maciejkula.github.io/2015/02/01/minhash/
# 3. https://robertheaton.com/2014/05/02/jaccard-similarity-and-minhash-for-winners/
# 4. http://www.bogotobogo.com/Algorithms/minHash_Jaccard_Similarity_Locality_sensitive_hashing_LSH.php

# Will work on more


from random import randint, seed, choice, random
import string
import sys
import itertools

def generate_random_docs(n_docs, max_doc_length, n_similar_docs):
	for i in range(n_docs):
		if n_similar_docs > 0 and i % 10 == 0 and i > 0:
			permuted_doc = list(lastDoc)
			permuted_doc[randint(0,len(permuted_doc))] = choice('1234567890')
			n_similar_docs -= 1
			yield ''.join(permuted_doc)
		else:
			lastDoc = ''.join(choice('aaeioutgrb ') for _ in range(randint(int(max_doc_length*.75), max_doc_length)))
			yield lastDoc

def generate_shingles(doc, shingle_size):
	shingles = set([])
	for i in range(len(doc)-shingle_size+1):
		shingles.add(doc[i:i+shingle_size])
	return shingles

def get_minhash(shingles, n_hashes, random_strings):
	minhash_row = []
	for i in range(n_hashes):
		minhash = sys.maxint
		for shingle in shingles:
			hash_candidate = abs(hash(shingle + random_strings[i]))
			if hash_candidate < minhash:
				minhash = hash_candidate
		minhash_row.append(minhash)
	return minhash_row

def get_band_hashes(minhash_row, band_size):
	band_hashes = []
	for i in range(len(minhash_row)):
		if i % band_size == 0:
			if i > 0:
				band_hashes.append(band_hash)
			band_hash = 0
		band_hash += hash(minhash_row[i])
	return band_hashes

def get_similar_docs(docs, n_hashes=400, band_size=7, shingle_size=3, collectIndexes=True):
	hash_bands = {}
	random_strings = [str(random()) for _ in range(n_hashes)]
	docNum = 0
	for doc in docs:
		shingles = generate_shingles(doc, shingle_size)
		minhash_row = get_minhash(shingles, n_hashes, random_strings)
		band_hashes = get_band_hashes(minhash_row, band_size)

		docMember = docNum if collectIndexes else doc
		for i in range(len(band_hashes)):
			if i not in hash_bands:
				hash_bands[i] = {}
			if band_hashes[i] not in hash_bands[i]:
				hash_bands[i][band_hashes[i]] = [docMember]
			else:
				hash_bands[i][band_hashes[i]].append(docMember)
		docNum += 1

	similar_docs = set()
	for i in hash_bands:
		for hash_num in hash_bands[i]:
			if len(hash_bands[i][hash_num]) > 1:
				for pair in itertools.combinations(hash_bands[i][hash_num], r=2):
					similar_docs.add(pair)

	return similar_docs

if __name__ == '__main__':
	n_hashes = 200
	band_size = 7
	shingle_size = 3
	n_docs = 1000
	max_doc_length = 40
	n_similar_docs = 10
	seed(42)
	docs = generate_random_docs(n_docs, max_doc_length, n_similar_docs)

	similar_docs = get_similar_docs(docs, n_hashes, band_size, shingle_size, collectIndexes=False)

	print(similar_docs)
	r = float(n_hashes/band_size)
	similarity = (1/r)**(1/float(band_size))
	print("similarity: %f" % similarity)
	print("# Similar Pairs: %d" % len(similar_docs))

	if len(similar_docs) == n_similar_docs:
		print("Test Passed: All similar pairs found.")
	else:
		print("Test Failed.")
