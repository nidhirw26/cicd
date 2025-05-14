from flask import Flask, render_template, request

app = Flask(__name__)

registrations = []

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    age = request.form.get('age')
    gender = request.form.get('gender')
    event_type = request.form.get('event_type')
    comments = request.form.get('comments')

    if name and email:
        registrations.append({
            'name': name,
            'email': email,
            'phone': phone,
            'age': age,
            'gender': gender,
            'event_type': event_type,
            'comments': comments
        })
        return f"Thanks for registering, {name}! You've registered for the {event_type}."
    else:
        return "Please provide required fields.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
