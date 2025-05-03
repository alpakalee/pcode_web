<?php
  session_start();
  
  // 데이터베이스 연결 (실제로는 사용하지 않음, 문제 설명용)
  $db_host = 'localhost';
  $db_user = 'guestbook_user';
  $db_pass = 'guestbook_password';
  $db_name = 'guestbook';
  
  // 메시지 저장 (간단한 파일 기반 저장소)
  $messages_file = 'messages.txt';
  
  // 메시지 제출 처리
  if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['message'])) {
    $name = isset($_POST['name']) ? $_POST['name'] : 'Anonymous';
    $message = $_POST['message'];
    
    // 새 메시지 저장
    $entry = "$name: $message\n";
    file_put_contents($messages_file, $entry, FILE_APPEND);
    
    // 리다이렉트로 새로고침 방지
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit;
  }
  
  // 메시지 불러오기
  $messages = file_exists($messages_file) ? file($messages_file) : [];
?>

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>보안 동아리 방명록</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    h1 {
      text-align: center;
      color: #333;
    }
    .message-form {
      background-color: #f9f9f9;
      padding: 15px;
      border-radius: 5px;
      margin-bottom: 20px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, textarea {
      width: 100%;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .messages {
      border-top: 1px solid #ddd;
      padding-top: 20px;
    }
    .message {
      background-color: #f1f1f1;
      padding: 10px;
      margin-bottom: 10px;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <h1>보안 동아리 방명록</h1>
  
  <div class="message-form">
    <h2>메시지 남기기</h2>
    <form method="POST" action="">
      <div class="form-group">
        <label for="name">이름:</label>
        <input type="text" id="name" name="name" placeholder="이름을 입력하세요">
      </div>
      <div class="form-group">
        <label for="message">메시지:</label>
        <textarea id="message" name="message" rows="4" required placeholder="메시지를 입력하세요"></textarea>
      </div>
      <button type="submit">제출</button>
    </form>
  </div>
  
  <div class="messages">
    <h2>방명록 메시지</h2>
    <?php if (empty($messages)): ?>
      <p>아직 메시지가 없습니다.</p>
    <?php else: ?>
      <?php foreach ($messages as $entry): ?>
        <div class="message">
          <?php echo $entry; ?>
        </div>
      <?php endforeach; ?>
    <?php endif; ?>
  </div>
  
  <?php if (isset($_COOKIE['admin']) && $_COOKIE['admin'] === 'true'): ?>
  <!-- 관리자 전용 섹션 -->
  <div style="margin-top: 50px; padding: 20px; background-color: #ffeeee; border: 1px solid #ffcccc;">
    <h2>관리자 전용 섹션</h2>
    <p>플래그: FLAG{xss_is_still_relevant_in_2023}</p>
  </div>
  <?php endif; ?>
  
  <script>
    // 관리자 인증 확인 (실제로는 이렇게 하지 않음, 문제용)
    function checkAdmin() {
      if (document.cookie.includes('admin=true')) {
        console.log('관리자로 로그인되었습니다.');
      }
    }
    
    // 페이지 로드 시 실행
    window.onload = function() {
      checkAdmin();
    };
  </script>
</body>
</html> 