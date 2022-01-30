import axios from 'axios';

import React, {useState} from 'react';
import Image from './components/Image';
import Form from './components/Form';

const API_URL = "http://localhost:5000";


function App() {
  const [gridImage, setGridImage] = useState([]);
  const [gridSize, setGridSize] = useState(10);
  const [selectedImage, setSelectedImage] = useState(null);

  const onSelectedImageInput = event => {
    setSelectedImage(event.target.files[0]);
  };

  const onGridSizeInput = event => {
    setGridSize(event.target.value);
  }

  const onSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();

    formData.append(
      "image",
      selectedImage,
      selectedImage.name
    );

    formData.append(
      "grid_size",
      gridSize
    );
  
  
    axios.post(`${API_URL}/upload`, formData)
      .then(response => {
        setGridImage(response.data);
      });
  };

  

  return (
    <div>
      <Form
        gridSize={gridSize}
        onGridSizeInput={onGridSizeInput}
        selectedImage={selectedImage}
        onSelectedImageInput={onSelectedImageInput}
        onSubmit={onSubmit}
      />
      {
        (selectedImage || gridImage.length > 0) && <Image image={selectedImage} splittedImages={gridImage} />
      }
      
    </div>
  );
};
 
export default App;
