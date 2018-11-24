# PentaHacks-2018

This web application is to provide rating recommendations to sales training manager based on problem statement from [Actoapp](https://actoapp.com/)

## Getting Started

Following are the required dependencies in order to run this application

- Install python3 (make sure numpy and pandas package are included)
- Install pip
- Install openCV
- Install Django
- Install Indico

## Running the Application

Clone the application to your local machine

`git clone https://github.com/jwdjj/PentaHacks-2018`

Go into the application folder

`cd ./PentaHacks-2018/vidcher/src/`

Run manage.py by doing the following

`python manage.py runserver`

Open your browser and paste the following url:

`http://localhost:8000/blog/`

*note*: this application is using python 3*

## Directories

- */*           : home page where the user can choose to upload the video or record a video
- *submission/* : this is where the user record theirselves and then submit the video
- *login/*      : this page is dedicated for the trainer to login
- *dashboard/*  : the trainer will be able to view overall data of assesment in charts
- *data/*       : the trainer can download individual data of the analysis in .csv format
- *settings/*   : ability to edit profile

## Deployment

_to be updated_

## Technology Used

- [django](https://www.djangoproject.com/) - web framework
- [python](https://www.python.org/) - for backend
- [pandas](https://pandas.pydata.org/) and [numpy](http://www.numpy.org/) - CSV data treatment
- [Indico](https://indico.io/) API - emotion recognition
- [OpenCV2](https://opencv.org/) - haarcascade_frontal_face model for face recognition 
- [Creative Tim](https://www.creative-tim.com/) - frontend template
- Database - To be implemented; using CSV temporarily

## Files

- *record.py: Records your video. Hit q to quit
- Indicotrain.py: Analyzes input video frame by frame using indico API. Result saved Into csv file
- dataanalyzeMASTER: specifically to get average value of each emotion of the BENCHMARK
- dataanalyzeUSER: produces 2 csv: individual percentage of each emotion, frequency of each emotion comparing to the benchmark, and append individual percentage to a master csv file. The line graph where we compare frame by frame score for each emotion is not exported into csv (unless you need it :D)

- *record.py and utils.py are totally copy pastaed from the link commented in the file

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/timcreative/freebies/blob/master/LICENSE.md) file for details

## Acknowledgements

- [Creative Tim](https://www.creative-tim.com/) 
- [Indico](https://indico.io/)