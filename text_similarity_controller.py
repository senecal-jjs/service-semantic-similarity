import hug 
import gensim.downloader as api

word_vectors = api.load("glove-wiki-gigaword-100")

@hug.default_input_format('application/json')
@hug.get('/similarity-search')
def compute_similarity(data: hug.types.json):
    print(data)
    searchTerm = data["searchTerm"]
    candidateList = data["candidateList"]
    cleanList = [term.replace(" ", "") for term in candidateList]
    similarities = [word_vectors.similarity(searchTerm, term) for term in cleanList]
    return {'term': candidateList[similarities.index(max(similarities))], 'score': max(similarities)}
        