var track = 0;
var total

(function () {
    var fileCatcher = document.getElementById('file-catcher');
    var fileInput = document.getElementById('id_image');
    var gallery_url = document.getElementById('upload_url').value;
    var progressBar = document.getElementById('progress-bar');
    var fileCounter = document.getElementById('file-counter');

    var fileList = [];
    var sendFile;

    fileCatcher.addEventListener('submit', function (event) {
        document.getElementById("upload-progress").style.display = "flex";
        progressBar.style.width = "0%";
        fileCounter.textContent = (total) + " files remaining.."
        event.preventDefault();
        fileList.forEach((file, index) => {
            sendFile(index, file);
        });
    });

    fileInput.addEventListener('change', function (evnt) {
        fileList = [];
        for (var i = 0; i < fileInput.files.length; i++) {
            fileList.push(fileInput.files[i]);
        }
        total = fileList.length
    });

    sendFile = function (index, file) {
        var formData = new FormData(fileCatcher);
        formData.delete("image");
        var request = new XMLHttpRequest();

        formData.set("image", file);
        request.open("POST", gallery_url);
        request.onload = function () {
            track++
            if (this.status == 200) {
                var progr = Math.round(track / total * 100);
                progressBar.style.width = progr + "%";
                progressBar.innerHTML = progr + "%";
                fileCounter.textContent = (total - track) + " files remaining.."
            }
            else {
                console.log("Cannot send " + file.name)
            }
            if (track == total) {
                document.getElementById("upload-progress").style.display = "none";
                fileList = []
                fileInput.value = ""
                total = 0
                track = 0
            }
        }
        request.send(formData);
    };
})();