import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    dbc.Form(children=[
        dbc.FormGroup([
            dbc.Label("Title"),        
            dbc.Input(type="text", id="editor/zettletitle")]),
            dbc.FormGroup([        
                dbc.Label("Editor"),
                dbc.Textarea(id="editor/zetteltextarea")
                ])
            ,]),
    dcc.Markdown(id="editor/markdown_display")])
    

@app.callback(
        Output("editor/markdown_display", "children"),
        [Input("editor/zetteltextarea", "value"),
         Input("editor/zettletitle", "value")])
def render_md(md, title):
    if not title:
        title = ""
    else:
        title = "# " + title + "\n"
    if not md:
        md = ""
    return title + md


if __name__ == "__main__":
    app.run_server(debug=True)
