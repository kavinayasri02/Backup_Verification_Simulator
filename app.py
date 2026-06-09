import os
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = '/tmp/uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

uploaded_files = {
    'original': None,
    'original_name': None,
    'original_size': None,
    'backup': None,
    'backup_name': None,
    'backup_size': None,
}

@app.route('/')
def index():
    return render_template('index.html', last_scan=datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

@app.route('/upload_original', methods=['POST'])
def upload_original():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], 'original_' + filename)
    file.save(path)
    size = os.path.getsize(path)
    uploaded_files['original'] = path
    uploaded_files['original_name'] = filename
    uploaded_files['original_size'] = size
    return jsonify({'name': filename, 'size': size})

@app.route('/upload_backup', methods=['POST'])
def upload_backup():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], 'backup_' + filename)
    file.save(path)
    size = os.path.getsize(path)
    uploaded_files['backup'] = path
    uploaded_files['backup_name'] = filename
    uploaded_files['backup_size'] = size
    return jsonify({'name': filename, 'size': size})

@app.route('/verify', methods=['POST'])
def verify():
    if not uploaded_files['original'] or not uploaded_files['backup']:
        return jsonify({'status': 'error', 'message': 'Upload both files first'})
    orig_size = uploaded_files['original_size']
    back_size = uploaded_files['backup_size']
    if orig_size == back_size:
        return jsonify({
            'status': 'matched',
            'message': 'MATCHED',
            'original_size': orig_size,
            'backup_size': back_size
        })
    else:
        return jsonify({
            'status': 'mismatch',
            'message': 'MISMATCH FOUND',
            'original_size': orig_size,
            'backup_size': back_size
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
