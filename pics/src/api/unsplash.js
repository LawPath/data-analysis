import axios from 'axios';

export default axios.create({
    baseURL: 'https://api.unsplash.com',
    headers: {
        Authorization: 'Client-ID rCGd5W85mxHM_YCfRo2sq2cMRpMmPEtMw7kIHimCMUM'
    } 
 }
)