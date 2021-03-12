### Link to the corpus: 
    1. parallel sentences: https://raw.github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/master/src/data/clean_paral_sents.csv?token=AAAARHXRZG4GO2M2QR6YBDTAJUT3A
    
    2. metadata: https://raw.github.ubc.ca/MDS-CL-2020-21/COLX523_Project_Group6/master/src/data/lang-8-users.csv?token=AAAARHUGEVEKKHAPDACK2RLAJUT3E

### Format: 2 csv files
    1. clean_paral_sents.csv
        - id, user_id, doc_id, original, corrected
        where id is row number, user_id is user's id of the sentences, doc_id is the journal id of the sentence pair, original is the sentence contains grammar mistakes, corrected is the sentence with corrections
        (Note: there might be some sentences have several corrections, you will see them stored in different rows with same original sentences)

    2. lang-8-users.csv (metadata)
        - "sex", "occupation", "lpoints", "user_id", "nation_region", "location", "age"

### Total number of words: 988986 

### Preprocessing:
    1. Remove rows which have NaNs in either original or corrected columns
    2. Remove duplicate rows(which has exact same original and corrected pairs)
    3. Remove sentences which has less than 4 tokens
    
### Potential problems:
    1. Some of the sentences might have other kinds of errors instead of grammar error.
    2. Some of the corrections need context from previous sentences but since our unit is sentence, we lose the context.
