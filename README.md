# Fibonacci-Generator
---
Simple small script that started with me wanting to make a fibonacci generator and evolved into a customized script that runs and is visualized exclusively in the command line with the thanks to [Greenstick](https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console). 
---
## Introduction

This script generates the Fibonacci sequence up until the users' specifcation of how big it wants the file to be. 

It also has other functionality such as whether the user wants each term numbered or an additional newline to sperate the terms in the text file.

The program produces a file `fibonacci-generator-output.txt` which defaults to the users desktop. Further refinement will be done to allow custom output location.

## Help

This script is simple. Runs in native Python without any dependencies. You can just download it and run it as normal. 

Be aware with larger file sizes, the program takes a while to run. Up to a few minutes if you want a 1GB file

Also be aware that the progress bar will not always be 100% when it is finished. The program is designed to reach a file size less than or equal to the limit. If the closest file size without going over is below the limit, that may be reflected in the progress bar.
ex. 99.6%, 99.9% is considered complete

## Roadmap

- [ ] Rework as CLI. Replace top variables with command line arguments.
- [ ] Allow user to determine where the output file is.
- [x] Add time taken to complete text file.