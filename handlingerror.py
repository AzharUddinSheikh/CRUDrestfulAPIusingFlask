from flask import Flask, jsonify
from flask import abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})
    
@app.errorhandler(404)
def error_handler(error):
    return '''<!DOCTYPE html>
<html>
	<head>
		<style>
			body {background-color: blue;}
			h1 {color: black;}
			p {color: red;}
		</style>
	</head>
	<body>

		<h1>404 Error Abort </h1>
		<p>Input is wrong</p>

	</body>
</html>'''
    
if __name__ == '__main__':
    app.run(debug=True)
    