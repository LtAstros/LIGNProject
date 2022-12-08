# LIGN Final Project 

## Benjamin Chen, Costin Smilovici, Vedan Desai

## File listing and directory

### pbp_data

#### regular_season

##### reg_pbp_2019

The raw play-by-play data for the 2019 NFL regular season as collected by NFLfastR(https://www.nflfastr.com/).

##### reg_pbp_2022

The raw play-by-play data for the 2022 NFL regular season as collected by NFLfastR(https://www.nflfastr.com/).

### 2019_NFL_highlight_transcript - Sheet1.csv

Transcripts collected from 2019 NFL regular season games.

### transcripts_2022

Transcripts collected from 2022 NFL regular season games.

### DataPreprocess2019.ipynb

Data pre-processing scripts for merging play-by-play and transcript data for 2019 season.

### DataPreprocess2022.ipynb

Data pre-processing scripts for merging play-by-play and transcript data for 2022 season.

### Demo.ipynb

Demo in the form of a Jupyter notebook that can be used to demonstrate JSON generation and 
GPT-3 results.

### HypothesisTest.ipynb

Notebook used for conducting final hypothesis test.

### NFLTranscriptQuiz.csv

All 28 valid results from the survey sent out (used to create hypothesis test).

### blind_test.csv

GPT-generated vs real transcripts used to create survey.

### blind_test_solutions.csv

Real transcripts to check survey selections against.

### config.py

Necessary configuration to use GPT-3 API (API key that expires on 12/17/2022)

### demo.py

Demo back-end code.

### gpt3.py

Code that processes an input through a GPT-3 model using the 'prompt_2019_2.txt' as input.

### gpt3Code.ipynb

Notebook used for testing gpt3.py and generating input-responses for paper.


### prompt_2019_1.txt

Initial prompt used for generating results, trained on 2019 data.

### prompt_2019_2.txt

Second prompt used for generating results, trained on 2019 data.

### prompt_2019_3.txt

Third prompt used for generating results, trained on 2019 data. All three prompts tested in gpt3Code.ipynb.

### test_input1.txt - test_input5.txt

5 inputs processed through GPT-3. Used for prompt engineering.

### test_output1.txt - test_output5.txt

All 5 resulting outputs. 