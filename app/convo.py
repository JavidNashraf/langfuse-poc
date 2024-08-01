import random
import time
from flask import jsonify, g, request

def langfuse_trace():
    data = request.json
    user_message = data.get('user_message', 'Hello, AI!')

    time.sleep(random.uniform(0.5, 2.0))
    llm_response = f"Hello! You said: '{user_message}'. How can I assist you today?"

    try:
        generation = g.trace.generation(
            name="llm_response",
            model="example-llm-model",
            model_parameters={"temperature": 0.7, "max_tokens": 100},
            metadata={
                "user_message": user_message
            },
            input = user_message,
            completion=llm_response,
        )
    except Exception as e:
        return jsonify({"error": f"Generation error: {str(e)}"}), 500

    g.trace.event(name="final_output", input=user_message,output =llm_response)

    return jsonify({
        "user_message": user_message,
        "llm_response": llm_response,
        "trace": {
            "id": g.trace.id,
            "generation_id": generation.id
        }
    })
