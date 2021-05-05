import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def plot_view(x, y, b=None):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    if b is None:
        axis.set_title("Line Drawing")
    else:
        axis.set_title(b)
    axis.set_xlabel("X-axis")
    axis.set_ylabel("Y-axis")
    axis.grid()
    axis.plot(x, y, "ro-")

    # Convert plot to PNG image
    png_image = io.BytesIO()
    FigureCanvas(fig).print_png(png_image)

    # Encode PNG image to base64 string
    png_image_b64_string = "data:image/png;base64,"
    png_image_b64_string += base64.b64encode(png_image.getvalue()).decode('utf8')

    return png_image_b64_string


def plot_view_1(x, y, b=None):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title(b)
    axis.set_xlabel("X-axis")
    axis.set_ylabel("Y-axis")
    axis.grid()
    for i in zip(x, y):
        axis.annotate(str((round(i[0], 2), round(i[1], 2))), i)
    axis.plot(x, y, "ro-")

    # Convert plot to PNG image
    png_image = io.BytesIO()
    FigureCanvas(fig).print_png(png_image)

    # Encode PNG image to base64 string
    png_image_b64_string = "data:image/png;base64,"
    png_image_b64_string += base64.b64encode(png_image.getvalue()).decode('utf8')

    return png_image_b64_string


def point_op(l1, b=None):
    x = list(map(lambda k: k[0], l1))
    y = list(map(lambda k: k[1], l1))
    image = plot_view(x, y, b)
    return image


def point_op_2(l1, b=None):
    x = list(map(lambda k: k[0, 0], l1))
    y = list(map(lambda k: k[1, 0], l1))
    image = plot_view_1(x, y, b)
    return image
