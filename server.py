from flask import Flask, request, Response
import sqlite3
import json

app = Flask(__name__)

def get_word_info(word):
    conn = sqlite3.connect('dict.db')
    cursor = conn.cursor()
    cursor.execute("SELECT level, sound, ja FROM dict WHERE en = ?", (word,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {
            "level": result[0],
            "ja": result[2],
            "sound": result[1]
        }
    else:
        return None

@app.route('/', methods=['GET'])
def word_info():
    word = request.args.get('word')
    if not word:
        return jsonify({"error": "Missing 'word' query parameter"}), 400
    info = get_word_info(word)
    if info:
        # ensure_ascii=False を設定して日本語がエスケープされないようにする
        response = app.response_class(
            response=json.dumps(info, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        return jsonify({"error": "Word not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)