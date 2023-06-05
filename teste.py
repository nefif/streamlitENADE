import pandas as pd
import streamlit as st
import altair as at

df = pd.read_csv('datasets\incriçõesEnade.csv')

filtro_2021 = df[df['NU_ANO'] == 2021]

#Gráfico de Barras por Quantidade por Ano
count_ano = df['NU_ANO'].value_counts()
count_ano = pd.DataFrame(count_ano).reset_index()
count_ano.index = range(1, len(count_ano) + 1)
count_ano.columns = ['Ano do ENADE', 'Total de Inscrições']
grafico_ano_barra = at.Chart(count_ano).mark_bar().encode(
    x=at.X('Ano do ENADE:N', axis=at.Axis(title='Ano do Enade')),
    y=at.Y('Total de Inscrições:Q', axis=at.Axis(title='Total de Inscrições')),
    text='Total de Inscrições:Q')
grafico_ano_linha = at.Chart(count_ano).mark_line(color='red').encode(
    x=at.X('Ano do ENADE:N', axis=at.Axis(title='Ano do Enade')),
    y=at.Y('Total de Inscrições:Q', axis=at.Axis(title='Total de Inscrições')))

#Gráfico de Barras por Região
count_regiao = filtro_2021['CO_REGIAO_CURSO'].value_counts()
count_regiao = pd.DataFrame(count_regiao).reset_index()
count_regiao.index = range(1, len(count_regiao) + 1)
count_regiao.columns = ['Região', 'Quantidade de Inscrições']
count_regiao = count_regiao.sort_values(by='Quantidade de Inscrições',
                                        ascending=False)
grafico_regiao = at.Chart(count_regiao).mark_bar().encode(
    x=at.X('Região:N',
           sort=at.SortField(field='Quantidade de Inscrições',
                             order='descending')),
    y='Quantidade de Inscrições:Q')

#Gráfico de Barras por Estado do Brasil
count_uf = filtro_2021['CO_UF_CURSO'].value_counts()
count_uf = pd.DataFrame(count_uf).reset_index()
count_uf.index = range(1, len(count_uf) + 1)
count_uf.columns = ['UF', 'Quantidade de Inscrições']
count_uf = count_uf.sort_values(by='Quantidade de Inscrições', ascending=False)
grafico_uf = at.Chart(count_uf).mark_bar().encode(
    x=at.X('UF:N',
           sort=at.SortField(field='Quantidade de Inscrições',
                             order='descending')),
    y='Quantidade de Inscrições:Q')

#Gráfico de Barras por Categoria de Universidade
count_categoria = filtro_2021['CO_CATEGAD'].value_counts()
count_categoria = pd.DataFrame(count_categoria).reset_index()
count_categoria.index = range(1, len(count_categoria) + 1)
count_categoria.columns = [
    'Categoria de Universidade', 'Quantidade de Inscrições'
]
count_categoria = count_categoria.sort_values(by='Quantidade de Inscrições',
                                              ascending=False)
grafico_categoria = at.Chart(count_categoria).mark_bar().encode(
    x=at.X('Categoria de Universidade:N',
           sort=at.SortField(field='Quantidade de Inscrições',
                             order='descending')),
    y='Quantidade de Inscrições:Q')

#Gráfico de Barras por Grupo de Cursos de Gradução
count_grupo_curso = filtro_2021['CO_GRUPO'].value_counts()
count_grupo_curso = pd.DataFrame(count_grupo_curso).reset_index()
count_grupo_curso.index = range(1, len(count_grupo_curso) + 1)
count_grupo_curso.columns = [
    'Grupo de Cursos (Graduação)', 'Quantidade de Inscrições'
]
count_grupo_curso = count_grupo_curso.sort_values(
    by='Quantidade de Inscrições', ascending=False)
grafico_grupo = at.Chart(count_grupo_curso).mark_bar().encode(
    x=at.X('Grupo de Cursos (Graduação):N',
           sort=at.SortField(field='Quantidade de Inscrições',
                             order='descending')),
    y='Quantidade de Inscrições:Q')

