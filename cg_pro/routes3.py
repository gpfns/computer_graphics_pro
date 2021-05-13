from cg_pro import app
from flask import render_template, url_for, redirect
from cg_pro.forms import TRSFrom
from cg_pro.c_algo2 import b_t_t, b_t_s, b_t_r, b_t_cr
from cg_pro.plotting_graphs import point_op_2, point_op, points_ready, plot_view_subs, points_matrix_ready


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
        l_op=[]
        image1 = point_op(x1, "Original")
        l_op.append(points_ready(x1))
        if o == 'T':
            op_list = b_t_t(x1, y1)
            image2 = point_op_2(op_list, "Translation")
        elif o == 'S':
            op_list = b_t_s(x1, y1)
            image2 = point_op_2(op_list, "Scaling")
        elif o == 'R':
            op_list = b_t_r(x1, y1)
            image2 = point_op_2(op_list, "Rotation")
        elif o == 'NR':
            op_list = b_t_cr(x1, y1)
            image2 = point_op_2(op_list, "Rotation Clockwise")
        l_op.append(points_matrix_ready(op_list))
        image3 = plot_view_subs(l_op[0][0], l_op[0][1], l_op[1][0], l_op[1][1])
        op_string = op_list
        d1 = {'image1': image1, 'image2': image2, 'op_string': op_string, 'image3': image3}
        return render_template('trs_transformations.html', form=form, d=d1)
    return render_template('trs_transformations.html', form=form)
