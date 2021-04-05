# About The Project

RESTful API that for every language _used by the most starred public repos created in the last 30 days on GitHub_calculate:
- Number of repos using this language
- The list of repos using the language

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

# Getting Started

## Prerequisites
You should have Python 3 installed on your machine



## Installation
1. Clone the repo

        git clone https://github.com/H0dah/repos-stats
        cd repos_stats
2. Install flask 

        pip3 install flask
3. Set environment variable


        export FLASK_APP=server
4. Run the file

        flask run
5. Go to URL

        http://127.0.0.1:5000/top_repos




# Response Structure

        {
            "Language_name": {
                "num_of_repos": 3,
                "repos": [
                        repo1,
                        repo2,
                        repo3
                ]
            }
        }