#Sidebar com os filtros
with st.sidebar:
    st.title('Filtros')
    st.header('Gráficos pela Quantidade de Incritos no Enade 2021')

    regioes_selecionadas = st.multiselect('Selecione uma ou mais regiões :',
                                          count_regiao['Região'])

    estados_selecionados = st.multiselect('Selecione um ou mais estados (UF):',
                                          count_uf['UF'])

    categorias_selecionas = st.multiselect(
        'Selecione a Categoria da Instituição de Ensino Superior:',
        count_categoria['Categoria de Universidade'])

    grupos_selecionados = st.multiselect(
        'Selecione o Grupo de Cursos:',
        count_grupo_curso['Grupo de Cursos (Graduação)'])

#Filtro e Exibição do Dataframe e do Gráfico das Regiões
count_regiao_filtrada = count_regiao[count_regiao['Região'].isin(
    regioes_selecionadas)]
grafico_regiao_filtrada = at.Chart(count_regiao_filtrada).mark_bar().encode(
    x='Região', y='Quantidade de Inscrições')

st.header('Quantidade de Inscrições por Região do Brasil')

if regioes_selecionadas:
    st.dataframe(count_regiao_filtrada, use_container_width=True)
    st.altair_chart(grafico_regiao_filtrada, use_container_width=True)
else:
    st.dataframe(count_regiao, use_container_width=True)
    st.altair_chart(grafico_regiao, use_container_width=True)

#Filtro e Exibição do Dataframe e do Gráfico dos Estados(UF)
count_uf_fitrado = count_uf[count_uf['UF'].isin(estados_selecionados)]
grafico_uf_filtrado = at.Chart(count_uf_fitrado).mark_bar().encode(
    x='UF', y='Quantidade de Inscrições')

st.header('Quantidade de Inscrições por Estado do Brasil')

if estados_selecionados:
    st.dataframe(count_uf_fitrado, use_container_width=True)
    st.altair_chart(grafico_uf_filtrado, use_container_width=True)
else:
    st.dataframe(count_uf, use_container_width=True)
    st.altair_chart(grafico_uf, use_container_width=True)

#Filtro e Exibição do Dataframe e do Gráfico da Categoria das Universidades
count_categoria_filtrado = count_categoria[
    count_categoria['Categoria de Universidade'].isin(categorias_selecionas)]
grafico_categoria_filtrado = at.Chart(
    count_categoria_filtrado).mark_bar().encode(x='Categoria de Universidade',
                                                y='Quantidade de Inscrições')

st.header('Quantidade de Inscrições por Categoria de Universidade')

if categorias_selecionas:
    st.dataframe(count_categoria_filtrado, use_container_width=True)
    st.altair_chart(grafico_categoria_filtrado, use_container_width=True)
else:
    st.dataframe(count_categoria, use_container_width=True)
    st.altair_chart(grafico_categoria, use_container_width=True)

#Filtro e Exibição do Dataframe e do Gráfico dos Grupos de Cursos de Gradução
count_grupos_filtrado = count_grupo_curso[
    count_grupo_curso['Grupo de Cursos (Graduação)'].isin(grupos_selecionados)]
grafico_grupo_filtrado = at.Chart(count_grupos_filtrado).mark_bar().encode(
    x='Grupo de Cursos (Graduação)', y='Quantidade de Inscrições')

st.header('Quantidade de Inscrições por Grupo de Cursos (Graduação)')

if grupos_selecionados:
    st.dataframe(count_grupos_filtrado, use_container_width=True)
    st.altair_chart(grafico_grupo_filtrado, use_container_width=True)
else:
    st.dataframe(count_grupo_curso, use_container_width=True)
    st.altair_chart(grafico_grupo, use_container_width=True)

st.dataframe(count_ano)
st.altair_chart(grafico_ano_barra + grafico_ano_linha,
                use_container_width=True)