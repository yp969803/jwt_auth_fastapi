document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
  const dropZoneElement = inputElement.closest(".drop-zone");

  dropZoneElement.addEventListener("click", (e) => {
    inputElement.click();
  });

  inputElement.addEventListener("change", (e) => {
    if (inputElement.files.length) {
      updateThumbnail(dropZoneElement, inputElement.files[0]);
    }
  });

  dropZoneElement.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZoneElement.classList.add("drop-zone--over");
  });

  ["dragleave", "dragend"].forEach((type) => {
    dropZoneElement.addEventListener(type, (e) => {
      dropZoneElement.classList.remove("drop-zone--over");
    });
  });

  dropZoneElement.addEventListener("drop", (e) => {
    e.preventDefault();

    if (e.dataTransfer.files.length) {
      inputElement.files = e.dataTransfer.files;
      updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
    }

    dropZoneElement.classList.remove("drop-zone--over");
  });
});

function updateThumbnail(dropZoneElement, file) {
  let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

  // First time - remove the prompt
  if (dropZoneElement.querySelector(".drop-zone__prompt")) {
    dropZoneElement.querySelector(".drop-zone__prompt").remove();
  }

  // First time - there is no thumbnail element, so lets create it
  if (!thumbnailElement) {
    thumbnailElement = document.createElement("div");
    thumbnailElement.classList.add("drop-zone__thumb");
    dropZoneElement.appendChild(thumbnailElement);
  }

  thumbnailElement.dataset.label = file.name;
  console.log(file);

  // Show thumbnail for image files
  if (file.type.startsWith("video/")) {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    console.log(reader);
    handleVideoUpload(file);
    // reader.readAsDataURL(file);
    // reader.onload = () => {
    //   thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
    // };
  } else {
    thumbnailElement.style.backgroundImage = null;
  }
}

function handleVideoUpload(file) {
  const formData = new FormData();
  formData.append("video", file);

  // You can use AJAX to upload the file to a server.
  // For example, using the Fetch API:
  fetch("/upload-video", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert("Video uploaded successfully.");
        // You can initiate further processing here.
      } else {
        alert("Video upload failed.");
      }
    })
    .catch((error) => console.error("Error:", error));
}
