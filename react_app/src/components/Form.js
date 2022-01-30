import React from 'react';

function Form({gridSize, onGridSizeInput, selectedImage, onSelectedImageInput, onSubmit}) {

    return (
        <>
            <h3>
                Upload an image you want to split
            </h3>
            <form onSubmit={onSubmit}>
                <input type="file" onChange={onSelectedImageInput} />
                <input type="number" onChange={onGridSizeInput} />
                <input type="submit" value="Split image" disabled={!selectedImage && gridSize}/>
            </form>
        </>
    );
};
 
export default Form;