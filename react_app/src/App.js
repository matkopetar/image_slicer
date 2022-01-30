import axios from 'axios';
import './App.css';

import React, {useState} from 'react';

const API_URL = "http://localhost:5000";


function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [gridImage, setGridImage] = useState([]);

  const onFileChange = event => {
    setSelectedFile(event.target.files[0]);
  };
  
  const onFileUpload = () => {
    const formData = new FormData();
  
    formData.append(
      "image",
      selectedFile,
      selectedFile.name
    );
  
  
    axios.post(`${API_URL}/upload`, formData)
      .then(response => {
        console.log(response);
        setGridImage(response.data);
      });
  };
  
  const fileData = () => {
    if (selectedFile) {
      return (
        <div>
          <h2>File Details:</h2>
            <p>File Name: {selectedFile.name}</p>                       
            <p>File Type: {selectedFile.type}</p>
            <p>
              Last Modified:{" "}
              {selectedFile.lastModifiedDate.toDateString()}
            </p>
        </div>
      );
    } else {
      return (
        <div>
          <br />
          <h4>Choose before Pressing the Upload button</h4>
        </div>
      );
    }
  };

  return (
    <div>
        <h3>
          Upload an image!
        </h3>
        <div>
            <input type="file" onChange={onFileChange} />
            <button onClick={onFileUpload}>
              Upload!
            </button>
        </div>
      {fileData()}
      <div className="grid-image">
        {gridImage.map(row => {
          return row.map(image => <div> <img src={image}/></div>)
        })
        }
      </div>
    </div>
  );
};
 
export default App;
