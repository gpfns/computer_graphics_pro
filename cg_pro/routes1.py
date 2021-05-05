from cg_pro import app
from flask import render_template, url_for, redirect
from cg_pro.forms import *
from cg_pro.c_algo1 import *
from cg_pro.routes2 import point_op


@app.route('/')
def home_page():
    items = [
        {'c1': "Line Drawing", 'c2': 'Brute Force',
         'c3': url_for('line_drawing', a=1), 'c4': 'link'},
        {'c1': "Line Drawing", 'c2': 'Basic Incremental Algorithm',
         'c3': url_for('line_drawing', a=2), 'c4': 'link'},
        {'c1': "Line Drawing", 'c2': 'Bresenham Line Drawing',
         'c3': url_for('line_drawing', a=3), 'c4': 'link'},
        {'c1': "Circle Drawing", 'c2': 'Brute Force',
         'c3': url_for('circle_drawing', a=1), 'c4': 'link'},
        {'c1': "Circle Drawing", 'c2': 'Midpoint Circle Drawing',
         'c3': url_for('circle_drawing', a=2), 'c4': 'link'},
        {'c1': "Circle Drawing", 'c2': 'Brute Force Degrees',
         'c3': url_for('circle_drawing', a=3), 'c4': 'link'},
        {'c1': "Ellipse Drawing", 'c2': 'Midpoint Ellipse Drawing',
         'c3': url_for('ellipse_drawing'), 'c4': 'link'},
        {'c1': "Geometric Transformation", 'c2': 'Translation Rotation Scaling',
         'c3': url_for('trans_rotate_scaling'), 'c4': 'link'},

    ]
    return render_template('home_page.html', items=items)


@app.route('/cg_lab_programs')
def cg_lab_programs():
    return render_template('cg_lab_programs.html')


@app.route('/line_drawing/<int:a>', methods=['GET', 'POST'])
def line_drawing(a=None):
    form = LineDrawing()
    if form.validate_on_submit():
        x1 = form.point1_x.data
        y1 = form.point1_y.data
        x2 = form.point2_x.data
        y2 = form.point2_y.data
        op_list = []
        if a == 1:
            op_list = bf_ld(x1, y1, x2, y2)
        elif a == 2:
            op_list = dda_bia(x1, y1, x2, y2)
        elif a == 3:
            op_list = bresenham_line(x1, y1, x2, y2)

        image = point_op(op_list)
        op_string = op_list
        d1 = {'image': image, 'op_string': op_string}
        return render_template('line_drawing.html', form=form, d=d1)

    return render_template('line_drawing.html', form=form)


@app.route('/circle_drawing/<int:a>', methods=['GET', 'POST'])
def circle_drawing(a=None):
    form = CircleDrawing()
    if form.validate_on_submit():
        x1 = form.radius_c.data
        op_list = []
        if a == 1:
            op_list = sc_circle_drawing(x1)
        elif a == 2:
            op_list = mp_circle(x1)
        elif a == 3:
            op_list = sc_circle_drawing_deg(x1)

        image = point_op(op_list, "Circle Drawing")
        op_string = op_list
        d1 = {'image': image, 'op_string': op_string}
        return render_template('circle_drawing.html', form=form, d=d1)
    return render_template('circle_drawing.html', form=form)


@app.route('/ellipse_drawing', methods=['GET', 'POST'])
def ellipse_drawing():
    form = EllipseDrawing()
    if form.validate_on_submit():
        x1 = form.point_a.data
        y1 = form.point_b.data
        op_list = ellipse_drawing_algo(x1, y1)
        image = point_op(op_list, "Ellipse Drawing")
        op_string = op_list
        d1 = {'image': image, 'op_string': op_string}
        return render_template('ellipse_drawing.html', form=form, d=d1)
    return render_template('ellipse_drawing.html', form=form)
