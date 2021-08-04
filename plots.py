# Import necessary modules 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header('Visualising Data')
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.subheader('Scatter Plot')
  feature_list = st.multiselect('Value at x',('carwidth','enginesize','horsepower','drivewheel'))
  for i in feature_list:
    plt.figure(figsize=(20,5))
    sns.scatterplot(x=i,y='price',data=car_df)
    st.pyplot()
  st.subheader("Visualisation Selector")
    plot_types = st.multiselect("Select charts or plots:", ('Histogram', 'Box Plot', 'Correlation Heatmap'))
    if 'Histogram' in plot_types:
        st.subheader("Histogram")
        columns = st.selectbox("Select the column to create its histogram",
                                      ('carwidth', 'enginesize', 'horsepower'))
        # Note: Histogram is generally created for continous values not for discrete values.
        plt.figure(figsize = (12, 6))
        plt.title(f"Histogram for {columns}")
        plt.hist(car_df[columns], bins = 'sturges', edgecolor = 'black')
        st.pyplot()
    if 'Box Plot' in plot_types:
        st.subheader("Box Plot")
        columns = st.selectbox("Select the column to create its box plot",
                                      ('carwidth', 'enginesize', 'horsepower'))
        plt.figure(figsize = (12, 2))
        plt.title(f"Box plot for {columns}")
        sns.boxplot(car_df[columns])
        st.pyplot()
    if 'Correlation Heatmap' in plot_types:
        st.subheader("Correlation Heatmap")
        plt.figure(figsize = (8, 5))
        ax = sns.heatmap(car_df.corr(), annot = True) # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim() # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5) # Increasing the bottom and decreasing the bottom margins respectively.
        st.pyplot()