`generate_quiz.py` is a python3 script to generate a randomized quiz
for sanskrit shlokas in the form of a PDF slide-deck.

```
Usage:
$   ./generate_quiz.py  <File> [number-of-quiz-questions]

```

**Example**
```
$ ./generate_quiz.py  Texts/Moola-Ramayana-itrans.txt 20
```

The script uses `pylatex` to generate the PDF from a text file
consisting of sanskrit shlokas.

The expected format of the text file should satisfy the following constraints:
* one shloka per line
* uses a comma (,) to delimit the pAda-s of the shloka.

Right now, the script assumes 4 pAda-s per shloka.

The script picks a set of random 4 shlokas from the file, and then
picks one of them, again at random. It then picks a random word from
the selected shloka and presents that as the quiz question.

The first pAda of each of the 4 shlokas is presented as options.  The
next slide would contain the answer, revealing the shloka containing
the word.

This is based on the format of the quiz conducted by Sri. Raghavendra
Aithal Acharya of Sri Vishvesha Dhama Gurukula.

**Note**: At the moment the output PDF contains text in ITRANS
  encoding.
