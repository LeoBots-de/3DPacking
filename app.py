
from flask import Flask, request, jsonify
from packaging import Organizer, Article, Package, Space

app = Flask(__name__)


def solpacking(req):
    packagelist = []
    package_types = req['package_types']
    for package_type in package_types:
        print(package_type['dimensions'])
        packagelist.append(Package(Space(package_type['dimensions']), package_type['cost']))
        pass

    articlelist = []
    articles = req['articles']
    for article in articles:
        #TODO delete cost from Article
        articlelist.append(Article(Space()))

    organizer = Organizer(packagelist, articlelist)
    organizer.solve()

    return req


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
