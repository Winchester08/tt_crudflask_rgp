from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL, MySQLdb
import MySQLdb.cursors

application = Flask(__name__)


application.config['MYSQL_HOST'] = "localhost"
application.config['MYSQL_USER'] = "ro_adt"
application.config['MYSQL_PASSWORD'] = "techtalk"
application.config['MYSQL_DB'] = "users"

mysql= MySQL(application)

@application.route('/index')
def begin():
    message="IOCS | ADC Team"
    tech="CRUD in Flask & MySQL"
    return render_template('index.html', hello=message, more=tech)
    #return ("Hello ADC Team, Welcome")

@application.route('/create')
def create():
    message="Create Window"
    tech="CRUD in Flask & MySQL"
    return render_template('users/create.html', hello=message, more=tech)

@application.route('/save', methods=['POST', 'GET'])
def save():
    if request.method == 'POST':
        n=request.form['name_user']
        ln=request.form['last_user']
        u=request.form['user']
        tu=request.form['type_user']
        p='us-ADC000'

        save = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        save.execute('''INSERT INTO admin_users(name, lastname, username, password, user_type)
                     VALUES(%s, %s, %s, %s, %s)''',(n,ln,u,p,tu))
        mysql.connection.commit()
        save.close()
        return redirect(url_for('list'))
    
    else:
        error_message='There is an error saving'
        return render_template('users/create.html',error=error_message)
        
@application.route('/list')
def list():
    message="List Window"
    result="Data Results"
    tech="CRUD in Flask & MySQL"
    data = mysql.connection.cursor()
    data.execute("Select * from admin_users order by lastname")
    info=data.fetchall()
    data.close()
    return render_template('users/list.html', info=info, hello=message, result=result,  more=tech) 

@application.route('/update/<id>/')
def update(id):
    message="Update Window"
    tech="CRUD in Flask & MySQL"
    edit=mysql.connection.cursor()
    edit.execute("Select * from admin_users where id=%s",(id,))
    d=edit.fetchall()
    edit.close()
    return render_template('users/update.html', hello=message, info=d[0],  more=tech)

@application.route('/delete/<int:id>/')
def delete(id):
    message="Delete Window"
    delete = mysql.connection.cursor()
    delete.execute("Delete from admin_users where id=%s",(id,))
    mysql.connection.commit()
    return redirect(url_for('list'))
    delete.close()

@application.route('/update_action/<int:id>', methods=['POST'])
def update_action(id):
    nu=request.form['name_user']
    lnu=request.form['last_user']
    user=request.form['user']
    tu=request.form['type_user']
    edit = mysql.connection.cursor()
    edit.execute("UPDATE admin_users set name=%s, lastname=%s, username=%s, user_type=%s where id=%s" ,(nu,lnu,user,tu,id))
    mysql.connection.commit()
    edit.close()
    return redirect(url_for('list'))

if __name__ == '__main__':
    application.run(debug=True, port=6500)
