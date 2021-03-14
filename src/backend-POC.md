backend.py file is used as a main Controller (Listener) of our project.

It is basically a RESTful service, which listens for a requests and returns results in JSON or basic (int, string, double..) format.

13-03-2020 it has the following methods:

1. `get_corpus(size)`: returns the rows from the corpus with the given size.

Ex.: `http://{domain}/corpus?size=3`

result: 

```
{
"0": [
"673707",
"132180776574210182836253618202132330403",
"Sun room",
"Sunroom"
],
"1": [
"673707",
"132180776574210182836253618202132330403",
"I've always wanted a sun room for a long time.",
"I've always wanted a sunroom for a long time."
],
"2": [
"673707",
"132180776574210182836253618202132330403",
"It's because it can dry laundry even if it rains, and can prevent pollen.",
"It's because I can dry the laundry there even if it rains, and it can prevent pollen."
]
}

```


2. `get_words_range(sent_type, start, end)`: returns the rows from the corpus which of the given sentence type (original or corrected) and in the given range (inclusively).

Ex.: `http://{domain}/corpus/original?start=3&end=7`

result: 
```
{
"1459": [
"648389",
"206501038149726701878528987849200475748",
"Now.",
"Now."
],
"3295": [
"588181",
"200247183467805741640763887008772688844",
"What?",
"What? [Alternative: Huh?]"
],
"3542": [
"198616",
"83855768473255160499590523040416795213",
"Week",
"Week"
...
```