# aoc2020
Advent of Code 2020

# Potential improvements

## General

* Work out how to get VSC to save without whitespace at end of lines.
* Can we get pycodestyle to fix things automatically?

## Day 8

There are various options for solving this in either a more analytic way, or at least not continually rerunning the code from scratch from the beginning. Worth thinking about? Some interesting ideas in the solutions thread.

## Day 9

Worth refactoring so we don't rerun bits of code, and
to put the number of steps as an optional variable for testing. The latter is a common paradigm, so want to do it more sensibly.

## Day 10

Another one to refactor to combine a and b more reliably

## Day 11

Optimisations:
* Do the visibility checking once, and maintain a list of the neighbouring seats we care about.
* On each pass, compile a list of seats which can see one that has changed state, and then only
run the update on those in the next pass.

## Day 13

A lot of people did this via the Chinese Remainder Theorem, and that's more efficient, but given the relatively small numbers involved, the direct search is still almost instantaneous. For the inputs provided, the bus numbers are coprime, so you could just multiply them rather than working out the LCM.

Perhaps worth tidying up a bit.

## Day 14

There are some more idiomatic ways of doing the Python bit-twiddling in the solutions thread.

## Day 15

Added a much simpler python version as alternative

## Day 16

Much better to have ticket and range as classes and abstract everything out

## Day 17

A lot of cut and paste - could be simplified?
Here and others: want a dict which assumes zero for unreferenced values.

## Day 18

My solution is iterative with a lot of regexs, so we are effectively reparsing the entire string multiple times. More efficient for complex expressions would be to lex it and construct a tree. Or, as some have done, create new objects which have different priorities and just run eval.

## Day 19

Need to add tests in 

## Day 20

Part a only for now and no tests. Needs tidying up - want one single rotate function

## Day 22

Review code

## Day 23

Refactor code to combine two parts. Add tests.

## Day 24

Again add tests.