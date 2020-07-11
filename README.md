# Python-One-Day-Challenge
The Optimized Exhibition Opening

##### PATIL Kunal [MSc AIS, EPITA]

### Understanding the challenge: 
```
To optimize the exhibition with ordering the pictures in frameglasses with list of tags. There are two types of paintings viz. Landscapes and portraits.
The Frameglass can consist of only single landscape or two portraits in it. Tags will be the combination of two portraits in case of portrait for frame and tags are same for landscape for the particular frame.
The scope of this optimization is to validate how interesting the order of paintings in a frame based on the relevancy of tags.
Robot will like if there is relevancy or continuity between tags of two consecutive frames.
```

### Arborescence
```
|- PDOC
    |- PODC_final_score_PATIL_Kunal.py 
        > pilot: Two Calls: 1. 
                 Execute function to create submit files for each input file given
                 provide Input Files and submit files to check score for each entry
                 calculate the global score for each and show the summation
    |- PDOC_PATIL_Kunal.py 
        > main program to execute function
    |- [Input Files]
        - 1_binary_landscapes.txt  
        - 10_computable_moments.txt
        - 11_randomizing_paintings.txt
        - 110_oily_portraits.txt
    |- [Submit Files]
        - submit_1_binary_landscapes.txt
        - submit_10_computable_moments.txt
        - submit_11_randomizing_paintings.txt
        - submit_110_oily_portraits.txt
    |- resume.ipynb 
        > Description of the project
```

### Different Stratergies used:
| Stratergy	| Description | Approach | Test data | Line count in submit file | Results | Summation |
| --- | --- | --- | --- | --- | --- | --- |
| Based on Tag size of Frame | Based on the tag size of each frame, making a list of the tagSize to arrange frames in a order | Sorted | 11_randomizing_paintings | 60000 | 212516 | 336601 |
| | | Sorted | 110_oily_portraits | 40000 | 123900 |
| | | Sorted | 1_binary_landscapes | 80000 | 9 |
| | | Unsorted | 11_randomizing_paintings | 60000 | 212478 |
| | | Unsorted | 110_oily_portraits | 40000 | 123865 |
| Random shuffle of frame sequence | Using Random.shuffle with seek 50, shuffling the result of frame arrangement to generate new order | - | 11_randomizing_paintings | 60000 | 174218 | 293159 |
| | |-| 110_oily_portraits | 40000 | 118762 |
| | |-| 1_binary_landscapes | 80000 | 9 |
| Straight frame sequence | No change after creation of sequence of frames | - | 11_randomizing_paintings | 60000 | 172791
| | |-| 110_oily_portraits | 40000 | 118534 | 291490 |
| | |-| 1_binary_landscapes | 80000 | 12 |
| maximum common tags | sequence of frames based on maximum number of common tags between consecutive frames | - | 11_randomizing_paintings | 60000 | FAIL |
| | |-| 110_oily_portraits | 40000 | FAIL |
| | |-| 1_binary_landscapes | 80000 | FAIL |

### Choosing Stratergy:
```
By analyzing results from above table, Ordering based on Tag size of frames:
1. Number of Tags for Frame containing Landscape = Number of tags of landscape
2. Number of Tags for Frame containing Portrait = Union of Tags for two portraits chosen

The result using this stratergy on some test dataset are twice than result of using other stratergies on same dataset.
Also the summation for global score of each dataset using different stratergies, Choosing frame ordering based on Tag Size of frames is the good approach.
```

### Output of Final score summation
```
|Input Files | Global Score |
|---|---|
| 0_example.txt | 0 |
| 1_binary_landscapes.txt | 9 |
|    10_computable_moments.txt    |   175 |
|  11_randomizing_paintings.txt   |     212516 |
|        110_oily_portraits.txt  |  123901 |
|                   Total Score | 336601 |
```
