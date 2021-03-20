#### Frontend documentation

- The content is separated into 3 files: `frontend.html`, `frontend.js`, frontend.css`.
    - `frontend.html`:
        - Contains html data. It imports `frontend.js` and `frontend.css` files.
        - Imports vue.js 3 framework, bootstrap 4 and google-charts.
        - Content is wrapped to `container-fluid` class, which is the Bootstrap requirement for PCs.
        - Content is separated into 3 Bootstrap columns:
            - Search column:
                - Contains a form required for search from the corpus. It contains:
                    - Corpus type search input
                    - Agreement type search input (active if corpus type is 'Annotated' or 'Both')
                    - Two numeric inputs for Word range(1)
                    - Type of the sentences to apply the word range
                    - Input for number of correctections per sentence(1)
                    - html-select to choose user gender
                    - html-select to choose user occupation
                    - html-select to choose user location
                    - Input to choose Lpoints per sentence(1)
                    (1) = inputs are validated as such:
                        - all five inputs can take the numbers in range [0,1000].
                        - 'from' value cannot be greater than 'to' value.
            - Table column:
                - Contains a y-scrollable table with fixed headers for orinal and corrected sentences respectively.
            - Visualization column:
                - Contains a static visualization for the corpus:
                    - Pie chart for annotated/unannotated corpus ratio.
                    - Pie chart for sentences with/without agreement ratio.
                    - Bar chart for journal counts distribution by occupation.
                    - Geo chart for users of the corpus distribution per country.
        - Each form group in the search column has a description. To see it, user has to hover it.
        - Each column has its own scrollbar.
    
    - `frontend.js`:
        - Contains javascript code for the front-end.
        - The syntax of the code obeys Vue.js standard.

    - `frontend.css`:
        - Contains some classes needed for front-end.
                    


                

- Content search:
    - Range of sentence length search:
        - Input: (min, max) where min is minimum length of sentence and max is the maximum length, both inclusive
        - Output: return sentence pairs whose length falls into this range
        - Reasons: Users might be interested in how length of the sentence interacts with the number of grammar errors.
    - Metadata search:
        - Input: Boolean operator combined with metadata headers, for example, sex, occupation, location, Lpoints and so on.
	(Note: Every time you make corrections or receive Thanks points, you get more L points. The more L points you have, the higher your posts will be listed, making them more likely to be corrected)
        - Output: return sentence pairs where it matches the author with those given metadata
        - Reasons: Users might be interested in if a subgroup of people will make similar grammar errors consistently.
		- Percentage of corpus having such attributes: sex - 47.1%, occupation - 22.47%, lpoints - 99.96%, nation_region - 43.67%, location - 42.3%, age - 27.42%
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

	 
			

    
	


