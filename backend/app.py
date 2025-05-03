from flask import Flask, jsonify, request, session
from flask_cors import CORS
import os
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app, supports_credentials=True)

# 데이터베이스 연결 함수
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'postgres'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres')
    )
    conn.autocommit = True
    return conn

# 초기 데이터베이스 테이블 생성
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # 테이블이 존재하는지 확인
    cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'users')")
    table_exists = cur.fetchone()[0]
    
    # 테이블이 존재하지 않는 경우에만 생성
    if not table_exists:
        # 사용자 테이블 생성
        cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(200) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        print("사용자 테이블이 생성되었습니다.")
    else:
        print("사용자 테이블이 이미 존재합니다.")
    
    cur.close()
    conn.close()

# 서버 시작 시 DB 초기화
init_db()

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'ok',
        'message': '서버가 정상적으로 동작 중입니다.'
    })

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify({
        'platform': '보안 동아리 웹사이트',
        'version': '0.1.0',
        'description': 'CTF 문제 공유 및 지식 공유 플랫폼'
    })

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # 필수 필드 확인
    if not all(field in data for field in ['username', 'email', 'password']):
        return jsonify({'error': '모든 필드를 입력해주세요'}), 400
    
    username = data['username']
    email = data['email']
    password = data['password']
    
    # 비밀번호 해싱
    password_hash = generate_password_hash(password)
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # 사용자 존재 여부 확인
        cur.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        if cur.fetchone() is not None:
            return jsonify({'error': '이미 존재하는 사용자명 또는 이메일입니다'}), 400
        
        # 새 사용자 등록
        cur.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s) RETURNING id",
            (username, email, password_hash)
        )
        user_id = cur.fetchone()[0]
        
        return jsonify({'message': '회원가입이 완료되었습니다', 'user_id': user_id}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        cur.close()
        conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # 필수 필드 확인
    if not all(field in data for field in ['username', 'password']):
        return jsonify({'error': '사용자명과 비밀번호를 입력해주세요'}), 400
    
    username = data['username']
    password = data['password']
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # 사용자 조회
        cur.execute("SELECT id, username, password_hash FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        
        if user is None or not check_password_hash(user[2], password):
            return jsonify({'error': '사용자명 또는 비밀번호가 올바르지 않습니다'}), 401
        
        # 세션에 사용자 정보 저장
        session['user_id'] = user[0]
        session['username'] = user[1]
        
        return jsonify({
            'message': '로그인 성공',
            'user': {
                'id': user[0],
                'username': user[1]
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        cur.close()
        conn.close()

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': '로그아웃 되었습니다'})

@app.route('/api/user', methods=['GET'])
def get_user():
    if 'user_id' not in session:
        return jsonify({'error': '로그인이 필요합니다'}), 401
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT id, username, email, created_at FROM users WHERE id = %s", (session['user_id'],))
        user = cur.fetchone()
        
        if user is None:
            session.clear()
            return jsonify({'error': '사용자를 찾을 수 없습니다'}), 404
        
        return jsonify({
            'user': {
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'created_at': user[3].isoformat() if user[3] else None
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 