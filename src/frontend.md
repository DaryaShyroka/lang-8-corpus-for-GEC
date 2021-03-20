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