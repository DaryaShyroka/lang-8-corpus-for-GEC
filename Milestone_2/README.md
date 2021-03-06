# README file for Milestone 1

- Corpus collection:
    - Corpus scraping instruction:
        1. Go to /src/scraper.py
        2. Define 
            *TOTAL_WORDS: number of words to scrape* 
            *user_profile: filepath to store user metadata*
            *corpus_file: filepath to store parallel sentences*
            (Note: LOGGING_FILE and CURRENT_USER_FILE are intermediate files created while scraping to keep track of total number of words scraped and current scraping user so that we can restore when scraper crashes)
        3. Run all code in /src/scraper.py
    - To test stop and restart:
        1. Run the while loop above the subtitle of Data Preprocessing
        2. After running a while, you can kill the kernel
        3. Run that cell again, it will read all metadata and keep writing to the user_profile and corpus_file
    - Data Preprocessing:
        1. Remove rows which have NaNs in original and corrected columns
        2. Remove duplicate rows(which has exact same original and corrected pairs)
        3. Remove sentences which has less than 4 tokens
      
    
    