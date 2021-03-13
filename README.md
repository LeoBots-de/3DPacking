# 3DPacking
This project was created in the Relaxdays Code Challenge Vol. 1. See https://sites.google.com/relaxdays.de/hackathon-relaxdays/startseite for more information. My participant ID in the challenge was:



#Idee
bins volumen/preis - max zu min

artikel nach volumen zu sort - max zu min

möglichst oft den max. bin mit Artikeln füllen

letzer Container wird in preis niedrigeren gepackt



TEST: 
wenn in den besten alles rein passt, dann nächst schlechteren testen

wenn dieser zu klein, dann mit dem überschuss mit nächst schlechteren nochmal TEST

vergleiche aktuellen preis mit erneuten test preis, wenn größer dann

##Docker
```commandline
docker build -t 3dpacking . && docker run -d -p 5000:5000 3dpacking 
```

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
