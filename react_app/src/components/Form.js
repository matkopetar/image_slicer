import React from 'react';

function Form({gridSize, onGridSizeInput, selectedImage, onSelectedImageInput, onSubmit}) {
    const styles = {
        form: {
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center'
        },
        inputFile: {
            display: 'block'
        },
        inputNumber: {
            display: 'block'
        },
        inputSubmit: {
            display: 'block'
        }
    };

    return (
        <>
            <h3>
                Upload an image you want to split
            </h3>
            <form style={styles.form}onSubmit={onSubmit}>
                <input type="file" style={styles.inputFile} onChange={onSelectedImageInput} />
                <br/>
                <input type="number" style={styles.inputNumber} onChange={onGridSizeInput} />
                <br/>
                <input type="submit" style={styles.inputSubmit} value="Split image" disabled={!selectedImage && gridSize}/>
            </form>
        </>
    );
};
 
export default Form;