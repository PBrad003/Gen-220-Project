Gen-220-Project

Title: Summary Statistics and File Format Conversion for Morphological Datasets

Members: Peggy Brady

Problem: 
Datasets downloaded off Morphobank are often in Nexus format. While PAUP can parse Nexus files, TNT (a tree-building program with a much faster algorithm) has its own required TNT format. These formatting issues extend to writing constraints for the trees. Each has a slightly different format. Morphological datasets that include fossils are also likely to contain highly incomplete taxa that can bog down analyses and greatly increase computation times. Sometimes, morphological matrices are poorly constructed, and have large numbers of surprising similarities between distantly related species. 

Approaches deconstructed by goal:
Goal: Determine how incomplete each taxa is
Approach: For loop that reads through the dataset as a string and adds up the total number of “?” or “-“ and divides by the total number of characters to get a percentage of characters that are incompete
Goal: Converting Nexus File to TNT format
Approach: Reading in Nexus blocks and grabbing necessary information to rewritten out in TNT format
Goal: Creating a distance matrix that compares each taxa to one another and shows how many similarities there are between each pair of taxa.
Approach: Read each string of characters for a taxon and break it up by column. Compare to each column to that column for other taxa and determine how many columns that are coded (not “?” or “-“) that are identical. Print out matrix that has the raw number of similarities. 
Goal: Rewrite PAUP constraints to work in TNT
Approach: Both allow taxa to be represented by a number. However PAUP starts at 1 while TNT starts at 0. I will read in a constraint and for each number found in the string, I will subtract one. 

Data: 
I have constructed a very simplistic morphological dataset of 10 taxa with 10 characters. Each has a different percentage of completion.

Assessment: 
I will do the comparisons for my small dataset by hand so I can compare the scripts output to the correct answer. 
