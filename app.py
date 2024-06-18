from flask import Flask,render_template,request

app=Flask(__name__)

name=''
level=''
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/',methods=['POST','GET'])
def save():
    if request.method=='POST':
        name=request.form.get('name')
        lev=request.form.get('lev')
        file=open('data/data.txt','a+')
        file.seek(0)
        read=file.readlines()
        for i in read:
            if name in i:
                return render_template('history.html',data=read)
        file.writelines([name,'-',lev,'\n'])
        file.close()
        return render_template('index.html')

@app.route('/history')
def history():
    file=open('data/data.txt','r')
    data=file.readlines()
    return render_template('history.html',data=data)
if __name__=='__main__':
    app.run(debug=True)
