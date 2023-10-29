import React from "react";
import "./style.scss";
import logoo from "./logo2.jpeg";
import sim1 from "./sideimg1.webp";
import sim2 from "./sideimg2.webp";

class MainBox extends React.Component {
  dropzoneclick = () => {
    let a = document.querySelector(".drop-zone__input");
    a.click();
  };

  inputChange = () => {
    let a = document.querySelector(".drop-zone__input");
    let dropZoneElement = document.querySelector(".drop-zone");
    if (a.files.length) {
      this.updateThumbnail(dropZoneElement, a.files[0]);
    }
  };

  mainfunc = (e) => {
    e.preventDefault();
    let inputElement = document.querySelector(".drop-zone__input");
    let dropZoneElement = document.querySelector(".drop-zone");
    if (e.dataTransfer.files.length) {
      inputElement.files = e.dataTransfer.files;
      this.updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
    }
    dropZoneElement.classList.remove("drop-zone--over");
  };
  updateThumbnail = (dropZoneElement, file) => {
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

    console.log(file);

    // Show thumbnail for image files
    if (
      file.type.startsWith("video/") ||
      file.type.startsWith("application/vnd.openxml")
    ) {
      thumbnailElement.dataset.label = file.name;
      const reader = new FileReader();
      reader.readAsDataURL(file);
      console.log(reader);
      //   handleVideoUpload(file);
      reader.onload = () => {
        thumbnailElement.style.backgroundImage = `url('https://cdn-icons-png.flaticon.com/128/2716/2716054.png')`;
      };
    } else {
      alert("Wrong file extension!!");
    }
  };
  render() {
    return (
      <div className="overall">
        <div className="info">
          <div className="infod1">
            <img className="sim1" src={sim1} alt="" />
          </div>
          <div className="infod2">
            {" "}
            <h1 className="infoh">
              How To Use <br></br>
            </h1>
            <img className="img1" src={logoo} alt="Briefify.AI" />
            <p className="infop">
              Upload a video or a document(in .docx or .txt format)
              <br></br>Or enter youtube link of a video. <br></br>
              Transcribe it.<br></br>Summarize it.<br></br>
              Even ask our chatbot queries regarding the doc/video.{" "}
            </p>
          </div>
          <div className="infod3">
            <img className="sim2" src={sim2} alt="" />
          </div>
        </div>
        <div className="outerbox">
          <div className="upload">
            <h4 className="upld">Upload your Video/Document</h4>
            <div className="drz">
              <form
                action="http://localhost:3000/upload"
                enctype="multipart/form-data"
                method="post"
                class="myform"
              >
                <div
                  class="drop-zone"
                  onClick={this.dropzoneclick}
                  onDrop={this.mainfunc}
                >
                  <span class="drop-zone__prompt">
                    Drop file here or click to upload
                  </span>
                  <input
                    type="file"
                    name="myFile"
                    class="drop-zone__input"
                    onChange={this.inputChange}
                  />
                </div>
                <div class="form-field">
                  <input type="submit" />
                </div>
              </form>
            </div>
            <h4 className="or">OR</h4>
            <label className="ytb-label">Paste YouTube link:</label>
            <input
              type="url"
              className="ytb-link"
              placeholder="https://www.youtube.com/watch?v=hNL_64MjELQ"
            />
            <button className="ytb-btn"> Submit</button>
          </div>
          <div className="output">
            <h2 className="txtc">Text Converter</h2>
            <label className="wrdl">Choose word limit:</label>
            <select name="" id="wrds">
              <option value="volvo">Full Transcript</option>
              <option>Upto 1000 words</option>
              <option>Upto 750 words</option>
              <option>Upto 500 words</option>
              <option>Upto 250 words</option>
              <option>Upto 100 words</option>
            </select>
            <button className="fbtn" type="button">
              Submit
            </button>
            <h3 className="otpt">
              Output File <br></br> Will Be Displayed <br></br>Here
            </h3>
          </div>
        </div>
        <div className="chtb">
          <h2 className="chtb-h">
            Want To Ask Queries <br></br>Related To The <br></br>Doc/Video ?
          </h2>
          <h4 className="chtbt">Try Our Chatbot</h4>
        </div>
      </div>
    );
  }
}

export default MainBox;
