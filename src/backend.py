from fastapi import FastAPI
import uvicorn
import helper as hp

app = FastAPI()

@app.get("/corpus")
def get_corpus(size):
    '''Returns corpus with n size'''
    return hp.get_dict_corpus(size = int(size))

@app.get("/corpus/{sent_type}")
def get_words_range(sent_type, start, end):
    '''Returns rows with sentences in {start} - {end} range'''
    return hp.get_by_range(sent_type, range = (int(start), int(end)))

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9999,debug=True)