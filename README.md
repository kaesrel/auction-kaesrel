## Auction Testing Problem

Write unit tests for the `Auction` class in `auction.py`.

You should write tests for how the code **should** behave based on the **specification**. Do not test for how this sample Auction code **actually** hehaves.

The sample code may contain errors! 

Documentation for the Auction class is in 2 places:

1. docstring comments in the Auction class
2. online PDF file

If there are any inconsistencies between the PDF and the docstrings, 
use the docstring comments as authoritative.

## Running Your Tests

When you push code to Github, it will automatically run your tests
using a Github Action.  Click the **Action** tab to view the results.

The Action will test your code using **8 different versions** of Auction.

Version 1: Auction is correct. Your tests should **all pass**.

Version 2-8: At least 1 error in Auction. Some test should **fail** or **error**.

## Assignment

1. Write tests for all the Auction requirements.
2. Try to make your tests PASS for Auction code 1 and at least one test FAIL/ERROR for the others.
3. Analyze the output on Github Actions and try to identify the errors. Complete the table below.

## What to Submit

Push your code to Github classroom.  The table below includes your analysis of the errors.

## Demo Code

`auction_demo.py` interactively runs a random auction on the console.
Press **Enter** after each line to run it.

`auction.py` contains doctest comments for a sample auction. Run using `python3 -m doctest -v auction.py`.


## Error Analysis

Study the output of Github Actions.  **Do not** try to look at the source code.  The goal is to identify the defelt based on your tests.

* What is the nature of the defect? Describe the behavior.
* Which of your test method(s) failed?
* Can you determine the cause of the defect? Which Auction method is incorrect?
  - sometimes you may not be able to determine the faulty method
* If your answer is too long to fit in the table, write a paragraph below & identify which Test Case you are writing about.


| Auction | Failing Test | Your analysis of defect                             |
|---------|--------------|:----------------------------------------------------|
| 1       |      ?       | No defects in this Auction code (or are there?)     |
| 2       |              |                                                     |
| 3       |              |                                                     |
| 4       |              |                                                     |
| 5       |              |                                                     |
| 6       |              |                                                     |
| 7       |              |                                                     |
| 8       |              |                                                     |
