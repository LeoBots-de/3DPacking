# 3DPacking
This project was created in the Relaxdays Code Challenge Vol. 1. See https://sites.google.com/relaxdays.de/hackathon-relaxdays/startseite for more information.
Our participant IDs in the challenge were: CC-VOL1-14, CC-VOL1-16, CC-VOL1-85





##Docker
Please use the following commands to execute the project 
and enter the relative path to the root directory as the path.
```commandline
docker build -t 3dp .   

docker run -d -p 5000:5000 3dp python /3DPacking/app.py "testcase.json"
```


##Alternative: API
Alternatively, you can also run the programme via an API. 
Please do not pass a JSON file as an argument. 
You will receive the answer as JSON via http://127.0.0.1:5000/packaging via POST request.


## JSON Input
```json
{
"package_types":[
  {"dimensions":[10,20,15],"cost":10},
  {"dimensions":[10,10,10],"cost":5}
],
"articles":[[10,10,5],[5,5,5],[9,4,5],[10,20,10],[10,10,10]]
}
```

## JSON Output
```json
{
  "used_packages":[0,1,1],
  "article_positions":[[2,0,0,0],[2,5,1,5],[2,1,6,5],[0,0,0,0],[1,0,0,0]]
}
```
