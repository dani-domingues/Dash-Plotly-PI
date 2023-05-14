from dash import Dash, html, dcc, Output, Input

# para crir graficos
import plotly.express as px 

# analise de dados
import pandas as pd                          

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# definindo aplicativo do flask
app = Dash(__name__, title='Tráfego Urbano')                         

# Uma tabela
df = pd.DataFrame({                          
    "Fruit": ["Macas", "Laranjas", "Bananas", "Limoes", "Laranjas", "Bananas"],
    "Amount": [6, 3, 5, 5, 6, 7],
    "City": ["Sao Paulo", "Rio de Janeiro", "Fortaleza", "Piracicaba", "Campinas", "Sao Tome"]
})

# Criacao do grafico
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
opcoes = list (df['City'].unique())
opcoes.append("Todas as Opcoes")

# Caixa layout
app.layout = html.Div([ 
    
    html.Div(
        className="header",
        children=[
            html.H1('SISTEMA DE MONITORAMENTO DE TRAFEGO URBANO', className="header-logo"),
        ]
    ),

        html.Div(
        className="body-do-painel",
        children=[
            html.Img(
                src="./assets/utils/logo.png", alt="logo", className='logo'),
            dcc.Dropdown(opcoes, 
                value='', 
                id='demo-dropdown',
                className='demo-dropdown'),
            html.H3(
                children='Para otimizar a fluidez e melhorar a mobilidade no transporte', className="body-do-painel-texto"),
            html.Div(
                children='''
                Lorem Ipsum é simplesmente um texto fictício da indústria tipográfica e de impressão. Lorem Ipsum tem sido o texto fictício padrão da indústria desde os anos 1500, quando um impressor desconhecido pegou uma galera de tipos e os embaralhou para fazer um livro de espécimes de tipos. Ele sobreviveu não apenas a cinco séculos, mas também ao salto para a composição eletrônica, permanecendo essencialmente inalterado. Foi popularizado na década de 1960 com o lançamento de folhas Letraset contendo passagens de Lorem Ipsum e, mais recentemente, com software de editoração eletrônica como Aldus PageMaker, incluindo versões de Lorem Ipsum.
                ''', className="body-do-painel-texto"),
        ]
    ),

    html.Div(
        className="grafico",
        children=[

            dcc.Graph(
                id='grafico_frutas',
                figure=fig
    )
        ]
    ),

])

@app.callback(
    Output ('grafico_frutas', 'figure'),  #Quem vai ser Modificado
    Input ('demo-dropdown', 'value')    #Quem traz a informacao
)
def update_output(value):
    if value == 'Todas as Opcoes':
        fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    else:
        tabela_filtrada = df.loc[df ['ID City']==value, :]
    return fig

# Coloca no ar
if __name__ == '__main__':
    app.run_server(debug=True)
