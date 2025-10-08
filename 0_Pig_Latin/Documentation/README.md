# Pig Latin Translator

This small Python module implements a Pig Latin translator function `pig_latin(message)` along with a simple CLI entry point.

## Files

- `Pig_latin.py` — Contains the implementation of `pig_latin(message)` and a `main()` function that reads from stdin when the module is executed directly.
- `test_pig_latin.py` — pytest-compatible tests (located in the same directory).

## Behaviour / Contract

- Function: `pig_latin(message: str) -> str`
  - Input: a string `message` containing one or more whitespace-separated words.
  - Output: the Pig Latin translation of the message as a single string where words and punctuation are preserved as described below.
  - Error modes: the function assumes a string input; non-string inputs will raise standard Python errors.

Rules implemented
- Leading non-letter characters on a token (for example, punctuation like `"..."` or numbers) are preserved and kept at the start of the token.
- Trailing non-letter characters are preserved and kept at the end of the token.
- A letter-only word that begins with a vowel (a, e, i, o, u, y) receives the suffix `yay`.
- A word that begins with one or more consonants moves that consonant cluster to the end of the word and appends `ay`.
- The function preserves original capitalization style:
  - If a word was all uppercase, the translated word is returned in uppercase.
  - If a word was title-cased (first letter uppercase, rest lowercase), the translated word is title-cased.

Examples

- `pig_latin('hello')` -> `'ellohay'`
- `pig_latin('apple')` -> `'appleyay'`
- `pig_latin('Hello')` -> `'Ellohay'`
- `pig_latin('HELLO')` -> `'ELLOHAY'`
- `pig_latin('string!')` -> `'ingstray!'`
- `pig_latin('...')` -> `'...'` (no letters to translate)
- `pig_latin('123abc')` -> `'123abcyay'` (leading digits preserved; 'abc' treated as vowel-starting)

Edge cases and notes

- The function treats the letter `y` as a vowel. This is a design choice to match the test-suite expectations; behavior for `y` can vary in different Pig Latin dialects.
- Tokens containing no alphabetic characters are returned unchanged (apart from grouping as the function preserves their prefix/suffix positions).
- Multiple whitespace sequences are collapsed by `str.split()`; if preserving exact spacing is required, additional logic would be needed.

How to run tests

1. Install pytest if you don't have it:

```bash
pip install -U pytest
```

2. Run tests from the package directory:

```bash
cd 0_Pig_Latin
pytest -q
```

How to run the translator interactively

```bash
python Pig_latin.py
# then type a message when prompted
```

Contact / Next steps

- If you want different handling for `y`, or to preserve exact whitespace, I can update the implementation and tests accordingly.
