document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    const formData = new FormData();
    const fileField = document.getElementById('videoFile');
    formData.append('videoFile', fileField.files[0]);
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  
    .then(data => {
        document.getElementById('result').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred while uploading the video.';
    });
});
