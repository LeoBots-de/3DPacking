import json

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

    #json.dumps({'4': 5, '6': 7}
    for b in organizer.packages:
        print("============", b.string())

        print("ITEMS:")
        for item in b.items:
            print("====> ", item.string())

        print("#########################")
    res = json.dumps({"used_packages": packages, "article_positions": items})
    print(res)
    return res


@app.route('/')
def hello_world():
    solver = Organizer()
    solver.solve()
    return 'Hello World!'


@app.route('/packaging', methods=['POST'])
def packaging():
    answer = solpacking(request.json)
    return answer


if __name__ == '__main__':
    app.run(host='0.0.0.0')
