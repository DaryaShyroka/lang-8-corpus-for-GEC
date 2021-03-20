from fastapi import FastAPI
import uvicorn
import helper as hp
from fastapi.responses import FileResponse, HTMLResponse
import ast

app = FastAPI()


@app.get("/")
def start():
    return FileResponse("frontend.html")


@app.get("/{filename}")
def get_file(filename):
    return FileResponse(filename)


@app.get("/corpus/request")
def get_sentence_pairs(
    corpusType,
    agreementType,
    sentenceType,
    wordRange,
    nCorrections,
    sex,
    occupation,
    location,
    Lpoints,
):
    params = {
        "corpusType": int(corpusType),
        "agreementType": int(agreementType),
        "sentenceType": int(sentenceType),
        "wordRange": ast.literal_eval(wordRange),
        "nCorrections": int(nCorrections),
        "sex": int(sex),
        "occupation": int(occupation),
        "location": int(location),
        "Lpoints": ast.literal_eval(Lpoints),
    }
    print(params)
    res = list(hp.get_target_sents(params))
    n = len(res)
    if n < 500:
        return res[:n]
    else:
        return res[:500]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999, debug=True)
