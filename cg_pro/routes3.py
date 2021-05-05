from cg_pro import app
from flask import render_template, url_for, redirect
from cg_pro.forms import TRSFrom
from cg_pro.c_algo2 import b_t_t, b_t_s, b_t_r
from cg_pro.routes2 import point_op_2, point_op


@app.route('/tsr', methods=['GET', 'POST'])
def trans_rotate_scaling():
    form = TRSFrom()
    if form.validate_on_submit():
        x1 = eval(form.point_a.data)
        y1 = eval(form.point_b.data)
        o = form.option.data
        op_list = []
        x1 = list(x1)
        if isinstance(x1[0], int):
            x1 = [list(x1)]

        image1 = point_op(x1, "Original")
        if o == 'T':
            op_list = b_t_t(x1, y1)
            image2 = point_op_2(op_list, "Translation")
        elif o == 'S':
            op_list = b_t_s(x1, y1)
            image2 = point_op_2(op_list, "Scaling")
        elif o == 'R':
            op_list = b_t_r(x1, y1)
            image2 = point_op_2(op_list, "Rotation")

        op_string = op_list
        d1 = {'image1': image1, 'image2': image2, 'op_string': op_string}
        return render_template('trs_transformations.html', form=form, d=d1)
    return render_template('trs_transformations.html', form=form)
