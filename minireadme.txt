Resources used:
- OpenCV2: haarcascade_frontal_face model for face recognition 
- Indico.io: emotion recognition
- Panda/numpy: CSV data treatment

Files:
*record.py: Records your video. Hit q to quit
Indicotrain.py: Analyzes input video frame by frame using indico API. Result saved Into csv file
dataanalyzeMASTER: specifically to get average value of each emotion of the BENCHMARK 
dataanalyzeUSER: produces 2 csv: individual percentage of each emotion, frequency of each emotion comparing to the benchmark, and append individual percentage to a master csv file. The line graph where we compare frame by frame score for each emotion is not exported into csv (unless you need it :D)

*record.py and utils.py are totally copy pastaed from the link commented in the file
