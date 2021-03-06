# README file for Milestone 2

- Corpus collection:
    - Corpus scraping instruction:
        1. Go to /src/scraper.py
        2. Define 
            *TOTAL_WORDS: number of words to scrape* 
            *user_profile: filepath to store user metadata*
            *corpus_file: filepath to store parallel sentences*
            (Note: LOGGING_FILE and CURRENT_USER_FILE are intermediate files created while scraping to keep track of total number of words scraped and current scraping user so that we can restore when scraper crashes)
        3. Run all code in /src/scraper.py
    - To simulate errors (stop and restart):
        1. Run the while loop to scrape the corpus(the cell above the subtitle of Data Preprocessing)
        2. After running a while, you can kill the kernel
        3. Run that cell again, it will read all metadata and keep writing to the user_profile and corpus_file
    - Data Preprocessing:
        1. Remove rows which have NaNs in either original or corrected columns
        2. Remove duplicate rows(which has exact same original and corrected pairs)
        3. Remove sentences which has less than 4 tokens
    - Some notes:
        In order to present a more interesting analysis, we only scrape at most 20 documents from each user since we want to analyze how different learners make different grammar mistakes. Also, the same thing applies to friends connections because we assume that people who are friends to each other might share some similarities between each other. We don't want our sub groups to be restricted to some certain type of users, so we only scrape at most 20 friends from each user.
      
    
    