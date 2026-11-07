# Technology Quiz Game

A Python command-line quiz that tests your knowledge of common technology abbreviations and terms.

## Features

- 100 technology and computing questions
- Automatic answer checking
- Correct answer shown after a wrong response
- Correct-answer score tracking
- Final score and percentage
- `q` option to quit during the quiz

## Requirements

- Python 3

## How to Run

From the project folder, run:

```bash
python Quiz_game.py
```

Enter `yes` when asked if you want to play. Type the full expansion of each abbreviation and press Enter. Enter `q` at any question prompt to stop the quiz.

## Example

```text
-----------Welcome to the QUIZ GAME-----------
Do you want to play? yes
-----------Okay! Let's Play :)-----------
What does CPU stand for? central processing unit
-----------Correct-----------
```

At the end, the game displays your number of correct answers and your percentage score.

## Scoring

- Each correct answer adds one point.
- Incorrect answers add no points.
- The final percentage is calculated from the total number of questions:

```text
Percentage = correct answers / 100 * 100
```

## Adding Questions

Questions are stored in the `questions` dictionary in `Quiz_game.py`. Add a new question and answer using this format:

```python
"What does ABC stand for?": "answer expansion",
```

Answers are converted to lowercase and leading or trailing spaces are removed before checking.

## Project Structure

```text
Quiz_game.py  Main quiz program
README.md     Project documentation
```
