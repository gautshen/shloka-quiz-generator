**generate_quiz.py**

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

The command above will generate a PDF slide deck containing 20
questions. Each question has three slides

* The first slide containing the word whose shloka needs to be
  guessed.

* The second slide containing the word and four options. Each option
  is the first pAda of a shloka from the text file. One of the options
  corresponds to the shloka containing the word.

* The third slide containing the word, the four options, with the
  correct option highlighted in a different color. The correct shloka
  is also presented in its entirety with the pAda containing the word
  highlighted in a different color.

**Dependencies**

* The script uses `pylatex` to generate the PDF with Devanagari fonts
  from an ITRANS text file consisting of sanskrit shlokas. To install
  pylatex:

  ```
  pip3 install pylatex

  ```

* The script uses `devtrans` to convert from ITRANS to Devanagari
  encoding. To install `devtrans`:
  ```
  pip3 install devtrans

  ```

* The script uses the `Lohit Devanagari` script, `polyglossia` latex
  package, `xelatex`. On Ubuntu,

  ```
  sudo apt install fonts-lohit-deva
  sudo apt install texlive-lang-other
  sudo apt install texlive-xetex

  ```

**Input File**

As mentioned above, the script takes as an input a ITRANS file
containing the Sanskrit Shlokas.

The expected format of the ITRANS text file should satisfy the
following constraints:

* one shloka per line.
* uses a comma (,) to delimit the pAda-s of the shloka.

Right now, the script assumes 4 pAda-s per shloka.

The `Texts` directory contains a sample ITRANS file containing the the
first chapter of Srimad Valmiki Ramayana known as Moola-Ramayana.


**How does the script work**

The script picks a set of random 4 shlokas from the file, and then
picks one of them, again at random. It then picks a random word from
the selected shloka and presents that as the quiz question. The 4
shlokas are presented as options.

This is based on the format of the quiz conducted by Sri. Raghavendra
Aithal Acharya of Sri Vishvesha Dhama Gurukula, Bengaluru.