# Peer Review Instructions

## Introduction to Corpus

This corpus is a collection of sentences written by English-langauge learners and corrections of these sentences offered by native English speakers. These sentences are scraped from the Lang-8 website, https://lang-8.com/, a web community of native speakers supporting language learners. Lang-8 users can submit a sentence in a language that they are learning, and this sentence will be examined and corrected by another user whose native language is hopefully the language of the sentence. This corpus has 75,122 pairs of original sentences and corrected sentences from the website. 

However, not all corrected sentences on Lang-8 are grammatical. Sometimes, the person correcting the sentence was not a native speaker of English, and other times, they could have just made a mistake or missed some errors in the original sentence. For this reason, we chose our annotations to be the approval of the corrections scraped from Lang-8. We asked mechanical turkers to state whether they agree with the corrections offered in the corrected sentence. The exact question was, "Does the corrected sentence correct all of the grammatical errors made in the original sentence?". We obtained 550 annotated sentences from Mechanical Turk workers, each annotated by three workers. 

The corpus contains the number of agreements from the annotators, as well as metadata such as location, occupation and Lpoints for some users. 

## Filter Criteria

The frontend allows to filter the sentences based on the annotation characterstics (such as number of annotator agreements, the number of words in the original or corrected sentences), and meta data (such as sex, occupation and the user's current location. ). The query response shows the first 500 pairs which satisfy the filter criteria. 

- Search from: 
  Both - all pair of sentences in the corpus 
  Unannotated Corpus - the pair of sentences unexamined by the annotators
  Annotated Corpus - the pair of sentences examined by the annotators
  

- Search by Agreement: Note that this section is applicable only when you select to search from Annotated corpus. This lets you choose the number of annotators who agree with the correction. 
  All 'yes' means all three annotators agreed with the correction.
  All 'no' means all three annotators disagreed with the correction.
  1 'yes' 2 'no' means one annotator agreed with the correction while two did not.
  2 'yes' 1 'no' means two annotators agreed with the correction while one did not. 

- Word Range: the number of words in the sentence. The top box is the minimum number of words and the box below is the maximum number of words in the sentence. 
  If you specify non-positive integer, the system will give you an error. You can also click on 'Does not matter' if you don't care about the word range. 

- Original or Corrected or Both: If original is checked, the filter criteria is applied to original sentences. If corrected is checked, the filter criteria is applied to corrected sentences. 
  If you check both, the filters will be applied to both original sentences and corrected sentences. 

- Sentences with n corrections: Some sentences have corrections offered by multiple native Speakers. You can search for sentence pairs where multiple corrections are offered. 

- Sex: gender of the author of the original sentence

- Occupation: occupation of the author of the original sentence

- Location: current location of the author of the original sentence

- Lpoints: points each user gains every time he / she makes corrections or receives Thanks points. Users with more Lpoints will be given preference, making them more likely to receive corrections. 

## A list of things you can try

You can combine several combination of these criteria.

- Example 1: you want to see the pair of original and corrected sentences agreed by all three annotators:

    (Search from: annotated corpus, Search by Agreement: 3)

- Example 2: you want to see all the pair of original and corrected sentences originally written by a user who currently lives in U.S.A:
    
    (Search from: Both, Location: USA)
    
- Exmample 3: you want to see the pair of original and corrected sentences originally written by users whose occupation is a designer that have not been examined by the annotators:
    
    (Search from: unannotated corpus, occupation: Designer )
    
- Example 4: you want to see all the pair of sentences with at most 25 words:

    (Search from: Both, Word Range: 1 in the first box and 25 in the second box - please note that you have to specify both minimum and maximum. 
     They can be the same number in which case you are searching for sentences with exactly n words.)
