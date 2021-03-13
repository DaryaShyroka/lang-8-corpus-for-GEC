#### Interface Plan

- Content search:
    - Range of sentence length search:
        - Input: (min, max) where min is minimum length of sentence and max is the maximum length, both inclusive
        - Output: return sentence pairs whose length falls into this range
        - Reasons: Users might be interested in how length of the sentence interacts with the number of grammar errors.
    - Metadata search:
        - Input: Boolean operator combined with metadata headers, for example, sex, occupation, location, Lpoints and so on.
        - Output: return sentence pairs where it matches the author with those given metadata
        - Reasons: Users might be interested in if a subgroup of people will make similar grammar errors consistently.
    - Multiple corrections search:
        - Input: an int to indicate how many correct sentences a sentence has
        - Output: return sentences which have that many of corrected versions
        - Reasons: Users might be interested in how different teachers will correct the same sentences in various ways.

- Annotation search
    - Search Annotated sentences:
        - Input: a boolean to indicate whether the user wants the annotated corpus or unannotated one
        - Output: return sentence pairs which have (not) been annotated
        - Reason: Users might only want to check the golden data.

    - Search by agreement:
        - Input: An int from 0-3 (0 = 3 no’s, 1 = 1 yes, 2 no’s, 2 = 2 yeses 1 no, 3 = 3 yeses)
        - Output: return sentences pairs which have the given number of agreements on annotators
        - Reason: Since we employed 3 Amazon Mechanical Turkers to annotate the corpus, users can search by number of annotators which give consistent results.

- Front-end architecture
    - Data types
        - JSON
        - Basic data types: integers, strings, doubles....
    - Frameworks
        - Vue.js, Bootstrap, other
- Back-end will be used as a RESTful service (no visualization elements from back-end)

	 
			

    
	


