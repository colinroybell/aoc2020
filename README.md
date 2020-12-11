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
