var isRecording = false;
var recognition;
const lang = 'en-US';

function showUploading() {
  var uploadButton = document.getElementById('upload');
  var uploadingButton = document.getElementById('uploading');

  // Hide the submit button and show the loading button
  uploadButton.style.display = 'none';
  uploadingButton.style.display = 'block';
}

function showLoadingButton() {
  var submitButton = document.getElementById('submitButton');
  var loadingButton = document.getElementById('loadingButton');

  // Hide the submit button and show the loading button
  submitButton.style.display = 'none';
  loadingButton.style.display = 'block';
}

function toggleRecording() {
  var recordButton = document.getElementById('recordButton');
  if (!isRecording) {
    if (window.hasOwnProperty('webkitSpeechRecognition')) {
      recognition = new webkitSpeechRecognition();

      recognition.continuous = true;
      recognition.interimResults = false;

      recognition.lang = lang;
      recognition.start();

      recognition.onresult = function (e) {
        document.getElementById('textInput').value += e.results[0][0].transcript + ' ';
        recognition.stop();
      };

      recognition.onerror = function (e) {
        console.log('error', e);
        recognition.stop();
      };

      //keeps recording until button pressed
      recognition.onend = function (e) {
        console.log('ended', e);
        if (isRecording){
          recognition.start();
        }
      };
    }
    recordButton.src = 'static/img/stop.svg';
    isRecording = true;
  }
  else {
    recordButton.src = 'static/img/record.svg';
    recognition.stop();
    isRecording = false;
  }
};