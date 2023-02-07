from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/english')
def english():
    return render_template('english.html')

@app.route('/tamil')
def tamil():
    return render_template('tamil.html')

@app.route('/telugu')
def telugu():
    return render_template('telugu.html')

@app.route('/hindi')
def hindi():
    return render_template('hindi.html')
    
if __name__=='__main__':
    app.run(debug=True)