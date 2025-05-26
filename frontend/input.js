document.addEventListener('DOMContentLoaded', function() {
    // Auto-resize textarea
    const textarea = document.getElementById('postContent');
    textarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
        
        // Character counter
        const charCount = this.value.length;
        const counter = this.nextElementSibling;
        counter.textContent = `${charCount}/500자`;
        
        if (charCount > 500) {
            counter.classList.add('text-red-500');
            counter.classList.remove('text-gray-500');
        } else {
            counter.classList.add('text-gray-500');
            counter.classList.remove('text-red-500');
        }
    });

    // Generate button click handler
    const generateBtn = document.getElementById('generateBtn');
    generateBtn.addEventListener('click', function () {
        const title = document.getElementById('postTitle').value.trim();
        const content = document.getElementById('postContent').value.trim();
        const style = document.getElementById('blogStyle').value;

        if (!title || !content || !style) {
            alert('모든 필드를 입력해주세요!');
            return;
        }

        // Show loading state
        generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i> 생성 중...';
        generateBtn.disabled = true;

        // 서버에 보낼 데이터 구성
        const postData = {
            postTitle: title,
            postContent: content,
            blogStyle: style
        };

        // FastAPI 서버로 POST 요청
        fetch('http://localhost:8000/generate-post', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('서버 응답 오류');
            }
            return response.json();
        })
        .then(data => {
            // 서버로부터 받은 콘텐츠 렌더링
            document.getElementById('postPreview').innerHTML = data.generatedContent;
            document.getElementById('previewSection').classList.remove('hidden');

            // 버튼 상태 초기화
            generateBtn.innerHTML = '<i class="fas fa-magic mr-2"></i> 포스트 생성하기';
            generateBtn.disabled = false;

            // Scroll to preview
            document.getElementById('previewSection').scrollIntoView({ behavior: 'smooth' });
        })
        .catch(error => {
            alert('포스트 생성 중 오류 발생: ' + error.message);
            generateBtn.innerHTML = '<i class="fas fa-magic mr-2"></i> 포스트 생성하기';
            generateBtn.disabled = false;
        });
    });

});