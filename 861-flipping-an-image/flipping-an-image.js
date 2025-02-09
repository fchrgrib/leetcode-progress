/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function(image) {
    for(let i = 0;i<image.length;i++){
        let l = 0, r = image.length - 1;
        while(l<=r){
            let tmp1 = image[i][l];
            image[i][l] = image[i][r];
            image[i][r] = tmp1;
            
            if(l!=r) image[i][l] = (image[i][l] === 1)?0:1;
            image[i][r] = (image[i][r] === 1)?0:1;
            l++;r--;
        }
        // if(r-l == 0) image[i][l]= (image[i][l] === 1)?0:1;
    }

    return image;
};