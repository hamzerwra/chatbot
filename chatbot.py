from flask import Flask, request, jsonify
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("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")

@app.route("/chat", methods=["POST", "GET"])
def chat():
    try:
        # Ensure the request contains JSON and a message
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"response": "Error: No message provided."}), 400
        
        # Handle exit message
        if user_message.lower() == "exit":
            return jsonify({"response": "Goodbye!"})

        # Get response from OpenAI GPT
        response = openai.Completion.create(
            model="text-davinci-003",  # You can change to another model like 'gpt-4'
            prompt=user_message,
            max_tokens=1500
        )

        # Return the OpenAI response
        return jsonify({"response": response.choices[0].text.strip()})

    except Exception as e:
        # Return error message if there's an exception
        return jsonify({"response": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    # Run the app on port 5000
    app.run(debug=True,host="0.0.0.0", port=5000)
