from flask import Flask, request, jsonify

app = Flask(__name__)
students = [{"id": 1, "name": "Krishna", "course": "CSE"}]

@app.route("/")
def home():
    return jsonify({"message": "Student API Running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("course"):
        return jsonify({"error": "Name and course required"}), 400
    student = {"id": len(students)+1, "name": data["name"], "course": data["course"]}
    students.append(student)
    return jsonify(student), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)