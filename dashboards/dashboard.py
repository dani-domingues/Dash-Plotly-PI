from dash import Dash, html, dcc, Output, Input
import plotly.express as px 
import pandas as pd             
import plotly.graph_objects as go
import plotly.subplots as sp

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# definindo aplicativo do flask
app = Dash(__name__, title='Tráfego Urbano')                         

df_2022 = pd.read_csv("/Users/danieladomingues/PycharmProjects/pythonProject/dashboards/assets/bd_transito_2022.csv", sep=",")
df_2022.head()
# Agrupar por mês e região e calcular a soma do tamanho
df_grouped = df_2022.groupby(['Mes', 'Regiao'], sort=False)['Tamanho'].sum().reset_index()
df_grouped.head()

# Criar o gráfico de barras
fig1 = go.Figure(data=[
    go.Bar(name='LESTE', x=df_grouped[df_grouped['Regiao'] == 'LESTE']['Mes'], y=df_grouped[df_grouped['Regiao'] == 'LESTE']['Tamanho']),
    go.Bar(name='CENTRO', x=df_grouped[df_grouped['Regiao'] == 'CENTRO']['Mes'], y=df_grouped[df_grouped['Regiao'] == 'CENTRO']['Tamanho']),
    go.Bar(name='NORTE', x=df_grouped[df_grouped['Regiao'] == 'NORTE']['Mes'], y=df_grouped[df_grouped['Regiao'] == 'NORTE']['Tamanho']),
    go.Bar(name='OESTE', x=df_grouped[df_grouped['Regiao'] == 'OESTE']['Mes'], y=df_grouped[df_grouped['Regiao'] == 'OESTE']['Tamanho']),
    go.Bar(name='SUL', x=df_grouped[df_grouped['Regiao'] == 'SUL']['Mes'], y=df_grouped[df_grouped['Regiao'] == 'SUL']['Tamanho'])
])

# Atualizar o layout do gráfico
fig1.update_layout(
    title='Comparação de Congestionamento por Mês e Região',
    xaxis_title='Mês',
    yaxis_title='Congestionamento (em metros)',
    barmode='group'
)

dias_semana_ordem = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

# Agrupar por dia da semana e região e calcular a soma do tamanho
df2 = pd.Categorical(df_2022['Dia da Semana'],categories=dias_semana_ordem, ordered=True)
df_grouped = df_2022.groupby(['Dia da Semana', 'Regiao'], sort=False)['Tamanho'].mean().reset_index()
df_grouped.head()
# Criar o gráfico de barras
fig2 = go.Figure(data=[
    go.Bar(name='LESTE', x=df_grouped[df_grouped['Regiao'] == 'LESTE']['Dia da Semana'], y=df_grouped[df_grouped['Regiao'] == 'LESTE']['Tamanho']),
    go.Bar(name='CENTRO', x=df_grouped[df_grouped['Regiao'] == 'CENTRO']['Dia da Semana'], y=df_grouped[df_grouped['Regiao'] == 'CENTRO']['Tamanho']),
    go.Bar(name='NORTE', x=df_grouped[df_grouped['Regiao'] == 'NORTE']['Dia da Semana'], y=df_grouped[df_grouped['Regiao'] == 'NORTE']['Tamanho']),
    go.Bar(name='OESTE', x=df_grouped[df_grouped['Regiao'] == 'OESTE']['Dia da Semana'], y=df_grouped[df_grouped['Regiao'] == 'OESTE']['Tamanho']),
    go.Bar(name='SUL', x=df_grouped[df_grouped['Regiao'] == 'SUL']['Dia da Semana'], y=df_grouped[df_grouped['Regiao'] == 'SUL']['Tamanho'])
])
# Atualizar o layout do gráfico
fig2.update_layout(
    title='Comparação de Tamanho por Dia da Semana e Região',
    xaxis_title='Dia da Semana',
    yaxis_title='Congestionamento (em metros)',
    barmode='group'
)


#Agrupando valores por mês e região e tirando a média de cada mês para cada região.
df_agrupado_mes_regiao = df_2022.groupby(['Mes', 'Regiao'], sort=False)['Tamanho'].mean().reset_index()
df_grouped.head()
fig3 = px.line(df_agrupado_mes_regiao, x="Mes", y="Tamanho", color="Regiao")
fig3.update_traces(textposition="bottom right")

# Agrupar por dia da semana e região e calcular a soma do tamanho
df2 = pd.Categorical(df_2022['Dia da Semana'],categories=dias_semana_ordem, ordered=True)
df_grouped_dia_semana = df_2022.groupby(['Dia da Semana', 'Regiao'], sort=False)['Tamanho'].mean().reset_index()
df_grouped_dia_semana.head()
fig4 = px.line(df_grouped_dia_semana, x="Dia da Semana", y="Tamanho", color="Regiao")
fig4.update_traces(textposition="bottom right")

df_2022.head()

#Agrupando por mês e local
df_grouped_local = df_2022.groupby(['Mes', 'Local'], sort=False)['Tamanho'].mean().reset_index()
df_grouped_local.head()
df_grouped_local.tail()
fig5 = px.line(df_grouped_local, x="Mes", y="Tamanho", color="Local")
fig5.update_traces(textposition="bottom right")
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
            # dcc.Dropdown(, 
            #     value='', 
            #     id='demo-dropdown',
            #     className='demo-dropdown'),
            html.H3(
                children='Para otimizar a fluidez e melhorar a mobilidade no transporte', className="body-do-painel-texto"),
            html.Div(
                children='''
                Lorem Ipsum é simplesmente um texto fictício da indústria tipográfica e de impressão. Lorem Ipsum tem sido o texto fictício padrão da indústria desde os anos 1500, quando um impressor desconhecido pegou uma galera de tipos e os embaralhou para fazer um livro de espécimes de tipos. Ele sobreviveu não apenas a cinco séculos, mas também ao salto para a composição eletrônica, permanecendo essencialmente inalterado. Foi popularizado na década de 1960 com o lançamento de folhas Letraset contendo passagens de Lorem Ipsum e, mais recentemente, com software de editoração eletrônica como Aldus PageMaker, incluindo versões de Lorem Ipsum.
                ''', className="body-do-painel-texto"),
        ]
    ),

    
    html.Div(
        className="grafico1",
        children=[
            dcc.Graph(
                id='grafico_frutas',
                figure=fig1,
                style={
                'borderRadius': '10px',
                'border': '20px solid #252a48'
            }            
                
    )
        ]
    ),
    html.Div(
    className="grafico2",
    children=[
        dcc.Graph(
            id='grafico_frutas',
            figure=fig2,
            style={
                'borderRadius': '10px',
                'border': '20px solid #252a48'
            }        
)
    ]
),
    html.Div(
    className="grafico3",
    children=[
        dcc.Graph(
            id='grafico_frutas',
            figure=fig3,
            style={
                'borderRadius': '10px',
                'border': '20px solid #252a48'
            }        
)
    ]
),
    html.Div(
    className="grafico4",
    children=[
        dcc.Graph(
            id='grafico_frutas',
            figure=fig4,
            style={
                'borderRadius': '10px',
                'border': '20px solid #252a48'
            }        
)
    ]
),
    html.Div(
    className="grafico5",
    children=[
        dcc.Graph(
            id='grafico_frutas',
            figure=fig5,
            style={
                'borderRadius': '10px',
                'border': '20px solid #252a48',
                'position':'fixed'
            }        
)
    ]
),


])

# Coloca no ar
if __name__ == '__main__':
    app.run_server(debug=True)
