# COLX523_Project_Group_6

**For milestone 4, please see the directories: Milestone_4 and src.**

**The rest of the directories are for the use of the team only.**

## Python Back-end
- Please see `src/backend.py, helper.py`. ([link to src directory](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/tree/master/src))
- Our corpus consists of the set of original and corrected sentences written by language learners. The front end allows the user to apply various types of filters to search the corpus and see the search result. 
  The corpus is annotated with the number of annotators who agree with the correction and this information can be easy accessed via `Search by agreement` criteria.  
                   
## HTML / Javascript Front-end
- Please see [`src/frontend.html`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/frontend.html). for the html file. 
- Please see [`src/frontend.js.`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/frontend.js) for the jsava script. 
- Please see [`src/frontend.css`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/frontend.css) for the css file. 
- Please see [`src/frontend.md`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/frontend.md) for the documentation.  for the frontend documentation. 

## Dockerization and peer review instructions 
- Please see `/src/Dockerfile, requirements.txt`([link to src directory](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/tree/master/src))
- The instructions and image are uploaded to the Google Drive. 

## Improvement on Annotation
- Pleae note that we received external help (Darya's brother) to correct annotation from one bad annotator.
- This improved the interannotator agreement from 10% to 13%
- The corpus is also updated to reflect this change: 
  - [`src/data/final_corpus.csv`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/data/final_corpus.csv) is the (old) corpus built in Milestone 3 which includes annotation from one bad annotator. 
  - [`src/data/final_corpus2.csv`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/data/final_corpus2.csv) is the updated corpus with the improved annotation. 
- For the updated interannotator agreement analysis, please see [`Milestone_4/Improved agreement.ipynb`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/Milestone_4/Improved%20agreement.ipynb). 
- Milestone 4 uses [`src/data/final_corpus2.csv`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/data/final_corpus2.csv).

## Other mentions:
- We also compared our corpus with the 2019 lang8 corpus. There are 2903 sentences in our corpus which also appears in the previous version. Please see [`/src/lang-8_corpus_comp.ipynb`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/lang-8_corpus_comp.ipynb) to see how we compared both corpus .
- We also run our corpus through Errant to check the grammar error types on each sentence. Please see [`/src/data/lang8_errant.txt`](https://github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/blob/master/src/data/lang8_errant.txt). 
