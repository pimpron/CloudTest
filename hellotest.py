from flask import Flask, render_template
app = Flask(__name__)




    
@app.route('/')
def John():
    return 'Pimpron Rattanawan 6006021620029.'

# @app.route('/welcome/<name>')
# def Welcome_name(name) : 
    #return 'Welcome' + name + '!'

if __name__ == '__main__':
    # app.debug = True
     app.run(host = '0.0.0.0', port = 80 )
    # app.run(host = '0.0.0.0')
   # app.run(debug=True)