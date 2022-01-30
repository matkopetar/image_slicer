import React from 'react';

function Image({ image, splittedImages }) {
    const milliseconds = Date.now();
    const styles = {
        splittedImagesStyle: {
            width: 'minContent',
            display: 'grid',
            gridTemplateColumns: `repeat(${splittedImages.length}, auto)`,
            gap: '5px'
        }
    };

    return (
        splittedImages.length ?
            <div style={styles.splittedImagesStyle}>
                { splittedImages.map(row => {
                    return row.map(image => <img src={image + '?' + milliseconds.toString()}/>)
                }) }
            </div> :
            <div className='image'> <img src={URL.createObjectURL(image)}/></div>
    );
};
 
export default Image;
