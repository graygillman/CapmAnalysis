'''Implement GUI app through dash or streamlit allowing ease of use'''
import streamlit as st
from CapmClass import CAPMAnalysis
from io import BytesIO
from datetime import date

# Streamlit UI
st.title("CAPM Analysis Dashboard")

# Inputs
benchmark = st.text_input('Enter your benchmark ticker (^GSPC): ', '^GSPC')
ticker = st.text_input('Enter your stock ticker: ', 'AAPL')
risk_free = st.text_input('Enter your risk free ticker (^TYX): ', '^TYX')
daily_or_monthly = st.selectbox('Do you want daily or monthly data?', ('D', 'M'))

if st.button('Perform Analysis'):
    analysis = CAPMAnalysis(ticker, benchmark, risk_free, daily_or_monthly)
    analysis.download_data()
    data_range_msg = analysis.calculate_returns()
    ols_results = analysis.perform_regression()
    beta_value = analysis.find_beta()

    st.write("Here are the results of the regression analysis:")
    st.dataframe(ols_results)
    st.write(f"OLS {data_range_msg}\n")


    st.write(f"{beta_value}")
    
    # For the plotting, you'll need to implement these methods in your CAPMAnalysis class
    fig1, _ = analysis.plot_regression()
    st.plotly_chart(fig1)


    analysis.calculate_rolling_beta()
    fig2, _ = analysis.plot_rolling_beta()
    st.plotly_chart(fig2)

    file_path = analysis.save_to_excel()
    with open(file_path, "rb") as file:
        excel_bytes = BytesIO(file.read())

    
    # Create the download button
    st.download_button(label="Download Excel File",
                    data=excel_bytes,
                    file_name=f"CAPM_Analysis_{ticker}_{daily_or_monthly}_{date.today()}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
