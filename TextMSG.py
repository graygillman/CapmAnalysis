# Imports
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from CapmClass import CAPMAnalysis

# Flask app setup
app = Flask(__name__)

# Function to parse the incoming message and extract command parameters
def parse_command(incoming_msg):
    parts = incoming_msg.split()
    # Assumes the command is always three words
    command = parts[:3]
    ticker = parts[3]
    benchmark = parts[4]
    risk_free = parts[5]
    frequency = parts[6]
    command_str = ' '.join(command)
    return command_str, ticker.upper(), benchmark, risk_free, frequency

# Main function to handle CAPM analysis based on user input
def main(ticker, benchmark, risk_free, daily_or_monthly):
    # Assuming CAPMAnalysis is your class for CAPM analysis
    analysis = CAPMAnalysis(ticker, benchmark, risk_free, daily_or_monthly)
    analysis.download_data()
    data_range_msg = analysis.calculate_returns()
    analysis.perform_regression()
    beta_message = analysis.find_beta()
    fig, image_path1 = analysis.plot_regression()
    analysis.save_to_excel()
    image_url1 = analysis.upload_to_web(image_path1)
    analysis.calculate_rolling_beta()
    fig, image_path2 = analysis.plot_rolling_beta()
    image_url2 = analysis.upload_to_web(image_path2)

    message = f'-------- {ticker} Betas --------'
    # Return the image URL as part of the response
    return message, beta_message, data_range_msg, image_url1, image_url2

# Flask route to handle incoming SMS requests
@app.route("/sms", methods=['POST'])
def sms_reply():
    incoming_msg = request.form.get('Body').lower()
    resp = MessagingResponse()
    
    command_str, ticker, benchmark, risk_free, frequency = parse_command(incoming_msg)

    if 'run my code' in command_str:
        message, beta_message, data_range_msg, image_url1, image_url2 = main(ticker, benchmark, risk_free, frequency)
        resp.message(f"{message}\n{beta_message}\n\n{data_range_msg}")
        if image_url1:  # Check if there's an image URL to send
            resp.message("").media(image_url1)  # Send the image as a separate message
        if image_url2:  # Check if there's an image URL to send
            resp.message("").media(image_url2)  # Send the image as a separate message
    else:
        resp.message("Send 'run my code' to execute your script.")

    return str(resp)

# Start the Flask application if this file is the main program
if __name__ == "__main__":
    app.run(debug=True)
