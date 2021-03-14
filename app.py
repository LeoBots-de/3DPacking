import json
import sys
from flask import Flask, request, jsonify
from packaging import Organizer, Article, Package

app = Flask(__name__)


def solpacking(req):
    packagelist = []
    package_types = req['package_types']
    count = 0
    for package_type in package_types:
        packagelist.append(Package(count,
                                   package_type['dimensions'][0],
                                   package_type['dimensions'][1],
                                   package_type['dimensions'][2],
                                   package_type['cost']))
        count += 1
        pass

    articlelist = []
    articles = req['articles']
    count2 = 0
    for article in articles:
        articlelist.append(Article(count2, article[0], article[1], article[2]))
        count2 += 1

    organizer = Organizer()
    organizer.bins = packagelist
    organizer.articles = articlelist
    packages, items = organizer.pack()

    res = json.dumps({"used_packages": packages, "article_positions": items})

    return res


@app.route('/')
def hello_world():
    return 'Es funzt!'


@app.route('/packaging', methods=['POST'])
def packaging():
    answer = solpacking(request.json)
    return answer


if __name__ == '__main__':

    if(len(sys.argv) == 2):
        with open(sys.argv[1]) as json_file:
            data = json.load(json_file)
        answer = solpacking(data)
        print(answer)
    else:
        app.run(host='0.0.0.0')
