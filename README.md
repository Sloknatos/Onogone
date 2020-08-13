# Onogone recruitment test
<br><br>
## Subject

### Features expected

- Get all comment
- Check spell (example: 'travail' -> 'travaille')
- Convert all plural in singular
- Convert all verb in the infinitive
- Convert integer in string
- **[Bonus point]** Check data entry error


### Environment

- Python or Java
- Input / output JSON format
- [Link to jeuxvideo.com news](https://www.jeuxvideo.com/news/1264198/hideo-kojima-a-contacte-junji-ito-concernant-un-projet-de-jeu-d-horreur.htm)

<br><br>

## Rendered work

### Installation

On Unix system :
```SHELL 
apt-get install python3.8
apt-get install python3-pip
git clone https://github.com/Sloknatos/Onogone.git
cd Onogone
pip install -r requirements.txt
```

### Usage

Usage :
`python3.8 main.py [command]`

commands available :
- `write` to get comments and generate the first JSON <sup>[1](#myfootnote1)</sup>
- `read` to read the JSON source and transform data <sup>[2](#myfootnote1)</sup>




### Scrapper module
From original link, get the comments page, scrap comments and write in `.files/original_comment.json` with this format :
```
{
  index: comment_as_string
}
```

index have to value :
- if comment is an original -> id_comment
- if comment is an answer -> answer + a hash of the text


I use BS4 lib.


### Converting module
I use num2words lib to convert integer in string.

I use Spacy to browse the commentary and determine the word type and get the radical.
I use SpellChecker lib to try to correct misspelling.

Module write results in `./files/results.json`.

<br><br>

## Summary of work / not work :

**Working**
- *Scrapper* get comments.
- *Scrapper* get answers.
- *Scrapper* ignore quote (avoid data redundancy).
- Convert integer in string.
- Convert verb in infinitive form.
- Convert plurial in singular form.

**Can be better**
- *Respeller* can be improve to not transform english word.
- *Respeller* transform adverb in infinitive rb.

**Don't work**
- "Les" doesn't convert in "Le".
- Some verb don't change (example: "veux" in my result.old.json).
- Some noun transform into verb and reverse.

I let my result with the .old.json ext.

I made a scrapper for the first time, and I enjoyed it, it was tricky but very fun at the same time.
I never work with text data (and linguistics) and I discovered the difficult of this field.

<br>
<a name="myfootnote1">1</a>: Network sound not working from OVH vps (error 403: forbidden).
<a name="myfootnote2">2</a>: Use from Unix env for Spacy lib (don't test with Anaconda / Windows setup).
