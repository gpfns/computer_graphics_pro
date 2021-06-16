from flask import request, render_template, url_for
from cg_pro import app
from cg_pro.forms2_res import CseSem5
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://test:test@csr.xup54.mongodb.net/Test1?retryWrites=true&w=majority")
db1 = client['cse_sem5']
col = db1['marks_db']
db2 = client['cse_sem6']
col2 = db2['marks_db']


@app.route('/sem5', methods=['GET', 'POST'])
def sem5_results():
    form = CseSem5()
    if form.validate_on_submit():
        rn = form.roll_number.data
        t1 = get_result_s5(rn)
        d1 = {'html_returned': t1, 'op_string': "op_string"}
        return render_template('cse_sem5.html', form=form, d=d1)

    return render_template('cse_sem5.html', form=form)


@app.route('/sem6', methods=['GET', 'POST'])
def sem6_results():
    form = CseSem5()
    if form.validate_on_submit():
        rn = form.roll_number.data
        t1 = get_result_s6(rn)
        d1 = {'html_returned': t1, 'op_string': "op_string"}
        return render_template('cse_sem6.html', form=form, d=d1)

    return render_template('cse_sem6.html', form=form)


@app.route('/sem5-all-r')
def sem5_all_results_r():
    t1 = col.find().sort("Roll_No")
    return render_template('cse_sem5.html', form=CseSem5(), d2=t1)


@app.route('/sem5-all-m')
def sem5_all_results_m():
    t1 = col.find().sort("Total_Marks", -1)
    return render_template('cse_sem5.html', form=CseSem5(), d2=t1)


@app.route('/sem5-all-g')
def sem5_all_results_g():
    t1 = col.find().sort("Student_Gpa", -1)
    return render_template('cse_sem5.html', form=CseSem5(), d2=t1)


def get_result_s5(rn):
    t1 = col.find_one({'Roll_No': int(rn)})
    return t1['Html_Res']


def get_result_s6(rn):
    t1 = col2.find_one({'Roll_No': int(rn)})
    return t1['Html_Res']
