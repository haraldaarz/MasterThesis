from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# read from xml file and store title value in list
def read_xml():
    import xml.etree.ElementTree as ET
    tree = ET.parse('static/data/data.xml')
    root = tree.getroot()
    title = []
    for child in root:
        title.append(child.attrib['title'])
    return title


@app.route('/')
def home():
    return render_template('index.html', data=55)


@app.route('/admin')
def admin():
    return '<h1>Admin</h1>'


@app.route('/test')
def test():
    # read from xml file and parse it



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)
