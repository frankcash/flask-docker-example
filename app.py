from flask import Flask, render_template, request, jsonify
import pandas as pd
from bokeh.plotting import figure
from bokeh.charts import Histogram
from bokeh.embed import components
app = Flask(__name__)


@app.route('/')
def helloWorld():
    resp = {
        "message": "flask is running"
    }
    return jsonify(resp)


@app.route("/bokeh")
def index():
    df = pd.read_csv("./data/shoes.csv")
    y = df["sales"]
    x = df["size"]
    plot = figure(title="Sales by Size", x_axis_label='size', y_axis_label='sales')
    plot.line(x, y, legend="Sales", line_width=2)
    script, div = components(plot)
    return render_template('graph.html', script=script, div=div)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
