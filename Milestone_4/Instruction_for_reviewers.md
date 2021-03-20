# Peer Review Instructions

## Introduction to Corpus

This corpus is a collection of sentences written by English-langauge learners and corrections of these sentences offered by native English speakers. These sentences are scraped from the Lang-8 website, https://lang-8.com/, a web community of native speakers supporting language learners. Lang-8 users can submit a sentence in a language that they are learning, and this sentence will be examined and corrected by another user whose native language is hopefully the language of the sentence. This corpus has 75,112 pairs of original sentences and corrected sentences from the website. 

However, not all corrected sentences on Lang-8 are grammatical. Sometimes, the person correcting the sentence was not a native speaker of English, and other times, they could have just made a mistake or missed some errors in the original sentence. For this reason, we chose our annotations to be the approval of the corrections scraped from Lang-8. We asked mechanical turkers to state whether they agree with the corrections offered in the corrected sentence. The exact question was, "Does the corrected sentence correct all of the grammatical errors made in the original sentence?". We obtained 550 annotated sentences from Mechanical Turk workers, each annotated by three workers. 

The corpus contains the number of agreements from the annotators, as well as metadata such as location, occupation and Lpoints for some users. 

## Filter Criteria

The frontend allows to filter the sentences based on the annotation characterstics (such as number of annotator agreements, the number of words in the original or corrected sentences), and meta data (such as sex, occupation and the user's current location. )

- Search from annotated corpus:

- Search by Agreement: the number of annotators who agree with the correction. The minimum number is 0 and the maximum number is 3. 

- Word Range: the number of words in the sentence

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

- Example 2: you want to see the pair of original and corrected sentences originally written by a user who currently lives in U.S.A:
    
    (Search from: annotated corpus, Location: USA)
