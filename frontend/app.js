function uploadFile() {
  const input = document.getElementById("fileInput");
  const file = input.files[0];
  const formData = new FormData();
  formData.append("file", file);

  fetch("http://127.0.0.1:8000/upload", {
    method: "POST",
    body: formData
  })
  .then(res => res.json())
  .then(data => alert("上傳成功: " + data.filename))
  .catch(err => console.error(err));
}

function askStyle() {
  const input = document.getElementById("styleInput").value;
  const formData = new FormData();
  formData.append("prompt", input);

  fetch("http://127.0.0.1:8000/ask_style", {
    method: "POST",
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("aiAnswer").innerText = data.answer;
  })
  .catch(err => console.error(err));
}
